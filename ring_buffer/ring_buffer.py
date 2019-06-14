class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # adds elements to the buffer
        # if current == len(self.storage) - 1, reset current to 0
        if current == capacity - 1:
            current = 0
        # append item to storage at current, increase current by 1
        self.storage.insert(current, item)
        current += 1


    def get(self):
        # returns all elements in a list in their given order
        # do not return any None values, even if they are present
        elements = list()
        # for each element in list, if not None, append to new list
        for item in self.storage:
            if item is None:
                continue
            elements.append(item)
        # print list
        return elements