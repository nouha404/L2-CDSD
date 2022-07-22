### Damier de nombres
```
On dit que deux entiers a et b ont même parité si a et b sont tous les deux pairs ou bien si a et b sont tous les deux impairs.

Par exemple, 81 et 31 ont même parité, 12 et 82 ont même parité et 81 et 12 ont des parités différentes.
```
```py
""" 
Ecrire un code qui à partir de deux entiers calcule la valeur d’une variable memeParite qui vaut True si les deux entiers ont même parité, et False sinon.
"""
def parite(a,b, memeParite : bool = False):
    
    if a % 2 == 0 and b % 2 == 0 or a%2 !=0 and b%2 !=0:
        memeParite = True
        return typer.secho(memeParite, fg=typer.colors.BRIGHT_GREEN)
    return  typer.secho(memeParite, fg=typer.colors.BRIGHT_RED)
   

parite(82,12)
```

```
Réaliser un programme qui affiche un damier de forme carrée, de côté de longueur n > 0 et rempli alternativement du nombre 4 et du nombre 2.
```


