def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def crc_division(data, divisor):
    pick = len(divisor)
    tmp = data[0:pick]

    while pick < len(data):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + data[pick]
        else:
            tmp = xor('0'*pick, tmp) + data[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def pad_data(data, pad_length):
    return data + '0' * (pad_length - 1)

def crc_encode(data, divisor):
    padded_data = pad_data(data, len(divisor))
    crc = crc_division(padded_data, divisor)
    return data + crc

def simulate_transmission(encoded_data):
    return encoded_data

def check_for_error(received_data, divisor):
    remainder = crc_division(received_data, divisor)
    return '1' in remainder

# Input
data = input("Enter data to be transmitted (in binary): ")
divisor = input("Enter generating polynomial (in binary): ")

# Encoding
encoded_data = crc_encode(data, divisor)

# Calculate and print CRC value
crc_value = encoded_data[-(len(divisor)-1):]
print("CRC Value (Check Value):", crc_value)

# Print Data with CRC
print("Data with CRC:", encoded_data)

# Simulate Transmission
received_data = simulate_transmission(encoded_data)
print("Received data:", received_data)

# Check for Error
error_detected = check_for_error(received_data, divisor)
if error_detected:
    print("Error detected!")
else:
    print("No errors detected.")