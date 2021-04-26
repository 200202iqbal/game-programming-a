knights = {"gallahad" : "the pure","robin": "the brave"}
for k,v in knights.items():
    print(k,v)

for i,v in enumerate (["tic","tac","toe"]):
    print(i,v)

question = ["name","quest","favorite color"]
answers = ["lancelot","the holy grail","blue"]
for q, a in zip(question,answers):
    print('What is your {0}? It is {1}.'.format(q,a))

for i in reversed(range(1,10,2)):
    print(i)

basket = ["apple","orange","apple","pear","orange","banana"]
for i in sorted(basket):
    print(i)

print()
for f in sorted(set(basket)):
    print(f)

from math import isnan
raw_data = [56.2,float("Nan"),51.7,55.3,52.5,float("Nan"),47.8]
filtered_data = []
for value in raw_data:
    if not isnan(value):
        filtered_data.append(value)
print(sorted(filtered_data))