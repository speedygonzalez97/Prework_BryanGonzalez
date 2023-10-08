guest_list = ["michael jackson", "alan rickman", "albert einstein"]

print("\nI invite you to dinner " + guest_list[0] + ", " + guest_list[1] 
      + ", and " + guest_list[2] + ".")

print("\nI've just heard that " + guest_list[2] + " cannot make it to dinner")
guest_list[2] = "Leonardo Davinci"

print("\nI invite you to dinner " + guest_list[0] + ", " + guest_list[1] 
      + ", and " + guest_list[2] + ".")
print("\nMore people are coming! ")

guest_list.insert(0,"shakira")
guest_list.insert(2,"heath ledger")
guest_list.append("freddie mercury")

print("\nI invite you to dinner " + guest_list[0] + ", " + guest_list[1] +", " 
      + guest_list[2] + ", " + guest_list[3] + ", " + guest_list[4] 
      + ", and " + guest_list[5] + ".\n")

print(len(guest_list))

print("\nUnfortunately i can invite only 2 people to dinner")

w= guest_list.pop(1)
x= guest_list.pop(1)
y= guest_list.pop(1)
z= guest_list.pop(2)

print("\nim sorry, " + w + ", but  i have no room for dinner")
print("\nim sorry, " + x + ", but  i have no room for dinner")
print("\nim sorry, " + y + ", but  i have no room for dinner")
print("\nim sorry, " + z + ", but  i have no room for dinner")

print("\nYou are lucky to come to my dinner " + guest_list[0] + " after disinviting some people")
print("\nYou are lucky to come to my dinner " + guest_list[1] + " after disinviting some people\n")

del guest_list[0]
del guest_list[0]

print(guest_list)
print(guest_list[-1])


