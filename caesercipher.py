

#//cryptogram with a caeser cipher


real_mg = input("what message do you want to encode? ")
shift_pattern = int(input("How much shift do you what? "))

#//lowers any uppercase letters
real_mg = real_mg.lower()

def encrypt(rl_txt,shift):
    encoded_list = []
    
    for x in rl_txt:
        #placement in the alphabet and the mod 26 so the letter wraps around back to "a"
        place = (ord(x) - 97)% 26
        
        #add 97 so it is back to normal unicode that can be turned in to letters
        new_letter = chr((place + shift)+97)

        encoded_list.append(new_letter)
        endstring = ''.join(encoded_list)
    return endstring




print("encrypted code = "+ encrypt(real_mg,shift_pattern))
print("real code = "+ real_mg)

