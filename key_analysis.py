import json
import math

data = {}

with open('archaea.txt') as json_file:
    data = json.load(json_file)

key_list = [int(x) for x in list(data.keys())]

key_list.sort()

differences = []
count = 0
value = 0
sub = 0
low = key_list[0]
for i in range(len(key_list)-1):
    d = key_list[i+1]-key_list[i]
    differences.append(d)
    value += d
    if d > 1:
        sub += d
        count += 1
        if d < low:
            low = d

#standard deviation
s = 0
ns = 0
for x in differences:
    s += (x - 1135.9225) ** 2
    if x > 1:
        ns += (x - 1135.9225) ** 2
dev = math.sqrt(s/len(differences))
ndev = math.sqrt(ns/count)
#statistics
print("min: " + str(low))
print("max: " + str(max(differences)))
print("mean: " + str(value/len(differences)))
print("standard deviation: " + str(dev))
#on non-consecutive jumps
print("mean non-consecutive: " + str(sub/count))
print("standard deviation non-consecutive: " + str(ndev))
print(count/len(differences))
