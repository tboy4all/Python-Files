# def gensquares(n):
#         for num in range(n):
#             yield num**2

# for x in gensquares(10):
#     print(x)


# # Fibonaccoi series

# def fib_with_generator(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#          # a,b = b, a+b -> tuple unpacking instead of the three lines below!
#         temp = a
#         a = b
#         b = temp + b

# for num in fib_with_generator(10):
#     print(num)

# Using Next function

#def use_next():
#     for x in range(10):
#         yield x

# # gen = use_next()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# for val in use_next():
#     print(val)

#       OR

    #return print((x for x in range(10)))


# Using iterator

str = "hello"
str_iter = iter(str)
next(str_iter) # h
next(str_iter) # e
next(str_iter) # l
next(str_iter) # l
next(str_iter) # o
#next(str_iter) # StopIteration Error!


# Using Enumerate to list both element and index i.e (index, value)

list = ['first','second','third']

# How do we get the indices at each iteration? Enumerate!

for idx, value in enumerate(list):
	print(f"index is {idx} and value is {value}")