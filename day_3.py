# ============================================
# INITIAL LIBRAIRIES AND VARIABLES
# ============================================
import numpy as np 

code_list = []
total_joltage = 0
# ============================================

# ============================================
# READ INPUT FILE
# ============================================
with open("input_day_3.txt", "r") as f:
    for line in f:
        code_list.append(line.strip())
# ============================================


# ============================================
# PART 1) 
# ============================================
def find_max_voltage(str_bank):
    digits_bank = []
    for i in range(len(str_bank)):
        digits_bank.append(int(str_bank[i]))

    max_voltage1 =  max(digits_bank[:-1])
    max_voltage1_id = np.argmax(digits_bank[:-1])
    max_voltage2 = max(digits_bank[max_voltage1_id+1::])
    largest_joltage = int(str(max_voltage1) +str(max_voltage2))

    return largest_joltage


# ============================================
# PART 2) 
# ============================================
def find_max_voltage_p2(str_bank):
    digits_bank = []
    for i in range(len(str_bank)):
        digits_bank.append(int(str_bank[i]))

        largest_joltage = 0

    for j in range(11):
        max_voltage = max(digits_bank[0:(j-11)])
        max_voltage_id = digits_bank.index(max_voltage)
        del digits_bank[:max_voltage_id+1]
        largest_joltage = int(str(largest_joltage)+ str(max_voltage))

    max_voltage = max(digits_bank)
    largest_joltage =  int(str(largest_joltage)+ str(max_voltage))



    return largest_joltage


# ============================================
# Main loop
# ============================================
for i in range(len(code_list)):
    largest_joltage = find_max_voltage_p2(code_list[i])
    print(largest_joltage)
    total_joltage += largest_joltage


print(total_joltage)