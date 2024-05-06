# Example usage:

# Initialize FitnessTracker
tracker = FitnessTracker()

# Add users
tracker.add_user(1, {'name': 'John', 'age': 30, 'gender': 'Male', 'weight': 180, 'height': 72})
tracker.add_user(2, {'name': 'Alice', 'age': 25, 'gender': 'Female', 'weight': 140, 'height': 65})

# Calculate BMI for a user
bmi = tracker.calculate_bmi(1)
if bmi:
    print("John's BMI:", bmi)

# Get user data
user_data = tracker.get_user_data(2)
if user_data:
    print("Alice's data:", user_data)

# Remove a user
tracker.remove_user(2)

# List all users
print("Existing users:", tracker.list_users())
