from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from key_generator import generate_keys
from encryption import encrypt_message
from decryption import decrypt_message

if __name__ == "__main__":
    public_key_file = input("Enter the name of the file where you want to store the public key: ")
    # Ask the user where to save the private key file
    print("Enter the name and the location of the file where you want to store the private key:")
    Tk().withdraw()  # to hide the main window
    private_key_file = asksaveasfilename()  # show a "Save As" dialog box and return the path to the selected file
    userid = input("Enter the user ID (email address): ")
    encrypted_message_file = input("Enter the name of the file where you want to keep the encrypted message: ")
    decrypted_message_file = input("Enter the name of the file where you want to store the decrypted message: ")
    passphrase = None #input("Enter passphrase to protect the private key") # Meter 'None' para não ter password e funcionar, ainda nao esta funcional :(
    generate_keys(public_key_file, private_key_file, userid, passphrase)
    message = input("Enter the message to encrypt: ")
    encrypt_message(message, public_key_file, encrypted_message_file)
    # Ask the user to select the private key file
    print("Enter the location of the private key file:")
    private_key_file = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    decrypt_message(encrypted_message_file, private_key_file, decrypted_message_file)
    

