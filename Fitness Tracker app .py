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


