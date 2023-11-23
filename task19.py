
def find_str(array1, another_string):
    if another_string in array1:
        return array1.index(another_string)

    return -1


array1 = input("First array: ")
another_string = input("Another string: ")

index = find_str(array1, another_string)

if index != -1:
    print(f"The string '{another_string}' starts at index {index} in '{array1}'")
else:
    print(f"The string '{another_string}' is not found in '{array1}'")
