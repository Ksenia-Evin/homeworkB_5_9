import time

def time_this(num_runs=10):
	def decorator(func):
		def timer(param):
			avg_time = 0
			for _ in range(num_runs):
			    t0 = time.time()
			    func(param)
			    t1 = time.time()
			    avg_time += (t1 - t0)
			avg_time /= num_runs
			return "при количестве итераций {0}, среднее время рассчета для последовательности Фибоначи сотавляет: {1} секунд".format(num_runs, avg_time)
		return timer
	return decorator

if __name__ == "__main__":
	num_runs = input("Введите количество итераций: ")
	@time_this(int(num_runs))
	def fabionachi(maximum):
		numbers = [1,2]
		i = 1
		while True:
			numbers.append(numbers[i] + numbers[i-1])
			if numbers[i] > int(maximum):
				del numbers[i]
				break
			i += 1
print(fabionachi(4000000))

