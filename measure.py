def cm_to_m(cm):
    return cm / 100

# Get input from user
cm = float(input("Enter length in centimeters: "))

# Convert cm to m
m = cm_to_m(cm)

# Create the result string
result = f"{cm} centimeters is equal to {m} meters"

# Print to console
print(result)

# Write to file
with open("conversion_result.txt", "w") as file:
    file.write(result)

print("Result has been saved to conversion_result.txt")