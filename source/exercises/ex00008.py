#!/usr/bin/env python3

from rich.prompt import Prompt
from rich.prompt import IntPrompt

answer = Prompt.ask("i. Which colour is at the [bold]top[/bold] of the tiranga? [bold]white/saffron/green[/bold]")
loweranswer = answer.lower()
if loweranswer == "saffron":
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")

answer2 = Prompt.ask("ii. Which colour is [bold]below[/bold] the white colour on the tiranga? [bold]pink/saffron/green[/bold]")
loweranswer2 = answer2.lower()
if loweranswer2 == "green":
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")

answer3 = Prompt.ask("iii. Which colour is [bold]above[/bold] the green colour on the tiranga? [bold]white/saffron/yellow[/bold]")
loweranswer3 = answer3.lower()
if loweranswer3 == "white":
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")

answer4 = Prompt.ask("iv. Where is the ashoka chakra on the tiranga? [bold]on a corner/in the middle/on a side[/bold]")
loweranswer4 = answer4.lower()
if loweranswer4 == "in the middle":
    print("The answer is right.\n")
else:
    print("The answr is wrong.\n")

answer5 = IntPrompt.ask("v. How many colours are there?")
if answer5 == 4:
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")
