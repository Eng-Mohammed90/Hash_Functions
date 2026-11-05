
# Define permissions for each role
role_permissions = {
    "Admin": ["Create", "View", "Update", "Delete"],
    "Manager": ["View", "Update"],
    "Customer": ["View"]
}

# Assign users to roles
users = {
    "Ali": "Admin",
    "Ahmad": "Manager",
    "Sara": "Customer"
}


# Check if a user has permission to perform an action
def check_permission(username, action):
    if username not in users:
        print("User not found!")
        return

    role = users[username]
    permissions = role_permissions[role]

    if action in permissions:
        print(f"Access Granted: {username} can {action} accounts.")
    else:
        print(f"Access Denied: {username} cannot {action} accounts.")


# Main program
while True:
    print("\n===== RBAC System =====")
    print("1. Assign a role to a user")
    print("2. Check permission")

    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")

        print("Available roles: Admin, Manager, Customer")
        role = input("Enter role: ")

        if role in role_permissions:
            users[username] = role
            print(f"{username} has been assigned to {role} role.")
        else:
            print("Invalid role!")

    elif choice == "2":
        username = input("Enter username: ")

        print("Available permissions: Create, View, Update, Delete")
        action = input("Enter action: ")

        if action in ["Create", "View", "Update", "Delete"]:
            check_permission(username, action)
        else:
            print("Invalid action!")

    else:
        print("Invalid choice!")
