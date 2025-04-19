from stats import word_count, char_count, sorted_list
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def header_text(book_path, text):
	text = f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ---------- 
Found {word_count(text)} total words 
--------- Character Count ------- """
	return (text)

footer_text = "============= END ==============="

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	print(header_text(book_path, text))
	chars = char_count(text)
	report = sorted_list(chars)
	for key, value in report:
		print(f"{key}: {value}")
	print(footer_text)

main()
