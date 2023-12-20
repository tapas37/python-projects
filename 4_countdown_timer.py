# countdown timer

import time
my_time=int(input("enter time in second: "))

'''for i in range(my_time,0,-1):
    print(i)
    time.sleep(1)  ##---> program will sleep for certin amount of time
print("happy new year")'''


'''for i in range(my_time,0,-1):
    minutes=int(i/60)
    hour=int(i/3600)
    print(f"00:00:{i:02}")
    time.sleep(1)
print("happy new year")

'''

## like a digital clock

for i in range(my_time,0,-1):
    minutes=int(i/60)
    hour=int(i/3600)
    print(f"{hour:02}:{minutes:02}:{i:02}")
    time.sleep(1)
print("happy new year")

