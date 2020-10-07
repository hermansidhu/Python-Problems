# Write a python program which finds the maximum number from num1 to num2
# (num2 inclusive) based on the following rules.

# .....1. Always num1 should be less than num2
# .....2. Consider each number from num1 to num2 (num2 inclusive). Populate the number
# .....into a list, if the below conditions are satisfied
# .........a. Sum of the digits of the number is a multiple of 3
# .........b. Number has only two digits
# .........c. Number is a multiple of 5
# .....3. Display the maximum element from the list
# .....4. In case of any invalid data or if the list is empty, display -1.


def find_max(num1, num2):

    # check for invalid data: 'num1' and 'num2' should be integers
    if type(num1) != int or type(num2) != int:
        return -1

    # check if 'num1' is greater than 'num2'
    if num1 > num2:
        return -1

    # initialize empty list
    num_list = []

    # find the nearest multiple of 15 to 'num1'
    if num1 % 15 == 0:
        nearest_multiple = num1
    else:
        nearest_multiple = num1 + 15 - num1 % 15

    # scan through possible numbers from 'nearest_multiple' to 'num2'
    for numbers in range(nearest_multiple, num2 + 1, 15):
        if 10 <= numbers <= 99 or -99 <= numbers <= -10:
            num_list.append(numbers)

    # if no valid number was detected, the list will remain empty
    if num_list == []:
        return -1

    print(num_list)
    return max(num_list)


print()
num1 = int(input("Enter num1 : "))
num2 = int(input(("Enter num2 : ")))
print(find_max(num1, num2))
print()
