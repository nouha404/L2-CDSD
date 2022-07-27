def division(n):
    etape = []
    array_compteur = []

    compteur = 0
    while n > 0:
        # si paire on divise par deux
        if n % 2 == 0:
            n //= 2
        else:
            # sinon on rajoute 1 puis divise
            n += 1
            n //= 2
        compteur += 1

        array_compteur.append(compteur)
        etape.append(n)
        if n == 1:
            break

    return print(f"Les different étapes : {str(etape).strip('[]')} et nombre de division effectuer {len(array_compteur)} ")


division(25)