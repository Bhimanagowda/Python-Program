import re
if re.search('Amith','he is amith from tmk',re.IGNORECASE):
   print("true")
else:
  print("false")

a=re.findall('amit.','he is amit from tmk amith')
for i in a:
  print(i)