#!/usr/bin/env python

from rich.prompt import IntPrompt

answer = IntPrompt.ask("A. How many bogies are there [bold]after[/bold] engine?")
if answer == 5:
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")

answer2 = IntPrompt.ask("B. How many bogies are there [bold]before[/bold] the red bogie?")
if answer2 == 2:
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")
