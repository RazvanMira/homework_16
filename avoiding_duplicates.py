words_list = []

more_words = True
while more_words:
    word = input("Please type in a word or type in a blank line to stop: ")
    if word == " ":
        more_words = False
    else:
        if word in words_list:
            pass
        else:
            words_list.append(word)

print(words_list)
for i in range (0, len(words_list)):
    print(words_list[i])