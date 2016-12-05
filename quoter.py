import random
lines = open('Quotes.txt').read().splitlines()
myline =random.choice(lines)
print(myline)
