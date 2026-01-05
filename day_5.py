# ============================================
# INITIAL LIBRAIRIES AND VARIABLES
# ============================================
ranges = []
# ============================================


# ============================================
# READ INPUT FILE
# ============================================
with open("input_day_5.txt") as f:
    for line in f:
        if line.strip()=="":
            break
        a,b = map(int, line.split("-"))
        ranges.append([a,b])
# ============================================


# Sort by start
ranges.sort()
# Merge
merged = []
start, end = ranges[0]


for a,b in ranges[1:]:
    if a <= end + 1:  # overlap or touching
        end = max(end, b)
    else:
        merged.append([start,end])
        start,end = a,b

merged.append([start,end])

print("Merged ranges:", merged)

# Count total
total = sum(b-a+1 for a,b in merged)
print("TOTAL :", total)
