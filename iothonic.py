# Read the number of lines
N = int(input("number of lines").strip())

# Initialize counters for 't'/'T' and 's'/'S'
count_t = 0
count_s = 0

# Process each line of text
for _ in range(N):
    line = input("enter the lines: ").strip()
    count_t += line.count('t') + line.count('T')
    count_s += line.count('s') + line.count('S')

# Determine and print the language
if count_t > count_s:
    print("English")
else:
    print("French")
