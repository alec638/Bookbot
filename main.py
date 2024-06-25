def main():
    path = "books/frankenstein.txt"
    text = print_text(path)
    print(text)
    book_len = word_count(text)
    print(f"{book_len} words found in the document")
    chars = char_count(text)
    print(chars)

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

main()
