model = {
    "A":"dirty",
    "B":"dirty"
}

def model_based_vacuum_agent(location,status):
    #update internal model
    model[location] = status

    #decide action based on model
    if status == "dirty":
        return "Clean"
    
    #check if other room is dirty
    elif model["A"] == "clean" and model["B"] == "clean":
        return "Stop"
    elif location == "A":
        return "Move to B"
    elif location == "B":
        return "Move to A"
    
#Simulation
print(model_based_vacuum_agent("A","dirty"))  # Clean A
model["A"] = "clean"  # Update model after cleaning A

print(model_based_vacuum_agent("A","clean"))  # Move to B
print(model_based_vacuum_agent("B","dirty"))  # Clean B
model["B"] = "clean"  # Update model after cleaning B

print(model_based_vacuum_agent("A","dirty"))  # Both rooms are clean, so stop
model["A"] = "clean"  # Update model after cleaning A
print(model_based_vacuum_agent("B","clean"))  # Both rooms are clean, so stop