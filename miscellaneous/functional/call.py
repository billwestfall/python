def create_multiplier(a):
  def multiplier(x):
    return x * a
  
  return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))
print(triple(6))
print(quadruple(7))
