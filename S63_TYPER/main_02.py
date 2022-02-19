import typer

def main(extension: str = typer.Argument('py')):
    """
    Affiche les fichiers trouvés avec l'extension donnéee
    """

    typer.echo(f"Recherche des fichiers avec l'extension {extension}.")

if __name__ == "__main__":
    typer.run(main)

