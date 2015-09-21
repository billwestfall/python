
# sage: load ("page020a.sage")
# [3*(x-2)-6==(4*x)-(3*x-1)], x)
# 6.5
# [(2*(x-(3+2*x)+9))==2*x+4], x)
# 2.0
# [((-2*(4*(x+2))-3*(x+1))==14+2*x)], x)
# -2.53846153846
# [((3*x/5)-((4/5)*(x+1))==(2-(3/10)*(3*x-4)))], x)
# 5.71428571429
# [(((4/3)*(x-2)-(1/2))==((2*((3/4)*x-1)))], x)
# -7.0
# [(((5*x)/6)-8==5-(2*(x/3))], x)
# 8.66666666667
# [(((x/2)-3)==(((3*x)/5)+1)], x)
# -40.0
# [((x/2)-(1/x)==((6*x)+5)/12)], x)
# 9.96867168501e-13
# [((((-((3*x)/2)+(((9*x)-5)/6)==((11*x)+8)/x))], x)
# 9.96767600166e-13


x = var('x')
print ("[3*(x-2)-6==(4*x)-(3*x-1)], x)")
print ((3*(x-2)-6==(4*x)-(3*x-1)).find_root(-9999,9999,x))

x = var('x')
print ("[(2*(x-(3+2*x)+9))==2*x+4], x)")
print (((2*(x-(3+2*x)+9))==2*x+4).find_root(-9999,9999,x))

x = var('x')
print ("[((-2*(4*(x+2))-3*(x+1))==14+2*x)], x)")
print (((-2*(4*(x+2))-3*(x+1))==14+(2*x)).find_root(-9999,9999,x))

x = var('x')
print ("[((3*x/5)-((4/5)*(x+1))==(2-(3/10)*(3*x-4)))], x)")
print (((3*x/5)-((4/5)*(x+1))==(2-(3/10)*(3*x-4))).find_root(-9999,9999,x))

x = var('x')
print ("[(((4/3)*(x-2)-(1/2))==((2*((3/4)*x-1)))], x)")
print ((((4/3)*(x-2)-(1/2))==((2*((3/4)*x-1)))).find_root(-9999,9999,x))

x = var('x')
print ("[(((5*x)/6)-8==5-(2*(x/3))], x)")
print ((((5*x)/6)-8==5-(2*(x/3))).find_root(-9999,9999,x))

x = var('x')
print ("[(((x/2)-3)==(((3*x)/5)+1)], x)")
print ((((x/2)-3)==(((3*x)/5)+1)).find_root(-9999,9999,x))

x = var('x')
print ("[((x/2)-(1/x)==((6*x)+5)/12)], x)")
print ((((x/2)-(1/x)==((6*x)+5)/12)).find_root(-9999,9999,x))

x = var('x')
print ("[((((-((3*x)/2)+(((9*x)-5)/6)==((11*x)+8)/x))], x)")
print ((((-((3*x)/2)+(((9*x)-5)/6)==((11*x)+8)/x))).find_root(-9999,9999,x))