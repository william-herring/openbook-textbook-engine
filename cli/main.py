import typer
import sys
import os

app = typer.Typer()
__version__ = "0.1.0"

def version_callback(value: bool):
    if value:
        print(__version__)
        raise typer.Exit()

@app.callback()
def common(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    pass

@app.command()
def build(outdir: str = __name__):
    """
    Build HTML and PDF textbook
    :param outdir:
    :return:
    """
    pass

@app.command()
def create(name: str):
    pass

if __name__ == "__main__":
    app()
