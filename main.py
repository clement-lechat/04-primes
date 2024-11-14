from math import sqrt

#### Fonction secondaire
def isprime(p):
    """
    Verifie que l'entier passé en argument est un nombre premier
    Args :
        p : valeur entiere >= 2
    Returns:
        isprime(p) : True or False
    >>> isprime(0)
    False
    >>> isprime(1)
    False
    >>> isprime(4)
    False
    >>> isprime(5)
    True
    """   
    if p<=1:
        return False
    d = int(sqrt(p))
    for i in range(2,d+1):
        if p%i == 0:
            return False

    return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici
    print(isprime(25))
    print(isprime(41))
    print(isprime(1433))
    print(isprime(19))
    help(isprime)
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()

if __name__ == "__main__":
    main()
