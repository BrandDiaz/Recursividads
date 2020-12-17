#no tail recursive
def factorial(n):
  	if n==0:
    	  return 1
  	else:
    	  return n*factorial(n-1)

     #tail recursive
      def factorial(n, total=1):
  	if n==0:
    	  return total
  	else:
    	  return factorial(n-1, total*n)
