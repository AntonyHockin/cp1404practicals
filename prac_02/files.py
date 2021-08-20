# 1.
OUTPUT_FILE = 'name.txt'
name = input("Enter your name: ")
out_file = open(OUTPUT_FILE, 'w')
print(name, file=out_file)
out_file.close()

# 2.
INPUT_FILE = 'name.txt'
in_file = open(INPUT_FILE, 'r')
print(f"Your name is {in_file.read()}")
in_file.close()

# 3.
INPUT_FILE = 'numbers.txt'
in_file = open(INPUT_FILE, 'r')
total = 0
for i in range(0, 2):
    total += int(in_file.readline())
print(total)
in_file.close()

# 4.
INPUT_FILE = 'numbers.txt'
in_file = open(INPUT_FILE, 'r')
total = 0
for line in in_file:
    total += int(line)
print(total)
in_file.close()
