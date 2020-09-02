import mising

print("Enter array numbers, seperated by commas, 1,N+1")

userarray = input()

userarray = userarray.split(",")
userarrayint = []
for number in userarray:
    userarrayint.append(int(number))
mising.missing(userarrayint)

