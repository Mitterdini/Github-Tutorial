from crypt import crypt

rotation = [1, 6, 3, 9, 5, 7, 4, 8, 2, 0]
salt_list = ['sU', 'lo', 'Gl', 'FI', 'Lo', 'cL', 'AT', 'nr', 'rP', 'Ci']
salt_select = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
counter = 0

while True:
    user_input = input()
    rotate = rotation[counter]
    salt_position = salt_select[rotate]
    salt = salt_list[salt_position]
    salt_select[rotate] = rotation[salt_position]

    print('salt:', salt)
    print('input:', user_input)
    encryption = crypt(user_input, salt)
    print('encryption:', encryption)
    counter += 1
    if counter == 10:
        counter = 0
    else:
        pass
