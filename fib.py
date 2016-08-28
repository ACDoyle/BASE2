#!/usr/bin/python

#check if number is a fibonnaci one

def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new

liczby_fib = []
for i in range(28):
    liczby_fib.append(fibi(i))

print liczby_fib

for i in range(100):
    if i in liczby_fib:
        print i
#    assert checkio(10000) == 0, "Newborn"
#    assert checkio(9999) == 1, "1 year"
#    assert checkio(9997) == 2, "2 years"
#    assert checkio(9994) == 3, "3 years"
#    assert checkio(9995) == 4, "4 years"
#    assert checkio(9990) == 5, "5 yea

limit=10000
solution = []
for i in range(5000):
    if i in liczby_fib:
        limit-=i
    else:
        limit+=1
    solution.append(limit)

print solution

def checkio(n):
    return solution.index(n)

if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"


