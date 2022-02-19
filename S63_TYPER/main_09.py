import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()


@app.command()
def search(extension: str):
    main(extension=extension, directory=None, delete=False)


@app.command()
def delete(extension: str):
    main(extension=extension, directory=None, delete=True)


@app.command('run')
def main(extension:str,
        directory: Optional[str] = typer.Argument(None, help='Dossier dans lequel chercher.'),
        delete: bool = typer.Option(False, help='Supprime les fichiers trouvés')):
    """
    Affiche les fichiers trouvés avec l'extension donnéee
    """
    if not directory:
        directory = Path.cwd()
    else:
        directory = Path(directory)

    if not directory.exists():
        typer.secho(f'Le dossier \'{directory}\' n\'existe pas', fg=typer.colors.RED)
        raise typer.Exit()

    files = directory.rglob(f"*.{extension}")
    if delete:
        typer.confirm('Voulez vous vraiment supprimer ces fichiers ? ', abort=True)
        for file in files:
            # file.unlink()
            typer.secho(f"Suppression du fichier {file} effectuée !", fg=typer.colors.RED) 
    else: 
        typer.secho(f"Fichiers trouvés avec l'extension {extension}.", bg=typer.colors.BLUE)
        for file in files:
            typer.echo(file) 


if __name__ == "__main__":
    app()
