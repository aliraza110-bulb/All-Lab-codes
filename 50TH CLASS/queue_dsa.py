class Queue:
    def __init__(self, size: int) -> None:
        self.max_size = size
        self.array = [None] * size
        self.front = 0
        self.rear = -1
        self.current_size = 0

    def enqueue(self, value: int) -> None:
        if self.current_size == self.max_size:
            print("Queue is full. Cannot enqueue", value)
            return
        self.rear = (self.rear + 1) % self.max_size
        self.array[self.rear] = value
        self.current_size += 1
        print(f"Enqueued {value}")

    def dequeue(self) -> int:
        if self.current_size == 0:
            print("Queue is empty. Cannot dequeue")
            return -1
        temp = self.array[self.front]
        self.front = (self.front + 1) % self.max_size
        self.current_size -= 1
        print(f"Dequeued {temp}")
        return temp

    def peek(self) -> int:
        if self.current_size == 0:
            print("Queue is empty. Nothing to peek")
            return -1
        return self.array[self.front]

    def is_empty(self) -> bool:
        return self.current_size == 0

    def is_full(self) -> bool:
        return self.current_size == self.max_size

if __name__ == "__main__":
    q=Queue(3)
    q.enqueue(10); q.enqueue(20); q.enqueue(30)
    print("peek : ",q.peek() )
    print("Dequeue : ",q.dequeue())
    q.enqueue(40)
    print("peek :",q.peek())