#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node *head = NULL;

void insertAtBeginning(int value) {
    struct node *newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = head;
    head = newnode;
    printf("%d inserted at beginning\n", value);
}

void insertAtEnd(int value) {
    struct node *newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    newnode->next = NULL;

    if (head == NULL) {
        head = newnode;
    } else {
        struct node *temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newnode;
    }
    printf("%d inserted at end\n", value);
}

void deleteNode(int value) {
    struct node *temp = head, *prev = NULL;

    if (temp != NULL && temp->data == value) {
        head = temp->next;
        free(temp);
        printf("%d deleted from list\n", value);
        return;
    }

    while (temp != NULL && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("%d not found in list\n", value);
        return;
    }

    prev->next = temp->next;
    free(temp);
    printf("%d deleted from list\n", value);
}

void display() {
    struct node *temp = head;
    if (head == NULL) {
        printf("List Empty\n");
        return;
    }
    printf("Linked List: ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main() {
    int value, choice;
    while (1) {
        printf("\nSingle linked list\n");
        printf("1. Insert Beginning\n");
        printf("2. Insert End\n");
        printf("3. Delete Node\n");
        printf("4. Display\n");
        printf("5. Exit\n");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            printf("Enter value to insert: ");
            scanf("%d", &value);
            insertAtBeginning(value);
            break;
        case 2:
            printf("Enter value to insert: ");
            scanf("%d", &value);
            insertAtEnd(value);
            break;
        case 3:
            printf("Enter value to delete: ");
            scanf("%d", &value);
            deleteNode(value);
            break;
        case 4:
            display();
            break;
        case 5:
            exit(0);
        default:
            printf("Invalid choice\n");
        }
    }
}
