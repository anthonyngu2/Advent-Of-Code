from collections import Counter
potential_passwords = []

def password_checker(password):
    valid = True
    
    if len(str(password)) != 6:
        return False
    if password <= 248345 and password >= 746315:
        return False
    if valid:
        duplicate = 0
        digits = list(str(password))
        for x in range(1,len(digits),1):
            cond = x
            if int(digits[x-1]) > int(digits[x]):
                return False                
##            if int(digits[x-1]) == int(digits[x]):
##                duplicate += 1
##        if duplicate == 0:
##            return False
        counter = Counter(digits)
        subpass = [digit for digit, count in counter.items() if count == 2]
        if len(subpass) == 0:
            return False
        return valid

for password in range(248345,746315,1):
    if password_checker(password):
        potential_passwords.append(password)

print(len(potential_passwords))

