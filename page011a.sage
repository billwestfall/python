# sage: load ("page011a.sage")
# [2*x + 1 == 19], x)
# [
# x == 9
# ]
# [5*x - 3 == 12], x)
# [
# x == 3
# ]
# [2*x + 3(x - 4) == 2*(x-3)], x)
# [
# x == 2
# ]
# [(42.19*x + 121.34) == (16.83*x) + 19.15], x)
# -4.02957413249
# [(x/10 - 2/15)==(3*x/20-1/5)], x)
# 1.33333333333
# [x/(x-2)==(2/(x-2))+2], x)
# [
#
# ]
# [(3*(a*x-5*a))+(4*b)==(4*x-2)], x, a, b)
# [
# x == (15*a - 4*b - 2)/(3*a - 4)
# ]

x = var('x')
print ("[2*x + 1 == 19], x)")
print solve([2*x + 1 == 19], x)

x = var('x')
print ("[5*x - 3 == 12], x)")
print solve([5*x - 3 == 12], x)

x = var('x')
print ("[2*x + 3(x - 4) == 2*(x-3)], x)")
print solve([2*x + 3*(x - 4) == 2*(x-3)], x)

x = var('x')
print ("[(42.19*x + 121.34) == (16.83*x) + 19.15], x)")
print find_root((42.19*x+121.34)==(16.83*x)+19.15,-100,100)

x = var('x')
print ("[(x/10 - 2/15)==(3*x/20-1/5)], x)")
print find_root((x/10 - 2/15)==(3*x/20-1/5),-999,999)

x = var('x')
print ("[x/(x-2)==(2/(x-2))+2], x)")
print solve([(x/(x-2))==(2/(x-2))+2], x)
#print find_root((x/(x-2))==(2/(x-2))+2,-999,999)

x, a, b = var('x', 'a', 'b')
print ("[(3*(a*x-5*a))+(4*b)==(4*x-2)], x, a, b)")
print solve([(3*(a*x-5*a))+(4*b)==(4*x-2)], x)
#print find_root((3*(a*x-5*a))+(4*b)==(4*x-2),-999,999)
