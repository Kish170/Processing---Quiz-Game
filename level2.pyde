#writing a file for my highscore in level 2
list1=[]

line1="Level 2 High Score : 0"
list1.append(line1)
saveStrings('highscore2.txt',list1)    

lines=loadStrings("highscore2.txt")
print(lines)
