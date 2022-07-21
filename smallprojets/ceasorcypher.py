alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt():
    message_actual = input("enter the message: ").lower()

    cypher_key = int(
        input("enter cypher key ! (*****rember key must be lesser than 26******)"))
    encrypted_message = ""

    for letter in message_actual:
        position = alphabets.index(letter)
        new_pos = position+cypher_key
        encrypted_message += alphabets[new_pos]

    print(encrypted_message)

    choice = input("do you want to decrypt the message ? yes / no :").lower()

    if choice == "yes":
        decrypt(encrypted_message, cypher_key)
    else:
        print("good bye !!")


def decrypt(encrypted_message, key):
    decrypted_message = ""
    for letter in encrypted_message:
        position = alphabets.index(letter)
        new_pos = position-key
        decrypted_message += alphabets[new_pos]
    print(f"decrypted message is {decrypted_message}\n \n")

    choice = input("do you like to encrypt the message again ? :").lower()

    if choice == "yes":
        encrypt()
    else:
        print("good bye !!")


def new_decrypt(encrypted_message, key):
    decrypted_message = ""
    for letter in encrypted_message:
        position = alphabets.index(letter)
        new_pos = position-key
        decrypted_message += alphabets[new_pos]
    print(f"decrypted message is {decrypted_message}\n \n")
    choice = input("do you like to encrypt the message again ? :").lower()
    if choice == "yes":
        encrypt()
    else:
        print("good bye !!")


def main_menu():
    print("\t1 >> encrypt\n")
    print("\t2 >> decrypt \n")
    choice = int(input("select one option : "))

    match(choice):
        case 1:
            encrypt()
        case 2:
            new_decrypt()


main_menu()
