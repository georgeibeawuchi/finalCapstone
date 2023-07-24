#this is the code for splitting individual letters
words = "hello world"
char = 1

print("The original is: " + str(words))

alt = ""
res = ""
for index in range (len(words)):
    if not index % 2:
        res = res + words[index].upper()
    else:
        res = res + words[index].lower()

print("The alternative is: " + str(res))


#this is the code for splitting whole words
sentence = "these alternate very well"

print("The original is: " + sentence)

new_string = input("Please enter a string: ").split()
char_storage = " ".join([x.upper() if i % 2 else x.lower() for i, x in enumerate(new_string)])
print(char_storage)
