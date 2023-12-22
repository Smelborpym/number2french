import click

from converter import Converter 
from utils import (load_from_file,
                   save_to_file)


@click.command()
@click.option('--number', '-n', type=int, help='Convert a single number.')
@click.option('--file', '-f', type=click.Path(exists=True), 
              help='Path to a JSON file containing a list of numbers.')
@click.option('--output', '-o', type=click.Path(), help='Output file path.')
@click.option('--language', '-l', type=click.Choice(['french', 'belgian'],
                                                     case_sensitive=False), 
                                                     default='french', 
                                                     help='Output language (French or Belgian).')
def main(number, file, output, language):
    """Convert numbers to French or Belgian words."""
    numbers = []

    if number is not None:
        numbers.append(number)
    elif file:
        numbers = load_from_file(file)

    converter = Converter(numbers, lang=language)
    words = converter.convert_to_words()

    if output:
        save_to_file(words, output, language)
    else:
        click.echo(words)

if __name__ == '__main__':
    main()
