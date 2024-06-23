def get_valid_input(prompt, valid_options):
    # Helper function to get valid input from the user.
    user_input = input(prompt).capitalize()
    while user_input not in valid_options:
        user_input = input(f"Invalid choice. {prompt}").capitalize()
    return user_input

# Initial prompt for pizza size with capitalization
size = get_valid_input("What size pizza do you want? S, M, or L: ", ["S", "M", "L"])

# Display the corresponding message based on the valid size and save the price
price_list = {"S": 15, "M": 20, "L": 25}
price = price_list[size]
print(f"{size} pizza is ${price}.")

# Prompt for pepperoni with validation
pepperoni = get_valid_input("Do you want pepperoni? Y or N: ", ["Y", "N"])

# Adjust price based on pepperoni and size
if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

print(f"Your total price is ${price}.")