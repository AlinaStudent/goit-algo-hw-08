# ---------------------------
# Базова структура вузла BST
# ---------------------------
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# ---------------------------
# Завдання 1: мінімум у BST/AVL
# ---------------------------
def find_min(root: Node):
    """Повертає мінімальний ключ у дереві. Якщо дерево порожнє — None."""
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.key

# ---------------------------
# Завдання 2: сума всіх значень у BST/AVL
# ---------------------------
def sum_tree(root: Node) -> int:
    """Повертає суму всіх ключів у дереві. Якщо дерево порожнє — 0."""
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)

# ---------------------------
# Завдання 3: мінімальна вартість з’єднання кабелів (мін-купа)
# ---------------------------
import heapq

def minimize_cable_cost(lengths):
    """
    Приймає список довжин кабелів.
    Повертає мінімальну можливу суму витрат на з’єднання.
    """
    if not lengths:
        return 0
    if len(lengths) == 1:
        return 0

    heap = lengths[:]
    heapq.heapify(heap)
    total_cost = 0

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        heapq.heappush(heap, cost)

    return total_cost
