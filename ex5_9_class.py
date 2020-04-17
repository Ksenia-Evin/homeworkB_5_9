import time

class Secudomer(object):
	def __init__(self):
		self.functional = functional
		self.NUM_RUNS = 100
	def __call__(self, *args, **kwargs):
		avg_time = 0
		for _ in range(self.NUM_RUNS):
			t0 = time.time()
			self.functional(*args, **kwargs)
			t1 = time.time()
			avg_time += (t1 - t0)
		avg_time /= NUM_RUNS
		print("Среднее время выполнения за %s запусков: %.5f секунд" % (NUM_RUNS, avg_time))
		return self.functional(*args, **kwargs)
