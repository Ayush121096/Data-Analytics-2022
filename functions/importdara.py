import random
def generate_name():
    list1 = ['red', 'orange', 'green', 'yellow', 'black']
    list2 = ['apple', 'banana', 'pear', 'grapes']
    list3 = ['cat', 'dog', 'bird', 'fish']
    
    p1 = random choice (list1)
    p2 = random choice (list2)
    p3 = random choice (list3)

    return f'{p1}-{p2}-{p3}'
