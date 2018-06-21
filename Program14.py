def insert(self,data):
    new_node=Node(data)
    if self.head is None:
        self.head=new_node
        return
    temp=self.head
    while temp:
        if new_node.data<temp.data:
            prev=temp
            temp=temp.left
        else:
            prev=temp
            temp=temp.right
    if new_node.data<prev.data:
        prev.left=new_node
    else:
        prev.right=new_node
def inOrder(self,root):
    if root:
        self.inOrder(root.left)
        print(root.data,end=' ')
        self.inOrder(root.right)
def preOrder(self,root):
    if root:
        print (root.data,end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)
def postOrder(self,root):
    if root:
        self.preOrder(root.left)
        self.preOrder(root.right)
        print (root.data,end=' ')