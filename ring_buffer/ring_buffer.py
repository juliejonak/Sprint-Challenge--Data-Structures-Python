class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # If storage is full, overwrite the oldest
    # Decide by comparing capacity to current

    # Else, add to the end of storage and increase current

  def get(self):
    # Create new list that filters out any None values
    get_list = list(filter(None, self.storage))
    return get_list