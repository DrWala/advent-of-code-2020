from collections import Counter

def count_valid_passwords_one(passwords):
    count = 0
    for password in passwords: # O(N)
        password_policy = password.split(":")[0]
        password_policy_repeat_min = int(password_policy.split(" ")[0].split("-")[0])
        password_policy_repeat_max = int(password_policy.split(" ")[0].split("-")[1])
        password_text = password.split(":")[1][1:]
        
        freq = Counter(password_text) #O(S)
        if freq[password_policy[-1]] >= password_policy_repeat_min and freq[password_policy[-1]] <= password_policy_repeat_max:
            count += 1
    return count
        
def count_valid_passwords_two(passwords):
    count = 0
    for password in passwords: # O(N)
        password_policy = password.split(":")[0]
        password_policy_idx_1 = int(password_policy.split(" ")[0].split("-")[0]) - 1
        password_policy_idx_2 = int(password_policy.split(" ")[0].split("-")[1]) - 1
        password_policy_character = password_policy[-1]

        password_text = password.split(":")[1][1:]
        
        # Python does not have XOR, so != functions like an XOR
        if (password_text[password_policy_idx_1] == password_policy_character) != (password_text[password_policy_idx_2] == password_policy_character):
            count += 1
    return count

file = open("input.txt", "r")
print(count_valid_passwords_one(file.readlines()))
file = open("input.txt", "r")
print(count_valid_passwords_two(file.readlines()))