def fibonacci(n):
  
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the value of n: "))

fibonacci_sequence = [fibonacci(i) for i in range(n)]

print(fibonacci_sequence)