# Caleb Southard


def encode(password):

    new_code = ""
    for i in range(0, len(password)):
        new_code = new_code + str((int(password[i]) + 3))

    return new_code






def main():

    t = 0
    new_code = ""
    while t == 0:

        new_code
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        inp = int(input("Please enter an option: "))

        if inp == 1:
            password = (input("Please enter your password to encode: "))
            new_code = encode(password)
            print("Your password has been encoded and stored!")
        elif inp == 2:
            old_code = decode(new_code)
            print("The encoded password is " + new_code + ", and the original password is " + old_code + ".")
        elif inp == 3:
            t = 1



if __name__ == '__main__':
    main()
