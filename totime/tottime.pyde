listtt=[]
line1="Game's Quickest Time : 0 seconds"
listtt.append(line1)

saveStrings('tottime.txt',listtt)    

lines=loadStrings("tottime.txt")
print(lines)
