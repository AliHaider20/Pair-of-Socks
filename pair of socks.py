number_of_socks=int(input("Enter the number of socks"))
print("Colors can be three 1, 2 and 3")
colors=list()
for i in range(number_of_socks):
    print("Enter the color of %d sock"%(i),end=" ")
    colors.append(int(input()))
ones=colors.count(1)
twos=colors.count(2)
threes=colors.count(3)
count=ones//2
count+=twos//2
count+=threes//2
print(count)
