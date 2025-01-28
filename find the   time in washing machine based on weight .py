def washing_machine(weight  ):
    #using the conditional statements  if elif 
    
    if weight <0 :
        return ("give positive number ")
    elif weight == 0 :
        return("Washing machine will take 0 second")
      
    elif weight >7000:
        return("over weight ")  
    # setting the condition   water level  if is ture is send tonparticular condition and return yhr output     
      
    
    if waterlevel =="low" :

        if weight <2000:
            return("Washing machine will take 25 minute ")
    elif waterlevel  == "medium" :
        if 2000 <weight <4000:
            return("Washing machine will take 35 minute ")
    elif waterlevel  == "large" :
        if 4000 < weight <6000:
            return ("Washing machine will take 45 min ")  
       #suppose all condition are wrong it return invald weight 
    return (" invalid weight ") 
# giving the value    
 
weight = 2002
waterlevel = "low"
# calling the funtion 


result = washing_machine(weight)     
print(result)