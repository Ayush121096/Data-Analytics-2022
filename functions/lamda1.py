# Lamda is used to solve mathematical question in pythan

# f(x) = x + x - 3 * 5

f = lambda x: x + x - 3 * 5

print(f(2))
print(f(3))
print(f(1.6))




g = lambda x,y: (x * y) - (x // y)

print(g(3,4))
print(g(12,10))

# mapping is used when you need to add some values in every values basically it used in list value


a = [2,1,3,5,6,7,]
num = 10 # which i want to add

a = list(map(lambda i: i + num, a))
print(a)



a = (1,2,3,4,5,6)
b = (4,5,6,7,8,9)

k = list(map(lambda j,i: j + i,a ,b ))
print(k)


# filter; is used for get only single value

x = [1,2,3,4,5,5,5,5,6,7,8,8,8,9,9,9,4,4,4,]

x = list(filter(lambda i: i == 4, x))
print(x)



x = list(range(1,100))

x35 = list((lambda i: i % 3 == 0 and i % 5 == 0, x))
print(x35)