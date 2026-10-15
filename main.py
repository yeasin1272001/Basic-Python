
# Insetion
a = [20, 25, 30, 40, 50]

pos = int(input("Enter Position: "))
item = int(input("Enter Item: "))

a.append(0)

i = len(a) - 1

while i >= pos:
    a[i] = a[i - 1]
    i = i - 1

a[pos - 1] = item

print("New Array:", a)

----------------------------
# Deletion

a = [10, 20, 30, 40]

pos = int(input("Enter position: "))

i = pos - 1

while i < len(a) - 1:
    a[i] = a[i + 1]
    i = i + 1

a.pop()

print(a)

---------------------------

# update

a = [10, 20, 30, 40]

pos = int(input("Enter position: "))
item = int(input("Enter new item: "))

a[pos - 1] = item

print(a)

-----------------------
# linear sarch

a = [10, 20, 30, 40]

item = int(input("Enter number: "))

i = 0

while i < len(a):
    if a[i] == item:
        print("Found")
        break
    i = i + 1

if i == len(a):
    print("Not Found")