# AllocateTables

# A Python program to try and
# efficiently allocate tables
# to restaurant diners.

import random

# list of tables, where each
# number represents how many
# chairs are available, 1-6

maxChairs = 10

tables = []
for i in range(1, 10):
    tables.append(random.randint(1, maxChairs))
    print("Table %d has %d chairs available." % (i, tables[i-1]))
print(tables)


while True:
    size = input("\nEnter your party size: ")
    try:
        size = int(size)
        if size < 1:
            print("\nEnter a party size of 1 or more: ")
        else:
            break
    except:
        print("\nNot an integer, try again")


orig_tables = tables
dynamic_size = size

while maxChairs != dynamic_size:
    for table in tables:
        if dynamic_size == table:
            print("\nYour party of size %d will take table %d" % (size, tables.index(table)+1))
            tables[tables.index(table)] = 0
            print(tables)
            break
        else:
            dynamic_size += 1
            print("Increased dynamic size")
            
    print("Broke out of loop")        
    break
