import typer
import time

def main():
    """
    Affiche les fichiers trouvés avec l'extension donnéee
    """
    # prenom = typer.style('Patrick', bold=True, bg=typer.colors.BRIGHT_RED)
    prenoms = range(100)
    with typer.progressbar(prenoms) as progress:
        for i in progress:
            time.sleep(0.1)

    typer.echo('Fin du script.')

if __name__ == "__main__":
    typer.run(main)
