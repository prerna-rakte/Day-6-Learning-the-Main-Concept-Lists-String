name = "Pine Apple"
print(name.upper())
print(name.lower())
print(len(name))

name = "Pine Appla"
print(name.replace("a", "e"))
print(name.count("p"))
print(name.find("l"))


num = [10,20,30,40]
num.append(50)
print(num)

num = [10,20,30,40,50,60]
num.remove(60)
print(num)

num = [10,20,30,40,50]
for i in num:
    print(i)

name = input("Enter your name: ")
rev = name[::-1]
print("Reverse letter of your Name:",rev)


name = input("Enter your name: ")
count = 0
for i in name:
    if i in "aeiouAEIOU":
        count += 1

print("Total Vowels:",count)


num = [10,20,30,40,50]
largest = num[0]
for i in num:
    if i > largest:
        largest = i

print("Largest Element:",largest)


num = [10,20,30,40,50]
sum = 0
for i in num:
    sum += i
print("Sum Of Element:",sum)


name = input("Enter your name: ")
for i in name:
    print(i, ":", name.count(i))

num = [10,20,30,40,30]
for i in num:
    if num.count(i) > 1:
        print(i)