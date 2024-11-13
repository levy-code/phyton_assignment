import tkinter as tk

class PalindromeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Palindrome Checker")
        self.configure(bg='#D4A5A5')

        self.label_1 = tk.Label(self, text="Enter a word or sentence to check if it's a palindrome:", fg='#ddf3f5', bg='#D4A5A5')
        self.label_1.pack(pady=(10, 5))
        self.entry_0 = tk.Entry(self, bg='#ddf3f5', width=40)
        self.entry_0.pack(pady=(0, 10))
        self.label_2 = tk.Label(self, fg='#ddf3f5', bg='#D4A5A5')
        self.label_2.pack(pady=(5, 10))
        self.btn = tk.Button(self, text='Check', command=self.check_palindrome, bg='#D4A5A5', fg='#ddf3f5')
        self.btn.pack()

    def check_palindrome(self):
        input_text = self.entry_0.get()
        cleaned_text = ''.join(char.lower() for char in input_text if char.isalpha())
        if cleaned_text == cleaned_text[::-1]:
            self.label_2['text'] = f"'{input_text}' is a palindrome!"
        else:
            self.label_2['text'] = f"'{input_text}' is not a palindrome."

if __name__ == '__main__':
    app = PalindromeApp()
    app.mainloop()
