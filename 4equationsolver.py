import random

while True:
   a = random.randint(1,10)
   b = random.randint(1,10)
   c = random.randint(1,10)
   d = random.randint(1,10)

   e1 = a + b * c - d
   e2 = a * d - c * b
   e3 = c + b + d - a
   e4 = d + a / c - b

   if e1 == 14 and e2 == 27 and e3 == 9 and e4 == 4:
      print ("a:", a, "b:", b,"c:", c,"d:", d)
      break
   
   else:
      continue
   