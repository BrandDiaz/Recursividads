def sum(n):
    for i in range (n):
    	n += i
    return n

    def factorial(n):
        fact = 1
        for i in range(1,n+1):
        	fact = fact * i
            return fact

            def gcd(a,b):
              while b:
                a, b = b, a % b
              return a
