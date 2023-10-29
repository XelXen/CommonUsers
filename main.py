# Import Libraries
from pyrogram import Client
from VarFile import api_id, api_hash, blacklist

# Create a new Telegram Client
with Client(name="my_account", api_id=api_id, api_hash=api_hash, in_memory=False) as app:
    
    # Get all participants from a chat
    def get_all_participants(chat):
        all_participants = []
        n = 0

        for member in app.get_chat_members(chat_id=chat):
            all_participants.append(member.user.id)
            n += 1
            print(f"{n} users processed", end="\r")

        return all_participants

    # Get the chat id/username
    chat = input("Enter chat id/username: ")

    if chat.isdigit(): chat = int(chat)
    elif chat == "exit" or chat.strip() == "": exit()
    else: chat = chat.replace("@", "").replace("https://t.me/", "")

    # Get all participants from the chat
    group = set(get_all_participants(chat=chat)) - set(blacklist)

    # Intersections Loop
    while True:
        # Get the chat id/username
        chat = input("\n\nEnter chat id/username: ")

        if chat.isdigit(): chat = int(chat)
        elif chat == "exit": break
        elif chat.strip() == "": continue
        else: chat = chat.replace("@", "").replace("https://t.me/", "")

        # Get intersections
        group = group & set(get_all_participants(chat=chat))

        # Print the intersections
        print("\n\nTotal intersections:", len(group))
        print("Users:", ", ".join([str(i) for i in group]))