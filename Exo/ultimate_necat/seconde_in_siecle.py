une_heure = 60 * 60
j = 24 * une_heure
an = 365

print(f'Dans un siecle il y a {j * 100 * an} seconds') 

# l'age a partir duquel un individu a vécu au moins 1 milliard de secondes
for age in range(20,90, 2):
    second_in_siecle = j * an * age
    
    if second_in_siecle >= 1000000000:
        print(f'A partir de {age}')
        break
        