# Binary Trees — Revision Notes 1

---

# 1. Height / Depth of Binary Tree

### Definition

Height (or maximum depth) = Number of nodes on the longest path from root to a leaf.

### Recursive Idea

For every node:

```text
height(node)
=
max(height(left), height(right)) + 1
```

### Code

```python
def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1
```

### Complexity

```text
Time  : O(N)
Space : O(H)
```

(H = height of tree)

---

# 2. Count Total Nodes

### Idea

Count nodes in left subtree +
Count nodes in right subtree +
Current node

### Formula

```text
count(root)
=
count(left)
+
count(right)
+
1
```

### Code

```python
def count(root):
    if root is None:
        return 0

    left_count = count(root.left)
    right_count = count(root.right)

    return left_count + right_count + 1
```

### Complexity

```text
Time  : O(N)
Space : O(H)
```

---

# 3. Sum of All Nodes

### Idea

Sum of left subtree +
Sum of right subtree +
Current node value

### Formula

```text
sum(root)
=
sum(left)
+
sum(right)
+
root.val
```

### Code

```python
def tree_sum(root):
    if root is None:
        return 0

    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)

    return left_sum + right_sum + root.val
```

### Complexity

```text
Time  : O(N)
Space : O(H)
```

---

# 4. Identical Trees

### Problem

Check whether two trees have:

* Same structure
* Same values

### Conditions

```text
1. Both NULL → True
2. One NULL → False
3. Values must match
4. Left subtrees identical
5. Right subtrees identical
```

### Code

```python
def isSameTree(p, q):

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val == q.val:
        return (
            isSameTree(p.left, q.left)
            and
            isSameTree(p.right, q.right)
        )

    return False
```

### Complexity

```text
Time  : O(N)
Space : O(H)
```

---

# 5. Subtree of Another Tree

### Problem

Check if `subRoot` exists somewhere inside `root`.

### Approach

For every node in root:

```text
If current node == subRoot root:
    Check if both trees are identical

Else:
    Search left subtree
    Search right subtree
```

---

### Helper Function

```python
def isIdentical(p, q):
    if p is None or q is None:
        return p == q

    return (
        p.val == q.val
        and isIdentical(p.left, q.left)
        and isIdentical(p.right, q.right)
    )
```

---

### Main Function

```python
def isSubtree(root, subRoot):

    if root is None or subRoot is None:
        return root == subRoot

    if isIdentical(root, subRoot):
        return True

    return (
        isSubtree(root.left, subRoot)
        or
        isSubtree(root.right, subRoot)
    )
```

### Complexity

```text
Worst Case:
O(M × N)

M = nodes in root
N = nodes in subRoot
```

---

# 6. Diameter of Binary Tree

### Definition

Longest path between any two nodes.

### Key Observation

At every node:

```text
Diameter through node
=
left height + right height
```

---

## Brute Force (O(N²))

### Idea

For every node:

```text
Find left height
Find right height
Compute diameter
```

But height is recomputed repeatedly.

### Code

```python
def height(root):
    if root is None:
        return 0

    return max(
        height(root.left),
        height(root.right)
    ) + 1


def diameter(root):
    if root is None:
        return 0

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    curr_diameter = (
        height(root.left)
        +
        height(root.right)
    )

    return max(
        left_diameter,
        right_diameter,
        curr_diameter
    )
```

### Complexity

```text
Time : O(N²)
```

---

## Optimized (O(N))

### Trick

While calculating height,
also update diameter.

### Code

```python
ans = 0

def height(root):
    global ans

    if root is None:
        return 0

    leftHt = height(root.left)
    rightHt = height(root.right)

    ans = max(ans, leftHt + rightHt)

    return max(leftHt, rightHt) + 1


def diameter(root):
    height(root)
    return ans
```

### LeetCode Style

```python
class Solution:
    def diameterOfBinaryTree(self, root):

        self.ans = 0

        def height(root):
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            self.ans = max(
                self.ans,
                left + right
            )

            return max(left, right) + 1

        height(root)

        return self.ans
```

### Complexity

```text
Time  : O(N)
Space : O(H)
```

---

# 7. Maximum Depth of Binary Tree (BFS)

### Problem

Return maximum depth using Level Order Traversal.

### Key Idea

Each BFS iteration processes exactly one level.

### Code

```python
from collections import deque

class Solution:
    def maxDepth(self, root):

        if root is None:
            return 0

        q = deque([root])
        lvl = 0

        while q:

            size = len(q)

            for _ in range(size):

                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            lvl += 1

        return lvl
```

### Complexity

```text
Time  : O(N)
Space : O(W)
```

(W = maximum width)

---

# 8. Maximum Level Sum of Binary Tree

### Problem

Find the level having maximum sum.

If multiple levels have same maximum sum:

```text
Return smallest level number
```

---

### Approach

Use BFS.

For every level:

```text
Compute current level sum

If current sum > max_sum:
    Update answer
```

---

### Code

```python
from collections import deque

class Solution:
    def maxLevelSum(self, root):

        max_sum = float('-inf')

        lvl = 1
        ans = 1

        q = deque([root])

        while q:

            size = len(q)
            curr_sum = 0

            for _ in range(size):

                node = q.popleft()

                curr_sum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = lvl

            lvl += 1

        return ans
```

### Complexity

```text
Time  : O(N)
Space : O(W)
```

---

# Binary Tree Patterns Cheat Sheet

### Postorder Pattern

Used for:

```text
Height
Count Nodes
Sum Nodes
Diameter
Balanced Tree
```

Template:

```python
def solve(root):

    if root is None:
        return BASE

    left = solve(root.left)
    right = solve(root.right)

    return PROCESS(left, right, root)
```

---

### DFS Comparison Pattern

Used for:

```text
Identical Tree
Subtree
Symmetric Tree
```

Template:

```python
def compare(p, q):

    if p is None or q is None:
        return p == q

    return (
        p.val == q.val
        and compare(p.left, q.left)
        and compare(p.right, q.right)
    )
```

---

### BFS Level Order Pattern

Used for:

```text
Maximum Depth
Level Sum
Level Average
Right Side View
Zigzag Traversal
```

Template:

```python
q = deque([root])

while q:

    size = len(q)

    for _ in range(size):
        node = q.popleft()

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
```

If you master these **3 patterns (Postorder, Compare DFS, BFS Level Order)**, you'll solve a large portion of common binary tree interview questions.
