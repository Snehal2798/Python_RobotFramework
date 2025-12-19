# 1. Global Variable: This exists outside any function and is accessible everywhere.
balance = 1000.00


def simulate_deposit(amount):
    # 2. Local Variable: This exists ONLY inside this function.
    # It performs a temporary calculation.
    local_balance = balance + amount

    print(f"--- Inside the Function ---")
    print(f"Temporary Local Balance: ${local_balance}")
    print(f"Actual Global Balance: ${balance}")
    print("----------------------------")


# Main program flow
print(f"Initial Account Balance: ${balance}")

# Simulate a $500 deposit
simulate_deposit(500)

# 3. Showing that the global balance remains unchanged
print(f"Final Account Balance (after function): ${balance}")