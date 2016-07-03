#!/usr/bin/env python
import click
from notes import notes

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    token_normalize_func=lambda x: x.lower()
    )

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
def bluetooth():
    print(notes["bluetooth"])
    pass

@cli.command()
def i3():
    print(notes["i3"]["navigation"])

@cli.command()
def accents():
    print(notes["input"]["accents"])

@cli.command()
def trackpad():
    print(notes["trackpad"])

@cli.command()
def keyboard():
    print(notes["keyboard"])

@cli.command()
def usb():
    print(notes["usb"])

@cli.command()
def battery():
    print(notes["battery"])

@cli.command()
def wifi():
    print(notes["wifi"])

@cli.command()
def displays():
    print(notes["displays"])

@cli.command()
def timezone():
    print(notes["timezone"])

@cli.command()
def files():
    print(notes["files"])

@cli.command()
def windows():
    print(notes["windows"])

@cli.command()
def etc():
    print(notes["etc"])

@cli.command()
def power():
    print(notes["power"])

@cli.command()
def vim():
    print(notes["vim"])

@cli.command()
def bash():
    print(notes["bash"])

@cli.command()
def aws():
    print(notes["aws"])

@cli.command()
def ethernet():
    print(notes["ethernet"])

@cli.command()
def git():
    print(notes["git"])

if __name__ == "__main__":
    cli(obj={})
