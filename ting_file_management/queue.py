class Queue:
    def __init__(self):
        self.dataFiles = list()

    def __len__(self):
        return len(self.dataFiles)

    def enqueue(self, value):
        return self.dataFiles.append(value)

    def dequeue(self):
        return self.dataFiles.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.dataFiles[index]
