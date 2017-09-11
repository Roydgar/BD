class Movie(object):
	def __init__(self, pid, mid, mname, country, producers):
		self.mid = mid
		self.pid = pid
		self.mname = mname
		self.country = country

	def __str__(self):
		return "Producer id = %d, Movie id = %d, Movie name = %s, Country = %s"%(self.pid, self.mid, self.mname, self.country)

