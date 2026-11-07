# Joyful Mathematics Class 1

[https://ncert.nic.in/textbook.php](https://ncert.nic.in/textbook.php)

## Page 1 and 2

Exercise 00001 - Python Code:
```python

import subprocess

text = (
"""
Where are you my furry cat?
Are you sitting on the window shed?
Are you sleeping under my bed?
Where are you my furry cat?
Looking, looking, looking
Looking for my furry cat!
Are you inside the backpack?
Are you outside the red rack?
Where are you my furry cat?

Come, come, come
Come to me, my furry cat!
Saw you scratching the bottom of my jar.
Saw you playing at the top of my car.
Come to me, my furry cat!

Come, come, come
Come to me my furry cat!
Saw you hopping above the hat.
Saw you hiding below the mat
Here comes my furry cat!
"""
)

print(text)

print("Read aloud the poem. Ask children to recite and enact it. Children can look at the pictures and tell what all they see and discuss the things which are above, below, on, under, and so on with the class. Encourage them to talk about the animals that they see around them, like cats, dogs, cows, etc.\n")


# 1. Generate WAV file directly using espeak
subprocess.run(["espeak", "-w", "ex00001.wav", text])

# 2. (Optional) Convert WAV to MP3 using ffmpeg if you specifically need an MP3
subprocess.run(["ffmpeg", "-y", "-i", "ex00001.wav", "ex00001.ogg"])

# 3. Remove wav file
subprocess.run(["rm", "-v", "ex00001.wav"]) 

print("Audio generated successfully without crashes!")

```

## Page 3
Exercise 00002 - Python Code:
```python
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
```

Exercise 00003 - Python Code:
```python
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
```

## Page 4
Exercise 00004 - Picture:\
A. Tick the things which are inside.
![](../exercises/ex00004.png)

## Page 5
Exercise 00005 - Picture:\
B. Tick the things which are outside.
![](../exercises/ex00005.png)

Exercise 00006 - Python Code:\
C. Look at the picture and tick the correct words.
```python
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
```

Exercise 00007 - Picture:\
D. Draw a smile below the nose and eyebrows above the eyes.
![Draw a smile and eyebrows](../exercises/ex00007.png)

## Page 6
Exercise 00008 - Python Code:\
E. Look at our National Flag which is also known as tiranga.

Tick the correct option.
```python
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
    print("The answer is wrong.\n")

answer5 = IntPrompt.ask("v. How many colours are there?")
if answer5 == 4:
    print("The answer is right.\n")
else:
    print("The answer is wrong.\n")
```

## Page 7
Exercise 00009 - Python Code:
```python
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
```

Exercise 00010 - Picture:\
C. Fill the orange colour in the bogies after the red bogie.
![Orange bogies](../exercises/ex00010.png)

Exercise 00011 - Picture:\
D. Fill the blue colour in the bogies before the red bogie.
![Blue bogies](../exercises/ex00011.png)

## Page 9
Exercise 00012 - Text:\
Suwali has placed all the buttons in three groups.
Why did Suwali make such groups?
```text
Answer: To sort them by colour.
```

Exercise 00013 - Picture:\
Help Suwali to sort these buttons in other ways by drawing them.
![Sorted buttons by shape](../exercises/ex00013.png)

## Page 11
Exercise 00014 - Markdown with Inline SVG Code:
```svg
A. Draw round objects in <svg width="24" height="24" style="vertical-align: middle;"><circle cx="12" cy="12" r="11" stroke="white" stroke-width="1" /></svg> and long objects in <svg width="36" height="24" style="vertical-align: middle;"><rect x="1" y="1" width="34" height="22" rx="2" stroke="white" stroke-width="1" /></svg> .
```

A. Draw round objects in <svg width="24" height="24" style="vertical-align: middle;"><circle cx="12" cy="12" r="11" stroke="white" stroke-width="1" /></svg> and long objects in <svg width="36" height="24" style="vertical-align: middle;"><rect x="1" y="1" width="34" height="22" rx="2" stroke="white" stroke-width="1" /></svg> .

Exercise 00015 - Picture:
![Round and long objects](../exercises/ex00015.png)

B. Match the objects which are similar in shape.
C. Tick the shape which is similar to ball.
D. Tick the shape which is similar to cap.
E. Tick the shape which is similar to glass.
F. Tick the shape which is similar to matchbox.

Let us Do
Make a house, toy, tower, robot, bus or anything you like
using different objects in your surroundings. You can also
use notebooks, books, pencil box, water bottle, waste or old
boxes, birthday caps, funnels, etc.
Divide the children in four groups. Give one shape to each group and
ask children to bring two different used or waste objects
similar to that shape. Display all the collected things in the
classroom and let children share their things and the reason
why they choose those particular things.

13

Reprint 2026-27
Chapter 2.indd 13

25-05-2023 11:54:07

Wise Grandmother
Once there was a little
lamb who was going to
meet her grandmother.
The wolf saw the lamb
and wanted to catch her.

Please don’t eat me now.
Let me first go to my
grandmother’s place and
grow big.

Okay, you
may go.

The lamb told everything about the wolf to her grandmother.
The grandmother got an idea and put the lamb into a
dholak and rolled it back to her house.

Read aloud the story and ask children to enact it.

Reprint 2026-27
Chapter 2.indd 14

25-05-2023 11:54:09

The dholak rolled very fast and the wolf started running
behind it.

The wolf could not catch the lamb and she
reached home safely.

Let children reason out why the dholak rolled. Arrange a
discussion about its shape and the sloppy/inclined surface
from the jungle to the lamb’s house.

Reprint 2026-27
Chapter 2.indd 15

25-05-2023 11:54:10

Let us Slide
Children are playing carrom as shown below. You can also
play and see how a striker slides to reach the corner.
My striker (gotti)
rolled instead
of sliding.

A.	Write ‘R’ for rolling objects and ‘S’ for sliding objects in
the
given in the below picture.

B.	Collect different objects from your surroundings and see if
they roll or slide.
C.	Do you see things which can do both, roll and slide? If
yes, discuss in the class.

16

Ask children to tell about different objects in their house or
school which roll as well as slide. Also discuss which features
of the objects help them to roll or slide on a plain surface.

Reprint 2026-27
Chapter 2.indd 16

13-12-2024 15:00:35

Think and Do
Find whether the following objects roll, slide or do both.
Put ü or X
Object

Rolls

Slides

Rolls as well
as slides

Project Work
A. Collect cardboard boxes like shoe boxes, empty food boxes, fruit boxes,
etc. Make a slit on front of the box and draw eyes, mouth and nose,
make a puppet with help of your parent or teacher and play with it.
Make puppets from your favourite stories and do a puppet show in your
classroom.
B. Make towers with different objects. Find which shape of objects make
taller and stable towers.
C. Create different shapes and objects by using clay.

17

Reprint 2026-27
Chapter 2.indd 17

25-05-2023 11:54:12

Mango Treat

3
Let us Read

The birds are watching a squirrel eating a mango.

One bird joins.

Now 2 of them are eating the mango.
One more
bird joins.

p!

u
dh

Now 3 of them are eating the mango.
One more bird joins.

One more
bird joins.
Now 4 of them
are eating the mango.

Now 5 of them are eating the mango.
Reprint 2026-27
Chapter 3.indd 18

09-06-2023 14:40:46

One more bird joins.

One more bird joins.

Now 6 of them are eating the mango.

Now 7 of them are eating the mango.
Now 8 of them are
eating the mango.

One more bird joins.

One more bird joins.

Now 9 birds and animals ate the mango.

Let us Talk
A. Identify the birds in the picture.
B. How many animals or birds were eating the mango in the
beginning?
C. How many more animals or birds joined every time?
D. What is 1 more than 1, 1 more than 2… up to 9?
E. How many animals and birds ate the mango at the end?
Talk about counting numbers as the animals join. Enact the story where
all children play the role of different animals or birds and make
their respective sounds. Talk about different birds or animals,
their sounds and their habitats.

19

Reprint 2026-27
Chapter 3.indd 19

09-06-2023 14:40:48

Match the number of birds with the number of fingers
(one has been done for you).

20

Reprint 2026-27
Chapter 3.indd 20

1/17/2025 12:29:51 PM

Match the fingers with correct number of dots.

Let us Play — Mime with Fingers
Show 3 fingers to your friend.
Your friend has to show 3
fingers but in a different
way. Similarly, you can play
for other numbers.
   What are the different
ways of showing 4 fingers
using one hand?

21

Reprint 2026-27
Chapter 3.indd 21

13-12-2024 15:02:26

Let us Play Outside

22

Children can move in a circle by holding hands and
singing songs. A child claps and says four. All children
can make groups of four by holding hands. The left out
children can count the number of children in each group.
Similarly, children continue this game by saying different
numbers up to 9.

Reprint 2026-27
Chapter 3.indd 22

09-06-2023 14:40:51

My Drawing Day
A drawing event held for children on ‘Ekta Diwas’
(31st October). Assign different objects to each child by
drawing a line as shown in the picture.

Help them to know if they have enough material.
Tick ü more or less or equal.
Objects

More than the
number of
children

Less than
the number
of children

Same as the
number of
children

Discuss with children how did they find out which items are
more or less or equal. Also discuss the habit of sharing objects
among the group when children are more than the items or
objects. Also discuss the importance of Ekta Diwas.

23

Reprint 2026-27
Chapter 3.indd 23

24-02-2026 12:16:09

Let us Do
A. Tick ü the one which is more in number.

B. Tick ü the one which is less in number.

C. Tick ü the one which is less in number.

Let us Play — Finger Game
A. Play this finger game with your friend. Show some
fingers for example, four fingers. Your friend has to
show less fingers than four.
B. Ask your friend to show more than that number, more
number in some other way, and less number in some
other way.
24

Reprint 2026-27
Chapter 3.indd 24

09-06-2023 14:40:53

Numbers 1, 2, 3... Go!

Look at the pictures and follow the instructions.
A. Draw a
around the objects which are one in number
in the above picture and write down 1 below.

One
around the objects which are two in number
B. Draw a
in the above picture and write down 2 below.

Two
C. Draw a
around the objects which are three in number
in the above picture and write down 3 below.

Three
25

Reprint 2026-27
Chapter 3.indd 25

09-06-2023 14:40:54

D. Draw a
around the objects which are four in number
in the above picture and write down 4 below.

Four
E. Draw a
around the objects which are five in number
in the above picture and write down 5 below.

Five
F. Draw a
around the objects which are six in number
in the above picture and write down 6 below.

Six
26

Reprint 2026-27
Chapter 3.indd 26

09-06-2023 14:40:55

G. Draw a around the objects which are seven in number
in the above picture and write down 7 below.

Seven
around the objects which are eight in number
H. Draw a
in the above picture and write down 8 below.

Eight
I. Draw a
around the objects which are nine in number
in the above picture and write down 9 below.

Nine
Encourage counting objects and writing numerals on sand. Ask a child
to scribble numeral on the back of another child. Let the child
guess which number is written. Tell the children that the group
of seven stars in the above picture which can be seen in the sky
every night is known as Saptarshi or Big Dipper.

27

Reprint 2026-27
Chapter 3.indd 27

13-02-2024 11:43:54

Count and Match

3

7
5

Count and Colour
A. Colour 8 stars.

B. Colour 5 flowers.

C. Colour 6 balls.

28

Reprint 2026-27
Chapter 3.indd 28

09-06-2023 14:40:58

Join the Numbers in a Order
A. Draw a path from numbers 1 to 9 in the correct order.
The lines should not cross each other.
i.

ii.

1

3

4

9

2

8

7

iii.

5

6

7

5

4

3

8

6

1

2

9

B. A naughty monkey shuffled the number cards. Write
them in a correct order from the smallest to the largest.

29

Reprint 2026-27
Chapter 3.indd 29

09-06-2023 14:40:59

C. The cat has walked all over the floor. Write down the
missing numbers.

, 5, 6,
, 2,

,8
, 4, 5

5,

,

,

3,

,

, 6,

,9

Colour the Biggest Number

30

Reprint 2026-27
Chapter 3.indd 30

19-12-2024 12:08:02

A. How many yellow boxes are there? Count and write
the number.

B. How many jamuns are there in the given picture?

C. Write the number of sheep seen in the picture.

31

Reprint 2026-27
Chapter 3.indd 31

09-06-2023 14:41:02

D. Draw any 4 fruits.

E. Which two groups together have 8 fruits? Encircle them.

F. Which two groups together have 7 umbrellas?
Encircle them.

G. Which are less in number? Cups or Spoons?
Encircle them.

Project Work

32

Ask children to make their own number cards 1 to 9. They can use
different colour papers. They can stick or draw equal number of
objects on the number card.

Reprint 2026-27
Chapter 3.indd 32

09-06-2023 14:41:04

4

Making 10

Dotty Bug and her Designs
Have you seen a ladybug?
She has dots on her body.
Have you ever noticed the
number of dots?
A. Write the number of dots on each bug.

B.	Make some dot designs with
objects like tamarind seeds,
pebbles, buttons, bindis,
etc., and identify the number
of dots in each arrangement.

Reprint 2026-27
Chapter 4.indd 33

19-06-2023 14:04:46

C. 	Identify and write the numbers formed by the arrangement
of the red bindis

Let us Play
D. 	Play with your friend. Roll the dice and colour a box with
the same number of dots as on the dice. Take turns with
your friend and roll again.
Choose the colour and
fill it in the below boxes.
My colour
Friend’s colour

The child with more number of coloured boxes will win.

34

Use the dot and colour flash cards to help children gain
instant recognition of numbers without counting. This is
called subitization. Make more cards with dot patterns of
numbers 1 to 9 in different designs and sizes as required.

Reprint 2026-27
Chapter 4.indd 34

19-06-2023 14:04:47

Vanishing Buttons
Gola monkey wears his favourite shirt with four buttons.
He went to the garden and ate too many bananas as he was
fond of them. What do you think happened then?
One of the buttons popped out and rolled away. But he
cannot dream of giving up bananas and he keeps on losing
all the buttons one by one.

Four

Three

Buttons

Buttons

Two

Buttons

One

Zero

Button

0 Buttons

Discuss the number of buttons left on the shirt at the end. Ask children
to name objects, things around them whose number is zero.
Let children understand that zero is also a number like one,
two and other numbers. Discuss with children about the
benefits of balanced diet and ill-effects of overeating.

35

Reprint 2026-27
Chapter 4.indd 35

19-06-2023 14:04:48

Write the number of birds sitting on the branch of the tree.

Write ‘0’

Think and Tell
A. How many suns do you see in the night?
B. How many moons do you see at noon?
Use concrete objects to demonstrate the idea of zero by reducing one object
each time. Discuss the situations where something is absent
and its number is called as ‘zero’ like there are 0 buses in the
classroom. Also encourage children to count backwards from
5 to 0 initially and later from 9 to 0.

36

Reprint 2026-27
Chapter 4.indd 36

19-06-2023 14:04:49

Tenth Birthday
It is Aastha’s tenth birthday. Her father prepared halwa for
her. She is celebrating the birthday with her friends.

I am 9 years old and after 1 more year,
I will be 10 years old.
So, 9 and 1 more makes 10.
She has lighted

diyas on her birthday.

Count and write the number of objects.

Beads

Laddoos

Crayons

Bananas

Leaves

37

Reprint 2026-27
Chapter 4.indd 37

13-12-2024 15:13:42

Let us Do
A. Count and draw beads to make a string of 10 beads.
i.

ii.

iii.

iv.

B. Draw buttons to make a ten frame of buttons.
i.

ii.

iii.

iv.

38

Reprint 2026-27
Chapter 4.indd 38

19-06-2023 14:04:51

The Handy Five and Ten
Follow the pattern and write the number pairs separated by
the stick.

1 and 4
__
__

__ and __

__ and __

__ and __

__ and __

Let us Play
Show 3 fingers. Your friend has to
show some fingers to make it 5.

39

Reprint 2026-27
Chapter 4.indd 39

19-06-2023 14:04:53

Number Pairs of 10
Let us play the finger game with our both hands. A child will
show some fingers. The other child has to show the other
fingers that are folded.
Follow the pattern and write the number pairs in the
given table.

			
1

9

=
=

			

=

			

=

			

=

			

=

			

=

			

=

			

=

			

=

10

40

Reprint 2026-27
Chapter 4.indd 40

19-06-2023 14:04:54

Let us Play a Card Game
Number Cards (Sets of 0 to 10)
Make 5 sets of (1 to 10) cards. Keep all 50 cards face down.
One child picks up a card and keeps it face up. The other
child picks up another card and keeps it face up. If the
pair of cards make 10 then the second student takes both
the cards. And the turn goes back to the first student who
will pick up another card. In the end the child with more
number of cards will be the winner.

Counting up to 20
Simran lives in Nagpur. She is helping her father in packing
oranges. A box can hold 10 oranges. Let us count the number
of oranges.

10

10 Ten

10 and 1 is

11 Eleven

10 and 2 is

12 Twelve

Have a discussion to help children to understand and remember the
number partitions of 5 and 10. For example, if the teacher says 2, the
child should respond 3, when doing partitions of 5. Similarly,
if the teacher says 4, the child should respond 6, when doing
partitions of 10. This is the time when children start counting
beyond 10. Draw attention towards the fact that there is
always a number one more than the previous number.

41

Reprint 2026-27
Chapter 4.indd 41

27-02-2025 16:03:57

10 and 3 is 13 Thirteen
10 and 4 is 14 Fourteen
10 and 5 is

15 Fifteen

10 and 6 is 16 Sixteen
10 and 7 is 17Seventeen
10 and 8 is 18 Eighteen
10 and 9 is 19 Nineteen
10 and 10 is 20 Twenty
42

Reprint 2026-27
Chapter 4.indd 42

13-12-2024 15:13:44

Write the numbers 11–20.

11 12 13 14

15

16

17

18

14

19 20
19

17
11

20
13

18
15

12

19

Help the children to count concrete objects up to 20 using groups of ten
and units. Give them a handful of seeds or buttons not more
than 20. Ask them to guess the number first, then group and
count. How close was the guess? Let children reason out the
basis for their guesses.

43

Reprint 2026-27
Chapter 4.indd 43

19-06-2023 14:04:59

Count and Write
A. Count and write the answers.

B. Colour the tens frames to show the number.

14
19
16
C. Write down the numbers in sequence.

1
8
9

3
6
15

12
20

44

Reprint 2026-27
Chapter 4.indd 44

13-12-2024 15:13:44

D.	Encircle a group of ten in the pictures and match with
the number.

17

16

20
10
E. A group of friends while playing built some towers.

i. Tick ü the tallest tower.
ii.	
Which tower used the most number of blocks?
Write the number of blocks used in it.
iii.	
Which tower used the least number of blocks?
Write the number of blocks used in it.

45

Reprint 2026-27
Chapter 4.indd 45

19-06-2023 14:05:01

Let us Do
A. Circle the smallest number.
i. 8,

12,

6

ii. 14, 11, 19

B. Circle the biggest number.
i. 16, 19, 11

ii. 11, 17, 9

C. Find the numbers hidden under the paw.
i.

, 15, 16,

ii.

, 12,

iii. 15,

,

iv. 13,

, 15,

, 18
, 14, 15
,

, 19
,

D. Write the numbers from the biggest to the smallest.
11, 3, 16, 20, 13, 9

Let children find out their ways to decide which number is bigger.
Ask them why have they decided so. The children must
understand that 15 is bigger than 11 because it is 4 more
than 11 and similarly for other numbers up to 20.

46

Reprint 2026-27
Chapter 4.indd 46

19-06-2023 14:05:01

E. Let us count and write.

i. Number of blocks

ii. Number of white dots

F. Join the numbers from 1 to 20.
3

2

4

1

5

20

6

7

8

19
18

9
10
11

17
16

12
15 14

13

Is it an animal or
a bird?

Project Work
A. Find out the things from your surroundings that are in the group of 10.
For example, bindi cards having bindis in the groups of 10.
B. Ask children to make their own number cards 10 to 20. They can use old
cardboards, waste materials, etc.
Encourage children to recognise the group of 10, while counting
the objects beyond 10.

47

Reprint 2026-27
Chapter 4.indd 47

19-06-2023 14:05:02

5

How Many?

Going out with Grandfather!

Let children look at the picture and share what activities they do in the
park. They may also discuss the number of people joining in the park,
for example, how many children are playing in the first picture
and how many joined them. Let children discuss or share the
importance of spending time with grandparents and discuss ways
of showing respect to them.

Reprint 2026-27

Chapter 5.indd 48

07-06-2023 10:49:33

Tell How many Altogether? Fill in the Blanks.

4 children and 2 children altogether make ___ children.
4+2=

3 tops and 1 top altogether make _____ tops.
3+1=

3 ants and 2 ants altogether make _____ ants.
3+2=

4 pencils and 3 pencils altogether make ____ pencils.
4+3=
Provide children enough opportunity to do addition with lots of concrete
objects. Encourage children to find the total number of objects by
combining two groups (aggregation) and also by adding more objects
to an existing group of objects (augmentation). Practice work should
be done with the children on both types of addition problems.

49
Reprint 2026-27

Chapter 5.indd 49

1/17/2025 12:27:05 PM

Add and Draw

6 balls and 2 balls altogether make ____ balls.
6+2=

7+1=

Let us Count
A. How many brothers and sisters do your parents have
altogether?
B. How many family members do you and your friend have
altogether?
C. How many fingers do you have in both your hands and
feet?
D. How many numbers can you count on your fingers?
Encourage children to understand and say the addition sentences aloud.
For example, 4 children and 2 children altogether make 6 children and
connect the word ‘make’ with the symbol of addition (+) and ‘altogether’
with the symbol of equal to (=). Children should be provided
opportunities to work with concrete material in developing the
vocabulary like ‘total’, ‘sum’, ‘altogether’, etc., before progressing
towards symbolic representation or addition of numbers.

50
Reprint 2026-27

Chapter 5.indd 50

07-06-2023 10:49:36

Count and write the total number of fingers.

4+3=

3+2=

5+3=

4+0=

4+4=

Let us Play— Addition with Dice!
Take turns and roll two dice together and
find the total number of dots on both the
dice. Now ask your friend to roll the dice
and find the total number of dots. Find out
who scores more.
51
Reprint 2026-27

Chapter 5.indd 51

07-06-2023 10:49:37

Let us Do
Kishore and Nitya also played the same game and here are
their dots on the dice. Find out how many times Kishore
won and how many times Nitya won by putting the () on
their score board.
Kishore

A.
B.

Nitya



C.
D.
E.

Kishore

Nitya

A.

and

=

B.

and

C.

6

and

=

=

and

=

and

=

and

=

D.

and

=

and

=

E.

and

=

and

=

5

52
Reprint 2026-27

Chapter 5.indd 52

07-06-2023 10:49:37

Beads and String
Colour the beads in the string as per the numbers given below
and find the total number of coloured beads.

A. 3 + 4 =

B. 4 + 2 =

C. 5 + 4 =

D. 2 + 7 =

E. 7 + 3 =

Encourage children to play with beads’ strings. Focus on the
process of addition and discuss the strategies they are using.

53
Reprint 2026-27

Chapter 5.indd 53

07-06-2023 10:49:38

Hop and Find the Sum
Hop and colour the strip and write the sum in the
given space.
4+2=

3+2=

5+3=

6+3=

54
Reprint 2026-27

Chapter 5.indd 54

03-03-2026 9.53.11 AM

Add in Your Own Way
Abdul and Rihana are adding numbers in two different ways.
Help them to find the sum.

2
+3

2+3=

5
+1

5+1=

3
+3

3+3=

9
+1

9+1=
55
Reprint 2026-27

Chapter 5.indd 55

07-06-2023 10:49:39

Let us Do
A. Fill up the number pairs.

7+1
5+3

8

1+7
5

2+6
3+5

1+8

6+1

5+2

7

1+6

3+6

9
2+7

B. Add and match the following.

Wheel in Konark Sun Chariot

1+4

5

4+2

6+3

6

3+4

5+2

7

3+2

0+6

9

5+4

Project Work

56

Take ten cards 0 to 9.
Arrange the cards in such a manner
that their sum must be 9.
There are many ways to do it. In how
many ways can you do it?

+
+

=9
  +

+

=9
=9

Reprint 2026-27

Chapter 5.indd 56

07-06-2023 10:49:39

Addition Story
A.	Raghav

has 4 shells

and Sarita

has 5 shells

. How many shells they have altogether?
B.	Ranjeet has 3 marbles

and Meenakshi has 6 marbles

. How many marbles they have in total?
C.	
There are 3 coconuts
coconuts

in one bag. There are 4

in another bag. How many coconuts

are there in all?
Let us see what we have in our bags.
Do it with your friend and write down the answers below.
A. I have ____ books in my bag
and my friend has
____ books. We both have _________ books in all.
B. I have ____ pencils and my friend has ____ pencils. We
have _______ pencils altogether.
C. I have ____ notebooks and my friend has ____ notebooks.
We have _______ notebooks in total.

Think and Do

3

Write the numbers 1, 2 and 3 in the given
table in a way as shown by the dotted lines
so that each way adds up to 6.

2
1

This activity can be conducted in pairs. Encourage children to create
their own problems and questions. Also discuss in class about
the world’s oldest Sun Temple, Konark, Odisha refer to the
image (Page 56) of wheel in Konark Sun Chariot.

57
Reprint 2026-27

Chapter 5.indd 57

07-06-2023 10:49:40

Five Little Children
Five little children
Raise your hand
Here comes your stand
One steps out, with a roar
Now, we are four!

Four little children
Raise your hand
Here comes your stand
One steps out, near a tree
Now, we are three!

Three little children
Raise your hand
Here comes your stand
One steps out,
with shining shoe
Now, we are two!
58
Reprint 2026-27

Chapter 5.indd 58

07-06-2023 10:49:41

Two little children
Raise your hand
Here comes your stand
One steps out,
looking at the sun
Now, remains one!

One little child
Raise your hand
Here comes your stand
Last steps out,
having much fun
Now, there are none!

Let us Talk
A. How many children are there in the bus at the beginning?
B. How many children get down from the bus on the first
stand?
C. How many children are left in the bus after the first
stop?
D. How many children are left after the second stand?
Answer the same for third, fourth and fifth stand.
E. How many children are left in the bus at the end?

Project Work
Find out the number of people at your home. How many are going to
school, for work and how many stay at home.

59

Reprint 2026-27

Chapter 5.indd 59

1/17/2025 12:13:32 PM

Let us Do
How Many Left?
A. Fill in the blanks.
i.

6 frogs

2 jumped away

		

6 − 2 = ______

______ left

ii.

7 balloons

______ flew away

5 left

7 − 2 = ______
iii.

9 bananas

6 took away

____ left

9 − 6 = ______
60
Reprint 2026-27

Chapter 5.indd 60

06-01-2025 10:13:35

B. Draw the objects that are being left and fill in the blanks.
i.

____ pots
		

____ pot broke

____ left

3 − ______ = ______

ii.

7 ladoos
		

4 eaten

____ left

7 − 4 = ______

iii.

7 balls
		

______ took away

______ left

7 − ______ = ______

C. Answer the following questions.
i.	Manisha

has 9 bananas

. She ate 3

bananas. How many bananas are left?
ii.	There are 8 butterflies

on the flowers. 5 butterflies

flew away. How many butterflies are left?
61
Reprint 2026-27

Chapter 5.indd 61

16-12-2024 11:32:45

Let us Do
Make your own
ten dots card
and hide a
few dots from
your friends.
Ask them how
many dots are
hidden.

How many dots are hidden and how many dots are visible?
Total Dots 10

Hidden Dots

Visible Dots

0

10

Project Work

62

Ask children to make a frame with 8 dots. Now hide few dots using their
hands or handkerchief and see how many dots are hidden and how many
are visible. Is there any pattern in the numbers? Extend this activity for
other numbers. Is it possible to do this without hiding the dots?
Reprint 2026-27

Chapter 5.indd 62

19-06-2023 11:25:26

Hop backwards on the number strip.

A. Jump 3 steps back from 9.

9−3=6
B. Jump 4 steps back from 7.

7−4=
Do the subtraction in your own way.
A. 8 − 2 =

D. 6 − 3 =

B. 7 − 3 =

E. 5 − 1 =

C. 9 − 5 =

F. 4 − 2 =

63

Reprint 2026-27

Chapter 5.indd 63

24-02-2026 12:42:36

6

Vegetable Farm

Rumi and Shami helped each other taking out vegetables
from the field. Each of them took a basket and plucked the
vegetables. Let’s see how many vegetables they both took out.
Reprint 2026-27

Chapter 6.indd 64

07-06-2023 10:56:56

Rumi’s Basket

Shami’s Basket

Both have

A. 7 tomatoes and 5 tomatoes altogether make 12 tomatoes.
7 + 5 = ______

B. 9 carrots in one basket and 4 carrots in another basket.
9 + 4 = ______

C. 8 radishes in one basket and 8 radishes in another basket.
8 + 8 = _____

Project Work
Plant any vegetable sapling at your home, school or nearby place. Share
your experiences with your family and take care of the sapling. You may
draw or take pictures of the growing sapling.

65

Reprint 2026-27

Chapter 6.indd 65

07-06-2023 10:56:57

Beads and Mala

Let us Play

How can you
add 12 and 4 on
ginladi?

I count 12 beads
first and now I am
counting 4 more.
13, 14, 15, 16

66
Reprint 2026-27

Chapter 6.indd 66

07-06-2023 10:56:58

Show how you can add these numbers on ginladi.
13 + 4 =

13

17

14 + 5 =
6+8=
5+7=
Hop and find the sum.

8 + 5 = 13

5

+

3

=8

13 + 3 =

+

= 13

2 + 16 =

+

= 10

4 + 12 =

+

= 18

Add in your own way.
A. Sapna has 12 coloured pencils
coloured pencils

and Gauri has 6

. How many

12, 13...18

pencils do they have in all?
Sapna counted 12 and 6 more and
got 18.
12 + 6 = 18
Discuss the process of addition. How do children count 12
and then further add 4? Discuss the strategies they are
using.

67

Reprint 2026-27

Chapter 6.indd 67

07-06-2023 10:56:59

Gauri did it as
12 + 6
10 + 2 + 6

10 + 8 = 18

10 + 8 = 18
Can you do it differently?
Try and discuss with your teacher.
B. Aman

has

8

laddoos

and

Charanjeet brought 6 laddoos.
How many ladoos are there in
all?
C. Sheena has 12 bangles, she got
6 more from her sister. How many
bangles does she have now?

Let us Do
What would you like to bring for the picnic? Discuss with
your friend. Draw the things you would like to take to the
picnic and write the total number of eatables in the space
provided.

68
Reprint 2026-27

Chapter 6.indd 68

24-02-2026 14:26:58

Subtraction
Subtract with some more numbers.

15 − 9 = 6

A.

B.
16 − 4 =

C.

12 − 5 =

D.
14 − 7 =

E.

G.

15 − 5 =

17 − 9 =

16 − 6 =

F.

H.

15 − 0 =

13 − 3 =

69
Reprint 2026-27

Chapter 6.indd 69

07-06-2023 10:57:03

Hop and Jump
Anjali and Renu are playing by hopping and jumping.
Anjali, I am
jumping 2
steps ahead
from 6.

I am jumping
7 steps back
from 15.

Oh! We both
have reached
the same place.

Let us Do
Make a number strip in the playground or at home and find
the different ways by which you can reach to the same place.
Add, Subtract and Match
8+7

12

15 − 3

9+9

15

18 − 1

10 + 2

14

17 − 2

16 + 1

17

18 − 0

11 + 3

18

16 − 2

Make similar questions and let children use their own
strategies to solve these questions.

70
Reprint 2026-27

Chapter 6.indd 70

03-03-2026 10.42.39 AM

Problem Stories
Write your answers in the boxes.
A. A potter had 9 diyas. He sold 5 diyas. Then he made
7 more diyas. How many diyas does he have
now?

B. 6 children sit in the bus at the first stop. At the second
stop, 8 more children board the bus. 7 children get down
at the third bus stop. How many children are there in the
bus at the third stop?

C. There are 18 seats in a bus. If 9 children are already sitting
in it, how many more children can sit inside the bus?
D. Kuljeet got 14 toffees in her box. She shared few toffees
with her friends. She was left with 6 toffees. How many
toffees did she share with her friends?
E. Raman got 12 bananas and ate a few of them. He is left
with 5 bananas. How many bananas did he eat?

71

Reprint 2026-27

Chapter 6.indd 71

07-06-2023 10:57:04

7

Lina’s Family

Lina’s Family Get Together
Lina stays with her family in a village. She stays with her
grandparents, parents and a brother Shanbor. Her uncles,
aunts and cousins live near to their house.

Lina is standing on the stool. She likes to be tall. Find
out and circle the tallest member in the family.

Reprint 2026-27
Chapter 7.indd 72

07-06-2023 10:58:15

Lina’s family invited all the family members for a get
together.

Let us Talk
A. How many members are there in Lina’s family?
B. Tick the tallest member in the family.
C. Draw a cap on the shortest family member.
D. Who is taller than Lina’s mother but shorter than Lina’s
father?
E. Who is the tallest and shortest member of your family?
F. Who is the tallest child in your class?
G. How many children in your classroom are taller than you?
73

Reprint 2026-27
Chapter 7.indd 73

07-06-2023 10:58:16

Lina lives in a hut-shaped house in a hilly area. Can you
locate her house in the picture? Circle the correct options:
A. Her house is nearest to/farthest from the shop and
nearest to/farthest from the school.
B. The school is nearest to/farthest from the shop and
nearest to/farthest from red roof house.
C. The child is nearest to/farthest from the school bus
and nearest to/farthest from the school.

Amazing Facts
This is a statue of Sardar
Vallabhbhai Patel also called
the Statue of Unity. It is the
tallest statue in the world and
is located in Gujarat, India.
74

Reprint 2026-27
Chapter 7.indd 74

24-02-2026 15:02:51

Let us Do
A. Tick ü the one which is longest.

i.							ii.

B. Tick ü the one which is shortest.

i.							ii.

C. Tick ü the one which is thickest.

i.							ii.

D. Tick ü the one which is thinnest.

i.							ii.

75

Reprint 2026-27
Chapter 7.indd 75

07-06-2023 10:58:19

Think and Do
Draw a stick or bamboo
longer than this­—

Draw a rope shorter
than this—

Dadi is checking the length of Chitra’s sweater by a
handspan.
We can also
use fingers for
smaller objects.

It is
ready.

Chitra also wants to find out the length of the stick, table,
pencil and notebook using her handspan.

76

Reprint 2026-27
Chapter 7.indd 76

07-06-2023 10:58:20

Think and Answer
A. My table is _________ handspans long.
B. My bag is _________ handspans long.
C. My classroom blackboard is _________ handspans long.
D. My Maths book is _________ handspans long.
E. My arm is _________ handspans long.
F. My friend’s arm is _________ handspans long.
Can Chitra use a handspan to find the length of all these
things? Find out and circle which things around you are
shorter than a handspan? Can we use fingers also to find
the length of these things?

77

Reprint 2026-27
Chapter 7.indd 77

07-06-2023 10:58:23

Let us Do
What would you choose, handspan or fingers to find the
length of these objects and why? Circle your options in
the table. Try to guess before finding the length of these
objects.
Name of the things

Circle, what will
you use?

My
guess

My
findings

Bottle

handspan or fingers
Spoon

handspan or fingers
Pencil

handspan or fingers
My friend’s nose

handspan or fingers
Leg

handspan or fingers
Key

78

handspan or fingers

Reprint 2026-27
Chapter 7.indd 78

07-06-2023 10:58:23

Measure by footspan

My guess of My findings
footspan
of footspan

Distance between my
seat and the door of
the classroom
One side of classroom
Distance between the
bed and washroom
Distance between two
walls of your room

Let us Do
A. Tick ü the heavier object.
i.							ii.

			
B. Tick ü the lighter object.
i.							ii.

		 		

79

Reprint 2026-27
Chapter 7.indd 79

06-Mar-25 11:46:28 AM

C. Colour the heavier object.
i.						ii.

iii.						iv.

D. Colour the lighter object.
i.						ii.

iii.						iv.

Let us Talk

80

A. Who is heavier between you and your friend? How will
you find out? Discuss in the class.
B. Find out your weight. Can you tell how and where
your weight is usually checked?

Reprint 2026-27
Chapter 7.indd 80

07-06-2023 10:58:25

Let us Do
A. Fill the bucket with water.
i. _______ jugs of water will fill the bucket.

ii. _______ glasses of water will fill the bucket.
iii. _______ bowls of water will fill the bucket.
B. Answer the following questions.
i.	How many cups of water will fill your water bottle?
_______
ii.	Now fill your friend’s water bottle with the same cup.
How many cups of water will fill your friend’s bottle?
_______
iii. Which bottle holds more water? _______
iv.	Try it with another bottle. Which bottle holds less
water?
C. Circle the one which holds more water.

81

Reprint 2026-27
Chapter 7.indd 81

07-06-2023 10:58:26

D. Water is very useful for us.

Tick ü the amount of water you need for the given activities.
i.

For brushing the teeth

A bucket full of water

A mug full of water

ii.

For bathing

A bucket full of water A tank full of water

iii.

For preparing 2 glasses
of lemon water

A jug of water

A bucket of water

iv.

For watering a plant

A mug of water

A bucket of water

82

Reprint 2026-27
Chapter 7.indd 82

03-03-2026 10.00.34 AM

Project Work
A. Discuss why is it important to take water in a bucket for bathing
instead of shower or running tap water.
B. Tear and paste colourful paper strips to make one portion of the strip
short and another longer. The strips should be of different sizes.
Shorter
These are shorter

Longer
These are longer

C. List things which are easier to carry and which are difficult to carry.
Easier to carry

Difficult to carry

D. Get bottles, bowls and glasses of different sizes. Now see how many
glasses or bowls of water can fill the bottle. Which of these can hold
more water?
Ask children how many glasses of water they drink in a day.
Discuss and sensitise them about water getting wasted around
them, what they would do if water is left in the glass, should it be
thrown or given to the plants. Also discuss other ways of saving
water like closing the tap when not in use, reusing water, etc.

83

Reprint 2026-27
Chapter 7.indd 83

07-06-2023 10:58:28

8

Fun with Numbers

Simran was putting oranges in boxes. Each box can hold 10
oranges. How many boxes would she need?

She packed them in boxes.

Do you know how many oranges are there?

21
Twenty One

22
Twenty Two

Reprint 2026-27
Chapter 8.indd 84

16-12-2024 11:45:21

Twenty
Three

24
Twenty
Four

Twenty
Five

Twenty
Six

27
Twenty
Seven

85

Reprint 2026-27
Chapter 8.indd 85

16-12-2024 11:45:22

28
Twenty
Eight

Twenty
Nine

30
Thirty

Write 21 to 30
25

21

30

23

27

22
86

Reprint 2026-27
Chapter 8.indd 86

16-12-2024 11:45:23

Let us count the number of flowers and the number of
neem daatun.

Number 31 to 50
36
Thirty Six

31
Thirty One

32
Thirty Two

Thirty
Three

Thirty Seven

Thirty Eight

Thirty Four

35
Thirty Five

39
Thirty Nine

40
Forty

87

Reprint 2026-27
Chapter 8.indd 87

16-12-2024 11:45:26

41
Forty One

46
Forty Six

Forty Two

Forty Seven

43
Forty Three

Forty Four

45
Forty Five

Forty Eight

49
Forty Nine

50
Fifty

Let us Do
A.	Pick up any number card from 1 to 50. Can you place
the number card with help of the clip on ginladi at the
right place?
B.	Write the number on the number cards placed on the
ginladi.

4
88

Reprint 2026-27
Chapter 8.indd 88

07-06-2023 11:21:55

Count and write the numbers.

Fill up the tens frames to show the number. One has
already been done for you.
29
Twenty one
41
Forty one

30
Thirty
Use ginladi to talk about tens and numbers 21 to 50. Also
encourage children to count backwards from any given
number using ginladi or number line initially. Once they
gain confidence, they can do without the ginladi.

89

Reprint 2026-27
Chapter 8.indd 89

07-06-2023 11:21:56

Fill up the missing numbers.
34

39

42

46

Project Work
Farha said that she has packed more than fifty amazing things in her
matchbox. Her friends wondered what these things could be. They had
a big surprise when she opened her box.
Can you collect some items and see how many a matchbox can hold?

90

Reprint 2026-27
Chapter 8.indd 90

19-06-2023 15:01:11

Numbers from 51 – 99
Ankita is pasting mirrors on her house. Help her to find out
how many mirrors she has used in the design.

Count and write the numbers from 51 to 60
51
Fifty
One

Fifty
Six

52
Fifty
Two

Fifty
Seven

Fifty
Three

Fifty
Eight

Fifty
Four

59
Fifty
Nine

Fifty
Five

60
Sixty

91

Reprint 2026-27
Chapter 8.indd 91

07-06-2023 11:21:59

Count and write the numbers from 61 to 80
61
Sixty
One

71
Seventy
One

62
Sixty
Two

72
Seventy
Two

Sixty
Three

Seventy
Three

Sixty
Four

74
Seventy
Four

Sixty
Five

75
Seventy
Five

Sixty
Six

Seventy
Six

Sixty
Seven

Seventy
Seven

Sixty
Eight

78
Seventy
Eight

Sixty
Nine

Seventy
Nine

70
Seventy

80
Eighty

92

Reprint 2026-27
Chapter 8.indd 92

07-06-2023 11:22:06

Count and write the numbers from 81 to 100
81
Eighty
One

91
Ninety
One

Eighty
Two

Ninety
Two

83
Eighty
Three

Ninety
Three

Eighty
Four

Ninety
Four

Eighty
Five

95
Ninety
Five

86
Eighty
Six

Ninety
Six

Eighty
Seven

97
Ninety
Seven

Eighty
Eight

Ninety
Eight

89
Eighty
Nine

Ninety
Nine

90
Ninety

100
Hundred

93

Reprint 2026-27
Chapter 8.indd 93

07-06-2023 11:22:13

Let us Do
Tie a ginladi from one end to the other. Choose a random
number (1 to 99) card. Attach the number cards at the
appropriate place on the ginladi with a clip. Play with your
friends using other cards also.

Use ginladi to add numbers. Ask about the numbers between
any two given numbers.

94

Reprint 2026-27
Chapter 8.indd 94

07-06-2023 11:22:15

Count and write the numbers.

Make a slide and ladder game by filling the missing numbers.
100

98

97

83

84

96

81

82

80

79

61

62

63

65

59

58

56

42

43

45

41
40

77

38

21

22

20

19

18

1

2

3

95
86

76

92
87

88

74

73

72

68

69

53

52

66
54

90

48

71

51
50

37

36

34

33

24

25

27

28

17

16

15

13

12

5

6

8

9

32

31
30
11

This game can be played outdoors (with a chalk draw squares with movable
sticks and ropes as ladders and slides). Some task cards can
be placed on the squares. Instructions can also be modified
like jump to a number where the digits are exchanged, skip
one number on your right and jump, etc.

95

Reprint 2026-27
Chapter 8.indd 95

07-06-2023 11:22:17

Look at the Picture

Let us Talk
A. Observe and discuss what is happening in the picture.
B. What are the different things which you see in the given
picture?
C. How many houses are there?
D. How many people are there in the picture?
E. Guess how many lines are used to draw the leaves of
a tree.
F. Do you know the special name for this type of painting?
G. Which part of India is famous for ‘Warli’ painting?
96

Reprint 2026-27
Chapter 8.indd 96

07-06-2023 11:22:18

Make your own warli drawing.

97

Reprint 2026-27
Chapter 8.indd 97

16-12-2024 11:45:26

9

Utsav

According to the Indian calendar, the festival of Uttarayan like Makar
Sankranti, Pongal, Bihu and Lohri marks the beginning of the transition from
winters to summers. The celebration signifies the return of sunny days and
the start of the harvest season. Discuss the various local festivals
celebrated by children with their families. The picture also highlights
the main elements of each celebration and various shapes and
patterns which can be discussed with children.

Reprint 2026-27
Chapter 9.indd 98

07-06-2023 11:23:01

99

Reprint 2026-27
Chapter 9.indd 99

07-06-2023 11:23:03

Extend the patterns by drawing further.
A.

B.

C.

D.

E.

F.

G.

H.

Encourage children to use concrete objects to make patterns.

100

Reprint 2026-27
Chapter 9.indd 100

07-06-2023 11:23:05

Let us Do
Munna

is very fond of

colouring. He created a pattern
by using the impression of his
thumb and fingers. You can
also create a pattern like this
by using your finger print in the
given space.

What colour should come after pink and why? Discuss.
Ask children to collect different vegetables and cut them into
slices with the help of adults. Use cut slices of these vegetables
to create a pattern of your choice.

101

Reprint 2026-27
Chapter 9.indd 101

19-06-2023 12:16:21

Look at the patterns and extend them by colouring.

Complete the pattern.

102

Reprint 2026-27
Chapter 9.indd 102

07-06-2023 11:23:08

Study the pattern and fill in the missing numbers.

103

Reprint 2026-27
Chapter 9.indd 103

07-06-2023 11:23:10

Murthy and Vani are helping their Amma in making
kolam or rangoli. You can also help them by completing
the below kolam.

Project Work
A. Collect pebbles, flowers, leaves, glasses, bowls, sticks, bangles,
coins, caps, etc., and arrange them in a pattern. Create different
patterns of jewellery, floral pot arrangements, art showpieces, etc.
B. Observe and find the patterns in nature like leaves, butterfly,
animal skins (cat, dog, zebra, tiger), curtains, sarees, dupattas,
tiles, beehive, etc.
C. Collect different objects seen around and make a collage.
D. Create patterns using different actions like clapping, snapping your
fingers, stamping your feet, etc.
The world around us is full of shapes. Encourage children to appreciate
the rich heritage of India through exploring beautiful patterns in
temples, mosque, church, gurudwara and monuments around
them. Also ask them to share their observations of patterns in
different art forms, movement patterns in dance forms, etc.

104

Reprint 2026-27
Chapter 9.indd 104

07-06-2023 11:23:10

10

How do I Spend
my Day?

Hello friends, I am Pihu.
I am 6 years old.
Today, I will share my daily routine,
what I do from morning to night.
Look, the sun is rising in
the sky. It is morning.

I get up from bed in the morning
and have a glass of warm water.

My day starts with
yoga or exercise.
Then, I brush my
teeth and take a bath.

I eat breakfast
and get ready for
school.

Reprint 2026-27
Chapter 10.indd 105

07-06-2023 14:12:49

I study and play with my classmates in the school.
The sun is high in the
sky. It is afternoon
time. I wash my hands
and have lunch with
my friends.

I come back home from school
and take rest for some time.

See, the sun is
setting. It is evening
time. I play with my
friends and then I
study.

Look there, the moon and the stars are
visible in the sky. It is night time.

I eat dinner with my family.

I read a story book and go to
sleep at night.
106

Reprint 2026-27
Chapter 10.indd 106

07-06-2023 14:12:50

Let us Talk
A. What is your daily routine?
B. When do you brush your teeth?
C. When do you take a bath?

Let us Do
A. Tick

ü

the activities that you do in the morning.

B.	Tick ü the activities or things that you do or see during
the day.

C. Tick

ü

the activities that you do at night.

107

Reprint 2026-27
Chapter 10.indd 107

07-06-2023 14:12:52

Guess the time of the day by looking at the picture.
Discuss with your friends what you do during that time.

Let us Do
Colour the activity that usually takes longer time.
A.

B.

108

Reprint 2026-27
Chapter 10.indd 108

07-06-2023 14:12:53

Seasons

Summer

Spring

Monsoon

Winter

Look at the above pictures and discuss the differences
among summer, winter, spring and monsoon seasons.
Match the objects with the season.

Monsoon

Spring

Summer

Winter
109

Reprint 2026-27
Chapter 10.indd 109

07-06-2023 14:12:54

Let us Talk
A. What do you like to eat in the summer season?
B. What do you like to wear in the winter season?

Let us Do
Write the name of the seasons and match them with the
pictures.

Project Work
110

Ask children to draw or stick pictures of their favourite food items during
different seasons and local festivals which are celebrated during these
seasons.
Reprint 2026-27

Chapter 10.indd 110

07-06-2023 14:12:56

11

How Many Times?

A Visit to an Amusement Park
A group of children visited an amusement park.
Wow! 2 of us can sit
on the horse. I will
sit with my friend.

The total
children are
2+2+2+2=
of us can sit on the horse swing altogether.
3 of us can sit in
a toy train. We all
will sit together.

There are 3 bogies. 3 + 3 + 3 =
Total

children can sit in 3 bogies.
Reprint 2026-27

Chapter 11.indd 111

07-06-2023 11:24:54

Here we are! This is
such a big wheel! 4 of us
can sit together. There
are 5 compartments.

+
Total

+

+

=

children can sit in the swing.

After riding on the swings, children planned to eat jalebis.
Each plate of jalebi has 3 pieces. They ordered 6 plates of
jalebis.

+

+

+

+

+

=

6 times 3 is
Discuss the number of groups in each activity through questions like
how many children are there in the picture, how many children
are sitting in each compartment, total number of children on
the ride.

112

Reprint 2026-27
Chapter 11.indd 112

07-06-2023 11:24:56

Travelling in the Bus
2+2+2+2+2+2+2+2+2=
9 times 2 =
Total number of people in the bus =
Some crates of water bottles are kept in the bus. Count
them.

+

+

+

=

4 times 5 =
Total number of bottles in the bus =
113

Reprint 2026-27
Chapter 11.indd 113

07-06-2023 11:24:57

Cheenu bought some packs of erasers, pencils and apples
from the shop. Find the total of each item.
A.

2+

+

+

=

erasers

4 times 2 =
Total number of erasers =
B.

3+

+

+

+

=

pencils

5 times 3 =
Total number of pencils =
C.

3+

+

=

apples

3 times 3 =
Total number of apples =

Project Work
114

Draw a cycle wheel. Ask your friends or find out how many cycles you
have at home. Find out the total number of wheels in all the cycles.

Reprint 2026-27
Chapter 11.indd 114

06-01-2025 10:11:31

12

How Much Can
We Spend ?

Riya started to count the number of coins `1, `2, `5, `10 and
Sahil started to count notes of `10, `20, `50 and `100. Look at
these coins and notes, and write their denominations below.

`1

`10

Reprint 2026-27
Chapter 12.indd 115

16-12-2024 11:49:39

Rahim Kaka — The Toy Seller

Let us Do
A. One ball

costs `20.

Riya gives _____ coins of `5 for the ball.
Sahil gives _____ note of `10 for the ball.
B. Name the toys you can buy for `10.
C. Name the toys you can buy for `20.
D.	If the cost of a car is `14 and Riya has `10 with her, how
much more money does she need to buy the car?
E.	Riya and Sahil together have `30. Write the name of the
toys which they can buy.

116

Reprint 2026-27
Chapter 12.indd 116

09-06-2023 14:21:13

Find the total amount and tick

ü

the correct option.

Let us Play
Make your own currency notes and coins of paper slips.
Play a shopping game in the classroom.
Some children will be shopkeepers and others customers.
Let them buy things using play money made by paper slips.
Encourage them to pay money in different combinations.

117

Reprint 2026-27
Chapter 12.indd 117

16-12-2024 11:49:41

Fill or draw the amount in different combinations using
the given currency.

`20

`10

`13

`8

118

Reprint 2026-27
Chapter 12.indd 118

09-06-2023 14:21:15

Match the same amount by drawing a line.
A.

B.

C.

Saving money is a good habit. Discuss.

Project Work
Try to make your own
gullak with a spare box at
your home with the help
of your siblings or elders.

Ask children to form different combinations for a given
amount using play money.

119

Reprint 2026-27
Chapter 12.indd 119

09-06-2023 14:21:16

So Many Toys

13

Look at the picture and find the number of different
toys.

Elephant s

Teddy Bears

Cars

Dolls

Complete the following sentences by using more than/
less than/equal to.
A. The number of dolls

is ______ the number of cars

.

B. The number of elephants
.
dolls

is ______ the number of

C. The number of teddy bears
.
elephants

is ______ the number of

D. The number of cars
.
bears

is ______ the number of teddy

Reprint 2026-27
Chapter 13.indd 120

09-06-2023 16:58:10

Colourful Flowers

Name the colour of the flowers which you
see mostly in a garden.
Look at the picture of colourful flowers and
write the number of flowers.

Blue flowers

Orange flowers

Red flowers

Purple flowers

A. Name the colour of flowers which are least
in number. ______________
B. Name the colour of the flowers which are
most in number. __________________
True or False

A. Number of red flowers

is more

than the blue flowers

.
is less

B. Number of orange flowers
than the purple flowers

.

Project Work
A.	Make a card with a border of colourful flowers.
B.	Find out in your class how many children
have 3 letters in their names, how many
children have 4 letters in their names and
how many children have more than 4 letters
in their names.

121

Reprint 2026-27
Chapter 13.indd 121

19-06-2023 14:57:49

Puzzles

A. Kopal arranged number cards in the below image and
Anaya hide them with bowls as shown. Can you recognise
the numbers?

You can also hide the numbers on a number card by
using your hands and play this game with your friends.
B. Count the number of logs. Is it 3 logs or 4 logs?

C. This is how Zarina set the glasses. Help her in extending
the arrangement.

  ____________   ____________
Reprint 2026-27
Puzzle Class 1.indd 122

09-06-2023 16:54:25

D. Find the numbers from 1 to 10.

e

i

g

h

t

t

s

f

i

v

e

h

t

e

o

t

w

o

r

x

v

u

n

i

n

e

o

e

r

n

t

t

e

n

n

s

i

x

o

w

e

n

E. Fill the numbers from 1 to 5 in the given balls so that the
sum on both sides is equal.

F. Gillu’s favourite number is 8. If the answer of the asked
question is 8, he becomes happy and if not, he becomes
sad.
Ask some questions to Gillu that has an answer 8 only.
123

Reprint 2026-27
Puzzle Class 1.indd 123

09-06-2023 16:54:26

G. Fill ,
and
in the boxes in such a way
that any shape occurs only once in a row
(horizontal) and column (standing).

column

row

H. Take 4 different objects (each object should be 4), such
as 4 buttons, 4 pebbles, 4 seeds, 4 clay balls, etc. Now
place them in the given boxes in such a way that every
object occurs only once in a row (horizontal) and a column
(vertical standing).

column

row

Can you fill them through some other ways?
I.

Who am I? (A mirror can help you.)

52

37

25

93

124

Reprint 2026-27
Puzzle Class 1.indd 124

09-06-2023 16:54:26

J. Who am I?
i. I am between 5 and 10. I become three
more when read upside down.
ii. I am 3 more than 8 and 3 less than 14.
iii. I am after 50 and before 54. Sum of my
digits is 7.
iv. I am just before 40.
v. Add 5 to me and you will get 24.
vi. I am just after 35.
vii. Reduce 8 from me and 14 will be left.
K. Six matchsticks are used to make a zero. Can you make
any other number by shifting a single matchstick?

L. Find out the missing piece and complete the pot.

125

Reprint 2026-27
Puzzle Class 1.indd 125

09-06-2023 16:54:26

M. How many times can you subtract 5 from 25?
N. Ranu has 3 seeds. She wants to place them on any 3
numbers of the given chart in such a way that the sum of
those numbers will be 17. Can you help Ranu in finding
the numbers.

4

9

6

7

16

0

8

5

15

13

1

2

17

10

3

12

In how many ways did you do it?
If you have 2 seeds, which numbers will you place them
to get a total of 17?
O. Encircle the identical shadow image.

i

ii

iii

iv

126

Reprint 2026-27
Puzzle Class 1.indd 126

09-06-2023 16:54:26

P. Write numbers from 5 to 9 in the card given below such
that the row and the column have the same total.

column

row

Q. Try to get the center number by doing addition or
subtraction.

3

6

3+

7–1

15

11

R. Write down the correct numbers in the

.

127

Reprint 2026-27
Puzzle Class 1.indd 127

26-06-2023 14:48:05

S. Sarita has four coins of different values.

What is the minimum number of coins used to spend
exactly `49?
T. Find out the value of orange

+

= 8

+

= 10

.

=
U. Let us play the ball game.*

i. Choose 3 balls in such a way that their sum will be 15.
ii. Choose 3 balls to get a maximum score.
iii. Choose 3 balls to get a minimum score.
*Hint: Try to solve by rotating the balls.
128

Reprint 2026-27

Notes

Reprint 2026-27
Puzzle Class 1.indd 129

09-06-2023 16:54:28

Notes

Reprint 2026-27
Puzzle Class 1.indd 130

09-06-2023 16:54:28


## Page 21

Exercise 00002 - Python Code:
[https://github.com/sealanco/blog/blob/main/source/codes/print.py](https://github.com/sealanco/blog/blob/main/source/codes/print.py)
```python
print("Hello")
```

Exercise 00003 - LaTeX Code:
```latex
The quadratic formula is given by $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.
```

The quadratic formula is given by $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

```latex
$$
f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi) \, e^{2\pi i \xi x} \, d\xi
$$
```

$$
f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi) \, e^{2\pi i \xi x} \, d\xi
$$

Exercise 0003 - Matplotlib Code:
```python
   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 10, 100)
   plt.figure()
   plt.plot(x, np.sin(x), color="tab:blue")
   plt.title("Sine Wave")
   # Save directly as an SVG file
   plt.savefig('my_plot.svg', format='svg', bbox_inches='tight')

```

```{eval-rst}
.. plot::

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 10, 100)
   plt.figure()
   plt.plot(x, np.sin(x), color="tab:blue")
   plt.title("Sine Wave")
   # Save directly as an SVG file
   plt.savefig('my_plot.svg', format='svg', bbox_inches='tight')

```

```svg
A. Draw round objects in <svg width="24" height="24" style="vertical-align: middle;"><circle cx="12" cy="12" r="11" stroke="white" stroke-width="2" /></svg> and long objects in <svg width="36" height="24" style="vertical-align: middle;"><rect x="1" y="1" width="34" height="22" rx="2" stroke="white" stroke-width="2" /></svg> .

Here is a larger blue square with a white border <svg width="24" height="24" style="vertical-align: middle;"><rect x="1" y="1" width="22" height="22" rx="2" fill="blue" stroke="white" stroke-width="2" /></svg> inline in your text.

Here is a blue rectangle with a white border <svg width="36" height="24" style="vertical-align: middle;"><rect x="1" y="1" width="34" height="22" rx="2" stroke="white" stroke-width="2" /></svg> inline in your text.
```
