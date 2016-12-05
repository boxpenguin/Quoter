import random
lines = open('quotes.txt').read().splitlines()
myline =random.choice(lines)
print(myline)
