from sys import exit
from Crypto.Util.number import bytes_to_long, inverse

# setup.py
def get_primes(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes


e = 65537

def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)

def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

def main(flag):
    pubkey, _privkey = gen_key(1024)
    encrypted = encrypt(pubkey, flag) 
    return (pubkey[0], encrypted)

if __name__ == "__main__":
    flag = r"vgu{cypher}"
    N, cypher  = main(flag)
    print("N:", N)
    print("e:", e)
    print("cyphertext:", cypher)
    exit()

    #N: 22288670703444247975244112687292880970272445281270703791050070450086770191308679207225495784351035496759315582533204578842648009832955620607347800555641398                                                                                  
    #e: 65537                                                                                                                
    #cyphertext: 12115668396642174059759476959958883825647633837617438069159222405597468881671488260859380832606224765010640192958018566738188032271385626338880834536020601