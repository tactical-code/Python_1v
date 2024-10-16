class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def insert_front(self, item):
        self.items.append(item)

    def insert_rear(self, item):
        self.items.insert(0, item)

    def delete_front(self):
        if not self.is_empty(): #true if list is not empty otherwise false
            return self.items.pop()
        return None

    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def traverse(self):
        return list(self.items)

    def count(self, item): #check how many 
        return self.items.count(item)

# Function to interact with the deque
def main():
    deque = Deque()

    while True:
        print("\nDeque Operations:")
        print("1. Insert Front")
        print("2. Insert Rear")
        print("3. Delete Front")
        print("4. Delete Rear")
        print("5. Traverse")
        print("6. Count Element")
        print("7. Exit")

        choice = input("Choose an operation (1-7): ")

        if choice == '1':
            item = input("Enter item to insert at front: ")
            deque.insert_front(item)
            print(f"Inserted '{item}' at front.")



        elif choice == '2':
            item = input("Enter item to insert at rear: ")
            deque.insert_rear(item)
            print(f"Inserted '{item}' at rear.")



        elif choice == '3':
            item = deque.delete_front()
            if item is not None:
                print(f"Deleted '{item}' from front.")
            else:
                print("Deque is empty, cannot delete from front.")



        elif choice == '4':
            item = deque.delete_rear()
            if item is not None:
                print(f"Deleted '{item}' from rear.")
            else:
                print("Deque is empty, cannot delete from rear.")



        elif choice == '5':
            items = deque.traverse()
            print("Current Deque:", items)



        elif choice == '6':
            item = input("Enter element to count: ")
            count = deque.count(item)
            print(f"Element '{item}' occurs {count} times in the deque.")

        elif choice == '7':
            print("Exiting...")
            break



        else:
            print("Invalid choice. Please try again.")

main()
