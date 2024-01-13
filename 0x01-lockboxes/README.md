# 0x01. Lockboxes
# Requirements 🏛️
## General🧵
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be documented
* Your code should use the `PEP 8` style (version 1.7.x)
* All your files must be executable

# Tasks 📃
## 0. Lockboxes: [0-lockboxes.py](0-lockboxes.py)
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A key with the same number as a box opens that box
* You can assume all keys will be positive integers
  * There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`
```groovy
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```
```groovy
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```
---

# REFERENCE 📚
## CODE IMPLEMENTATION 💻
```groovy
def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.

    :param boxes:
    :return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
```
## CODE EXPLANATION ✍️
```groovy
The canUnlockAll function takes a list of lists (boxes) as input.
Each inner list represents a box and contains the indices of other boxes that can be unlocked using their keys.
The function uses a depth-first search algorithm to traverse the boxes and determine if all of them can be opened.

In the provided example, the first box is initially unlocked, and its key opens the second box.
The second box's key opens the third box, and so on.
Since all the boxes can be opened, the output is True.

In the second example, the keys in the boxes form a loop,
allowing access to all the boxes. Hence, the output is True.

In the third example, there is no way to open the fifth box because it doesn't have any keys.
Therefore, the output is False.
```

# Other Solution 📚
1. First one
```groovy
#!/usr/bin/python3
'''
Module Docs
'''


def canUnlockAll(boxes):
    '''
    Function Docs
    '''
    if (boxes):
        numOfBoxes = len(boxes)
        setOfKeys = {0}
        setOfKeys.update(boxes[0])
        visitedBoxes = {0}
        while True:
            newBoxVisited = False
            keys = setOfKeys.copy()
            # print(f"Set of keys copy = {keys}")
            for key in keys:
                # print(f"Key in loop = {key}")
                if key not in visitedBoxes.copy() and key < numOfBoxes:
                    # print(f"box opened = {key}")
                    setOfKeys.update(boxes[key])
                    visitedBoxes.add(key)
                    # print(f"set of Keys updated = {setOfKeys}")
                    # print(f"visitedBoxes updated = {visitedBoxes}")
                    newBoxVisited = True
            if not newBoxVisited:
                break
        for n in range(numOfBoxes):
            if n not in setOfKeys:
                return False
        return True
    return False
```

2. Second one
```groovy
#!/usr/bin/python3
"""
Module 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1,
    and each box may contain keys to the other boxes.
    Determine if all the boxes can be opened.
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
```
