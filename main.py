import time


time_h = (time.localtime().tm_hour + 8) % 24
time_m = time.localtime().tm_min
time_s = time.localtime().tm_sec

print(time_h)
print(time_m)
print(time_s)
