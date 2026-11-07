#!/usr/bin/env python3

from rich.prompt import Prompt
answer = Prompt.ask("A. Where do you put your shoes? [bold]Inside/Outside[/bold] the room.")
loweranswer = answer.lower()
if loweranswer == "outside":
    print("That answer is correct.\n")
else:
    print("That answer is wrong.\n")

answer = Prompt.ask("B. Where do you throw the garbage? [bold]Inside/Outside[/bold] the dustbin.")
loweranswer = answer.lower()
if loweranswer == "inside":
    print("That answer is correct.\n")
else:
    print("That answer is wrong.\n")
