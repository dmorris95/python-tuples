#Task 1

flight_it = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def format_tuple(flight_info):
    count = 1
    flight_string = ""
    for flight in flight_info:
        (name, origin, destination) = flight
        flight_string += (f"Itinerary {count}: {name} - From {origin} to {destination}\n")
        count += 1
    return flight_string
print(format_tuple(flight_it))