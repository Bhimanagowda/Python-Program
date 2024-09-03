import array

a="amith"

arr=array.array('u',a)
print(arr)

arr.reverse()
rev=''.join(arr)
print(rev)

#Count the how many vowels and constnants
consocount=0
vowelcount=0

vowel='aeiou'

for i in rev:
  if i in vowel:
    vowelcount+=1
  else:
    consocount+=1
print(f"vowelcount is{vowelcount} \n and constnants is:{consocount}")

