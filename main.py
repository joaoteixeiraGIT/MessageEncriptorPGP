from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from key_generator import generate_keys
from encryption import encrypt_message
from decryption import decrypt_message

if __name__ == "__main__":
    option = None
    #Menu principal
    while option != "4":
        print("Bem vindo ao programa de encriptação e desencriptação de mensagens! :D")
        print("Selecione uma das opções:")
        print("1. Gerar chaves")
        print("2. Encriptar mensagem")
        print("3. Desencriptar mensagem")
        print("4. Sair")

        option = input("Opção: ")
    
        if option == "1":
            public_key_file = input("Introduza o nome do ficheiro onde quer guardar a chave pública: ")
            print("Introduza o nome e a localização do ficheiro onde quer guardar a chave privada:")
            Tk().withdraw()  
            private_key_file = asksaveasfilename()  
            userid = input("Introduza o ID do utilizador (endereço email): ")
            passphrase = None #input("Introduza uma palavra-passe para proteger a chave privada") # Meter 'None' para não ter password e funcionar, ainda não esta funcional :(
            generate_keys(public_key_file, private_key_file, userid, passphrase)    
            
        elif option == "2":
            print("Localize o ficheiro da chave pública: ")
            sender_public_key_file = askopenfilename()
            encrypted_message_file = input("Introduza o nome do ficheiro onde quer guardar a mensagem encriptada: ")
            message = input("Introduza a mensagem: ")
            encrypt_message(message, sender_public_key_file, encrypted_message_file)

        elif option == "3":
            print("Localize o ficheiro da mensagem encriptada: ")
            recieved_encrypted_message_file = askopenfilename()
            decrypted_message_file = input("Introduza o nome do ficheiro onde quer guardar o ficheiro desencriptado: ")
            print("Localize o ficheiro da chave privada: ")
            my_private_key_file = askopenfilename()
            decrypt_message(recieved_encrypted_message_file, my_private_key_file, decrypted_message_file)
        elif option == "4":
            print("Obrigado por usar o programa! Até à próxima! :D")

        

