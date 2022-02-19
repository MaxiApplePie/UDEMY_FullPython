import typer

def main(delete : bool = typer.Option(False, help="Supprime les fichiers trouvés") ,
         extension: str = typer.Argument('py')):
    """
    Affiche les fichiers trouvés avec l'extension donnéee
    """

    extension = typer.prompt('Quelle extension souhaitez-vous rechercher ?')
    if delete:
        do_delete = typer.confirm("'Vous confirmez la suppression ?")
        if not do_delete:
            typer.echo('Annulation ...')
            raise typer.Abort()

    print('Suppression des fichiers')

if __name__ == "__main__":
    typer.run(main)

