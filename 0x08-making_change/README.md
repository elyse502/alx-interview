# 0x08. Making Change
For the `“0. Change comes from within”` project, you will tackle a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to apply your understanding of algorithms to devise a solution that is not only correct but also efficient. Below are the key concepts and resources necessary to complete this project successfully.

# Concepts Needed🗞️:
1. **Greedy Algorithms:**

    * Understanding how greedy algorithms work and why they are suitable for the coin change problem.
    * Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.

2. **Dynamic Programming:**

    * Basic principles of dynamic programming as a method to solve optimization problems.
    * The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.

3. **Algorithmic Complexity:**

    * Analyzing the time and space complexity of algorithms.
    * Striving for solutions with lower complexity to meet runtime constraints.

4. **Problem-Solving Strategies:**

    * Breaking down the problem into smaller, manageable sub-problems.
    * Iterative vs recursive approaches to dynamic programming.

5. **Python Programming:**

    * Manipulating lists and using list comprehensions.
    * Implementing functions with efficient looping and conditional statements.

# Resources🏗️
* **Python Official Documentation🐍:**
    * [More Control Flow Tools (for loops, if statements)](https://docs.python.org/3/tutorial/controlflow.html)

* **GeeksforGeeks Articles📰:**
    * [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
    * [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

* **YouTube Tutorials📹:**
    * [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw) for a visual and step-by-step explanation of the dynamic programming approach.

By thoroughly understanding these concepts and utilizing the provided resources, you will be well-prepared to tackle the coin change problem. You will need to decide whether a greedy algorithm suffices for your particular set of coin denominations or if a more comprehensive dynamic programming approach is necessary to ensure correctness and efficiency. This project not only tests algorithmic skills but also reinforces the importance of choosing the right strategy based on problem constraints.

# Additional Resources 🏣
* [Mock Technical Interview](https://www.youtube.com/watch?v=9BSSIsJ-fWg)

# Requirements 🏛️
<b>General ⛩️</b>

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version 1.7.x)
* All your files must be executable

# Tasks 📃
## 0. Change comes from within: [0-making_change.py](0-making_change.py)
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

* Prototype: `def makeChange(coins, total)`
* Return: fewest number of coins needed to meet `total`
   * If `total` is `0` or less, return `0`
   * If `total` cannot be met by any number of coins you have, return `-1`
* `coins` is a list of the values of the coins in your possession
* The value of a coin will always be an integer greater than `0`
* You can assume you have an infinite number of each denomination of coin in the list
* Your solution’s runtime will be evaluated in this task
```groovy
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```

<div align="center">

# Reference 📚
</div>

A coin system is said to be canonical if the number of coins given in change by the greedy algorithm is the same as the minimum possible number of coins. In other words, the greedy algorithm always yields the optimal solution for a canonical coin system.


For example, the US coin system (1, 5, 10, 25 cents) is canonical. If you need to make 36 cents in change, the greedy algorithm would choose one quarter (25 cents), one dime (10 cents), and one penny (1 cent), for a total of three coins. This is indeed the minimum number of coins that can make 36 cents.


A non-canonical coin system, on the other hand, is one where the greedy algorithm does not always yield the optimal solution.


For example, consider a coin system with coins of 1, 3, and 4. If you need to make 6 units in change, the greedy algorithm would choose one 4-unit coin and two 1-unit coins, for a total of three coins. However, the optimal solution is to use two 3-unit coins, for a total of two coins. So in this case, the greedy algorithm does not yield the optimal solution, and the coin system is non-canonical.


In general, whether a coin system is canonical or non-canonical depends on the specific denominations of the coins. If the denominations have the property that the greedy algorithm always yields the optimal solution, the system is canonical; otherwise, it's non-canonical.

---

Greedy algorithms and dynamic programming are two strategies for solving optimization problems. Here's when you might use each:

**Greedy Algorithm:** You can use a greedy algorithm when the problem has the "greedy property", which means that a global optimum can be arrived at by selecting a local optimum. Greedy algorithms are generally simpler and faster, but they don't always provide the optimal solution.

For example, in the coin change problem, if the coin denominations are canonical (like 1, 5, 10, 25 in the US), a greedy algorithm will provide the optimal solution. This is because the largest denomination coin is always part of the optimal solution, unless that coin's value is greater than the change needed.

**Dynamic Programming:** You can use dynamic programming when the problem can be broken down into overlapping subproblems and the optimal solution to the main problem depends on the optimal solution to its subproblems. Dynamic programming is typically used when the greedy approach does not provide an optimal solution.

For example, in the coin change problem, if the coin denominations are not canonical (like 1, 3, 4), a dynamic programming approach will provide the optimal solution. This is because the optimal solution may involve using fewer coins of a larger denomination in favor of more coins of a smaller denomination.

The greedy algorithm can fail in non-canonical coin systems because it always selects the largest denomination coin without considering the remaining coins. For example, if you have coins of denominations 1, 3, and 4, and you're trying to make change for 6, the greedy algorithm would choose two coins (4 and 1), but the optimal solution is to use two 3-coin.

So, to decide which approach to use, you need to consider whether the problem has the greedy property (i.e., whether choosing a local optimum at each step will lead to a global optimum). If it does, you can use a greedy algorithm. If not, you should use dynamic programming.

---

In the context of optimization problems, a local optimum is the best solution within a neighboring set of candidate solutions, while a global optimum is the best solution among all possible solutions.


**Local Optimum:**
In a problem space, a solution is said to be a local optimum if there are no other solutions in the immediate vicinity that are better. However, there might be better solutions elsewhere in the problem space. 


For example, if you're climbing a hill and you reach a peak, you're at a local optimum because you can't go any higher by just taking a single step in any direction. But there might be a taller peak elsewhere that you can't see from your current position.


**Global Optimum:**
A solution is a global optimum if it's the best possible solution out of all candidate solutions. 


Continuing the hill-climbing example, the highest peak in the entire range is the global optimum. No matter where you are in the range, there's no single step you can take that will get you to a higher point than the top of this peak.


In the context of the coin change problem, a local optimum would be the best solution that can be achieved by changing the next coin, while a global optimum would be the least possible total number of coins that can make up the given amount. The greedy algorithm always chooses the local optimum, while dynamic programming strives to find the global optimum.

---




