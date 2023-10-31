# Task19

# Use sequence unpacking to extract the values you stored within the address tuple earlier.
# Unpack the tuple into variables named house_num, street and postcode.

address = (3, "Bayswater Row", "LS8 5LH",)
house_number, street_name, postcode = address

print(f"Your Address: {house_number}. {street_name}")
print(f"   Post Code: {postcode}")

# The Output:

# Your Address: 3. Bayswater Row
#    Post Code: LS8 5LH