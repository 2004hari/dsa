def find_vehicles(V, W):
    # Constraint Checks
    if W < 2 or W % 2 != 0 or V >= W:
        print("INVALID INPUT")
        return
    
    # Calculate the number of two-wheelers (TW) and four-wheelers (FW)
    TW = (4 * V - W) // 2
    FW = V - TW

    # Check if calculated values are valid
    if TW < 0 or FW < 0:
        print("INVALID INPUT")
    else:
        print(f"TW={TW} FW={FW}")

# Example Input
V = int(input())  # Total number of vehicles
W = int(input())  # Total number of wheels

# Function Call
find_vehicles(V, W)
