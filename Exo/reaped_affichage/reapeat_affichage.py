
import typer


def liste(L : list , n : int = 1):
    array = L
    
    if len(array) > 9:
        return typer.secho('Le tableau doit etre inferieur ou egale a 9', fg=typer.colors.BRIGHT_RED)
    
    for i in range(1,n+1):   
        array[0] = i     
        array_in_string = "".join(str(array)).replace(',','').strip('[]')
        typer.secho(array_in_string, fg=typer.colors.BRIGHT_YELLOW)


liste([1,4,8,0,9,6,3,2,8],4)   