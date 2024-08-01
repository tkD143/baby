# Passcode and reasons
PASSCODE = "baby"
reasons = [
    "Your kindness and compassion inspire me every day.",
    "You have an amazing sense of humor that always makes me laugh.",
    "Your intelligence and curiosity keep me constantly learning.",
    "You are incredibly supportive and always believe in me.",
    "Your smile brightens my day and makes everything better.",
    "You are my best friend, and I love sharing my life with you.",
    "You have a unique way of seeing the world that I adore.",
    "Your creativity and passion for life are contagious.",
    "You make even the simplest moments special and memorable.",
    "You love me for who I am, and I love you for who you are."
]

def main():
    # Loop until the correct passcode is entered
    while True:
        input_passcode = input("Enter the passcode to access the reasons: ").strip()
        if input_passcode == PASSCODE:
            break
        else:
            print("Incorrect passcode. Please try again.")
    
    # Show title and start the reason loop
    print("\nTitle: Why I Love You\n")
    seen_reasons = set()

    while len(seen_reasons) < 10:
        try:
            # Ask the user to input a number from 1 to 10
            user_input = int(input("Enter a number (1-10) to see a reason: ").strip())

            # Validate input
            if user_input < 1 or user_input > 10:
                print("Invalid input. Please enter a number between 1 and 10.")
            elif user_input in seen_reasons:
                print("You have already seen this reason. Please choose a different number.")
            else:
                # Display the corresponding reason
                print(f"Reason {user_input}: {reasons[user_input - 1]}")
                seen_reasons.add(user_input)

        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 10.")

    print("\nYou have seen all the reasons! Thank you for playing.")

if __name__ == "__main__":
    main()
