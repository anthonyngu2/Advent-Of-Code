def password_checker(password):
    valid = True
    
    if len(str(password)) != 6:
        return False
    if password <= 248345 and password >= 746315:
        return False
    if valid:
        digits = list(str(password))
        duplicate = 0
        for x in range(1,len(digits),1):
            if int(digits[x-1]) > int(digits[x]):
                return False
            if int(digits[x-1]) == int(digits[x]):
                duplicate += 1
        if duplicate == 0:
            return False
    return valid

potential_passwords = []

for password in range(248345,746315,1):
    if password_checker(password):
        potential_passwords.append(password)
        
print(len(potential_passwords))
print(potential_passwords)

