#!/usr/bin/env python
import click
from notes import notes

# find the nearest comand based on the letter sequence
# so you can type dkr for doker, etc..
def normalize_nearest_command(x):
    x = x.lower()
    def find_letters(letters, command):
        ptr = [[0, command]]
        for l in letters:
            ptr.append(find_letter(l, ptr[-1][1]))
        return ptr

    def find_letter(x, command):
        if len(command) == 0:
            return 0, ''
        if command[0] == x:
            return 1, command[1:]
        return find_letter(x, command[1:])
    def count_points(arr):
        return sum([x[0] for x in arr])

    stats = sorted([[key, count_points(find_letters(x, key))] for key in notes.keys()], key=lambda x : x[1])[-1]
    return stats[0]


def execute(note, name):
    click.secho("")
    click.secho("   Hi i'm here to halp!, you have chosen:")
    click.secho("   #############   "+name + "   #############   ",fg='blue', bold=True)
    if isinstance(note, dict):  
        for key in note: 
            click.secho("   ===== "+ key + " =====",fg='red') 
            click.secho(note[key], fg='yellow')    
    else:      
        click.secho(note, fg='yellow')  

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    token_normalize_func=normalize_nearest_command
    )

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

def make_command(name):
    exec(
"""
@cli.command()
def {rep_name}():
    execute(notes["{name}"],"{name}")
""".format(rep_name = name.replace("-","_"), name=name))

[make_command(x) for x in notes.keys()]

if __name__ == "__main__":
    cli(obj={})

