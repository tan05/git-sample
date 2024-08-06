# Ask for the username
#name = input("What's your name? ")

# Print Hello to the user
#print("Hello,", name + "!")

# "end" is a parameter in print function to accept, also "sep"
#print("Hello, ", end="?? ")

# escape "
#print("Hello, \"friend\"")

# String Str methods
# Clean up input string, strip away the white space
# Cap the first letter as name
#name = name.strip().title()

# Ask for the username and chain all functions
name = input("What's your name? ").strip().title()

# Split username to first and last
first, last = name.split(" ")

# Add {} - format string fstring
#print(f"Hello, {name}")
print(f"Hello, {last}")

