# Day 3 - Binary Trees (DFS Path Problems & BFS Width)

---

# 1. All Root to Leaf Paths

## Problem

Return all paths from root node to leaf nodes.

Example:

```text
      1
     / \
    2   3
     \
      5
```

Output:

```python
[[1,2,5],[1,3]]
```

---

## Pattern

```text
DFS + Path State
```

Each recursive call carries its own copy of the path.

---

## Key Learning

Instead of:

```python
temp.append(root.val)
```

use:

```python
temp = temp + [root.val]
```

This creates a new list for every recursive call and avoids path corruption.

---

## Code

```python
class Solution:
    def allRootToLeaf(self, root):

        self.l = []

        def pathfinder(root, path):

            if root is None:
                return

            path = path + [root.data]

            if root.left is None and root.right is None:
                self.l.append(path)
                return

            pathfinder(root.left, path)
            pathfinder(root.right, path)

        pathfinder(root, [])

        return self.l
```

---

## Complexity

### Time Complexity

```text
O(N)
```

### Space Complexity

```text
O(H)
```

---

# 2. Path Sum I

## Problem

Determine whether there exists a root-to-leaf path whose sum equals the target sum.

---

## Pattern

```text
DFS + Running Sum
```

---

## Idea

Maintain a running sum while traversing.

At every leaf node:

```python
currSum == targetSum
```

---

## Code

```python
class Solution(object):

    def hasPathSum(self, root, targetSum):

        self.l = set()

        def pathfinder(root, currSum):

            if root is None:
                return

            currSum += root.val

            if root.left is None and root.right is None:
                self.l.add(currSum)
                return

            pathfinder(root.left, currSum)
            pathfinder(root.right, currSum)

        pathfinder(root, 0)

        return targetSum in self.l
```

---

## Better Interview Approach

Instead of storing all sums:

```python
return left or right
```

directly from DFS.

---

## Complexity

### Time Complexity

```text
O(N)
```

### Space Complexity

```text
O(H)
```

---

# 3. Path Sum II

## Problem

Return all root-to-leaf paths whose sum equals the target sum.

---

## Pattern

```text
DFS + Running Sum + Path State
```

---

## Key Learning

Combines:

```text
Binary Tree Paths
+
Path Sum
```

---

## Code

```python
class Solution(object):

    def pathSum(self, root, targetSum):

        self.l = []

        def pathfinder(root, currSum, temp):

            if root is None:
                return

            currSum += root.val
            temp = temp + [root.val]

            if root.left is None and root.right is None:

                if targetSum == currSum:
                    self.l.append(temp)

                return

            pathfinder(root.left, currSum, temp)
            pathfinder(root.right, currSum, temp)

        pathfinder(root, 0, [])

        return self.l
```

---

## Complexity

### Time Complexity

```text
O(N)
```

### Space Complexity

```text
O(H)
```

---

# 4. Maximum Width of Binary Tree

## Problem

Find the maximum width among all levels of a binary tree.

---

## Pattern

```text
BFS + Position Indexing
```

---

## Core Idea

Treat the tree like a complete binary tree.

Assign positions:

```text
Root = 0

Left Child  = 2*i
Right Child = 2*i + 1
```

---

## Example

```text
        1(0)
       /   \
    2(0)   3(1)
    /         \
 4(0)         7(3)
```

Width:

```text
3 - 0 + 1 = 4
```

---

## Normalization

At every level:

```python
pos -= left_pos
```

to avoid extremely large numbers.

---

## Code

```python
class Solution(object):

    def widthOfBinaryTree(self, root):

        if root is None:
            return 0

        queue = deque([(root, 0)])

        ans = 0

        while queue:

            size = len(queue)

            left_pos = queue[0][1]
            right_pos = queue[-1][1]

            ans = max(
                ans,
                right_pos - left_pos + 1
            )

            for _ in range(size):

                node, pos = queue.popleft()

                pos -= left_pos

                if node.left:
                    queue.append(
                        (node.left, 2 * pos)
                    )

                if node.right:
                    queue.append(
                        (node.right, 2 * pos + 1)
                    )

        return ans
```

---

## Complexity

### Time Complexity

```text
O(N)
```

### Space Complexity

```text
O(N)
```

(BFS Queue)

---

# Day 3 Patterns Learned

| Problem | Pattern |
|----------|----------|
| All Root to Leaf Paths | DFS + Path State |
| Path Sum I | DFS + Running Sum |
| Path Sum II | DFS + Running Sum + Path |
| Maximum Width of Binary Tree | BFS + Position Index |

---

# Biggest Learning of the Day

## Shared Mutable State vs New State

Wrong:

```python
temp.append(root.val)
```

Why?

```text
Both recursive branches share the same list.
```

Correct:

```python
temp = temp + [root.val]
```

Why?

```text
Every recursive call gets its own copy of the path.
```

This pattern will appear again in:

- Binary Tree Paths
- Path Sum II
- Subsets
- Combination Sum
- Permutations
- Backtracking Problems

---

# Revision Keywords

```text
Binary Tree Paths  -> DFS + Path

Path Sum I         -> DFS + Running Sum

Path Sum II        -> DFS + Running Sum + Path

Maximum Width      -> BFS + Position Index
```