import typer

def parite(a,b, memeParite : bool = False):
    
    if a % 2 == 0 and b % 2 == 0 or a%2 !=0 and b%2 !=0:
        memeParite = True
        return typer.secho(memeParite, fg=typer.colors.BRIGHT_GREEN)
    return  typer.secho(memeParite, fg=typer.colors.BRIGHT_RED)



def damier(n: int = 7):
    case = []
    
    for i in range(1,n+2):
        case.append(i) 
        
    print(case)
 
damier()     