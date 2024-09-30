input_text = input("Please enter a word or sentence: ")
cleaned_text = ""
for char in input_text:
        if char.isalpha():
                cleaned_text += char.lower()
input_words = list(cleaned_text)
input_words.reverse()
words_joined = "".join(input_words)

if cleaned_text == words_joined:
        print(f"'{input_text}' is a palindrome.")

else:
    print(f"'{input_text}' is not a palindrome.")
        
        

    
    
