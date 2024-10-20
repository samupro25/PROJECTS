import random
import string

class PasswordGenerator:
    def __init__(self):
        self.characters = {
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'digits': string.digits,
            'special': string.punctuation
        }

    def generate_password(self, length=12, use_uppercase=True, use_digits=True, use_special=True, avoid_ambiguous=True):
        """
        Generates a random password with the specified options.
        """
        pool = self.characters['lowercase']
        if use_uppercase:
            pool += self.characters['uppercase']
        if use_digits:
            pool += self.characters['digits']
        if use_special:
            pool += self.characters['special']

        if avoid_ambiguous:
            ambiguous_chars = "il1Lo0O"
            pool = ''.join([char for char in pool if char not in ambiguous_chars])

        if length < 4:
            print("Password length must be at least 4.")
            return None
        
        password = ''.join(random.choices(pool, k=length))
        return password

def main():
    generator = PasswordGenerator()
    
    print("\n=== Password Generator ===")
    
    try:
        length = int(input("Enter the password length (min 4): "))
        if length < 4:
            raise ValueError("Password length must be at least 4.")
            
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        avoid_ambiguous = input("Avoid ambiguous characters? (y/n): ").lower() == 'y'

        password = generator.generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_special=use_special,
            avoid_ambiguous=avoid_ambiguous
        )
        
        if password:
            print(f"\nYour generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
