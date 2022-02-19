import typer

def main():
    """
    Affiche les fichiers trouvés avec l'extension donnéee
    """
    # prenom = typer.style('Patrick', bold=True, bg=typer.colors.BRIGHT_RED)
    prenom = typer.style('Patrick', bold=True, underline=True)
    typer.echo(f'Bonnjour {prenom}')


if __name__ == "__main__":
    typer.run(main)
