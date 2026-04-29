#Program counts the word frequencies but produces incorrect results
words = "red blue red green blue blue".split()
counts = {}

for word in words:
    counts[word] = counts[word] + 1
#Program tries to use counts["red] which doesn't exist yet
print(counts)

#----------------------------------------------------------------------------


words = "red blue red green blue blue".split()
counts = {}
#Add defensive code to account for nonexisting counts
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

print(counts)
