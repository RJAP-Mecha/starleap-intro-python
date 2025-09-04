def print_lyrics():
    print('Boots')
    print('Cats')             

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    print_lyrics()

# repeat_lyrics()

def print_twice(input):
    print(input)
    print(input)

# print_twice('Spam'* 999)

def is_it_even(input):
    if input % 2 == 0:
        print ('It is even')
    else:
        print('It is odd')

    
# is_it_even(4)


def compare(x,y):
    if x < y:
        print(str(x)+'is less than'+str(y))
    elif x > y:
        print(str(x)+'is greater than'str(y))
    else:
        print(str)
