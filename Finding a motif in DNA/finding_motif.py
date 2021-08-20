
matching_positions = []
start = 0

s = input("Enter the 's' sequence:\n")
t = input("Enter the 't' substring of 's':\n")

while (start + len(t)) <= len(s):
    s_unit = s[start: (start + len(t))]
    print(s_unit)

    if t == s_unit:  
        print(f"match found at position {start}")
        matching_positions.append(start+1) # +1 because counting start from 0
        start += 1

    if t != s_unit:
        start += 1

print(matching_positions)



























