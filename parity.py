def calculate_parity(binary):
    return '1' if binary.count('1') % 2 else '0'

def main():
    name = input("Enter your name: ")

    print(f"{'Character':<12} {'ASCII':<7} {'Binary':<9} {'VRC':<5}")

    vrc_values = []
    binary_columns = [[] for _ in range(7)]

    for char in name:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:].zfill(7)
        vrc = calculate_parity(binary_value)
        vrc_values.append(vrc)

        for i, bit in enumerate(binary_value):
            binary_columns[i].append(bit)

        print(f"{char:<12} {ascii_value:<7} {binary_value:<9} {vrc:<5}")

    vrc_ones = ''.join(vrc_values).count('1')
    
    lrc_values = [calculate_parity(''.join(column)) for column in binary_columns]
    lrc = ''.join(lrc_values)

    print(f"LRC = {lrc}")

    lrc_ones = lrc.count('1')

    result = (vrc_ones + lrc_ones) % 2
    print(f"Result: {result}")

if _name_ == "_main_":
    main()