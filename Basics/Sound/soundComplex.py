# import os
# from playsound import playsound

# # Get the directory of the current script
# script_dir = os.path.dirname(os.path.abspath(__file__))
# alert_path = os.path.join(script_dir, "alert.mp3")
# error_path = os.path.join(script_dir, "error.mp3")

# try:
#     playsound(alert_path)
#     print("New Message Received")
# except Exception as e:
#     print(f"(alert.mp3 not found or error: {e})")

# # For bugs , too!!

# try:
#     playsound(error_path)
#     print("An error occurred!")
# except Exception as e:
#     print(f"(error.mp3 not found or error: {e})")


from playsound import playsound

try:
    playsound("Basics/Sound/alert.mp3")
    print("New Message")
except:
    print("New Message Received (alert.mp3 not found)")

# For bugs , too!!

try:
    playsound("Basics/Sound/error.mp3")
    print("An error")
except:
    print("An error occurred! (error.mp3 not found)")