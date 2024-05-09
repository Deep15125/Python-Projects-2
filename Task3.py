# Author --> Deep Gupta
def read_and_replace(file_path, old_word, new_word):
    with open(file_path, 'r+') as file:
        data = file.read()
        data = data.replace(old_word, new_word)
        file.seek(0)
        file.write(data)
        file.truncate()

file_path = 'example.txt'
old_word = str(input("Enter the Word you want to change:"))
new_word = str(input("Enter the new word to change:"))

read_and_replace(file_path, old_word, new_word)