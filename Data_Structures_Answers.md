Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
Runtime is O(1) (constant time) because it's only adding one item at a time, and the capacity of the buffer doesn't change the length of time the method needs to run. The main reason this is true is the use of indexing -- the entire buffer does not need to be traversed.

2. What is the space complexity of your ring buffer's `append` function?
Space complexity is O(1) (constant time) because the same amount of stack frames are being used every time it is run.

3. What is the runtime complexity of your ring buffer's `get` method?
Runtime is O(n) where n is the length of the list being used to implement the ring buffer. It must iterate over the entire length of the list to print all the elements (even if most/all of the elements are None).

4. What is the space complexity of your ring buffer's `get` method?
It is at worst O(n) because it needs to store essentially a copy of the storage list inside `elements`, and that takes up, at most, an amount of memory based on the length of `self.storage`.

5. What is the runtime complexity of the provided code in `names.py`?
When simplified, the runtime is at worst O(n^2) where n is the (equal) length of the name lists -- this is due to the nested `for` loops. It may run slightly better if the name files weren't of equal length, and especially if one file was very short.

6. What is the space complexity of the provided code in `names.py`?
If including the portion of code that reads and splits the names from the text files, it is O(n), because the variables containing lists names_1 and names_2 take up more memory based on the size of the read files.

If we're only considering the code after the instantiation of `duplicates` (which takes up O(1) space, by the way), it is O(1) because we're only ever storing variables name_1 and name_2. The space is not relative to the size of lists names_1 and names_2.

7. What is the runtime complexity of your optimized code in `names.py`?
It is O(n log n), where n is the lengths of the lists. It still has two for loops, but they are not nested - they happen on the same "level" of the code. The loops run at n compexity, and the `.append` and `.contains` binary search tree methods run at log n time, because about half of the search elements are removed at each pass.

8. What is the space complexity of your optimized code in `names.py`?
Again, if including the portion of code that reads and splits the names from the text files, it is O(n), because the variables containing lists names_1 and names_2 take up more memory based on the size of the read files.

If only considering the edited code, it is at worst O(n) where n is the height of the tree (assuming it's balanced). Everything else in that portion of the code takes up constant space.