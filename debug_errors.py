# Function 1: Calculate average safely
def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]

        return total / len(numbers)

    except ZeroDivisionError:
        print("Error: Cannot calculate average of an empty list.")
        return None


# Function 2: Safe list element access
def get_list_element(my_list, index):
    try:
        return my_list[index]

    except IndexError:
        print("Error: Index is out of bounds.")
        return None

    except TypeError:
        print("Error: Provided object is not a list.")
        return None


# --- Test Data for Debugging ---
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []  # This previously caused ZeroDivisionError

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")


# --- Test Cases for Error Handling ---
print("\nTesting get_list_element:")

# Valid case
print(get_list_element([1, 2, 3], 1))

# Out of bounds
print(get_list_element([1, 2, 3], 10))

# Wrong type
print(get_list_element("not a list", 0))