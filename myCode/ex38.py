ten_things="Apples Oranges Crows Telephone Light Sugar"

print("wait there are not 10 things in that list.Let's fix that.")

stuff=ten_things.split(' ') #分割成单个字符
more_stuff=["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one=more_stuff.pop()
    print("Adding: ",next_one) #why从最后一个开始加？
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ",stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
