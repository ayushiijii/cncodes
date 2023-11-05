def validate_ip(ip):
    # Split the IP address into octets
    octets = ip.split('.')

    # Check if the IP address has 4 octets
    if len(octets) != 4:
        return False

    # Check if each octet is a valid number between 0 and 255
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            return False

    return True

def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])
    
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D"
    elif 240 <= first_octet <= 255:
        return "Class E"
    else:
        return "Invalid IP"

# Take user input for the IP address
ip_address = input("Enter an IP address: ")

# Validate the IP address
if validate_ip(ip_address):
    print("The IP address is valid.")
    ip_class = get_ip_class(ip_address)
    print(f"The IP address belongs to {ip_class}.")
else:
    print("Invalid IP address format.")