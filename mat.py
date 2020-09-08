import os
import click

@click.command()
@click.argument('filename')
def mat(filename):
	try:
		file_path = os.path.join(os.getcwd(), filename)
		if not(os.path.exists(file_path)):
			raise FileNotFoundError(f"Unable to resolve name {file_path}")
			exit()

		command = f'matlab -batch "{os.path.splitext(filename)[0]}; exit"'
		os.system(command)
		click.echo()
	except:
		click.echo("There is something wrong with the Python script 'mat.py'")

