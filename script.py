# A function that takes a list and target parameter
# Multiple variables metal, start, end and steps
# recursion or while loop
# Increase the steps each time a split is done
# Conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list) - 1
    steps = 0

    while(start<=end):
        middle = start + (end -start)//2
        mid_val = list[middle]

        if mid_val == element:
            return middle
        elif mid_val < element:
            start = middle + 1
            steps += 1
        else:
            end = middle - 1
            steps += 1

    return -1
def verify(index):
    if index != -1:
        print("Target found at position: ", index +1)
    else: 
        print("Value not found in the list")

list = [45, 56, 86, 98, 99, 100, 121, 134, 154]
result = binary_search(list, 121)
verify(result)
# Recursive Binary Search

