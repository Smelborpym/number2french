import click
from src.converter import Converter
from src.utils import load_from_file, save_to_file


@click.command()
@click.option('--number', '-n', type=int, help='Convert a single number.')
@click.option('--file', '-f', type=click.Path(exists=True), 
              help='Path to a JSON file containing a list of numbers.')
@click.option('--output', '-o', type=click.Path(), 
              help='Full path including the name of the output file, applicable only if --file is used.')
@click.option('--language', '-l', type=click.Choice(['french', 'belgian'],
                                                     case_sensitive=False), 
              default='french', required=True,
              help='Output language (French or Belgian).')
def main(number, file, output, language):
    """Convert numbers to French or Belgian words."""
    if number is not None and file is not None:
        raise click.UsageError("You must provide either a number or a file, not both.")
    
    if number is None and file is None:
        raise click.UsageError("You must provide either a number or a file.")

    numbers = []
    if number is not None:
        numbers.append(number)
    elif file:
        numbers = load_from_file(file)

    converter = Converter(numbers, lang=language)
    words = converter.convert_to_words()

    if file and output:
        save_to_file(words, output, language)
    else:
        click.echo(words)

if __name__ == '__main__':
    main()
