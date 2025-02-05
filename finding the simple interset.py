def findthesimple_interest(p,t,r):
    simple_interest = (p * t * r) / 100
    return simple_interest
p=int(input("Enterthe principle"))
t=int(input("Enterthe time period"))
r=int(input("Enterthe rate of interest"))
print(findthesimple_interest(p,t,r))