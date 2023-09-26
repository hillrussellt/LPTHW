from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("If you don't want that hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm doing to ask you for three lines.")

l1 = input("line 1: ")
l2 = input("line 2: ")
l3 = input("line 3: ")
full = (f"{l1}\n{l2}\n{l3}\n")

print("I'm going to write these to the file.")

target.write(full)

print("And finally, we can close it.")
target.close()
