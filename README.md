# Setup do projeto e instalação das bibliotecas necessárias

No terminal do VS Code, navegue até o diretório recém-clonado.<br>
python -m venv venv<br>
Ative o ambiente virtual:<br>
No Windows: .\\venv\\Scripts\\activate<br>
No macOS/Linux: source venv/bin/activate<br>
Instale as dependências dentro do ambiente virtual: pip install -r requirements.txt<br>

# Implementação dos Scripts
  ## key_generator.py
Este script gera chaves públicas e privadas.<br>

Função generate_keys<br>
-Aceita: public_key_file, private_key_file, userid, e passphrase opcional.<br>
-Cria uma chave PGP RSA de 4096 bits.<br>
-Associa o userid à chave.<br>
-Protege a chave privada com a passphrase, utilizando AES256 e SHA256.<br>
-Salva a chave pública em public_key_file e a chave privada em private_key_file. <br>

  ## encryption.py
Este script encripta mensagens.<br>

Função encrypt_message<br>
-Aceita: message, public_key_file, e encrypted_message_file.<br>
-Lê a chave pública do public_key_file.<br>
-Cria uma mensagem PGP.<br>
-Encripta a mensagem com AES256.<br>
-Salva a mensagem encriptada em encrypted_message_file.<br>

  ## decryption.py
Este script desencripta mensagens encriptadas.<br>

Função decrypt_message<br>
-Aceita: encrypted_message_file, private_key_file, e decrypted_message_file.<br>
-Lê a chave privada do private_key_file.<br>
-Desbloqueia a chave privada.<br>
-Lê a mensagem encriptada.<br>
-Tenta desencriptar a mensagem.<br>

  ## main.py
Este script contém a interface gráfica do utilizador.<br>

Funcionalidades<br>
-Importa classes e funções de key_generator, encryption, e decryption.<br>
-Apresenta um menu com ações disponíveis.<br>
-Opção "1": gera chaves públicas e privadas.<br>
-Opções "2" e "3": encripta e desencripta mensagens, respetivamente.<br>
