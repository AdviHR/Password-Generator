import random
import string  # Add this import statement

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    """
    Generates a secure password based on user-specified requirements.

    Args:
        length: The desired length of the password.
        include_uppercase: Whether to include uppercase letters.
        include_lowercase: Whether to include lowercase letters.
        include_numbers: Whether to include numbers.
        include_symbols: Whether to include symbols.

    Returns:
        A randomly generated secure password.
    """
    characters = []
    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_lowercase:
        characters.extend(string.ascii_lowercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_symbols:
        characters.extend(string.punctuation)

    # Ensure at least one character from each desired category is included
    if not characters:
        raise ValueError("At least one character type must be included")
    
    # Add one random character from each category if specified
    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the remaining characters with random selections from the full pool
    password.extend(random.sample(characters, length - len(password)))

    # Shuffle the password for better randomness
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length < 8:
                raise ValueError("Password length must be at least 8 characters")
            include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
            include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
            include_numbers = input("Include numbers (y/n)? ").lower() == 'y'
            include_symbols = input("Include symbols (y/n)? ").lower() == 'y'

            password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
            print(f"Your secure password: {password}")
            break
        except ValueError as e:
            print(f"Error: {e}")
