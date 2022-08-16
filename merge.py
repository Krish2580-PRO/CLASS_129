import csv

d1 = []
d2 = []

with open ("stars.csv", "r") as x:
    a = csv.reader(x)

    for i in a:
        d1.append(i)


with open ("converted.csv", "r") as x:
    a = csv.reader(x)

    for i in a:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p1 = d1[1:]

p2 = d2[1:]

headers = h1 + h2

planet_data = []

for i , data in enumerate(p1):
    planet_data.append(p1[i] + p2[i])



with open ("x.csv" , "a+")  as x:
    a = csv.writer(x)
    a.writerow(headers)
    a.writerows(planet_data)

#remove blank lines
with open('x.csv') as input, open('final.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)







