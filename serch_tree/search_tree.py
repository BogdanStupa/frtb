class Node:
    def __init__(self, bucket_range, bucket_id):
        self.left = None
        self.right = None
        self.bucket_range = bucket_range
        self.bucket_id = bucket_id

    def insert(self, bucket_range, bucket_id):
        if bucket_range[1] < self.bucket_range[0]:
            if self.left is None:
                self.left = Node(bucket_range, bucket_id)
            else:
                self.left.insert(bucket_range, bucket_id)
        else:
            if self.right is None:
                self.right = Node(bucket_range, bucket_id)
            else:
                self.right.insert(bucket_range, bucket_id)

    def find(self, value):
        if value < self.bucket_range[0]:
            if self.left is None:
                return str(value) + " Not Found"
            return self.left.find(value)
        elif value >= self.bucket_range[1]:
            if self.right is None:
                return str(value) + " Not Found"
            return self.right.find(value)
        else:
            return self.bucket_id


class SearchTree:

    def __init__(self):
        self.root = None

    def insert(self, bucket_range, bucket_id):
        if self.root is None:
            self.root = Node(bucket_range=bucket_range, bucket_id=bucket_id)
        else:
            self.root.insert(bucket_range=bucket_range, bucket_id=bucket_id)

    def get_bucket(self, value):
        if self.root:
            return self.root.find(value=value)
        else:
            return False

def print_tree(root):
    if root.left:
        print_tree(root.left)
    print(root.bucket_range, root.bucket_id)
    if root.right:
        print_tree(root.right)
