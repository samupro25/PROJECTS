import random

class DiceRoller:
    def __init__(self):
        self.history = []

    def roll_dice(self, num_dice=1, num_sides=6):
        """
        Rolls specified number of dice with the given number of sides.
        Default is 1d6 (one 6-sided die).
        """
        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total = sum(rolls)
        self.history.append((num_dice, num_sides, rolls, total))
        return rolls, total

    def display_history(self):
        """Displays all the previous rolls and their totals."""
        if not self.history:
            print("No rolls yet.")
        else:
            for i, (num_dice, num_sides, rolls, total) in enumerate(self.history, 1):
                print(f"Roll {i}: {num_dice}d{num_sides} -> Rolls: {rolls} | Total: {total}")

    def clear_history(self):
        """Clears the rolling history."""
        self.history = []
        print("History cleared.")

def main():
    roller = DiceRoller()
    while True:
        print("\n=== Dice Roller ===")
        print("1. Roll dice")
        print("2. View roll history")
        print("3. Clear history")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            try:
                num_dice = int(input("Enter number of dice to roll: "))
                num_sides = int(input("Enter number of sides per die: "))
                rolls, total = roller.roll_dice(num_dice, num_sides)
                print(f"\nYou rolled: {rolls}")
                print(f"Total: {total}")
            except ValueError:
                print("Invalid input. Please enter integers.")
        elif choice == "2":
            roller.display_history()
        elif choice == "3":
            roller.clear_history()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
