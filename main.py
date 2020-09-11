def multiplesOf3and5(number):
   five = set([ x for x in range(0,number,5)])
   three = set([ x for x in range(0,number,3)])
   return sum(five.union(three))
   
print(multiplesOf3and5(1000))