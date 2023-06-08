#!/usr/bin/env python3
import signal
import argparse
import sys
import os
from pathlib import Path

from ImageGoNord import GoNord

from rich.console import Console
from rich.panel import Panel

# CHANGE narmis TO YOUR OWN USER NAME, DO NOT CHANGE THE DIRECTORY ITSELF
mypath="/home/narmis/Pictures/eff/"

def main():

    signal.signal(signal.SIGINT, signal_handler)
    console = Console()

    ef_factory = GoNord()
    ef_factory.reset_palette()
    add_ef_palette(ef_factory)

    # Checks if there's an argument
    if len(sys.argv) > 1:
        image_paths = fromCommandArgument(console)
    else:
        image_paths = fromTui(console)

    for image_path in image_paths:
        if os.path.isfile(image_path):
            process_image(image_path, console, ef_factory)
        else:
            console.print(
                f"❌ [red]We had a problem in the pipeline! \nThe image at '{image_path}' could not be found! \nSkipping... [/]"
            )
            continue

# Gets the file path from the Argument
def fromCommandArgument(console):
    command_parser = argparse.ArgumentParser(
        description="A simple cli to manufacture Everforest themed wallpapers."
    )
    command_parser.add_argument(
        "Path", metavar="path", nargs="+", type=str, help="The path(s) to the image(s)."
    )
    args = command_parser.parse_args()

    return args.Path

# Gets the file path from user input
def fromTui(console):

    console.print(
        Panel(
            "🌲 [green] Everforest Factory [/] 󰈏 ", expand=False, border_style="green"
        )
    )

    return [
        os.path.expanduser(path)
        for path in console.input(
            "󰈟 [bold yellow]Which image(s) do you want to manufacture? (image paths separated by spaces):[/] "
        ).split()
    ]

def process_image(image_path, console, ef_factory):
    image = ef_factory.open_image(image_path)
    
    console.print(f"🔨 [blue]manufacturing '{os.path.basename(image_path)}'...[/]")

    # Todo: might be a better idea to save the new Image in the same directory the command is being run from
    save_path = os.path.join(
        mypath, "ef_" + os.path.basename(image_path)
    )

    ef_factory.convert_image(image, save_path=(save_path))
    console.print(f"✅ [bold green]Done![/] [green](saved at '{save_path}')[/]")

def add_ef_palette(ef_factory):

    efPalette = ["#293136","#333c43","#3a464c","#434f55","#4d5960","#555f66","#5d6b66","#d3c6aa","#e67e80","#e69875","#dbbc7f","#a7c080","#83c092","#7fbbb3","#d699b6","#7a8478"]

    for color in efPalette:
        ef_factory.add_color_to_palette(color)

## handle CTRL + C
def signal_handler(signal, frame):
    print()
    sys.exit(0)

if __name__ == "__main__":
    main()
