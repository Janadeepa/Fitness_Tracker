class FitnessTracker:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_data):
        if user_id not in self.users:
            self.users[user_id] = user_data
            print("User added successfully!")
        else:
            print("User already exists!")

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print("User removed successfully!")
        else:
            print("User not found!")

    def update_user_data(self, user_id, updated_data):
        if user_id in self.users:
            self.users[user_id].update(updated_data)
            print("User data updated successfully!")
        else:
            print("User not found!")

    def get_user_data(self, user_id):
        if user_id in self.users:
            return self.users[user_id]
        else:
            print("User not found!")
            return None

    def list_users(self):
        return self.users.keys()

    # Advanced features

    def calculate_bmi(self, user_id):
        if user_id in self.users:
            user_data = self.users[user_id]
            weight_kg = user_data['weight'] / 2.205  # convert pounds to kilograms
            height_m = user_data['height'] * 0.0254  # convert inches to meters
            bmi = weight_kg / (height_m ** 2)
            return round(bmi, 2)
        else:
            print("User not found!")
            return None

    def recommend_workout(self, user_id):
        # Here you can implement a recommendation algorithm based on user's fitness goals, preferences, and current fitness level.
        pass

    def track_progress(self, user_id):
        # This method could track the user's progress over time, analyzing trends and providing insights for improvement.
        pass

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
