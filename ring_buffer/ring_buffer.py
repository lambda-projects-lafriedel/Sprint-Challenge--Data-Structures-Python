class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # if current (index) == capacity, reset current to 0
        if self.current == self.capacity:
            self.current = 0
        # remove item at current, append item to storage at current
        self.storage.pop(self.current)
        self.storage.insert(self.current, item)
        # increase current by 1
        self.current += 1


    def get(self):
        elements = list()
        # for each element in list, if not None, append to new list
        for item in self.storage:
            # do not return any None values, even if they are present
            if item is None:
                continue
            elements.append(item)
        # print list
        return elements