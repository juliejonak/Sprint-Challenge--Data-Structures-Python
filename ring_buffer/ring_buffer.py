class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # If storage is full, overwrite the oldest
    # Decide by comparing capacity to current
    if self.current == len(self.storage):
      print("Ring Buffer is full. Overwriting oldest item.")
      # Reset current to start of the list
      self.current = 0
      self.storage[self.current] = item
      self.current += 1

    # Else, add to the end of storage and increase current
    else:
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    # Create new list that filters out any None values
    get_list = list(filter(None, self.storage))
    return get_list