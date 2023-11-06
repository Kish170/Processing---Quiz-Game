#writing a file for my highscore in level 3
list3=[]

line3="Level 3 High Score : 0"
list3.append(line3)
saveStrings('highscore3.txt',list3)    

lines=loadStrings("highscore3.txt")
print(lines)
