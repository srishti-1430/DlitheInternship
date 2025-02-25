#list
list=["apple","orenge"]
print(list)

list=["apple","orenge","apple","orenge"]
print(list)

list=["apple","orenge","apple","orenge"]
print(len(list))

a=["cloud","drive","location"]
b=[129,454,434]
c=[True,False]
d=[54.65,45.75,46.46]
print(a)
print(b)
print(c)
print(d)


a=["srishti",8578,True,67.876]
print(a)

#type
a=["cloud","drive","location"]
b=[129,454,434]
print(type(a))
print(type(b))

#list constructor
fruits=list(("apple","orenge"))
print(fruits)

fruits=["apple","orenge","mango","watermelon","grapes"]
print(fruits[1])
print(fruits[-1])
print(fruits[-2])
print(fruits[1:4])
print(fruits[1:])
print(fruits[:1])

fruits=["apple","orenge","mango","watermelon","grapes"]
if "grapes" in fruits:
    print("present")
else:
    print("no")

###replace
ic=["chikku almond","venilla","butterscoch","rosted almond","pista kesar"]
ic[1]="chocolate"
print(ic)

ic=["chikku almond","venilla","butterscoch","rosted almond","pista kesar"]
ic[1:4]="chocolate","belgium choclate","black current"
print(ic)

ic=["chikku almond","venilla","butterscoch","rosted almond","pista kesar"]
ic.append("belgium chocolate")
print(ic)

ic=["chikku almond","venilla","butterscoch","rosted almond","pista kesar"]
ic.insert(1,"chocolate")
print(ic)

ic=["chikku almond","venilla","butterscoch","rosted almond","pista kesar"]
ic.insert(-2,"chocolate")
print(ic)

ic=["chikku almond","venilla"]
ic2=["butterscoch","rosted almond"]
print(ic+ic2)

ic=["chikku almond","venilla"]
ic2=["butterscoch","rosted almond"]
ic.extend(ic2)
print(ic)

###tuple
ic=["chikku almond","venilla"]
ic2=("butterscoch","rosted almond")
ic.extend(ic2)
print(ic)

ic=["chikku almond","venilla","butterscoch","rosted almond"]
ic.remove("venilla")
print(ic)

ic=["chikku almond","venilla","butterscoch","rosted almond"]
ic.pop(1)
print(ic)

bikes=["ninja","ducati","xpulse10","himalayan"]
bikes.clear()
print(bikes)

cities=["udupi","manglore","banglore"]
cities[2]="hebri"
print(cities)

ws=["last in space","squid game","kota factory"]
ws.insert(0,"my girlfriernd is an alien")
print(ws)

cars=["rr evoque","defender","range rover","sports"]
cars.insert(2,"vellar")
print(cars)

crkt=["ICT","RCB","KB","CSK"]
crkt.remove("CSK")
print(crkt)

a=[7,3,5,6,2,29,75,23,13]
a.sort()
print(a)


x=["d","f","q","k","x"]
x.sort()
print(x)

s=["srishti","prithvi","deeksha"]
s.append("veech")
s.sort()
print(s)

h=["sleeping","singing","talking","art"]
h.pop(0)
h.append("python")
print(h)

h=["sleeping","singing","talking","art"]
h[0]="python"
print(h)




