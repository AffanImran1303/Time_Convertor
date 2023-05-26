def timeConversion(time):
  
  #Converting the time into list
    list(time)
    
    #Slicing the list to get the "AM/PM" and actual time digits.
    if time[-2:]=="AM" and time[:2]=="12":
        return "00"+time[2:-2]
    elif time[-2:]=="AM":
        return time[:-2]
    elif time[-2:]=="PM" and time[:2]=="12":
        return time[:-2]
    else:
        return str(int(time[:2])+12)+time[2:8]
print(timeConversion("12:10:09 AM"))
