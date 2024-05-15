with open("/Users/vladislavcehov/cs_lab_18/test.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    if '-' in line[0]:
        print(line)
