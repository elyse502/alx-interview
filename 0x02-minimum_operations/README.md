# 0x02. Minimum Operations
For this project, you will need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only “Copy All” and “Paste” operations. Here is a list of concepts and resources that will be helpful:

# Concepts Needed✴️:
1. **Dynamic Programming:**
    * Familiarity with dynamic programming can help in breaking down the problem into simpler subproblems and building up the solution.
    * [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)

2. **Prime Factorization:**
    * Understanding how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number `n`.
    * [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization)

3. **Code Optimization:**
    * Knowing how to approach problems from an optimization perspective can be useful in finding the most efficient solution.
    * [How to optimize Python code](https://stackify.com/how-to-optimize-python-code/)

4. **Greedy Algorithms:**
    * The problem can also be approached with greedy algorithms, choosing the best option at each step.
    * [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)

5. **Basic Python Programming:**
    * Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
    * [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the “Minimum Operations” problem effectively, applying both mathematical reasoning and programming skills to find the most efficient solution.

# Additional Resources 🧰
* [Mock Technical Interview](https://www.youtube.com/watch?v=h4i4kjwncoU)


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
## 0. Minimum Operations: [0-minoperations.py](0-minoperations.py)
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

* Prototype: `def minOperations(n)`
* Returns an integer
* If `n` is impossible to achieve, return `0`

**Example:**

`n = 9`

`H` => `Copy All` => `Paste` => `HH` => `Paste` =>`HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`
```groovy
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```

---

# Reference 📚
For those who have been challenged by the task minimum operations.

Let's say you are given n = 100, so the minimum operations need to copy and paste H can be calculated as:

1) You don't have to copy and paste 100 times. So what you can do is, finding the half.  If you have the first 50 'H's is your text file, then you can copy all and paste it.

Example:
```groovy
n = 100
100/2 = 50. 
Number of operation one= 2
n is now: 50
````

2) Repeat the process until n becomes 1.
```groovy
n = 50
50/2= 25
Number of operation two =  2

n = 25
25/2 ❌
25/3 ❌
25/4 ❌
25/5 ✅

25/5=5
Number of operation three = 5

n = 5
5/5= 1
Number of operation four = 5
```

At last n becomes: `1`, add up all the above operations.

Finally the number of operations: `2+2+5+5=14`

So the minimum operations to copy and paste 'H' 100 times is `14`.

## FeedBack from Peers:
1. If you really think about it, it's the sum of prime factors, the math is mathing....😆


