import os
import pyaes

## abrir o arquivo criptografado


file_path = input("Write the file path\n")
file_name_crypted = file_path + ".ransomwaretroll"
file = open(file_name_crypted, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"chavede16digitos"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name_crypted)

## criar o arquivo descriptografado
new_file = file_path
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
