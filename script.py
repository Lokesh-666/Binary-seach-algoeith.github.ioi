# Function to do a binary search in given list for a given element
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


# Function to verify whether the element was found or not
def verify(index):
    if index != -1:
        print("Target found at position: ", index +1)
    else: 
        print("Value not found in the list")

# Main function to call the binary search function
def main():
    print("Would you like to give list items yourself? (y/n)")
    choice = input()
    if choice.lower() == 'y':
        list = []
        print("Enter the number of items in the list: ")
        n = int(input())
        print("Enter the items in the list: ")
        for i in range(n):
            list.append(int(input()))
        print(list)
        element = int(input("What would u like to search?"))
    else:
        list = [45, 56, 86, 98, 99, 100, 121, 134, 154]
        element = 121
    result = binary_search(list, element)
    verify(result)

# Driver code to call the main function
if __name__ == '__main__':
    main()