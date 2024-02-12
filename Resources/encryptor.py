def GGGGotate(lol):
    bit = lol << 1
    movebit = bit & 255
    if (lol > 127 ):
        movebit = movebit | 1
    return (movebit)
def main():
    value = input("Enter your value: ")
    ListMoveBit = []
    Index_Move_bit = 1
    Index_Value = 0
    ORD_value = []
    ORD_key = []
    Under_10 = []
    Index_star = 0
    Final_encrypted = ""
    Passs = []
    List_values_back = []
    Uncrypt = []
    for i in value:
        ORD_value.append(ord(i))
    a = ord("a")
    ORD_key.append(a)
    lol = int(ORD_key[0]) ^ int(ORD_value[0])
    ListMoveBit.append(GGGGotate(lol))
    for chars in ORD_value:
        if Index_Value == 0:
            Index_Value += 1
            pass
        else:
            lol = int(ListMoveBit[Index_Value-1]) ^ int(chars)
            ListMoveBit.append(GGGGotate(lol))
            Index_Value += 1
    for i in ListMoveBit:
        Under_10.append("0")
    for i in ListMoveBit:
        if (i < 9):
            Under_10[Index_star] = "1"
        Index_star += 1
    for i in ListMoveBit:
        x = hex(i)
        val = x[2:]
        if(i > 9) and (i < 16):
            Final_encrypted = Final_encrypted + "0" + val
        else:
            if (i<10):
                Final_encrypted = Final_encrypted +"0"+val
            else:
                Final_encrypted = Final_encrypted + val
    print("\nThe encrypted message is:")
    print(Final_encrypted + "\n")
if __name__ == '__main__':
    main()

