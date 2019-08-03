import random

def change_char(s, p, r):
    # add the r (replaccement) in the p (spot)
    return s[:p]+r+s[p+1:]

def add_noise(binary_string, probability_of_noise):
    # result string
    noised_string = binary_string

    for char in range(len(binary_string)):
        # throw a random number to see if the character will recieve noise
        probabiliy = random.uniform(0, 1)
        if probabiliy < probability_of_noise:
            # perform a switch
            if binary_string[char] == '0':
                noised_string = change_char(noised_string, char, "1")
            elif binary_string[char] == '1':
                noised_string = change_char(noised_string, char, "0")
    
    return noised_string

# test the noise at 50% probability 
#print(add_noise('01001', 0.5))