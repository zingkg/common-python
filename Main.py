from RSA import generate_key

__author__ = 'zingkg'

print 'Testing main\n'

key = generate_key(661, 547)
cipher = key.encrypt(55)
decrypt = key.decrypt(cipher)
if 55 == decrypt:
    print 'matches\n'
else:
    print 'nope\n'
