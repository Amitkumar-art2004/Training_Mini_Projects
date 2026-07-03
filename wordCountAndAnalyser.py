
para = input("Enter a paragraph : ");
count = 1;
vowels = "aeiouAEIOU"
vowelsCount = 0
for i in para:
    if i == " ":
        count += 1;
    if i in vowels:
        vowelsCount += 1
print("Total words present in paragraph :",count)
print("Total vowels present in paragraph :",vowelsCount)

words = para.split() 
longest = ""
for i in words:
    if len(i) > len(longest):
        longest = i
print("Longest word is :", longest)
