words = {}
with open("poem.txt",'r') as f:
    for line in f:
        lineWords = line.split(" ")
        for j in lineWords:
            j = j.replace("\n","")
            if j in words:
                words[j] += 1
            else:
                words[j] = 1
print(words)