from math import sqrt

def my_sqrt(num):

  est = num / 2
  for i in range(1, 6):
    est = (est + num / est) / 2

  return est


est = my_sqrt(100)
print("est sqrt =", est)
print("math sqrt =", sqrt(100))

est = my_sqrt(40)
print("est sqrt =", est)
print("math sqrt =", sqrt(40))

est = my_sqrt(72)
print("est sqrt =", est)
print("math sqrt =", sqrt(72))


