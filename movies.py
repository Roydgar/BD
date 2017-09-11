class Movies(object):
	def __init__(self):
		self.movies = []

	def add(self, movie):
		self.movies.append(movie)

	def __str__(self):
		return "\n".join(str(movie) for movie in self.movies)

	def exists(self, pid):
		for movie in self.movies:
			if movie.pid == pid:
				return True
		return False

	def delete(self, mid):
		index = -1
		for i, movie in enumerate(self.movies):
			if movie.mid == mid:
				index = i

		if (index > -1):
			return self.movies.pop(index)