maxNum = int(input("Enter max number:"))
oddNums = []
for i in range(maxNum + 1):
    if i % 2 != 0:
        oddNums.append(i)
print(oddNums)