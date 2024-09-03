import random
n=100
rand=random.randrange(1,n)

print("A random number between 1 and 100 has been generated.")
print(rand)

while True:
  guess=int(input("guess number"))
  
  if guess > n:
    print("Invalid number")
    break
  
  if rand == guess:
    print("successfully guess")
    break
  elif rand > guess:
    print("guess is smaller")
  elif rand < guess:
    print("guess is greater")
  
  
    