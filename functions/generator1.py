#
def get_cube(*args):
    for i in args:
        yield  i ** 3

get_cube()


for i in get_cube(1, 5, 87):
    print(i)



# for short form of any word

def acronym_generator(listofword):
    for word in listofword:
        w1 = word.spliy()
        acr = ''
        for w in w1:
            acr += w[0] .upper()
        yield acr

word = ['Project Manager', 'Software Engineer']
for acr in  