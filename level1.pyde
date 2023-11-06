#writing a file for my highscore in level 1
list1=[]

line1="Level 1 High Score : 0"
list1.append(line1)
saveStrings('highscore1.txt',list1)    

lines=loadStrings("highscore1.txt")
print(lines)
