people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks")
elif trucks < cars:
    print("May be we could take the trucks.")
else:
    print("We stll can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine. Let's just stay home then.")

num1 = -2
num2 = 3
negnum = -5

def pos_neg(a, b, negative):
  if negative:
    return(a < 0 and b < 0)
  else:
    return((a < 0 and b>0) or (a > 0 and b < 0))

val = pos_neg(num1, num2, negnum)
print("pos_neg returns: ", val)
