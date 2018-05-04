import random, string, time

class URLShortener:

	def __init__(self):
		self.urls = {}
		self.shorts = {}
		# a-z, A-Z, 0-9 = 62 possible characters
		self.alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
		self.numerals = [str(i) for i in range(0, 10)]
		self.possible_characters = self.alphabet + self.numerals

	def shorten(self, url):
		if url in self.shorts:
			# check if we already have it
			return self.shorts[url]
		url_hash = self.generate_bijective_hash(url)
		# store twice: once with hash as key, once with url as key
		# alternative: store the URL as a prefix tree
		self.urls[url_hash] = url
		self.shorts[url] = url_hash
		return url_hash

	def restore(self, short):
		try:
			return self.urls[short]
		except KeyError:
			return None # or "not found"

	def restore_bijective_hash(self, short):
		digits = []
		for char in list(short):
			digit = self.possible_characters.index(char)
			digits.append(str(digit))
		key = int("".join(digits[::-1]))
		return int("".join([str(i) for i in self.convert_base(key, 10)]))


	def generate_hash(self, url):
		output_hash = [] 
		random.seed(time.time() // len(url)) # probably vulnerable to a timing attack
		for i in range(6):
			rand_index = random.randint(0, len(self.possible_characters) - 1)
			output_hash.append(str(self.possible_characters[rand_index]))
		return "".join(output_hash)

	def generate_bijective_hash(self, url):
		key = random.randint(100000, 10000000)
		base_62_key = self.convert_base(key, 62)
		short_url = []
		for digit in base_62_key:
			short_url.append(str(self.possible_characters[digit]))
		return "".join(short_url)

	def convert_base(self, num, base):
		# convert the base-10 numerical key into base_62
		if num == 0 or base <= 0:
			return [0]
		digits = []
		while num > 0:
			rem = num % base
			digits.append(rem)
			num = num // base
		return digits[::-1]

if __name__ == '__main__':
	short = URLShortener()
	a = short.shorten("https://google.com")
	b = short.shorten("http://facebook.com/123is9ensdufns_1283210jnsns")
	c = short.shorten("http://facebook.com/123is9ensdufns_1283210jnsnxs")
	print(a, b, c)
	print(short.restore(a))
	print(short.restore(b))
	print(short.shorten("http://facebook.com/123is9ensdufns_1283210jnsns"))
	print(short.restore(c))
	print(short.restore("h"))
	d = short.shorten("https://google.com")
	print(d)
	e = short.shorten("https://google.com/1")
	print(e)

