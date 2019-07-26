Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

`O(1)` because len() has an O(1) complexity, as well as setting an item in a list.

2. What is the space complexity of your ring buffer's `append` function?

`O(1)` as it only sets existing space allocated for the RingBuffer.

3. What is the runtime complexity of your ring buffer's `get` method?
`O(n)` because filter runs through each itme in self.storage, to only add to the new list items that are not None.

4. What is the space complexity of your ring buffer's `get` method?

`O(n)` -- although it is O(n * 2) because it takes up twice the space by creating a new list, that still reduces to O(n).



5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
