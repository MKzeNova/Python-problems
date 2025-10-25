# program that converts that amount of seconds into days, hours, minutes

sec=int(input("Input the amount of seconds : "))
days=sec//86400 #gives an integer value,ie a full day,the fraction parts (got after dividing entered seconds by 86400)contain hours,minutes,and seconds
reminding_sec=sec%86400
hours=reminding_sec//3600
reminding_sec2=reminding_sec%3600
minutes=reminding_sec2//60
reminding_sec3=reminding_sec2%60
seconds=reminding_sec3
print(f"{days}d,{hours}h,{minutes}m,{seconds}s")