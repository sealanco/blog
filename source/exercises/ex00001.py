#!/usr/bin/env python3

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
