def main():
    path = "books/frankenstein.txt"
    text = print_text(path)
    book_len = word_count(text)
    chars = char_count(text)
    summary = report(chars, book_len)
    print(summary)
    



def print_text(path):
	with open("books/frankenstein.txt") as f:
		contents = f.read()
	return contents


def word_count(text):
	words = text.split()
	num_words = len(words)
	return num_words

def char_count(text):
	dictionary = {}
	lowered = text.lower()
	for letter in lowered:
		if letter in dictionary:
			dictionary[letter] += 1
		else:
			 dictionary[letter] = 1
	return dictionary

def report(chars, book_len):
	char_list = []
	for key, value in chars.items():
		if key.isalpha():
			new_dic = {"char": key, "num": value}
			char_list.append(new_dic)
	char_list.sort(key=lambda x: x["num"], reverse=True)
	print("---Begin report---")
	print(f"{book_len} words found in document")
	for entry in char_list:
		char = entry["char"]
		count = entry["num"]
		print(f"The '{char}' character was found {count} times")
	print("---End report---")




main()
