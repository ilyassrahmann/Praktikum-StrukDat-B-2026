class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        if self.root is None:
            self.root = Node(id_buku, judul)
            return
        current = self.root
        while True:
            if id_buku == current.id_buku:
                return

            if id_buku < current.id_buku:
                if current.left is None:
                    current.left = Node(id_buku, judul)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(id_buku, judul)
                    return
                current = current.right

    def search(self, id_buku):
        current = self.root
        while current is not None:
            if id_buku == current.id_buku:
                return True
            if id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return False

    def traverse_inorder(self):
        if self.root is None:
            return
        stack = []
        current = self.root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(f"{current.id_buku}({current.judul})")
            current = current.right

    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def height(self):
        if self.root is None:
            return 0
        max_height = 0
        queue = [(self.root, 1)]
        while queue:
            node, depth = queue.pop(0)
            max_height = max(max_height, depth)
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))
        return max_height

bst = BinarySearchTree()
bst.insert(50, "dasar Pemrograman")
bst.insert(30, "struktur Data")
bst.insert(70, "kecerdasan Buatan")
bst.insert(20, "matematika Diskrit")
bst.insert(40, "basis Data")
bst.insert(60, "jaringan Komputer")
bst.insert(80, "sistem Operasi")
print("inorder traversal:")
bst.traverse_inorder()
print("\npencarian Buku:")
cari = [60, 100]
for id_buku in cari:
    found = bst.search(id_buku)
    if found:
        print(f"buku dengan id {id_buku} ditemukan.")
    else:
        print(f"buku dengan id {id_buku} tidak ditemukan.")
min_book = bst.get_min()
max_book = bst.get_max()
print(f"\nbuku dengan id Terkecil: {min_book.judul}({min_book.id_buku})")
print(f"buku dengan id Terbesar: {max_book.judul}({max_book.id_buku})")
print(f"\nheight dari BST: {bst.height()}")


