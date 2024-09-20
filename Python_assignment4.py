input_words = input("Please input your word: ")
list_words = list(input_words)
print(f"Your word in letters: {list_words}")
list_words.reverse()
print(f"Your word in reverse: {list_words}")
string_from_list = "".join(list_words)
print(f"Joined word from reverse: {string_from_list}")
print(f"Is the word palindrome? {string_from_list == input_words}")





