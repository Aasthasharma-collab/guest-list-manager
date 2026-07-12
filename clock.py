import time

current_time=time.localtime()  

twelve_hour_format=time.strftime("%I:%M:%S %p")
print(f"current time: {twelve_hour_format}")
if current_time.tm_hour>=0 and current_time.tm_hour<12:
    print("good morning")
elif current_time.tm_hour>=12 and current_time.tm_hour<18:
    print("good afternoon")
elif current_time.tm_hour>=18 and current_time.tm_hour<24:
    print("good evening")    
else:
    print("good night")

