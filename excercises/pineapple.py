"""
Exercise 1: Listing pineapple routes

https://buildingai.elementsofai.com/Getting-started-with-AI/optimization
"""

# Intermediate
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Modify this if statement to check if the route is valid
                    if len(set(route)) == len(portnames):
                    # if(all(True if num in route else False for num in range(5))):
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

print("Intermediate:")
main()


# Advanced
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # Write your recursive code here
    for port in ports:
        new_route = route[:] + [port]
        new_ports = ports[:]
        new_ports.remove(port)
        permutations(new_route, new_ports)
    if len(ports) < 1:
        # Print the port names in route when the recursion terminates
        print(' '.join([portnames[i] for i in route]))
print("- " * 10)
print("Advanced:")
# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))


