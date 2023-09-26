from sys import argv

script, filename = argv

try:
    with open(filename, 'r') as file:
        print(file.read())
except Exception as e:
    print(e)
