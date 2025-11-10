class parentarent class:
    def method(self):
        return "Parentclass method"
        class childclass (parent calss ):
            def method(self):
                return "child class method"
                parent_obj=parentclass()
                child_obj=childclass()
                print(parent_obj.method())
                print(child_obj.method())