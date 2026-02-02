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