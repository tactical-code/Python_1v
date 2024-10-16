class RestrictedQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue_front(self):
        """Remove and return an item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def dequeue_rear(self):
        """Remove and return an item from the rear of the queue."""
        if not self.is_empty():
            return self.items.pop()  # Remove from the end of the list
        return None

    def traverse(self):
        """Return a list of items in the queue."""
        return list(self.items)

    def count(self, item):
        """Count occurrences of a specific item in the queue."""
        return self.items.count(item)

def main():
    queue = RestrictedQueue()

    while True:
        print("\nRestricted Queue Operations:")
        print("1. Enqueue (from rear)")
        print("2. Dequeue (from front)")
        print("3. Dequeue (from rear)")
        print("4. Traverse")
        print("5. Count Element")
        print("6. Exit")

        choice = input("Choose an operation (1-6): ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
            print(f"Enqueued '{item}'.")

        elif choice == '2':
            item = queue.dequeue_front()
            if item is not None:
                print(f"Dequeued '{item}' from front.")
            else:
                print("Queue is empty, cannot dequeue from front.")

        elif choice == '3':
            item = queue.dequeue_rear()
            if item is not None:
                print(f"Dequeued '{item}' from rear.")
            else:
                print("Queue is empty, cannot dequeue from rear.")

        elif choice == '4':
            items = queue.traverse()
            print("Current Queue:", items)

        elif choice == '5':
            item = input("Enter element to count: ")
            count = queue.count(item)
            print(f"Element '{item}' occurs {count} times in the queue.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

main()
