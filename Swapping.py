#To write a program that swaps two numbers using a temporary variable, simulating the process of swapping locker codes.

# initial locker codes
code1 = 1234
code2 = 5678

print("********************STUDENT LOCKER SYSTEM*********************")
print("Before swapping:")
print("Locker 1 code:", code1)
print("Locker 2 code:", code2)

# Using a temporary variable (the holding tray)
temp = code1
code1 = code2
code2 = temp

print("\nAfter swapping:")
print("Locker 1 code:", code1)
print("Locker 2 code:", code2)