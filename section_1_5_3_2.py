name = input('Enter a name: ')

for index, _ in enumerate(name):
    print(name[:index])

print(name)