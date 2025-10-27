class NoAVL:
    def __init__(self, key, cidade=None):
        self.key = key
        self.cidade = cidade
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    AVL - Árvore Binária de Busca Auto-Balanceada
    - Inserção: O(log n)
    - Remoção: O(log n)
    - Busca: O(log n)
    """

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    # Rotações
    def rotate_right(self, y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def rotate_left(self, x):
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    # Inserção com balanceamento
    def insert(self, node, key, cidade=None):
        if not node:
            return NoAVL(key, cidade)

        if key < node.key:
            node.left = self.insert(node.left, key, cidade)
        else:
            node.right = self.insert(node.right, key, cidade)

        return self._rebalance(node)

    # Remoção com rebalanceamento
    def remove(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self.remove(node.left, key)
        elif key > node.key:
            node.right = self.remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.cidade = temp.cidade
            node.right = self.remove(node.right, temp.key)
        return self._rebalance(node)

    # Percursos
    def inorder(self, node):
        return [] if not node else self.inorder(node.left) + [node.key] + self.inorder(node.right)

    def preorder(self, node):
        return [] if not node else [node.key] + self.preorder(node.left) + self.preorder(node.right)

    def postorder(self, node):
        return [] if not node else self.postorder(node.left) + self.postorder(node.right) + [node.key]

    # Funções auxiliares
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _rebalance(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        # Casos de desbalanceamento
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
