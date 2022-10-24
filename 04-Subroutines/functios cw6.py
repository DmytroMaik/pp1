def get_phone_keypad():
    row=""
    for x in range(1, 10):
        row = row + str(x) + " "
        if x %3==0:
            row = row + "\n" 
    return row

print(get_phone_keypad())