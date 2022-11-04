# step 1: create an empty list named beatles;
Beatles = []
print("Step 1:", Beatles)

# step 2: use the append() method to add the following members of the band to the list;

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Step 2:", Beatles)

# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list;
for members in range(2):
    Beatles.append(input("New band member: ")) # add Stu Sutcliffe, Pete Best;
print("Step 3:", Beatles)

# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del Beatles[-1]
del Beatles[-1]
print("Step 4:", Beatles)

# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
Beatles.insert(0, "RingoStarr")
print("Step 5:", Beatles)
print("The Fab:",len(Beatles))
