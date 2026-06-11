def trafficAgent(light_color):
    if light_color == "red":
        return "Stop"
    elif light_color == "yellow":
        return "Get ready"
    elif light_color == "green":
        return "Go"
    else:
        return "Invalid traffic light color"
    
#Testing the agent
signal = input("Enter the traffic light color (red/yellow/green): ")
print(trafficAgent(signal))