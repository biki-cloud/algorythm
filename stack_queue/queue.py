class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, data) -> None:
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)