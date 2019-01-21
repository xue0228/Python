import rsa,pyperclip


def readPubKeyFile(name):
    fo = open('%s_pubkey.txt' % (name))
    content = fo.read()
    fo.close()
    keySize, n, e = content.split(',')
    return int(keySize), rsa.PublicKey(int(n), int(e))

def readPriKeyFile(name):
    fo = open('%s_privkey.txt' % (name))
    content = fo.read()
    fo.close()
    keySize, n, e, d, p, q= content.split(',')
    return int(keySize), rsa.PrivateKey(int(n), int(e), int(d), int(p), int(q))

def getMessage():
    message = pyperclip.paste()
    try:
        message = eval(message)
        mode = 'decrypt'
    except:
        mode = 'encrypt'
    return message, mode

def copyMessage(message, mode):
    if mode == 'decrypt':
        message = message + '   --yw'
    pyperclip.copy(message)
    return None

def encrypt(message,keySize,pubKey):
    block = []
    for i in range(0, len(message.encode('utf8')), keySize // 8 - 11):
        block.append(message.encode('utf8')[i:min(i + (keySize // 8 - 11), len(message.encode('utf8')))])
    crypto = []
    for i in range(len(block)):
        crypto.append(rsa.encrypt(block[i],pubKey))
    enMessage = str(crypto)
    return enMessage

def decrypt(message, priKey):
    deMessage = ''
    for i in range(len(message)):
        deMessage = deMessage + (rsa.decrypt(message[i], priKey)).decode('utf8','replace')
    return deMessage

def main():
    size, pubKey=readPubKeyFile('xue')
    size, priKey=readPriKeyFile('xue')
    message, mode =getMessage()
    if mode == 'encrypt':
        text = encrypt(message,size,pubKey)
    else:
        text = decrypt(message,priKey)
    copyMessage(text,mode)

if __name__ == '__main__':
    main()