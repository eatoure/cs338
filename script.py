import math

array = [17645, 100861, 96754, 160977, 120780, 90338, 130962, 74096,
         128123, 25052, 119569, 39404, 6697, 82550, 126667, 151824,
         80067, 75272, 72641, 43884, 5579, 29857, 33449, 46274,
         59283, 109287, 22623, 84902, 6161, 109039, 75094, 56614,
         13649, 120780, 133707, 66992, 128221]

newArray = []
d = 124757
n = 162991

for num in array:
    m = pow(int(num), d,n)
    newArray.append(m)
    
print(newArray)

# Convert each integer to its hexadecimal equivalent and filter out invalid ASCII characters
ascii_chars = []
for num in newArray:
    hex_value = hex(num)[2:]  # Convert to hex and strip the '0x' prefix
    try:
        ascii_rep = bytes.fromhex(hex_value).decode('ascii')  # Attempt to decode as ASCII
        ascii_chars.append(ascii_rep)
    except (ValueError, UnicodeDecodeError):
        ascii_chars.append(f"Invalid ASCII for {hex_value}")

print(ascii_chars)

# "Dear Bob, check this out. 
# https://www.surveillancewatch.io/ See ya, Alice."
