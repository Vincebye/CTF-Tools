def encrypt():
    pass

def decrypt(key,str):
    decrypt_str=''
    for i in str:
        decrypt_words=ord(i)+key
        if decrypt_words>ord('Z'):
            decrypt_words=decrypt_words-26
        decrypt_str=decrypt_str+chr(decrypt_words)
    return decrypt_str

if __name__=="__main__":
    decrypt_list=[]
    str=raw_input('Please enter the string to be decrypted:')
    for i in range(1,26):
        decrypt_list.append(decrypt(i,str))
    for i in decrypt_list:
        print i+'\n'

