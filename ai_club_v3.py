import os
from datetime import datetime

filename = "ai_club_members.txt"

# Create the file if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("ID\tName\t\tRole\t\tJoined On\n")

# Load members into a dictionary
members = {{}}
next_id = 1

with open(filename, "r") as f:
    lines = f.readlines()[1:]  # skip header
    for line in lines:
        parts = line.strip().split("\t")
        if len(parts) >= 3:
            members[parts[1]] = parts[2]
            next_id += 1

print("👾 Welcome to the AI Club Interactive System!")

while True:
    name = input("Enter a name (or type 'exit' to quit): ").strip()

    if name.lower() == "exit":
        print("👋 Bye! See you next time.")
        break

    if name == "Eric":
        if name in members:
            print("You again, Eric! 👨‍💻 Welcome back, Founder.")
        else:
            print("Eric, you're the Club Founder! 👑")
            members[name] = "Club Founder"
            with open(filename, "a") as f:
                f.write(f"{next_id}\t{name}\tClub Founder\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                next_id += 1
            print("✔ Founder status saved!")
    else:
        if name in members:
            print(f"You again, {name}! 👋 Welcome back.")
        else:
            print(f"Hey {name}, you’re now part of the AI club!")
            members[name] = "Member"
            with open(filename, "a") as f:
                f.write(f"{next_id}\t{name}\tMember\t{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                next_id += 1
            print("✔ Member status saved!")