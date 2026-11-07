#!/usr/bin/env python3

from rich.prompt import Prompt
answer = Prompt.ask("A. The red ball is [bold]above/under/on[/bold] the bed.")
loweranswer = answer.lower()
if loweranswer == "under":
    print("That answer is correct.\n")
else:
    print("That answer is wrong.\n")

answer = Prompt.ask("B. The cat is [bold]inside/outside/on[/bold] the car.")
loweranswer = answer.lower()
if loweranswer == "on":
    print("That answer is correct.\n")
else:
    print("That answer is wrong.\n")

answer = Prompt.ask("C. The man is lying [bold]under/inside/on[/bold] the tree.")
loweranswer = answer.lower()
if loweranswer == "under":
    print("That answer is correct.\n")
else:
    print("That answer is wrong.\n")

answer = Prompt.ask("D. The cow is [bold]inside/top of/outside[/bold] the house.")
loweranswer = answer.lower()
if loweranswer == "outside":
    print("That answer is correct.\n")
else:
    print("That answer is wrong.\n")
