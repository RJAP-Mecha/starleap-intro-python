
# ##### Template for Chapter 5.14, Exercises 1 - 4 ######


# print("********** Ch 5 Exercise 1 **********")

# # def time_since_epoch():
# #     import time
# #     t = time.time()
# #     print("t = ", t)
# #     days = int(t // 60 // 60 // 24)
# #     print("days = ", days)
# #     remainder = t % (days * 60 * 60 * 24)
# #     print("remainder = ", remainder)

# # time_since_epoch()
    




# print("********** Ch 5 Exercise 2 **********")

# # Do your work for Excercise 2 here.




# print("********** Ch 5 Exercise 3 **********")

def is_triangle(a, b, c):
     print('is_triangle()', a, b, c)
     if a >= b + c:
      print('No')
     elif b >= a + c:
      print('No')
     elif c >= a + b:
      print('No')
     else:
        print('Yes')


is_triangle(3, 4, 5)
is_triangle(2, 1, 1)

a = float(input('How long is side a? '))
print('a is', a, type(a))
b = float(input('How long is side b?' ))
print('b is', b, type(b))
c = float(input('How long is side c? '))
print('a is', c, type(c))

is_triangle(a, b, c,)





# print("********** Ch 5 Exercise 4 **********")
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)





# Do your work for Exercise 4 here.

