import random
def shuffle(original):
    randomised = ''.join(random.sample(original, len(original)))
    return(randomised)


woord1 = shuffle("Hello")
woord2 = shuffle("Wessel")
woord3 = shuffle("Programma")

print(woord1)
print(woord2)
print(woord3)
