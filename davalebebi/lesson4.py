name1 = input("Enter Your Name : ")
name2 = input("Enter Your Name: ")

volwes1 = 0
volwes = 0

for char in name1:
    if char in "aeiou":
        volwes1 += 1
for char in name2:
    if char in "aeiou":
        volwes += 1


if volwes1 > volwes:
 print("Sul gamovida pirvelshi {} luwi".format(volwes1))

elif volwes1 < volwes:
 print("Sul gamovida meoreshi {} luwi".format(volwes))

else:
   volwes1 = volwes
   print("Tolia luwebis raodenoba ".format(volwes, volwes1))