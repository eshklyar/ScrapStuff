def dig_pow(n, p):
    sum = 0
    ns = str(n)
    for i in range(len(ns)):
        sum += int(ns[i])**(i+p)
    if sum % n == 0:
        return (sum/n)
    else:
        return -1


def dig_pow1(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1


def dig_pow2(n, p):
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1



print(dig_pow(46289,3))