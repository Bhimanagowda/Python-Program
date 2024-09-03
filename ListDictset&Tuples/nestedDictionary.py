people={1:{"name":"Amith","age":20,"city":"Tumkur"},
        2:{"name":"Amith","age":20,"city":"Tumkur"},
        3:{"name":"Amith","age":20,"city":"Tumkur"}}
print(people)

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['city'])


for p_id,p_info in people.items():
  print("\n personal ID:",p_id)
  for key in p_info:
    print(key + ' : ',p_info[key])