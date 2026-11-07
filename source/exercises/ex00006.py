#!/usr/bin/env python3

from rich.prompt import Prompt

answer = Prompt.ask("i. A boy is sitting [bold]on/under[/bold] the tree.")
loweranswer = answer.lower()
if loweranswer == "under":
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")

answer2 = Prompt.ask("ii. Birds are [bold]on/under[/bold] the tree.")
loweranswer2 = answer2.lower()
if loweranswer2 == "on":
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")
