#!/usr/bin/env python
import click
from notes import notes

CONTEXT_SETTINGS = dict(
    help_option_names=["-h", "--help"], token_normalize_func=lambda x: x.lower()
)


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@cli.command()
def accents():
    print(notes["accents"])


@cli.command()
def android():
    print(notes["android"])


@cli.command()
def input():
    print(notes["input"])


@cli.command()
def apache():
    print(notes["apache"])


@cli.command()
def aws():
    print(notes["aws"])


@cli.command()
def backup():
    print(notes["backup"])


@cli.command()
def bash():
    print(notes["bash"])


@cli.command()
def battery():
    print(notes["battery"])


@cli.command()
def bluetooth():
    print(notes["bluetooth"])
    pass


@cli.command()
def defaults():
    print(notes["defaults"])
    pass


@cli.command()
def etc():
    print(notes["etc"])


@cli.command()
def ethernet():
    print(notes["ethernet"])


@cli.command()
def files():
    print(notes["files"])


@cli.command()
def games():
    print(notes["games"])


@cli.command()
def git():
    print(notes["git"])


@cli.command()
def google_fi():
    print(notes["google-fi"])


@cli.command()
def gpg():
    print(notes["gpg"])


@cli.command()
def displays():
    print(notes["displays"])


@cli.command()
def docker():
    print(notes["docker"])


@cli.command()
def gandi():
    print(notes["gandi"])


@cli.command()
def printing():
    print(notes["printing"])


@cli.command()
def i3():
    for key in notes["i3"]:
        print("===== {} =====".format(key))
        print(notes["i3"][key])
    # print(notes["i3"]["navigation"])
    # print(notes["i3"]["navigation"])


@cli.command()
def images():
    print(notes["images"])


@cli.command()
def iptables():
    print(notes["iptables"])


@cli.command()
def jq():
    print(notes["jq"])


@cli.command()
def keyboard():
    print(notes["keyboard"])


@cli.command()
def markdown():
    print(notes["markdown"])


@cli.command()
def mysql():
    print(notes["mysql"])


@cli.command()
def network():
    print(notes["network"])


@cli.command()
def power():
    print(notes["power"])


@cli.command()
def readline():
    print(notes["readline"])


@cli.command()
def regex():
    print(notes["regex"])


@cli.command()
def ruby():
    print(notes["ruby"])


@cli.command()
def session():
    print(notes["session"])


@cli.command()
def sound():
    print(notes["sound"])


@cli.command()
def system():
    print(notes["system"])


@cli.command()
def sudo():
    print(notes["sudo"])


@cli.command()
def terminal():
    print(notes["terminal"])


@cli.command()
def timezone():
    print(notes["timezone"])


@cli.command()
def trackpad():
    print(notes["trackpad"])


@cli.command()
def trash():
    print(notes["trash"])


@cli.command()
def travis():
    print(notes["travis"])


@cli.command()
def usb():
    print(notes["usb"])


@cli.command()
def vim():
    print(notes["vim"])


@cli.command()
def vpn():
    print(notes["vpn"])


@cli.command()
def wifi():
    print(notes["wifi"])


@cli.command()
def windows():
    print(notes["windows"])


if __name__ == "__main__":
    cli(obj={})
