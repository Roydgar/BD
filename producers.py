import bisect 

class Producers(object):
	def __init__(self):
		self.producers = [] #empty list

	def add(self, producer):
		for i, p in enumerate(self.producers):
			if p.pname == producer.pname: 
				return i
		self.producers.append(producer) 
		return -1

	def __str__(self):
		return "\n".join(str(producer) for producer in self.producers)

	def exists(self, pid):
		for producer in self.producers:
			if producer.pid == pid:
				return True
			return False

	def delete(self, pid, movies):
		if movies.exists(pid):
			print("Cannot delete. Producer has movies attached in database")
			return
		index = -1
		for i, producer in enumerate(self.producers):
			if producer.pid == pid:
				index = i

		if (index > -1):
			return self.producers.pop(index)

	def searchByCountry(self, name, movies):
		for producer in self.producers:
			for movie in movies.movies:
				if (movie.pid == producer.pid and movie.country.lower() == name.lower()):
					print(producer)



