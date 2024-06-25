import uuid
from datetime import datetime
from app.persistence.data_manager import save_data, load_data

class UserService:
    @staticmethod
    def validate_email(email):
        import re
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def validate_string(input_string, min_len=2):
        """ Validate that the string is not empty and meets the minimum length requirement """
        return input_string and len(input_string) >= min_len

    @staticmethod
    def get_all_users():
        users = load_data('users')  # Load data dynamically within the method
        return users

    @staticmethod
    def create_user(data):
        users = load_data('users')
        if not UserService.validate_email(data['email']):
            raise ValueError("Invalid email format")
        if any(u['email'] == data['email'] for u in users):
            raise ValueError("Email must be unique")

        # Validate first name and last name with default min_len
        if not all(UserService.validate_string(data.get(field)) for field in ['first_name', 'last_name']):
            raise ValueError("First name and last name must be at least 2 characters long")
    
        # Validate password with a min_len of 4
        if not UserService.validate_string(data.get('password'), min_len=4):
            raise ValueError("Password must be at least 4 characters long")
        
        user = {
            'id': str(uuid.uuid4()),
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        users.append(user)
        save_data('users', users)  # Save the updated list back to the JSON file
        return user

    @staticmethod
    def find_user(user_id):
        users = load_data('users')
        return next((user for user in users if user['id'] == user_id), None)

    @staticmethod
    def update_user(user_id, data):
        users = load_data('users')
        user = next((u for u in users if u['id'] == user_id), None)
        if user is None:
            raise ValueError("User not found")

        # Validate and update first name, last name
        for field in ['first_name', 'last_name']:
            if field in data and not UserService.validate_string(data[field]):
                raise ValueError(f"{field.capitalize()} must be at least 2 characters long")
            user[field] = data.get(field, user[field])

        '''
        # Validate and update password with a minimum length of 4
        if 'password' in data and not UserService.validate_string(data['password'], min_len=4):
            raise ValueError("Password must be at least 4 characters long")
        user['password'] = data.get('password', user['password'])

        # Explicitly set each field you want to update        
        user['first_name'] = data.get('first_name', user['first_name'])
        user['last_name'] = data.get('last_name', user['last_name'])
        '''
        user['updated_at'] = datetime.now().isoformat()
    
        # Save the entire users list back to the JSON file
        save_data('users', users)
        return user

    @staticmethod
    def delete_user(user_id):
        users = load_data('users')
        original_length = len(users)
        users[:] = [user for user in users if user['id'] != user_id]
        if len(users) == original_length:
            raise ValueError("User not found")
        save_data('users', users)
        return True
