def washing_machine(weight  ):
    
    if weight <0 :
        return ("give positive number ")
    elif weight == 0 :
        return("Washing machine will take 0 seconds ")
      
    elif weight >7000:
        return("over weight ")      
      
    
    if waterlevel =="low" :

        if weight <2000:
            return("Washing machine will take 25 minute ")
    elif waterlevel  == "medium" :
        if 2000 <weight <4000:
            return("Washing machine will take 35 minute ")
    elif waterlevel  == "large" :
        if 4000 < weight <6000:
            return ("Washing machine will take 45 min ")  
    return (" invalid weight ")    
 
weight = 2002
waterlevel = "low"

result = washing_machine(weight)     
print(result)