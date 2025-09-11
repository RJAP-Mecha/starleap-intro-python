
##### Template for Chapter 3.14, Exercises 1 - 3 ######


print("********** Ch 3 Exercise 1 **********")

# def right_justify(input):
   # length = len(input)
   # print("length = ", length)
   # target = 70
   # spaces = target - length
   # space_string = ' '*spaces
   # print(space_string + input)

#ight_justify('WAAAAAAAAAH')
#right_justify('WAAAAAAAAAH')
#right_justify('WAAAAAAAAAH')
#right_justify('reeeeeeeeeeeeeeeeeeee')
#ight_justify('dsdsfdsffdsffdsfdssfsd')

print("Ch 3 Exercise 1: Not implemented") # Delete this line when you write your code!





#def do_twice(f):
#f()
#f()

#def print_spam():
    #print('spam')

#do_twice(print_spam)

#print("Ch 3 Exercise 2: Not implemented") # Delete this line when you write your code!



#print("********** Ch 3 Exercise 3 **********")

# Do your work for Exercise 3 here.

print("Ch 3 Exercise 3: Not implemented") # Delete this line when you write your code!      

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()