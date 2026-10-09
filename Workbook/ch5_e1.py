



capacity_text = input("Capacity: ")

try:
    capacity = int(capacity_text)
except ValueError:
    print("Please input a number")
else:
    if 1 <= capacity <= 500:
        print("Valid Capacity")
    elif capacity < 1 or capacity > 500:
        print("Capacity must be 1 to 500")
