  #7.There are 12 musical notes in chromatic scale namely
    # "C C# D D# E F F# G G# A A# B"
 #Interval between each pair of notes is called as semitone. D# is 3 semitones above C, 
 #E is 2 semitones above D. Every note has a major scale which comprises of 7 out of 12 notes 
 #which are 0,2,4,5,7,9 and 11 semitones above the current note.
 #Example: For note D, major scale comprises of (D, E, F#, G, A, B,C#), For note C, major scale 
 #comprises of (C, D, E, F, G, A, B) Write a script which accepts a note and prints its major scale.

scale=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
note=input('Enter the note :')
count=0
for i in range(12) :
    if (note==scale[i]) : break
result=[]
while (count<7) :
    if (i<12) :
        result.append(scale[i])
        count+=1
    else :
        result.append(scale[i-12])
        count+=1
    if (count==3) : i+=1
    else : i+=2
print(result)