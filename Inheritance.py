#inheritance-Salary Management System using Object-Oriented Programming with inheritance, involving Employee and Manager classes.
#Scenario:
#You're creating a salary management program for a company. There are two types of people:
#Employees: Have basic details like name, ID, and base salary.
#Managers: Are also employees but get additional bonuses and perks.

class Employee:
    def __init__(self, name: str, emp_id: str, base_salary: float):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = float(base_salary)

    def compute_salary(self) -> float:
        """Return total salary for a regular employee (just base)."""
        return self.base_salary

    def display_info(self) -> None:
        total = self.compute_salary()
        print(f"Employee: {self.name} (ID: {self.emp_id})")
        print(f"  Base salary:      ₹{self.base_salary:,.2f}")
        print(f"  Total salary:     ₹{total:,.2f}")
        print("-" * 40)


class Manager(Employee):
    def __init__(self, name: str, emp_id: str, base_salary: float,
                 bonus: float = 0.0, perks: list | None = None):
        super().__init__(name, emp_id, base_salary)
        self.bonus = float(bonus)
        self.perks = perks or []  # list of strings describing perks

    def compute_salary(self) -> float:
        """Managers get base + bonus (you could add perk value if needed)."""
        return self.base_salary + self.bonus

    def add_perk(self, perk: str) -> None:
        self.perks.append(perk)

    def display_info(self) -> None:
        total = self.compute_salary()
        print(f"Manager:  {self.name} (ID: {self.emp_id})")
        print(f"  Base salary:      ₹{self.base_salary:,.2f}")
        print(f"  Bonus:            ₹{self.bonus:,.2f}")
        print(f"  Total salary:     ₹{total:,.2f}")
        if self.perks:
            print(f"  Perks:            {', '.join(self.perks)}")
        else:
            print("  Perks:            None")
        print("-" * 40)


# Example usage:
if __name__ == "__main__":
    # Create employees
    e1 = Employee("Asha Patel", "E001", 45000)
    e2 = Employee("Vikram Singh", "E002", 38000)

    # Create managers with bonus and perks
    m1 = Manager("Renu Sharma", "M001", 90000, bonus=15000, perks=["Car allowance", "Stock options"])
    m2 = Manager("Anil Mehra", "M002", 80000, bonus=10000)
    m2.add_perk("Gym membership")

    # Put everyone in one list — demonstrates polymorphism
    staff = [e1, e2, m1, m2]

    # Display info for all staff
    for person in staff:
        person.display_info()

    # Example: total payroll
    total_payroll = sum(person.compute_salary() for person in staff)
    print(f"Total payroll for this period: ₹{total_payroll:,.2f}")