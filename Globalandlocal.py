#local_and_global_variable -You’re building a basic banking system. There’s a global variable balance that stores the user’s total account balance. Inside a function, you perform a temporary calculation (like a test deposit) using a local variable, which does not affect the actual balance unless updated globally.
#Create a global variable to store the account balance.
#Write a function that uses a local variable to simulate a change.
#Show how local changes don't affect the global value unless explicitly updated.

# Global balance
balance = 1000.00

def simulate_local_change():
    # local variable only — doesn't change global balance
    local_balance = balance  # reads global
    local_balance += 500.00  # simulate a test deposit
    print(f"(inside simulate_local_change) local_balance = {local_balance:.2f}")

def update_global_using_global_keyword():
    global balance
    balance += 500.00
    print(f"(inside update_global_using_global_keyword) balance updated to {balance:.2f}")

def update_global_by_returning(old_balance):
    new_balance = old_balance + 500.00
    return new_balance

print(f"Initial global balance: {balance:.2f}")
simulate_local_change()
print(f"After simulate_local_change: global balance = {balance:.2f}")

# Option 1: use global keyword to change global variable
update_global_using_global_keyword()
print(f"After update_global_using_global_keyword: global balance = {balance:.2f}")

# Option 2: explicitly return and reassign (preferred pattern)
balance = update_global_by_returning(balance)
print(f"After update_global_by_returning and reassign: global balance = {balance:.2f}")