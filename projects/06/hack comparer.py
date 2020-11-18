
file1 = open(input("input name of first file: "), "r")
file2 = open(input("input name of second file: "), "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

for line_index in range(len(lines1)):
    if lines1[line_index] != lines2[line_index]:
        print(f"disparity between lines:\nl1: {lines1[line_index]}\nl2: {lines2[line_index]}")
        input("")
