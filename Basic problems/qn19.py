# program to convert all units of time into seconds.
print("input the time in: ")
days=int(input("Input days= "))*86400
hour=int(input("Input time in hrs= "))*3600
min=int(input("Input time in min= "))*60
sec=int(input("Input time in sec= "))
res=days+hour+min+sec
print(f"The amount of seconds = {res}")
