mammal = ['cat', 'dog', 'cat', 'cat', 'tiger']
while 'cat' in mammal:
    mammal[mammal.index('cat')] = 'lion'

print(mammal)
