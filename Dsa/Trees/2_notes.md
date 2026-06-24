# Day 2 - Binary Trees Revision Notes

---

# Kth Level of a Tree

## Idea

Given a level `K`, recursively move down the tree while decrementing `K`.

When:

```python
k == 1
```

we have reached the required level, so print the node.

---

## Algorithm

1. Start from root with level `K`.
2. Move to left and right child with `K-1`.
3. When `K == 1`, print the current node.

---

## Code

```python
def kthLvl(root, k):

    if root is None:
        return

    if k == 1:
        print(root.val)
        return

    kthLvl(root.left, k - 1)
    kthLvl(root.right, k - 1)
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

where:

- `N` = Number of Nodes
- `H` = Height of Tree

---

# Lowest Common Ancestor (LCA)

## Definition

The Lowest Common Ancestor of two nodes `p` and `q` is the deepest node that has both nodes in its subtree.

---

## Cases

### Case 1

```text
leftLca = None
rightLca = None
```

Return:

```python
None
```

---

### Case 2

```text
leftLca != None
rightLca == None
```

Return:

```python
leftLca
```

---

### Case 3

```text
leftLca == None
rightLca != None
```

Return:

```python
rightLca
```

---

### Case 4

```text
leftLca != None
rightLca != None
```

Current node becomes LCA.

Return:

```python
root
```

---

## Code

```python
def Lca(root, p, q):

    if root is None:
        return None

    if root == p or root == q:
        return root

    leftLca = Lca(root.left, p, q)
    rightLca = Lca(root.right, p, q)

    if leftLca and rightLca:
        return root

    elif leftLca:
        return leftLca

    else:
        return rightLca
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

# Build Tree from Preorder and Inorder

---

## Traversals

### Preorder

```text
Root Left Right
```

### Inorder

```text
Left Root Right
```

---

## Key Idea

The first element of preorder is always the root.

Example:

```python
preorder = [3,9,20,15,7]
```

Root:

```text
3
```

Find `3` inside inorder:

```python
inorder = [9,3,15,20,7]
```

```text
9 | 3 | 15 20 7
```

Everything left of root belongs to left subtree.

Everything right of root belongs to right subtree.

Recursively repeat the process.

---

## Example

```python
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

```text
9 3 15 20 7
0         4
L         R
```

---

## Code

```python
class Solution(object):

    def search(self, inorder, left, right, val):

        for i in range(left, right + 1):
            if inorder[i] == val:
                return i

        return -1

    def helper(self, preorder, inorder, left, right):

        if left > right:
            return None

        root = TreeNode(preorder[self.preIdx])

        self.preIdx += 1

        inIdx = self.search(
            inorder,
            left,
            right,
            root.val
        )

        root.left = self.helper(
            preorder,
            inorder,
            left,
            inIdx - 1
        )

        root.right = self.helper(
            preorder,
            inorder,
            inIdx + 1,
            right
        )

        return root

    def buildTree(self, preorder, inorder):

        self.preIdx = 0

        return self.helper(
            preorder,
            inorder,
            0,
            len(inorder) - 1
        )
```

---

## Complexity

### Time Complexity

```text
O(N²)
```

Reason:

```text
Every recursive call performs a linear search in inorder.
```

Can be optimized to:

```text
O(N)
```

using a hashmap.

---

### Space Complexity

```text
O(H)
```

---

# Transform to Sum Tree

---

## Definition

Convert a tree such that every node stores:

```text
Sum of values present in its left subtree
+
Sum of values present in its right subtree
```

---

## Idea

Use Postorder Traversal:

```text
Left
Right
Root
```

because we need the sums of children before updating the current node.

---

## Algorithm

1. Recursively calculate left subtree sum.
2. Recursively calculate right subtree sum.
3. Update current node.
4. Return subtree sum.

---

## Code

```python
def transform(root):

    if root is None:
        return 0

    leftSum = transform(root.left)
    rightSum = transform(root.right)

    root.val = leftSum + rightSum

    return root.val
```

---

## Complexity

### Time Complexity

```text
O(N)
```

Every node is visited once.

---

### Space Complexity

```text
O(H)
```

where:

- `H` = Height of Tree

---

# Patterns Learned

| Problem | Pattern |
|----------|----------|
| Kth Level | DFS with Level Tracking |
| LCA | DFS Returning Node |
| Build Tree (Pre + In) | Tree Construction |
| Transform to Sum Tree | Postorder DFS |

---