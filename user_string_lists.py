"""
Modify this docstring.

"""

# imports first

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

text_listA = list('Penne', 'Ziti', 'macaroni', 'ditalini')

text_listB = list('fettuccine', 'Spaghetti', 'rigatoni','angel hair')

text_listC = list('shells', 'tortellini', 'ravoli', 'manicotti')

text_listD = list('ricciol', 'radiatori', 'orecchiette', 'campanelle')

print('these pasta have hollow centers: ', set(text_listA))
print('these are the popular pastas: ', zip(text_listB, text_listC))

import random
random.choice(text_listD)
print('this is an unpopular pasta: ', random.choice(text_listD))

