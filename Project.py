def is_valid_integer_literal(s):
    if len(s) == 0:
        return False

    if s[0] == '0' and len(s) > 1 and s[1] != '_':
        return False
    
    has_digit = False
    for i in range(len(s)):
        if s[i] == '_':
            if not has_digit or (i < len(s) - 1 and s[i+1] == '_'):
                return False
            elif not s[i].isdigit():
                return False
            else:
                has_digit = True

    return has_digit

    #    if len(s) == 1 or (s[1] != 'o' and s[1] != 'O' and s[1] != 'x' and s[1] != 'X'):
    #        return is_valid_decimal_integer(s)
    #    elif (s[1] == 'o' or s[1] == 'O') and len(s) > 2:
    #        return is_valid_octal_integer(s[2:])
    #    elif (s[1] == 'x' or s[1] == 'X') and len(s) > 2:
    #        return is_valid_hexadecimal_integer(s[2:])
    #    else:
    #        return False
    #else:
    #    return is_valid_decimal_integer(s)

def is_valid_decimal_integer(s):
    has_digit = False
    for i in range(len(s)):
        if s[i] == '_':
            if not has_digit or (i < len(s) - 1 and s[i+1] == '_'):
                return False
        elif not s[i].isdigit():
            return False
        else:
            has_digit = True
    return has_digit

def is_valid_octal_integer(s):
    has_digit = False
    for i in range(len(s)):
        if s[i] == '_':
            if not has_digit or (i < len(s) - 1 and s[i+1] == '_'):
                return False
        elif not (s[i] >= '0' and s[i] <= '7'):
            return False
        else:
            has_digit = True
    return has_digit

def is_valid_hexadecimal_integer(s):
    if len(s) < 3 or s[0] != '0' or (s[1] != 'x' and s[1] != 'X'):
        return False
    
    has_digit = False
    for i in range(2, len(s)):
        if s[i] == '_':
            if not has_digit or (i < len(s) - 1 and s[i+1] == '_'):
                return False
        elif not ((s[i] >= '0' and s[i] <= '9') or (s[i] >= 'a' and s[i] <= 'f') or (s[i] >= 'A' and s[i] <= 'F')):
            return False
        else:
            has_digit = True
    return has_digit

def is_valid_floating_point_literal(s):
    if len(s) == 0:
        return False

    i = 0
    if s[i] == '.':
        i += 1
        if not is_valid_digitpart(s[i:]):
            return False
    else:
        if is_valid_digitpart(s[i:]):
            i += len(s[i:].split('_')[0])
        if i < len(s) and s[i] == '.':
            i += 1
            if i < len(s) and is_valid_digitpart(s[i:]):
                i += len(s[i:].split('_')[0])
        if i < len(s) and (s[i] == 'e' or s[i] == 'E'):
            i += 1
            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                i += 1
            if not is_valid_digitpart(s[i:]):
                return False

    return True

def is_valid_digitpart(s):
    if len(s) == 0:
        return False

    has_digit = False
    for i in range(len(s)):
        if s[i] == '_':
            if not has_digit or (i < len(s) - 1 and s[i+1] == '_'):
                return False
        elif not s[i].isdigit():
            return False
        else:
            has_digit = True

    return has_digit

def is_valid_literal(s):
    return is_valid_integer_literal(s) or is_valid_floating_point_literal(s)

def checkLiteral (literal_type, s):
    if literal_type == 1:
        return is_valid_decimal_integer(s)
    elif literal_type == 2:
        return is_valid_octal_integer(s)
    elif literal_type == 3:
        return is_valid_hexadecimal_integer(s)
    elif literal_type == 4:
        return is_valid_floating_point_literal(s)
    else:
        return False
    
while True:
    print ("Please select the type of literal to check:")
    print("1. Decimal Integer")
    print("2. Octal Integer")
    print("3. Hexadecimal Integer")
    print("4. Floating-Point")
    print("5. Quit")
    print()

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        break
    if choice < '1' or choice >'4':
        print("Invalid choice. Please try again.")
        continue

    literal_type = int(choice)
    user_input = input ("Enter a string: ")

    if checkLiteral(literal_type, user_input):
        print(f"{user_input} is a valid {['Decimal Integer', 'Octal Integer', 'Hexadecimal Integer', 'Floating-Point'][literal_type - 1]} literal.")
    else:
        print(f"{user_input} is not a valid {['Decimal Integer', 'Octal Integer', 'Hexadecimal Integer', 'Floating-Point'][literal_type - 1]} literal.")

    print()
