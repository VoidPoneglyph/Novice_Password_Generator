import random
def Convert(String): # function to convert string into list
    lis = []
    lis[:0] = String
    return lis

def ListToString(lis1): # function to convert list to string
    str1 = ""
    for s in lis1:
        str1 = str1 + s
    return str1


def password_generator(): # main function
    lowerchars = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9']
    specialchars = ['%', '!', '$','#','@','&','*']
    upperchars = [str(x.upper()) for x in lowerchars]
    password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(numbers) + random.choice(specialchars) + random.choice(lowerchars) + random.choice(upperchars) + random.choice(numbers) + random.choice(specialchars)
    z = int(input('Enter the number of characters for your password - please note that the minimum is 4 chars and you can choose between - 8 chars/16 chars/24 chars/32 chars'))
    z = z//8

    generator = str(password) * z # repeats the randomized set of characters, however we randomize(shuffle) it again
    # in the next few lines of code.
    generator = Convert(generator)
    final_pw = random.sample(generator,z*8) # shuffles the list of password characters specified by it's character size
    # so that the pattern doesn't repeat itself
    final_pw = ListToString(final_pw) # converts this list into the string form
    print(final_pw)


print(password_generator())
