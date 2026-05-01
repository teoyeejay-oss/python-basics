import time

my_time = int(input("Please enter a second: "))

for x in range(my_time,0,-1):
   seconds = x%60
   minutes = int((x/60)%60)
   hours = int((x/3600)%24)
   days = int((x/86400)%30)
   print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")
   time.sleep(1)

print("Times Up!")
