import functools
fruits = ["Яблоко", "Банан", "Груша", "Абрикос", "Апельсин"]
third_list = filter(lambda a: len(a) > 5, fruits)
print(list(third_list))


result = map(lambda a: len(a) > 5, fruits)
result_2 = map(lambda a: len(a), fruits)
print(list(result))
print(list(result_2))
a = functools.reduce(lambda k, w: k+w, [1,2,3,4])
print(a)
e = input("------- > ")
print(e)

d = type(3)
print(d)
d = type("gggg")
print(d)
d = type(3.00005)
print(d)

g = int(input('Number:  '))
f = bin(g)
print(f)
a = input("first ")
b = input("second ")
c = input("third ")
s = '{0}, {1}, {2}'.format(a, b, c)
print(s)
