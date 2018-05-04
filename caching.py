class CacheObject:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class LeastRecentlyUsedCache:
	def __init__(self, size):
		self.cache = []
		self.items = {}
		self.size = size

	def set(key, value):
		if len(cache) >= size:
			# remove if we go over size
			cache.pop(0)
		cache.append(value)
		items[key] = cache[-1]
	

	def get(key):
		return cache[0]
