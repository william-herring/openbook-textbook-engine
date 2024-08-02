import json

import typer
import sys
import os
import shutil
from pathlib import Path

from exports import build_html, build_pdf

app = typer.Typer()
__version__ = "0.1.0"
SAMPLE_DIR = str(Path(__file__).parent.parent.resolve()) + '/sample_textbook'


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
def build(outdir: str = os.getcwd() + '/out'):
    """
    Build HTML and PDF textbook
    :param outdir:
    :return:
    """

    try:
        with open(os.getcwd() + '/options.json', 'r') as file:
            options = json.load(file)
            build_html(options, os.getcwd(), outdir)
            return
    except FileNotFoundError:
        try:
            with open(os.getcwd() + '/options.xml', 'r') as file:
                pass
        except FileNotFoundError:
            raise Exception('Cannot locate options file. Ensure the command is executed from the project directory.')


@app.command()
def create(name: str):
    """
    Initialise a new book directory
    :param name:
    :return:
    """
    current_dir = os.getcwd()
    shutil.copytree(SAMPLE_DIR, f'{current_dir}/{name}')


if __name__ == "__main__":
    app()
