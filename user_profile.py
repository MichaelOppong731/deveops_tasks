import os

# Define the filename for the profile file and path to user's home directory
PROFILE_FILENAME = "profile.txt"
HOME_DIR = os.path.expanduser("~")

# Function to get user input for profile details
def get_user_input():
    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    email = input("Enter your email: ")
    return name, phone, email

# Function to create or update the profile file with provided data
def write_profile(filepath, name, phone, email):
    with open(filepath, "w") as file:
        file.write(f"Name: {name}\nPhone: {phone}\nEmail: {email}\n")
    print("Profile information saved successfully.")

# Check if current directory matches the username
def check_user_directory():
    username = os.getlogin()  # Get current logged-in username
    current_dir = os.getcwd()  # Get current working directory
    
    # Check if current directory matches user's home directory
    if os.path.basename(current_dir) == username:
        print("User directory matches username.")

        profile_path = os.path.join(current_dir, PROFILE_FILENAME)

        # Check if the profile file exists
        if os.path.isfile(profile_path):
            with open(profile_path, "r") as file:
                profile_data = file.read()
            
            print("Profile information:\n", profile_data)
            confirmation = input("Is this information up to date? (yes/no): ").strip().lower()

            if confirmation == "no":
                # If user wants to update information, gather new details and save them
                name, phone, email = get_user_input()
                write_profile(profile_path, name, phone, email)
        else:
            # If profile file doesn't exist, create it
            print("Profile not found. Creating a new profile.")
            name, phone, email = get_user_input()
            write_profile(profile_path, name, phone, email)
    else:
        # If current directory doesn't match username, create a new directory and profile file
        user_dir = os.path.join(HOME_DIR, username)
        os.makedirs(user_dir, exist_ok=True)
        profile_path = os.path.join(user_dir, PROFILE_FILENAME)
        print(f"Directory created: {user_dir}")

        # Gather and save profile information in the new directory
        name, phone, email = get_user_input()
        write_profile(profile_path, name, phone, email)

    print("You may continue using the terminal.")

# Run the check when the user logs into the terminal
if __name__ == "__main__":
    check_user_directory()

