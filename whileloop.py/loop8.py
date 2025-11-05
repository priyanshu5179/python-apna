from flask import Flask, render_template, request, redirect, session
import pandas as pd
import qrcode
import os
from web3 import Web3
import json

app = Flask(__name__)
app.secret_key = "mysecret"

# ---------------- BLOCKCHAIN SETUP ----------------
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if not web3.is_connected():
    raise Exception("⚠️ Web3 is not connected! Please start Ganache first.")

web3.eth.default_account = web3.eth.accounts[0]

# Load contract ABI and address
with open("blockchain/build/contracts/HerbRegistry.json") as f:
    contract_json = json.load(f)
    abi = contract_json["abi"]

# Auto-detect contract address from Truffle build
try:
    network_id = list(contract_json["networks"].keys())[0]
    contract_address = contract_json["networks"][network_id]["address"]
except Exception:
    # fallback manual address
    contract_address = "0xD37022f8A68F0D1F6d1cD618b8936aF91D6d3B2a"

contract = web3.eth.contract(address=contract_address, abi=abi)

# ---------------- CSV SETUP ----------------
DATA_FILE = "herbs.csv"

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Farmer", "Herb", "Location", "HarvestDate", "BatchID"])
    df.to_csv(DATA_FILE, index=False)

# ---------------- LOGIN SETUP ----------------
USERNAME = "krishna"
PASSWORD = "krishna@123"

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == USERNAME and password == PASSWORD:
        session["user"] = username
        return redirect("/form")
    else:
        return render_template("login.html", error="Invalid login!")

@app.route("/form")
def form():
    if "user" not in session:
        return redirect("/")
    return render_template("form.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

@app.route("/submit", methods=["POST"])
def submit():
    if "user" not in session:
        return redirect("/")

    farmer = request.form["farmer"]
    herb = request.form["herb"]
    location = request.form["location"]
    harvest = request.form["harvest"]

    # 1️⃣ Add to blockchain
    try:
        tx_hash = contract.functions.addHerb(farmer, location, herb).transact()
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    except Exception as e:
        return f"<h3>⚠️ Blockchain error: {e}</h3>"

    # 2️⃣ Generate Batch ID
    batch_id = f"{farmer[:3]}_{herb[:3]}_{harvest.replace('-', '')}"

    # 3️⃣ Save to CSV
    df = pd.read_csv(DATA_FILE)
    df.loc[len(df)] = [farmer, herb, location, harvest, batch_id]
    df.to_csv(DATA_FILE, index=False)

    # 4️⃣ Generate QR Code linking to /track/<batch_id>
    qr_link = f"http://localhost:5000/track/{batch_id}"
    os.makedirs("static/qrcodes", exist_ok=True)
    qr_path = f"static/qrcodes/{batch_id}.png"
    img = qrcode.make(qr_link)
    img.save(qr_path)

    return f"""
    <h2>🌿 Herb Registered Successfully!</h2>
    <p>✅ Saved on Blockchain.</p>
    <p><b>Transaction Hash:</b> {tx_hash.hex()}</p>
    <p><b>Batch ID:</b> {batch_id}</p>
    <p>QR Code (Scan to Track):</p>
    <img src='/{qr_path}' width='200'><br><br>
    <a href='/form'>➕ Add Another</a> | <a href='/logout'>🚪 Logout</a> | 
    <a href='/track/{batch_id}'>🔍 View Record</a>
    """

# ---------------- TRACKING PAGE ----------------
@app.route("/track/<batch_id>")
def track(batch_id):
    if not os.path.exists(DATA_FILE):
        return "<h3>No data available yet.</h3>"

    df = pd.read_csv(DATA_FILE)
    record = df[df["BatchID"] == batch_id]

    if record.empty:
        return f"<h3>❌ No record found for Batch ID: {batch_id}</h3>"

    row = record.iloc[0]
    try:
        blockchain_data = contract.functions.getHerb(row["Farmer"]).call()
    except:
        blockchain_data = ("N/A", "N/A", "N/A")

    return f"""
    <h2>🔍 Herb Tracking Details</h2>
    <p><b>Batch ID:</b> {row["BatchID"]}</p>
    <p><b>Farmer:</b> {row["Farmer"]}</p>
    <p><b>Herb:</b> {row["Herb"]}</p>
    <p><b>Location:</b> {row["Location"]}</p>
    <p><b>Harvest Date:</b> {row["HarvestDate"]}</p>
    <h3>🌿 Blockchain Record</h3>
    <p><b>Farmer:</b> {blockchain_data[0]}</p>
    <p><b>Location:</b> {blockchain_data[1]}</p>
    <p><b>Herb:</b> {blockchain_data[2]}</p>
    <br><a href='/form'>🏠 Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
