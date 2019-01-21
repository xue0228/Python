import rsa,sys,os


def main():
    print('Making key files...')
    makekey('xue',4096)
    print('Key files made.')

def makekey(name,keySize):
    (pubKey, priKey) = rsa.newkeys(keySize)
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))

    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (keySize, pubKey.n, pubKey.e))
    fo.close()

    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s,%s,%s,%s' % (keySize, priKey.n, priKey.e, priKey.d, priKey.p, priKey.q))
    fo.close()

if __name__ == '__main__':
    main()