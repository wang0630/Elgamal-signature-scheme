from elgamal import *

if __name__ == '__main__':
    elgamal_ins = Elgamal('hello!!!!!!!')

    elgamal_ins.sign()

    print(f'alpha: {elgamal_ins.alpha}, which belongs to (Z_p)*')
    print(f'The hash of the message is {elgamal_ins.hs_int}')
    print(f'private key: {elgamal_ins.private}, where 1 <= private <= p-1')
    print(f'k is {elgamal_ins.k}, where k is selected at random by signing party, k belongs to (Z_(p-1))*')
    print(f'Signature 1 is gamma: {elgamal_ins.gamma}, where gamma = alpha^k mod p')
    print(f'Signature 2 is delta: {elgamal_ins.delta}, where delta = (hash(msg)-private*gamma)k^(-1) mod (p-1)')
    print(f'Signature should equal to {pow(elgamal_ins.alpha, elgamal_ins.hs_int, elgamal_ins.p)}')

    if elgamal_ins.verify():
        print('Correct sign')
    else:
        print('Incorrect sign')
