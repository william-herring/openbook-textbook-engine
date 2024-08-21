import json

import typer
import os
import shutil
from pathlib import Path

from .exports import build_html
import xmltodict

app = typer.Typer()
__version__ = "0.1.4"
SAMPLE_DIR = Path(__file__).parent.resolve() / 'sample_textbook'  # Resolve the path to the sample textbook


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
def build(outdir=Path(os.getcwd()) / 'out'):
    """
    Build HTML and PDF textbook
    :param outdir:
    :return:
    """

    # Try/except in case the options file is missing
    try:
        with open(Path(os.getcwd()) / 'options.json', 'r') as file:
            options = json.load(file)
            build_html(options, Path(os.getcwd()), outdir)
            return
    except FileNotFoundError:
        # If the options file isn't found initially, check if it is XML-formatted
        try:
            with open(Path(os.getcwd()) / 'options.xml', 'r') as file:
                options = xmltodict.parse(file.read())['root']
                options['book']['page_numbers']['book/pre-content.md'] = options['book']['page_numbers']['pre-content.md']  # Need to substitute pre-content.md for book/pre-content.md since the '/' character can't be used to name XML elements
                build_html(options, Path(os.getcwd()), outdir)
                return
        except FileNotFoundError:
            raise Exception('Cannot locate options file. Ensure the command is executed from the project directory.')


@app.command()
def create(name: str):
    """
    Initialise a new book directory
    :param name:
    :return:
    """
    current_dir = os.getcwd()  # Get current working directory
    shutil.copytree(SAMPLE_DIR, Path(current_dir) / name)  # Copy-paste the sample directory and rename with the name argument


if __name__ == "__main__":
    app()
