import re

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    return score, feedback


def main():
    print("=== Password Security Checker ===")
    while True:
        password = input("\nEnter your password (or type 'exit'): ")

        if password.lower() == "exit":
            print("Goodbye!")
            break

        score, feedback = check_password(password)

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

        print(f"\nPassword Strength: {strength}")
        print(f"Security Score: {score}/5")
        if feedback:
            print("Suggestions:")
            for item in feedback:
                print("-", item)


if __name__ == "__main__":
    main()