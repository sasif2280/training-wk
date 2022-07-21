alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message_actual = input("enter the message: ").lower()

cypher_key = 5


def encrypt(message, key):
    encrypted_message = ""

    for letter in message:
        position = alphabets.index(letter)
        new_pos = position+key
        encrypted_message += alphabets[new_pos]

    print(encrypted_message)

    choice = input("do you want to decrypt the message ? yes / no :").lower()

    if choice == "yes":
        decrypt(encrypted_message, key)
    else:
        pass


def decrypt(encrypted_message, key):
    decrypted_message = ""
    for letter in encrypted_message:
        position = alphabets.index(letter)
        new_pos = position-key
        decrypted_message += alphabets[new_pos]
    print(f"decrypted message is {decrypted_message}")


encrypt(message_actual, cypher_key)
