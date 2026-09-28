# Initial setup: Location and room conditions
vacuum_location = "A"  
rooms = {"A": "Dirty", "B": "Dirty"} 

print("Starting simulation...")
print(f"Initial Status: {rooms}\n" + "-"*30)


while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":
    

    if rooms[vacuum_location] == "Dirty":
        print(f"Vacuum is in Room {vacuum_location}. It is Dirty -> Sucking dirt!")
        rooms[vacuum_location] = "Clean"
    else:
        print(f"Vacuum is in Room {vacuum_location}. It is already Clean.")


    if vacuum_location == "A":
        print("Action: Moving RIGHT to Room B.")
        vacuum_location = "B"
    else:
        print("Action: Moving LEFT to Room A.")
        vacuum_location = "A"
        
    print(f"Current Status: {rooms}")
    print("-" * 30)

print("Both rooms are clean! Vacuuming complete.")
