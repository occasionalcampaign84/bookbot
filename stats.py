def word_count(s):
	return len(s.split())

def char_count(s):
	counts = {}
	for char in s:
		char = char.lower()
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
	return counts

def sorted_list(dictionary):
	return sorted(dictionary.items(), key = lambda item: item[1], reverse = True)
