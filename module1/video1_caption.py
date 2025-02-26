captions = """WEBVTT

00:00:00.000 --> 00:00:05.000
This is the first caption.

00:00:05.500 --> 00:00:10.000
This is the second caption.

00:00:10.500 --> 00:00:15.000
Another caption appears here.
"""

with open("captions.vtt", "w") as file:
    file.write(captions)

print("Caption file saved as captions.vtt")
