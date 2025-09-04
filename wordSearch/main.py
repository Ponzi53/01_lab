# Add Your Name Here

# Note: To execute this code use the command
# uv run main.py data/ haiku.md house

import os
from rich import print, box
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
import typer

app = typer.Typer()
console = Console()

def file_exists(file_path):
    """ DOCSTRING: TODO """
    return os.path.isfile(file_path)

def read_file(file_path):
    """ DOCSTRING: TODO """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
    # TODO: Print a warning message if the file cannot be read
    # Example: print(f"Error reading file: {e}")
        return None

def count_word(content, word):
    """ DOCSTRING: TODO """
    return content.count(word)

def report_result(file_path, word, count):
    """ DOCSTRING: TODO """
    if count > 0:
        # TODO: Print a message showing the word was found File (file_path) and how many times (count)
        pass
    else:
        # TODO: Print a message showing the word was not found
        pass

@app.command()
def search(
    path: str = typer.Argument(..., help="Path to the directory containing the text file"),
    filename: str = typer.Argument(..., help="Name of the text file to search"),
    word: str = typer.Argument(..., help="Word to search for in the text file")
):
    """
    Search for a word in a text file and count its occurrences.
    
    Command: 
    uv run main.py data/ haiku.md house
   """
    # TODO: Print an example command showing how to run the script
    # Example: print("💡 Example: python main.py search data/ story.md house")

    file_path = os.path.join(path, filename)
    if not file_exists(file_path):
        # TODO: Print an error message if the file is not found
        # Example: print(f"File not found: {file_path}")
        raise typer.Exit(code=1)

    content = read_file(file_path)
    if content is None:
        raise typer.Exit(code=1)

    count = count_word(content, word)
    report_result(file_path, word, count)

if __name__ == "__main__":
    """ DOCSTRING: TODO """
    app()
