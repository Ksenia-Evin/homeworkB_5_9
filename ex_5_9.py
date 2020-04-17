import time


def time_this(NUM_RUNS=10):
	def decorate(functional):
		def func(*args, **kwargs):
			avg_time = 0
			for _ in range(NUM_RUNS):
			    t0 = time.time()
			    functional(*args, **kwargs)
			    t1 = time.time()
			    avg_time += (t1 - t0)
			avg_time /= NUM_RUNS
		return func
		print("Среднее время выполнения за %s запусков: %.5f секунд" % (NUM_RUNS, avg_time))
	return decorate


