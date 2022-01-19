import statistics
import math
data = [60,61,65,63,98,99,90,95,91,96]

mean = statistics.mean(data)

#Arrays
deviations = []

for i in data:
    d = i - mean
    deviations.append(d)

sq_dev = []

for i in deviations:
    sq_d = i * i
    sq_dev.append(sq_d)

variance = statistics.mean(sq_dev)

std_dev = math.sqrt(variance)
print(std_dev)

std = statistics.stdev(data)
print(std)