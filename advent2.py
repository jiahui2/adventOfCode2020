def pw_is_valid(passwordline):
    limit_str, letter, password = passwordline.split(' ')
    least, most = list(map(int, limit_str.split('-')))
    # print(limit_str, letter, password, least, most)
    # print(password.count(letter[0]))
    if least <= password.count(letter[0]) <= most:
        return True
    return False

with open('adv2_input.txt') as file_handle:
    all_pw = file_handle.read().splitlines()
    # print(all_pw[:5])
    # print(pw_is_valid(all_pw[0]))
    count = 0
    for line in all_pw:
        count += 1 if pw_is_valid(line) else 0
    print(count)