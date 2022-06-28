import random  #first import function


for i in range(10):
    print(random.random()) # for random values except 0,1,


for i in range(10):
        print(random.randint(1, 105), end='') 


smile = [😊, 😁, 😐]
print(random.choice(smile))


print(random.choices(smile, k=3))


