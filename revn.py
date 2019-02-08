sam = int(input())    
Reverse = 0    
while(sam > 0):    
    Reminder = sam %10    
    Reverse = (Reverse *10) + Reminder    
    sam = sam //10        
print("\n%d" %Reverse)  
