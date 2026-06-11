#Simple Reflex Agent Example
def reflex_agent(status):
    if status == "dirty":
        return "Clean the room"
    elif status == "clean":
        return "Do nothing"
    else:
        return "Invalid input"
    
#Testing the agent
room_status = "dirty"  # Initialize with a default value
while room_status != "clean":
    room_status = input("Enter the status of the room (dirty/clean): ")
    action = reflex_agent(room_status)
    print(action)
