class Producer(object):
	def __init__(self, pid, pname):
		self.pid = pid
		self.pname = pname
	def __str__(self):
		return "Producer id = %d, Producer name = %s"%(self.pid, self.pname)