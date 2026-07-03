passage = input("Enter a passage: ")
words = passage.lower().split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
sorted_words = sorted(frequency.items(),key=lambda item: item[1],reverse=True);

print(sorted_words)
print("\nTop 5 Most Frequent Words:")

for word, count in sorted_words[:5]:
    print(word, ":", count)
