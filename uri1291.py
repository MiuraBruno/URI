from math import pi
while True:
  try:
    a = float(input())
    a3 = (-a)*a*(3.0*(3.0**(1/2)-4.0)+2.0*pi)/3.0
    a2 = 4.0 * (a * a * (1 - pi/4.0) - (a3) / 2.0)
    a1 = a * a - a2 - a3
    print("%.3f %.3f %.3f" %(a1,a2,a3))
  except EOFError:
    break

#ERRADO
