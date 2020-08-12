import hashlib

flag = 0
counter = 0

pass_hash = input('Enter md5 hash: ')

wordlist = input('Enter name of wordlist: ')

try:
    pass_file = open(wordlist,'r')
except:
    print('File not found/Incorrect file name')
    quit()

for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()
    
    print(word)
    print(digest)
    print(pass_hash)
    counter += 1
    
    if digest == pass_hash:
        print('Password Found')
        print('Password is: ' + word)
        print(counter)
        flag = 1
        break

if flag == 0:
    print('Password/Passphrase not found in the list')