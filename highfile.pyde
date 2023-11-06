#writing a highscore file for the total of the scores of the levels
listt=[]
line1="Total of High Scores : 0"
listt.append(line1)
saveStrings('tothigh.txt',listt)    

lines=loadStrings("tothigh.txt")
print(lines)
