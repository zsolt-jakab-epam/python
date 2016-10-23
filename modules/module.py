c = "a"
print(" id : " + str(id(c)))

def func(a):
    c = 9
    print(c)
    print("FUNCTION")
    a += "10"
    print(a)
    print(" id : " + str(id(a)))
    return a

c = func(c)
print("MAIN")

print(c)
print(" id : " + str(id(c)))
print("hello")

c = 2
c = None

class Node(object):
     
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

    
head = Node(5)

def print_list(head):
    if head != None:
        print(head.data)    
        print_list(head.next)

print_list(head)