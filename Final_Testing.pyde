
#stating the page the user will open up to, the welcome page
page="Welcome"      

#adding a library which I will be using to make sounds
add_library("minim")

#setting up the starting scores for the game
scores1=0
scores2=0
scores3=0
scores=0

#seting up positions for my animations
xPos= 650
yPos= 250
ydir=2
dir=2
di=2
pos= 50
pas=400
xpos=100
ypos=100
x=720
y=500
qy=-210
yq=768
sec=400
diry=2
ques=50
diryy=2
old=500
dirxx=2
time=30
duration=30

#setting up quickest time scores for level one
q1time=0
q2time=0
q3time=0
times=0

#setting up quickest time scores for level two
q4time=0
q5time=0
q6time=0
times2=0

#setting up quickest time scores for level three
q7time=0
q8time=0
q9time=0
times3=0

#setting time score for whole game
tottimes=0

#setting up the size of the page/game quiz
def setup():
    size(1024,768)
    smooth()
    noStroke()
    frameRate(40)
    
    #globlizing my images, font, readers and files that will be used later on
    global readtime1
    #creating a reader that will read my quickest time for level one
    readtime1 = createReader("time1.txt")
    
    global readtime2
    #creating a reader that will read my quickest time for level two
    readtime2 = createReader("time2.txt")
    
    global readtime3
    #creating a reader that will read my quickest time for level three
    readtime3 = createReader("time3.txt")
    
    global readtottime
    #creating a reader that will read my quickest time for the game
    readtottime = createReader("tottime.txt")
    
    global reader
    #creating a reader that will read my highscore for the game
    reader = createReader("tothigh.txt")
    
    global read
    #creating a reader that will read my highscore for level one
    read = createReader("highscore1.txt")
    
    global read2
    #creating a reader that will read my highscore for level two
    read2 = createReader("highscore2.txt")
    
    global read3
    #creating a reader that will read my highscore for level three
    read3 = createReader("highscore3.txt")

    #adding image to setup as background for my welcome page  
    global img
    img = loadImage("Yellow.png")
    
     #adding image to setup as background for highscore, hint, keys. help and results page
    global mos
    mos = loadImage("mosaic.png")
    
    #adding image being used for buttons in my pages
    global but
    but = loadImage("Button.png")
    
    #adding image being used for buttons in my pages
    global butw
    butw = loadImage("Buttonw.png")
    
    #adding image being used for animations in my welcome page
    global seimg
    seimg = loadImage("oooo.png")
    
    #adding image that follows the cursor through out the game
    global s
    s = loadImage("backkk.png")
    
    #adding image being used for animations in my level pages
    global q
    q = loadImage("scribqb.png")
    
     #adding a background image for my question pages
    global ima
    ima = loadImage("qpage.png")
    
     #adding an image for my level one page
    global scrib1
    scrib1 = loadImage("scrib1.png")
    
    #adding an image level to page
    global scrib2
    scrib2 = loadImage("scrib2.png")
    
     #adding an image level three page
    global scrib3
    scrib3 = loadImage("scrib3.png")
    
     #adding an image being used for animations in level pages
    global scribqw
    scribqw = loadImage("scribqw.png")
    
    #adding an image being used in question 1
    global one
    one = loadImage("1.png")
    
    #adding an image being used in question 2
    global two
    two = loadImage("2.png")
    
     #adding an image being used in question 3
    global three
    three = loadImage("3.png")
    
     #adding an image being used in question 4
    global four
    four = loadImage("4.png")
    
    #adding an image being used in question 5
    global five
    five = loadImage("5.png")
    
    #adding an image being used in question 6
    global six
    six = loadImage("6.png")
    
    #adding an image being used in question 7
    global seven
    seven = loadImage("7.png")
    
    #adding an image being used in question 8
    global eight
    eight = loadImage("8.png")
    
    #adding an image being used in question 9
    global nine
    nine = loadImage("9.png")
    
    #adding a font 
    global font
    font = loadFont("AgencyFB-Reg-48.vlw")
    
    #reference for sounds
    #Title: How to get sound files in processing.py
    #Author: Netrate
    #Date: August 2017
    #Code Version: 2.2.1
    #Availability: https://forum.processing.org/two/discussion/23738/how-to-get-sound-files-in-processing-py
    
    #adding a sound that plays when user clicks the right answer
    global sf
    minim=Minim(this)
    sf = minim.loadFile("correct.mp3")
    
     #adding a sound that plays when the user clicks the wrong answer
    global wrong
    minim=Minim(this)
    wrong = minim.loadFile("wrong.mp3")
    
    #adding a sound that plays at the last 5 seconds
    global countdown
    minim=Minim(this)
    countdown = minim.loadFile("countdown.mp3")
    
    #adding a sound that plays at the last 5 seconds
    global lobby
    minim=Minim(this)
    lobby = minim.loadFile("lobby.mp3")
    
    #adding a sound that plays at the last 5 seconds
    global qmusic
    minim=Minim(this)
    qmusic = minim.loadFile("qmusic.mp3")
    
    #variable for the timer
    global start
    start=millis()
    
    lobby.loop()
    
    
#drawing the different pages
def draw():
    #making the different variables from the main code global
    global page
    global highscore
    global scores
    global font
    global xPos
    global yPos
    global ydir
    global pos
    global pas
    global dir
    global di
    global high1
    global high2
    global high3
    global scores1
    global scores2
    global scores3
    global s
    global xpos
    global ypos
    global x
    global y
    global qy
    global yq
    global sec
    global diry
    global ques
    global diryy
    global old
    global dirxx
    global time 
    global duration
    global q1time
    global q2time
    global q3time
    global l1time
    global start
    global times
    global q4time
    global q5time
    global q6time
    global l2time
    global times2
    global q7time
    global q8time
    global q9time
    global l3time
    global times3
    global hightimes
    global tottimes
        
    #drawing the welcome page
    if page=="Welcome":
        #adding background image and page title
        image(img, 0, 0)
        fill(255)
        textFont(font,90)
        textSize(70)
        text("Welcome to Prepquiz",50,100)
        
        #setting a different frame rate for the animations in this page
        frameRate(40)
        
        #reference for animations
        #Title:Introduction to Processing: Simple Animation
        #Author: Stevie Dickie
        #Date: 22 July 2011
        #Code Version: 2.2.1
        #Availability: https://www.youtube.com/watch?v=jLuMjfxgBpc
        
        #adding an image for animation
        image(seimg, xPos,yPos,100,100) 
        #animation details 
        yPos=yPos+ydir
        if yPos>height-475 or yPos<200:
            ydir=ydir*-1
            
        #adding an image for animation
        image(seimg, 850,pos,150,150)  
        #animation details 
        pos=pos+dir
        if pos>height-700 or pos<0:
            dir=dir*-1
            
        #adding an image to animation
        image(seimg,920,pas,75,75)
        #animation details 
        pas=pas+ydir
        if pas>height-300 or pas<200:
            ydir=ydir*-1
            
         #adding an image to animation
        image(seimg,700,sec,150,150)
        #animation details 
        sec=sec+diry
        if sec>height-300 or sec<320:
            diry=diry*-1
            
        #adding an image to animation
        image(seimg,700,ques,90,90)
        #animation details 
        ques=ques+diry
        if ques>height-400 or ques<300:
            diryy=diryy*-1
            
        #adding an image to animation
        image(seimg,850,old,175,175)
        #animation details 
        old=old+dirxx
        if old>height-210 or old<450:
            dirxx=dirxx*-1
    
        #drawing the start button
        image(but,20,190,300,120)        
        textSize(40)
        fill(255)
        text("Start(s)",70,270)
        
        #drawing the highscore button 
        fill(255)
        image(butw,20,295,300,120)
        fill(0)
        text("Highscore(h)",70,375)
        
        #drawing the quit button
        fill(255)
        image(but,20,400,300,120)
        fill(255)
        text("Quit(q)",70,480)
        
        #drawing a button to a page that shows the different keys that can be used
        fill(255)
        image(butw,20,505,300,120)
        fill(0)
        text("Keys(k)",70,585)
        
        #drawing a button to a page that helps the user
        fill(255)
        image(but,20,610,300,120) 
        fill(255)
        text("Help(p)",70,690)
        
        #making a question mark thats follows the cursor
        image(s, mouseX,mouseY,50,50)
        
        #reading the highscore total file
        try:
            linee = reader.readLine()
        except:
            linee = None
    
        if (linee == None) is False:
            strip=linee.strip()
            global f
            a,b,c,d,e,f = strip.split(" ")
            highscore=float(f)
        
        #comparing the scores of the quiz to the highscore and changing them
        if highscore<scores:
            highscore=scores
    
        #rewriting the scores based of comparison above
        High=open("tothigh.txt","w")
        High.write("Total of High scores : "+str(highscore))
        High.close()
        
        #reading my high score for level 1 
        try:
            level1 = read.readLine()
        except:
            level1 = None
    
        if (level1 == None) is False:
            stripline=level1.strip()
            global l1
            a,b,c,d,e,l1 = stripline.split(" ")
            high1=float(l1)
        #comparing the level 1 score of the quiz done and the level 1 highscore
        if high1<scores1:
            high1=scores1
        
        #rewriting my scores based on the comparison done above
        High1=open("highscore1.txt","w")
        High1.write("Level 1 High Score : "+str(high1))
        High1.close()
        
        #reading my high score for level 2 
        try:
            level2 = read2.readLine()
        except:
            level2 = None
    
        if (level2 == None) is False: 
            strip2=level2.strip()
            global l2
            a1,b1,c1,d1,e1,l2 = strip2.split(" ")
            high2=float(l2)
        #comparing my level 2 score of the quiz done and level 2 highscore
        if high2<scores2:
            high2=scores2
        
        #rewriting my scores based on the comparison done above
        High2=open("highscore2.txt","w")
        High2.write("Level 2 High Score : "+str(high2))
        High2.close()
        
         #reading my high score for level 3 
        try:
            level3 = read3.readLine()
        except:
            level3 = None
    
        if (level3 == None) is False: 
            strip3=level3.strip()
            global l3
            a3,b3,c3,d3,e3,l3 = strip3.split(" ")
            high3=float(l3)
        #comparing my level 3 score of the quiz done and the level 3 highscore
        if high3<scores3:
            high3=scores3
        
        #rewriting my scores based on the comparison done above
        High3=open("highscore3.txt","w")
        High3.write("Level 3 High Score : "+str(high3))
        High3.close()
        
        #reading the file that has the quickest time for level 1
        try:
            linetime1 = readtime1.readLine()
        except:
            linetime1 = None
    
        if (linetime1 == None) is False:
            striptime1=linetime1.strip()
            global t1
            qas,iat,bp,l,j,t1,tp = striptime1.split(" ")
            l1time=int(t1)
        
        #comparing the scores of the quickest time and changing them
        if times==0:
            l1time=l1time
        elif l1time==0:
            l1time=times
        elif l1time>times:
            l1time=times
    
        #rewriting the scores based of comparison above
        time1=open("time1.txt","w")
        time1.write("Level 1 Quickest time : "+str(l1time)+" seconds")
        time1.close()
        
        #reading the file that has the quickest time for level 2
        try:
            linetime2 = readtime2.readLine()
        except:
            linetime2 = None
    
        if (linetime2 == None) is False:
            striptime2=linetime2.strip()
            global t2
            saq,ia,pb,asd,jak,t2,tpl = striptime1.split(" ")
            l2time=int(t2)
        
        #comparing the scores of the quickest time and changing them
        if times2==0:
            l2time=l2time
        elif l2time==0:
            l2time=times2
        elif l2time>times2:
            l2time=times2
    
        #rewriting the scores based of comparison above
        time2=open("time2.txt","w")
        time2.write("Level 2 Quickest time : "+str(l2time)+" seconds")
        time2.close()
        
        #reading the file that has the quickest time for level 3
        try:
            linetime3 = readtime3.readLine()
        except:
            linetime3 = None
    
        if (linetime3 == None) is False:
            striptime3=linetime3.strip()
            global t3
            swq,iw,pw,awd,jwk,t3,wpl = striptime3.split(" ")
            l3time=int(t3)
        
        #comparing the scores of the quickest times and changing them
        if times3==0:
            l3time=l3time
        elif l3time==0:
            l3time=times3
        elif l3time>times3:
            l3time=times3
    
        #rewriting the scores based of comparison above
        time3=open("time3.txt","w")
        time3.write("Level 3 Quickest time : "+str(l3time)+" seconds")
        time3.close()
        
        #reading the file that has the quickest time for level 3
        try:
            linetottime = readtottime.readLine()
        except:
            linetottime = None
    
        if (linetottime == None) is False:
            striptottime=linetottime.strip()
            global tot1
            lk,jk,pw,awd,jwk,tot,wpl = striptime3.split(" ")
            hightimes=int(tot)
            #comparing the scores of the quickest times and changing them
        if tottimes==0:
            tottimes=hightimes
        elif hightimes==0:
            hightimes=tottimes
        elif hightimes>tottimes:
            hightimes=tottimes
        
        #rewriting the scores based of comparison above
        totime=open("tottime.txt","w")
        totime.write("Game's Quickest time : "+str(hightimes)+" seconds")
        totime.close()
        lobby.play()
            
        #drawing the highscore page
    elif page=="Highscore":
        #adding a background image and page title
        image(mos,-20,0)
        fill(0)
        textSize(80)
        text("Highscore",350,100)
        
        #writing the new highscores
        fill(255)
        stroke(0)
        rect(150,180,700,450)
        noStroke()
        xl=200
        yl=230
        #writing the highscore for the whole quiz
        lines=loadStrings("tothigh.txt")
        textSize(25)
        for x in lines:
            fill(0)
            text(x,xl,yl)
        #writing the highscore for level one
        lin=loadStrings("highscore1.txt")
        textSize(25)
        for x in lin:
            fill(0)
            text(x,200,280)
        #writing the highscore for level two
        lin2=loadStrings("highscore2.txt")
        textSize(25)
        for x in lin2:
            fill(0)
            text(x,200,330)
        #writing the highscore for level three
        lin3=loadStrings("highscore3.txt")
        textSize(25)
        for x in lin3:
            fill(0)
            text(x,200,380)
            
        #writing the quickest time i the game
        tottim=loadStrings("tottime.txt")
        textSize(25)
        for x in tottim:
            fill(0)
            text(x,200,430)
            
        #writing the quickest time for level 1
        tim1=loadStrings("time1.txt")
        textSize(25)
        for x in tim1:
            fill(0)
            text(x,200,480)
            
        #writing the quickest time for level 2
        tim2=loadStrings("time2.txt")
        textSize(25)
        for x in tim2:
            fill(0)
            text(x,200,530)
            
        #writing the quickest time for level 3
        tim3=loadStrings("time3.txt")
        textSize(25)
        for x in tim3:
            fill(0)
            text(x,200,580)
    
        #drawing a button to go back to the welcome page
        image(but,20,610,300,120) 
        fill(255)
        textSize(40)
        text("Homepage(w)",65,690)
        
        image(s, mouseX,mouseY,50,50)
        
    elif page=="Keys":
        #adding background image and title for page 
        image(mos,-20,0)
        fill(0)
        textSize(80)
        text("Keys",400,100)
        
        #drawing a box that shows the different keys that can be pressed to play the game
        fill(255)
        stroke(0)
        rect(150,200,700,400)
        noStroke()
        fill(0)
        textSize(25)
        text("Start:Press (s)",200,250)
        text("Highscore:Press (h)",200,275)
        text("Quit/Exit:Press (q)",200,300)
        text("Keys:Press (k)",200,325)
        text("Homepage:Press (w)",200,350)
        text("(1)Choice: Press (1)",200,375)
        text("(2)Choice: Press (2)",200,400)
        text("(3)Choice: Press (3)",200,425)
        text("(4)Choice: Press (4)",200,450)
        text("Redo: Press (r)",200,475)
        text("Next Question: Press (n)",200,500)
        text("Level Number: Press (f)",200,525)
        text("Results: Press (c)",200,550)
        
        #button to return to the welcome page
        image(but,20,610,300,120)
        fill(255)
        textSize(40)
        text("Homepage(w)",65,690)
        
        image(s, mouseX,mouseY,50,50)
        
    elif page=="Help":
        #adding a background image and title for page
        image(mos,-20,0)
        fill(0)
        textSize(80)
        text("Instructions",320,100)
        
        #writing instructions/rules for the game 
        fill(255)
        stroke(0)
        rect(150,160,700,440)
        noStroke()
        textSize(28)
        fill(0)
        text("Level 1 Time Limit:30 seconds",200,220)
        text("Level 2 Time Limit:25 seconds",200,260)
        text("Level 3 Time Limit:20 seconds",200,300)
        text("If you click the wrong answer or next question in level 1:-25 points",200,340)
        text("If you click the wrong answer or next question in level 2:-30 points",200,380)
        text("If you click the wrong answer or next question in level 3:-35 points",200,420)
        text("If you click the right answer in level 1:(100-(3.3 x timescore))=points",200,460)
        text("If you click the right answer in level 2:(100-(4 x timescore))=points",200,500)
        text("If you click the right answer in level 3:(100-(5 x timescore))=points",200,540)

        #button to go to the homepage
        image(but,60,600,250,120)
        textSize(20)
        fill(255)
        text("Homepage(w)",125,675)
        
        #a button so the user can leave the game
        image(but,735,600,250,120)
        fill(255)
        text("Exit(q)",840,675)
        
        #a button so they can start the game
        image(but,380,600,250,120)
        fill(255)
        text("Start(s)",480,675)
        
        
    #drawing a page that sends the user to level one
    elif page=="Level One":
        #pausing background music
        lobby.pause()
        #background image
        image(mos,-20,0)
        
        #reference for animations
        #Title:Introduction to Processing: Simple Animation
        #Author: Stevie Dickie
        #Date: 22 July 2011
        #Code Version: 2.2.1
        #Availability: https://www.youtube.com/watch?v=jLuMjfxgBpc
        
        #adding an image
        image(scrib1,275,-25,449,880)
            
        #animation image    
        image(q,50,qy,200,200) 
        
        #animation details
        frameRate(200)
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,250,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,450,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,650,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
        #animation image    
        image(q,850,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
        #animation image    
        image(scribqw,-50,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,150,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,350,yq,200,200) 
        
       #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,550,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
        #animation image    
        image(scribqw,750,yq,200,200) 
        
         #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
        #title of the page
        fill(255)
        textSize(80)
        text("Level One",375,350)
        
       #creating a button so they can start level one
        image(but,60,620,250,120)
        textSize(20)
        fill(255)
        text("Start(s)",155,690)
            
        #creating a button so they can return to the  welcome page
        image(butw,710,620,250,120)
        fill(0)
        text("Homepage(w)",780,690)
        
        #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)

    #drawing question 1
    elif page=="Question 1":
        #playing background music
        qmusic.play()
        
        #drawing background and details of the page
        image(ima,0,0)
        image(one,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:One",50,150)
        
        #drawing the question(1)
        stroke(0)
        fill(250)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 1: When making a function, inside the parentheses we put...",120,250,800,300)
        
        #drawing the multiple choices
        #drawing choice 1
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)Parameters",125,455)
            
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)Lists",625,455)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)Numbers",125,615)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)Docstring",625,615)
            
        #drawing the exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
            
        #drawing Welcome button, so user can return to homepage
        image(but,60,645,250,120)
        fill(255)
        text("Homepage(w)",200/2,720)
        noStroke()
        
         #making a question mark to follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #Title: Countdown Timer
        #Author: Digital Dragon
        #Date: 24 June 2016
        #Code Version: 2.2.1
        #Availability: https://openprocessing.org/sketch/375820/
        
         #creatin a timer in question 1
        image(but,760,20,250,120)
        if (time > 0): 
            time = duration - (millis() - start)/1000
            fill(255)
            text("Timer: "+str(time),800, 88)
        if time==0:
            page="Question 2"
            #rewinding music
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores1=scores1-25
            scores-=25
            #resetting timer
            start=millis()-start
            time=30
            duration=30
            start=millis()
            #setting and adding time scores if time == 0
            q1time=0
            q1time=30-q1time
            times=times+q1time
            q2time=0
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
            
        
    #drawing the hint page for question 1
    elif page=="Hint1":
    #drawing the hint for question 1
        #background image and title of the page
        image(mos,-20,0)
        fill(255)
        stroke(0)
        rect(150,200,700,400)
        fill(0)
        textSize(80)
        text("Hint",425,120)
        
        #writing down the hint for question 1
        fill(255,0,0)
        rect(150,200,700,100)
        textSize(30)
        fill(255)
        text("Incorrect Answer",400,250)
        fill(0)
        text("Hint: What are the variables/arguments listed inside the parentheses in the function definition called?(not a list).",200,350,500,200)
        fill(0)
        textSize(30)
        text("Note: Functions should usually be before the main code",200,480,500,300)
        fill(255)
        noStroke()
        
        #creating a redo button
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
            
        #creating a next question button so they can go to the next question
        image(butw,735,610,275,120)
        fill(0)
        text("Next Question(n)",800,685)
        
         #creatin a timer in hint 1
        image(but,760,20,250,120)
        if (time > 0): 
            time = duration - (millis() - start)/1000
            fill(255)
            text("Timer: "+str(time),800, 88)
        if time==0:
            page="Question 2"
            #rewinding sounds
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores1=scores1-25
            scores-=25
            #resetting timer
            start=millis()-start
            time=30
            duration=30
            start=millis()
            #setting and adding time scores if time == 0
            q1time=0
            q1time=30-q1time
            times=times+q1time
            q2time=0
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
        #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
            
    #drawing the page for question 2
    elif page=="Question 2":
        #playing background music
        if time<=28:
            qmusic.play()
        #background image and details of the page
        image(ima,0,0)
        image(two,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:One",50,150)
        
        #writing in the question(2)
        stroke(0)
        fill(255)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 2: What is the purpose of the def keyword in Python?",120,250,800,300)
            
        #drawing the multiple choices
        #drawing choice 1
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)Says what the function does",125,425,350,450)
        
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)Indicates the start of a function definition",625,415,350,450)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)Is shown to tell us the function is done",125,575,350,675)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)Used to add ",625,615)
            
        #drawing exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
        
        #creatin a timer in question 2
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 3"
            #rewinding sounds
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores1=scores1-25
            scores-=25
            #resettng timer
            start=millis()-start
            time=30
            duration=30
            start=millis()
            #setting and adding time scores if time == 0
            q2time=0
            q2time=30-q2time
            times=times+q2time
            q3time=0
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
            
        #drawing Welcome button, so user can return to homepage

        fill(255)
        image(but,60,645,250,120)
        text("Homepage(w)",200/2,720)
        noStroke()
        
        #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
    #drawing the hint page for question 2
    elif page=="Hint2":
        #drawing the hint for question 2
        #adding bakcground image and title of page
        image(mos,-20,0)
        fill(255)
        stroke(0)
        rect(150,200,700,400)
        fill(0)
        textSize(80)
        text("Hint",425,120)
        fill(255,0,0)
            
        #writing down the hint for question 2
        rect(150,200,700,100)
        fill(255)
        textSize(30)
        text("Incorrect Answer",400,250)
        fill(0)
        textSize(30)
        text("Hint: The def keyword is followed by the function name and parameters",200,350,500,200)
        fill(0)
        text("Note: Parameters can have more than two variables/arguments",200,460,620,300)
        fill(255)
        noStroke()
            
        #creating a redo button so user can redo the question after getting it wrong
        fill(255)
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
            
        #creating a next question button so the user can go to the next question
        fill(255)
        image(butw,735,610,275,120)
        fill(0)
        text("Next Question(n)",800,685)
        
         #creatin a timer in hint 2
        fill(255)
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 3"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores1=scores1-25
            scores-=25
            #resettng timer
            start=millis()-start
            time=30
            duration=30
            start=millis()
            #setting and adding time scores if time == 0
            q2time=0
            q2time=30-q2time
            times=times+q2time
            q3time=0
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
        #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
            
    #drawing question 3
    elif page=="Question 3":
        #playing background music
        if time<=28:
            qmusic.play()
        #adding a background image and page details
        image(ima,0,0)
        image(three,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:One",50,150)
            
        #writing the question(3)
        stroke(0)
        fill(255)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 3: Whats the first optional statement in a function called?",125,250,700,300)
            
        #drawing the multiple choices
        #drawing choice one
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)Parameters",125,455)
            
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)Arguments",625,455)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)Return",125,615)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)Docstring",625,615)
        
         #drawing the exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
            
        #drawing Welcome button, so user can return to homepage
        image(but,60,645,250,120)
        fill(255)
        text("Homepage(w)",200/2,720)
        noStroke()
        
        #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #creatin a timer in question 3
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            #setting and adding time scores if time == 0
            q3time=0
            q3time=30-q3time
            times=times+q3time
            tottimes+=times
            #adding scores
            scores1=scores1-25
            scores-=25
            page="Results"
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
            
    
    #drawing the hint page for question 3
    elif page=="Hint3":
            
        #drawing the hint for question 3
        #adding background image and title of page
        fill(255)
        image(mos,-20,0)
        stroke(0)
        rect(150,200,700,400)
        fill(0)
        textSize(80)
        text("Hint",425,150)
        fill(255,0,0)
            
        #writing down the hint for question 3
        rect(150,200,700,100)
        fill(255)
        textSize(30)
        text("Incorrect Answer",400,250)
        fill(0)
        textSize(30)
        text("Hint: It has the word string in it",200,350,500,200)
        fill(0)
        text("Note: Return statements without an expression return as none",200,430,530,300)
        noStroke()
            
        #creating a redo button so user can redo question after getting it wrong
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
            
        #creating a button that takes them to the results of level 1
        image(butw,735,610,275,120)
        fill(0)
        text("Results(c)",800,685)
        
        #creatin a timer in hint 3
        fill(255)
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            #setting and adding time scores if time == 0
            q3time=0
            q3time=30-q3time
            times=times+q3time
            tottimes+=times
            page="Results"
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
            #adding scores
            scores1=scores1-25
            scores-=25
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
        #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
            
    #drawing the results of level 1
    elif page=="Results":
        countdown.pause()
        #pausing the music
        qmusic.pause()
        #background image and title of page
        image(mos,-20,0)
        fill(0)
        textSize(80)
        text("Results",375,100)
        fill(255)
        stroke(0)
        rect(150,150,700,400)
        fill(0)
        
        #writing in the results of level one
        textSize(30)
        text("Score="+str(scores),200,220)
        text("Score for Level 1="+str(scores1),200,270)
        text("Time score="+str(tottimes),200,320)
        text("Time for level 1="+str(times),200,370)
        #writing if they tied, got higher or lesser than the highscore for level one
        if int(scores1)<int(high1):
            low=high1-scores1
            text("Your score is "+str(low)+" points less than the highscore for level one",200,420)
        elif int(scores1)>int(high1):
            higher=scores1-high1
            higher=float(higher)
            text("Your score is "+str(higher)+" points higher than the highscore for level one",200,420)
        elif int(scores1)==int(high1):
            text("Your in tie with the highscore, "+str(high1)+", for level one",200,420)
         #writing if they tied, got higher or lesser than quickest time for level one
        if int(l1time)<int(times):
            quixck=times-l1time
            text("Your time score is "+str(quixck)+" seconds slower than the quickest time score for level one",200,450,650,450)
        elif int(l1time)>int(times):
            highertim=l1time-times
            text("Your time score is "+str(highertim)+" seconds faster than the quickest time score for level one",200,450,650,450)
        elif int(l1time)==int(times):
            text("Your in tie with the time score, "+str(l1time)+", for level one",200,450,650,450)
        noStroke()
        
        #button to go to the homepage
        image(but,60,600,250,120)
        textSize(20)
        fill(255)
        text("Homepage(w)",125,675)
        
        #a button so the user can leave the game
        image(but,735,600,250,120)
        fill(255)
        text("Exit(q)",840,675)
        
        # a button so they can start level 2
        image(but,380,600,250,120)
        fill(255)
        text("Level 2(f)",480,675)
        
        #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
     #creating the page for level 2   
    elif page=="Level Two":
        image(mos,-20,0)
        
        #reference for animations
        #Title:Introduction to Processing: Simple Animation
        #Author: Stevie Dickie
        #Date: 22 July 2011
        #Code Version: 2.2.1
        #Availability: https://www.youtube.com/watch?v=jLuMjfxgBpc
        
        #adding an image
        image(scrib2,275,-25,449,880)
            
        #animation image    
        image(q,50,qy,200,200) 
        
        #animation details
        frameRate(200)
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,250,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,450,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,650,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
        #animation image    
        image(q,850,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
        #animation image    
        image(scribqw,-50,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,150,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,350,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,550,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
        #animation image    
        image(scribqw,750,yq,200,200) 
        
         #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
        
        #adding title of the page
        fill(255)
        textSize(80)
        text("Level Two",375,350)
        
       #creating a button so they can start level two
        image(but,60,620,250,120)
        textSize(20)
        fill(255)
        text("Start(s)",155,690)
            
        #creating a button so they can return to homepage
        image(butw,710,620,250,120)
        fill(0)
        text("Homepage(w)",780,690)
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
    
    #creating a page for question 4
    elif page=="Question 4":
        #playing background music
        qmusic.play()
        
        #adding background image and details of the page 
        image(ima,0,0)
        image(four,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:Two",50,150)
        
        #writing the question(4)
        stroke(0)
        fill(255)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 4: Which of the following is a for loop used for",120,250,800,300)
        
        #drawing the multiple choices
        #drawing choice one
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)Definite Iterations",125,455)
            
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)Indefinite Iterations",625,455)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)List of Iterations",125,615)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)Numbers of Iterations",625,615)
            
        #drawing exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
            
        #drawing Welcome button, so user can return to homepage
        image(but,60,645,250,120)
        fill(255)
        text("Homepage(w)",200/2,720)
        noStroke()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #creatin a timer in question 4
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 5"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores2=scores2-30
            scores-=30
            #resettng timer
            start=millis()-start
            time=25
            duration=25
            start=millis()
            #setting and adding time scores if time == 0
            q4time=0
            q4time=25-q4time
            times2=times2+q4time
            q5time=0
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
    #drawing the hint page for question 4
    elif page=="Hint4":
    #drawing the hint for question 4
        #background image and title of page
        stroke(0)
        image(mos,-20,0)
        fill(255)
        rect(150,200,700,400)
        fill(0)
        textSize(80)
        text("Hint",425,120)
        fill(255,0,0)
        
        #writing down the hint for question 4
        rect(150,200,700,100)
        fill(255)
        textSize(30)
        text("Incorrect Answer",400,250)
        fill(0)
        text("Hint: For loops repeat a certain amount of times according to the range or when the number of repetitions is specified in advance.",200,350,590,200)
        fill(0)
        text("Note: While loops are best used when the range isn't specified",200,480,590,300)
        fill(255)
        noStroke()
        
        #creating a redo button so user can redo question after getting it wrong
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
            
        #creating a next question so they can go to the next question
        image(butw,735,610,275,120)
        rect(755,650,225,50)
        fill(0)
        text("Next Question(n)",800,685)
        
        #creatin a timer in hint 4
        fill(255)
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 5"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores2=scores2-30
            scores-=30
            #resettng timer
            start=millis()-start
            time=25
            duration=25
            start=millis()
            #setting and adding time scores if time == 0
            q4time=0
            q4time=25-q4time
            times2=times2+q4time
            q5time=0
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
            
    #drawing the page for question 5
    elif page=="Question 5":
        #playing background music
        if time<=23:
            qmusic.play()
        #background image and details of the page
        image(ima,0,0)
        image(five,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:Two",50,150)
        
        #writing the question(5)
        stroke(0)
        fill(255)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 5: How do you find the index in a list?",120,250,800,300)
            
        #drawing the multiple choices
        #drawing choice one
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)list.find(search)",125,425,350,450)
        
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)list.findindex(search)",625,425,350,450)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)list.index(search)",125,595,350,675)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)list.add(search)",625,615)
            
        #drawing exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
            
        #drawing Welcome button, so user can return to homepage
        image(but,60,645,250,120)
        fill(255)
        text("Homepage(w)",200/2,720)
        noStroke()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #creatin a timer in question 5
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 6"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores2=scores2-30
            scores-=30
            #resettng timer
            start=millis()-start
            time=25
            duration=25
            start=millis()
            #setting and adding time scores if time == 0
            q5time=0
            q5time=25-q5time
            times2=times2+q5time
            q6time=0
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
    #drawing the hint page for question 5
    elif page=="Hint5":
        #drawing the hint for question 5
        #background image and thge title of the page
        image(mos,-20,0)
        stroke(0)
        fill(255)
        rect(150,200,700,400)
        textSize(80)
        fill(0)
        text("Hint",425,120)
        fill(255,0,0)

        #writing down the hint for question 5
        rect(150,200,700,100)
        fill(255)
        textSize(30)
        text("Incorrect Answer",400,250)
        fill(0)
        textSize(30)
        text("Hint: Find only works when you are looking for something in a string",200,350,550,200)
        fill(0)
        text("Note: When looking for an index and the index isn't in the list, it'll return as a syntax error",200,450,470,450)
        noStroke()
        fill(255)
            
        #creating a redo button so user can redo question after getting it wrong
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
            
        #creating a next question so they can go to the next question
        image(butw,735,610,275,120)
        fill(0)
        text("Next Question(n)",800,685)
        
        #creatin a timer in hint 5
        fill(255)
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 6"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores2=scores2-30
            scores-=30
            #resettng timer
            start=millis()-start
            time=25
            duration=25
            start=millis()
            #setting and adding time scores if time == 0
            q5time=0
            q5time=25-q5time
            times2=times2+q5time
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
            
    #making the page for question 6
    elif page=="Question 6":
        #playing background music
        if time<=23:
            qmusic.play()
        image(ima,0,0)
        image(six,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:Two",50,150)
            
        #drawing question
        stroke(0)
        fill(255)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 6: What's the code to open a file and write in it?",125,250,700,300)
            
        #drawing the multiple choices
        #drawing choice one
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)open(filename,w)",125,455)
            
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)x=open(w)",625,455)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)x=open('w','filename')",125,615)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)x=open('filename','w')",625,615)
        
        #drawing exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
            
        #drawing Welcome button, so user can return to homepage
        image(but,60,645,250,120)
        fill(255)
        text("Homepage(w)",200/2,720)
        noStroke()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #creatin a timer in question 6
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            #adding scores
            scores2=scores2-30
            scores-=30
            #setting and adding time scores if time == 0
            q6time=0
            q6time=25-q6time
            times2=times2+q6time
            tottimes+=times2
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
            page="Results1"
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
    
    #drawing the hitn page for question 6
    elif page=="Hint6":
            
        #drawing the hint for question 6
        #background image and details
        image(mos,-20,0)
        fill(255)
        stroke(0)
        rect(150,200,700,400)
        textSize(80)
        fill(0)
        text("Hint",425,150)
        fill(255,0,0)
            
        #writing down the hint for question 6
        rect(150,200,700,100)
        fill(255)
        textSize(30)
        text("Incorrect Answer",400,250)
        fill(0)
        textSize(30)
        text("Hint:The filename and the w should be in quotations",200,350,500,200)
        fill(0)
        text("Note:You can also find a sum of something using a for loop, instead of using a function",200,435,460,300)
        noStroke()
            
        #creating a redo button so user can redo question after getting it wrong
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
            
        #creating a results button so they can see the results of level 2
        image(butw,735,610,275,120)
        fill(0)
        text("Results(c)",800,685)
        
        #creatin a timer in hint 6
        fill(255)
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            #adding scores
            scores2=scores2-30
            scores-=30
            #setting and adding time scores if time == 0
            q6time=0
            q6time=25-q6time
            times2=times2+q6time
            tottimes+=times2
            page="Results1"
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #drawing the results of level 2
    elif page=="Results1":
        countdown.pause()
        #pausing music
        qmusic.pause()
        #background image and titel of the page
        image(mos,-20,0)
        fill(0)
        textSize(80)
        text("Results",375,100)
        fill(255)
        stroke(0)
        rect(150,150,700,400)
        fill(0)
        textSize(30)
        
        #writing in the scores and results for level 2
        text("Score="+str(scores),200,220)
        text("Score for Level 2="+str(scores2),200,270)
        text("Time for level 2="+str(times2),200,370)
        text("Time score="+str(tottimes),200,320)
         #writing if they tied, got higher or lesser than quickest time for level two
        if int(l2time)<int(times2):
            quixck2=times2-l2time
            text("Your time score is "+str(quixck2)+" seconds slower than the quickest time score for level two",200,450,650,450)
        elif int(l2time)>int(times2):
            highertim2=l2time-times2
            text("Your time score is "+str(highertim2)+" seconds faster than the quickest time score for level one",200,450,650,450)
        elif int(l2time)==int(times2):
            text("Your in tie with the time score, "+str(l2time)+", for level one",200,450,650,450)
        #writing if their score for level one is higher, lower or in tie with the highscore for level one
        if int(scores2)<int(high2):
            low2=high2-scores2
            text("Your score is "+str(low2)+" less than the highscore for level two",200,420)
        elif int(scores2)>int(high2):
            higher2=scores2-high2
            text("Your score is "+str(higher2)+" higher than the highscore for level two",200,420)
        elif int(scores2)==int(high2):
            text("Your in tie with the highscore, "+str(high2)+", for level two",200,420)
        noStroke()
        
        #button to go to the homepage
        image(but,60,600,250,120)
        textSize(20)
        fill(255)
        text("Homepage(w)",125,675)
        
        #a button so the user can leave the game
        image(but,735,600,250,120)
        fill(255)
        text("Exit(q)",840,675)
        
         # a button so they can start level 3
        image(but,380,600,250,120)
        fill(255)
        text("Level 3(f)",480,675)
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
         #starting level 3   
    elif page=="Level Three":
        #background image and details
        image(mos,-20,0)
        
        #reference for animations
        #Title:Introduction to Processing: Simple Animation
        #Author: Stevie Dickie
        #Date: 22 July 2011
        #Code Version: 2.2.1
        #Availability: https://www.youtube.com/watch?v=jLuMjfxgBpc
        
         #adding an image
        image(scrib3,275,-25,449,880)
            
        #animation image    
        image(q,50,qy,200,200) 
        
        #animation details
        frameRate(200)
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,250,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,450,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
         #animation image    
        image(q,650,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
        #animation image    
        image(q,850,qy,200,200) 
        
        #animation details
        qy=qy+1
        if (qy > height):
            qy = -110
            
        #animation image    
        image(scribqw,-50,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,150,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,350,yq,200,200) 
        
       #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
         #animation image    
        image(scribqw,550,yq,200,200) 
        
        #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
            
        #animation image    
        image(scribqw,750,yq,200,200) 
        
         #animation details
        yq=yq-1
        if (yq < -110):
            yq = height+110
        fill(255)
        textSize(80)
        text("Level Three",375,350)
        
       #creating a button so they can start level three
        image(but,60,620,250,120)
        textSize(20)
        fill(255)
        text("Start(s)",155,690)
            
        #creating a button so they can return to homepage
        image(butw,710,620,250,120)
        fill(0)
        text("Homepage(w)",780,690)
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
    
    #creating a page for question 7
    elif page=="Question 7":
        #playing background music
        qmusic.play()
        
        #background image and details of the page
        image(ima,0,0)
        image(seven,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:Three",50,150)
        
        #writing the question(7)
        stroke(0)
        fill(255)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 7: What does the function .strip() do",120,250,800,300)
        
        #drawing the multiple choices
        #drawing choice one
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)Takes out the tab characters",125,455)
            
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)Takes out the escape characters",625,455)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)Puts the files into a list",125,615)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)Takes out the comments",625,595,650,700)
            
        #drawing exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
            
        #drawing Welcome button, so user can return to homepage
        image(but,60,645,250,120)
        fill(255)
        text("Homepage(w)",200/2,720)
        noStroke()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #creatin a timer in question 7
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 8"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores3=scores3-35
            scores-=35
            #resettng timer
            start=millis()-start
            time=20
            duration=20
            start=millis()
            #setting and adding time scores if time == 0
            q7time=0
            q7time=20-q7time
            times3=times3+q7time
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
    #drawing the hint page for question 7
    elif page=="Hint7":
    #drawing the hint for question 7
        #background image and title of the page
        image(mos,-20,0)
        fill(255)
        stroke(0)
        rect(150,200,700,400)
        fill(0)
        textSize(80)
        text("Hint",425,120)
        fill(255,0,0)
        
        #writing down the hint for question 7
        rect(150,200,700,100)
        fill(255)
        textSize(30)
        text("Incorrect Answer",400,250)
        fill(0)
        text("Hint: It takes out one of the special characters",200,350,500,200)
        fill(0)
        text("Note: You can use .split() to assign different parts of a string to multiple variables ",200,430,490,500)
        fill(255)
        noStroke()
        
        #creating a redo button so user can redo question after getting it wrong
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
            
        #creating a next question so they can go to the next question
        image(butw,735,610,275,120)
        fill(0)
        text("Next Question(n)",800,685)
        
        #creatin a timer in hint 7
        fill(255)
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 8"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores3=scores3-35
            scores-=35
            #resettng timer
            start=millis()-start
            time=20
            duration=20
            start=millis()
            q7time=0
            q7time=20-q7time
            times3=times3+q7time
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
            
    #drawing the page for question 5
    elif page=="Question 8":
        #playing background music
        if time<=18:
            qmusic.play()
            
        #adding background details and details of the page
        image(ima,0,0)
        image(eight,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:Three",50,150)
        
        #writing the question(8)
        stroke(0)
        fill(255)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 8:What is needed before the function .join() in order to use it?",120,250,800,300)
            
        #drawing the multiple choices
        #drawing choice one
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)List of tokens",125,425,350,450)
        
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)Search",625,425,350,450)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)Delimiters",125,590,350,675)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)Variables",625,615)
            
        #drawing exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
            
        #drawing Welcome button, so user can return to homepage
        image(but,60,645,250,120)
        fill(255)
        text("Homepage(w)",200/2,720)
        noStroke()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #creatin a timer in question 8
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 9"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores3=scores3-35
            scores-=35
            #resettng timer
            start=millis()-start
            time=20
            duration=20
            start=millis()
            q8time=0
            #settting and addding time scores if time==0
            q8time=20-q8time
            times3=times3+q8time
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
    #drawing the hint page for question 8
    elif page=="Hint8":
        #drawing the hint for question 8
        #background image and title of the page
        image(mos,-20,0)
        fill(255)
        stroke(0)
        rect(150,200,700,400)
        fill(0)
        textSize(80)
        text("Hint",425,120)
        fill(255,0,0)
            
        #writing down the hint for question 8
        rect(150,200,700,100)
        fill(255)
        textSize(30)
        text("Incorrect Answer",400,250)
        fill(0)
        textSize(30)
        text("Hint: The boundary between separate, independent regions in text or other data streams is specified using a sequence of one or more characters .",200,350,600,500)
        fill(0)
        text("Note: List of tokens are the strings joined by the function .join()",200,490,600,500)
        fill(255)
        noStroke()
            
        #creating a redo button so user can redo question after getting it wrong
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
        
         #creating a next question button 
        image(butw,735,610,275,120)
        fill(0)
        text("Next Question(n)",800,685)
        
        #creatin a timer in hint 8
        fill(255)
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            page="Question 9"
            #rewinding sound
            qmusic.rewind()
            qmusic.play()
            #adding scores
            scores3=scores3-35
            scores-=35
            #resettng timer
            start=millis()-start
            time=20
            duration=20
            start=millis()
            #settting and addding time scores if time==0
            q8time=0
            q8time=20-q8time
            times3=times3+q8time
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
            
    #creating a page for question 9
    elif page=="Question 9":
        #playing background music
        if time<=18:
            qmusic.play()
            
        image(ima,0,0)
        image(nine,475,100)
        textSize(20)
        fill(255)
        text("Grade:10",50,50)
        text("Subject:Computer Science",50,100)
        text("Level:Three",50,150)
            
        #writing the question(9)
        stroke(0)
        fill(255)
        rect(80,210,900,150)
        fill(0)
        textSize(30)
        text("Question 9:Which of the following is not used when opeing a file?",125,250,700,30)
            
        #drawing the multiple choices
        #drawing choice one
        fill(255)
        rect(80,390,400,100)
        fill(0)
        textSize(30)
        text("(1)x=open('filename','w')",125,455)
            
        #drawing choice 2
        fill(255)
        rect(580,390,400,100)
        fill(0)
        text("(2)x=open('filename','r')",625,455)
            
        #drawing choice 3
        fill(255)
        rect(80,550,400,100)
        fill(0)
        text("(3)x=open('filename','f')",125,615)
            
        #drawing choice 4
        fill(255)
        rect(580,550,400,100)
        fill(0)
        text("(4)x=open('filename','x')",625,615)
        
        #drawing exit button
        textSize(20)
        image(but,760,86,250,120)
        fill(255)
        text("Exit(q)",800,155)
            
        #drawing Welcome button, so user can return to homepage
        image(but,60,645,250,120)
        fill(255)
        text("Homepage(w)",200/2,720)
        noStroke()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #creatin a timer in question 9
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            #adding scores
            scores3=scores3-35
            scores-=35
            #settting and addding time scores if time==0
            q9time=0
            q9time=20-q9time
            times3=times3+q9time
            tottimes+=times3
            page="Results2"
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
    
    #drawing the hint page for question 9
    elif page=="Hint9":
            
        #drawing the hint for question 9
        #background image andthe title of the page
        image(mos,-20,0)
        fill(255)
        stroke(0)
        rect(150,200,700,400)
        fill(0)
        textSize(80)
        text("Hint",425,150)
        fill(255,0,0)
            
        #writing down the hint for question 9
        rect(150,200,700,100)
        fill(255)
        textSize(30)
        text("Incorrect Answer",400,250)
        fill(0)
        textSize(30)
        text("Hint:When opening a file you can read, write, create, and append",200,350,550,200)
        fill(0)
        text("Note: When using write when opening a file it overwrites the file",200,430,450,300)
        noStroke()
            
        #creating a redo button so user can redo question after getting it wrong
        image(but,50,610,275,120)
        textSize(20)
        fill(255)
        text("Redo(r)",150,685)
            
        #creating a next question so they can go to the next question
        image(butw,735,610,275,120)
        fill(0)
        text("Results(c)",800,685)
        
        #creatin a timer in hint 9
        fill(255)
        image(but,760,20,250,120)
        if (time > 0):  
            time = duration - (millis() - start)/1000
            text("Timer: "+str(time), 800, 88)
            int(time)
        elif time==0:
            #adding scores
            scores3=scores3-35
            scores-=35
            q9time=0
            q9time=20-q9time
            times3=times3+q9time
            tottimes+=times3
            page="Results2"
            #playing a sound when time is up
            wrong.rewind()
            wrong.play()
        if time==6:
            # playing a sound that tells them there is 5 seconds left
            countdown.rewind()
            countdown.play()
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
        #drawing the results of level 3
    elif page=="Results2":
        countdown.pause()
        #pausig music
        qmusic.pause()
        #background image and details
        image(mos,-20,0)
        fill(0)
        textSize(80)
        text("Results",375,100)
        fill(255)
        stroke(0)
        rect(150,150,700,430)
        fill(0)
        textSize(27)
        #writing in the scores and the score for level 3
        text("Score="+str(scores),200,220)
        text("Score for Level 3="+str(scores3),200,270)
        text("Time score="+str(tottimes),200,320)
        text("Time for Level 3="+str(times3),200,370)
         #writing if they tied, got higher or lesser than quickest time for level two
        if int(l3time)<int(times3):
            quixck3=times3-l3time
            text("Your time score is "+str(quixck3)+" seconds slower than the quickest time score for level three",200,500,650,500)
        elif int(l3time)>int(times3):
            highertim3=l3time-times3
            text("Your time score is "+str(highertim3)+" seconds faster than the quickest time score for level three",200,500,650,500)
        elif int(l3time)==int(times3):
            text("Your in tie with the time score, "+str(l3time)+", for level three",200,500,650,500)
        #writing if their score for level one is higher, lower or the same as the highscore for level 3
        if int(scores3)<int(high3):
            low3=high3-scores3
            text("Your score is "+str(low3)+" points less than the highscore for level three",200,420)
        elif int(scores3)>int(high3):
            higher3=scores3-high3
            text("Your scores is "+str(higher3)+" points higher than the highscore for level three",200,420)
        elif int(scores3)==int(high3):
            text("Your in tie with the highscore, "+str(high3)+", for level three",200,420)
        if int(scores)<int(highscore):
            scorer=highscore-scores
            text("Your score is "+str(scorer)+" points less than the highscore",200,470)
        elif int(scores)>int(highscore):
            scoring=scores-highscore
            text("Your score is "+str(scoring)+" points higher than the highscore",200,470)
        elif int(scores3)==int(high3):
            text("Your in tie with the highscore, "+str(highscore),200,470)
        noStroke()
        
        #button to go to the homepage
        image(but,60,600,250,120)
        textSize(20)
        fill(255)
        text("Homepage(w)",125,675)
        
        #a button so the user can leave the game
        image(but,735,600,250,120)
        fill(255)
        text("Exit(q)",840,675)
        
          #making a question mark follow the cursor
        image(s, mouseX,mouseY,50,50)
        
def mouseClicked():
    #make the variables i need global so I can use within this function
    global page
    global scores
    global highscore
    global high1
    global high2
    global high3
    global scores1
    global scores2
    global scores3
    global sf
    global wrong
    global time 
    global duration
    global q1time
    global q2time
    global q3time
    global times
    global q4time
    global q5time
    global q6time
    global times2
    global start
    global q7time
    global q8time
    global q9time
    global times3
    global tottimes
        
    #buttons for welcome page
    #start button
    if (mouseX>20 and mouseX<20+300 and mouseY>190 and mouseY<190+120 and page=="Welcome"):
        page="Level One"
        #setting up scores and time scores
        scores=0
        tottimes=0
        scores1=0
        times=0
    #highscore button
    elif (mouseX>20 and mouseX<20+300 and mouseY>295 and mouseY<295+120 and page=="Welcome"):
        page="Highscore"
    #exit/close button
    elif (mouseX>20 and mouseX<20+300 and mouseY>400 and mouseY<400+120 and page=="Welcome"):
        exit()
    #button to keys page
    elif (mouseX>20 and mouseX<20+300 and mouseY>505 and mouseY<505+120 and page=="Welcome"):
        page="Keys"
        #button to help page
    elif (mouseX>20 and mouseX<20+300 and mouseY>610 and mouseY<610+120 and page=="Welcome"):
        page="Help"
            
    #buttons in highscore page
    #hompage/welcome button to return to homepage from highscore page
    elif (mouseX>20 and mouseX<20+300 and mouseY>610 and mouseY<610+120 and page=="Highscore"):
        page="Welcome"
        
    #buttons in key page
    #button to return to welcome page
    elif (mouseX>20 and mouseX<20+300 and mouseY>610 and mouseY<610+120  and page=="Keys"):
        page="Welcome"
        
    #buttons in help page   
      #button to go back to homepage
    elif(mouseX>60 and mouseX<60+250 and mouseY>600 and mouseY<600+120 and page=="Help"):
        page="Welcome"
    #button to leave game
    elif (mouseX>735 and mouseX<735+250 and mouseY>600 and mouseY<600+120 and page=="Help"):
        exit()
    #button to start the quiz
    elif (mouseX>380 and mouseX<380+250 and mouseY>600 and mouseY<600+120 and page=="Help"):
        page="Level One"
        #setting up scores and time scores
        times=0
        scores=0
        scores1=0
        tottimes=0
            
    #buttons in Level pages
    #button to start level one
    #start button for question 1
    #Reference for sounds
    #Title: How to get sound files in processing.py
    #Author: Netrate
    #Date: August 2017
    #Code Version: 2.2.1
    #Availability: https://forum.processing.org/two/discussion/23738/how-to-get-sound-files-in-processing-py
    elif (mouseX>60 and mouseX<60+250 and mouseY>620 and mouseY<620+120 and page=="Level One"):
        page="Question 1"
        #rewinding the sound
        qmusic.rewind()
        #setting up scores and time scores
        scores1=0
        q1time=0
        
        #Title: Time Reset
        #Author: printIn_h...
        #Date: March 2021
        #Code Version: 3.5.4
        #Availability: https://forum.processing.org/one/topic/time-reset.html#:~:text=Re%3A%20Time%20reset&text=There%20is%20no%20way%20to%20reset%20the%20millis%20timer.
        
        #resetting timer
        start=millis()-start
        time=30
        duration=30
        #setting time scores and scores for question 1
        scores=0
        scores1=0
        times=0
        start=millis()
    #to go to the homepage from level 1 page
    elif (mouseX>710 and mouseX<710+250 and mouseY>620 and mouseY<620+120 and page=="Level One"):
        page="Welcome"
    #buttons for level two
     #start button for question 4 and start button of level 2
    elif (mouseX>60 and mouseX<60+250 and mouseY>620 and mouseY<620+120 and page=="Level Two"):
        page="Question 4"
        #rewinding the sound
        qmusic.rewind()
        #resetting timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        #setting time scores and scores for question 4
        scores2=0
        q4time=0
        times2=0
    #to go to the homepage from level 2 page
    elif (mouseX>710 and mouseX<710+250 and mouseY>620 and mouseY<620+120 and page=="Level Two"):
        page="Welcome"
    #buttons for level 3
    #start button for level 3 nd question 7
    elif (mouseX>60 and mouseX<60+250 and mouseY>620 and mouseY<620+120 and page=="Level Three"):
        page="Question 7"
        #rewinding the sound
        qmusic.rewind()
        #resetting timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        #setting up time scores and scores for question5
        scores3=0
        q7time=0
        times3=0
    #to go to the homepage from level 3 page
    elif (mouseX>710 and mouseX<710+250 and mouseY>620 and mouseY<620+120 and page=="Level Three"):
        page="Welcome"

        
    #buttons for question 1
    #button to exit on question 1 if they want to stop doing the quiz
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 1"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 1"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(parameters) is clicked in question 1
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 1"):
        #rewinding the sound
        qmusic.rewind()
        #resetting my sounds
        sf.rewind()
        sf.play()
        #adding their time scores from question 1
        q1time=time
        q1time=30-q1time
        times=times+q1time
        q2time=0
        #their scores if they get it right
        scores1=100-(3.3*q1time)
        scores+=100-(3.3*q1time)
        #resetting timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        page="Question 2"
        countdown.pause()
        qmusic.pause()
    #button to show what will happen when choice 2(lists) is clicked in question 1
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 1"):
        #setting scores if they get it wrong
        scores1=scores1-25
        scores=scores-0
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint1"
    #button to show what will happen when choice 3(numbers) is clicked in question 1
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 1"):
        #scores if they get it wrong
        scores1=scores1-25
        scores-=0
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint1"
    #button to show what will happen when choice 4(docstring) is clicked in question 1
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 1"):
        #scores if they get it wrong
        scores1=scores1-25
        scores-=0
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint1"
        
    #buttons in hint pages
    #redo button for question 1
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint1"):
        page="Question 1"
    #to go to the next question(question 2)
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint1"):
        page="Question 2"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        #Their time score if they go to the next question
        q1time=30
        times=times+q1time
        q2time=0
        countdown.pause()
        qmusic.pause()
    #redo button for question 2
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint2"):
        page="Question 2"
    #to go to the next question(question 3)
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint2"):
        page="Question 3"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        #Their time score if they go to the next question
        q2time=30
        times=times+q2time
        q3time=0
        countdown.pause()
        qmusic.pause()
    #redo button for question 3
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint3"):
        page="Question 3"
    #to go to the results of level one
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint3"):
        page="Results"
        #rewinding the sound
        qmusic.rewind()
        #Their time score if they go to the results page and skip the question
        q3time=30
        times=times+q3time
        tottimes+=times
        scores=scores-25
    #to redo question 4
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint4"):
        page="Question 4"
    #to go to the next question(question 5)
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint4"):
        page="Question 5"
        #rewinding the sound
        qmusic.rewind()
        #resetting timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        #Their time score if they go to the next question
        q4time=25
        times2=times2+q4time
        q5time=0
        countdown.pause()
        qmusic.pause()
    #to redo question 5
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint5"):
        page="Question 5"
    #to go to the next question(question 6)
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint5"):
        page="Question 6"
        #rewinding the sound
        qmusic.rewind()
        #resetting timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        #Their time score if they go to the next question
        q5time=25
        times2=times2+q5time
        q6time=0
        countdown.pause()
        qmusic.pause()
    #to redo question 6
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint6"):
        page="Question 6"
    #to go to the results for end of level 2
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint6"):
        page="Results1"
        #rewinding the sound
        qmusic.rewind()
        #their time scores and scores if they go to the results page and skip the questions
        q6time=25
        times2=times2+q6time
        tottimes+=times2
        scores2=scores2-30
        scores=scores-30
      #to redo question 7
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint7"):
        page="Question 7"
    #to go to the next question(question 8)
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint7"):
        page="Question 8"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        #their time score if they go to the next question
        q7time=20
        times3=times3+q7time
        q8time=0
        countdown.pause()
        qmusic.pause()
    #to redo question 8
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint8"):
        page="Question 8"
    #to go to the next question (question 9)
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint8"):
        page="Question 9"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        #their time scores if they go to the next question
        q8time=20
        times3=times3+q8time
        q9time=0
        countdown.pause()
        qmusic.pause()
    #to redo question 9
    elif (mouseX>50 and mouseX<50+275 and mouseY>610 and mouseY<610+120 and page=="Hint9"):
        page="Question 9"
    #to go to the results page for the end of level 3
    elif (mouseX>735 and mouseX<735+275 and mouseY>610 and mouseY<610+120 and page=="Hint9"):
        page="Results2"
        #rewinding the sound
        qmusic.rewind()
        #their time scores and scores if they go to the results page and skip the questions
        q9time=25
        times3=times3+q9time
        tottimes+=times3
        scores3=scores3-35
        scores=scores-35
        
    #buttons in question 2
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 2"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 2"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(says what the function does) is clicked in question 2
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 2"):
        scores1=scores1-25
        scores-=25
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint2"
    #button to show what will happen when choice 2(Indicates the start of a function definition) is clicked in question 2
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 2"):
        #rewinding the sound
        qmusic.rewind()
        #resetting the sound
        sf.rewind()
        sf.play()
        #adding their time scores
        q2time=time
        q2time=30-q2time
        times=times+q2time
        q3time=0
        #scors if they get the right answer
        scores1+=100-(3.3*q2time)
        scores+=100-(3.3*q2time)
        #restting timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        page="Question 3"
        countdown.pause()
        qmusic.pause()
    #button to show what will happen when choice 3(is shown to tell us a function is done) is clicked in question 2
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 2"):
        scores1=scores1-25
        scores-=25
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint2"
    #button to show what will happen when choice 4(Used to add) is clicked in question 2
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 2"):
        scores1=scores1-25
        scores-=25
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint2"
            
    #buttons in question 3
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 3"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 3"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(parameters) is clicked in question 3
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 3"):
        scores1=scores1-25
        scores-=25
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint3"
    #button to show what will happen when choice 2(arguments) is clicked in question 3
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 3"):
        scores1=scores1-25
        scores-=25
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint3"
    #button to show what will happen when choice 3(return) is clicked in question 3
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 3"):
        scores1=scores1-25
        scores-=25
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint3"
    #button to show what will happen when choice 4(docstring) is clicked in question 3
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 3"):
        #rewinding the sound
        qmusic.rewind()
        #resetting sounds
        sf.rewind()
        sf.play()
        #adding time scores
        q3time=time
        q3time=30-q3time
        times=times+q3time
        #adding their scores if they get the answer right
        scores1+=100-(3.3*q3time)
        scores+=100-(3.3*q3time)
        tottimes+=times
        qmusic.pause()
        page="Results"
            
    #button in results page 1
    #button to go back to homepage
    elif(mouseX>60 and mouseX<60+250 and mouseY>600 and mouseY<600+120 and page=="Results"):
        page="Welcome"
    #button to leave game
    elif (mouseX>735 and mouseX<735+250 and mouseY>600 and mouseY<600+120 and page=="Results"):
        exit()
    #button to start level 2
    elif (mouseX>380 and mouseX<380+250 and mouseY>600 and mouseY<600+120 and page=="Results"):
        page="Level Two"
    
    #buttons in question 4
     #button to exit on question 4 if they want to stop doing the quiz
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 4"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 4"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(definite iterations) is clicked in question 4
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 4"):
        #rewinding the sound
        qmusic.rewind()
        #resetting sounds
        sf.rewind()
        sf.play()
        #setting and adding time scores
        q4time=time
        q4time=25-q4time
        times2=times2+q4time
        q5time=0
        #adding their scores if they are right
        scores2+=100-(4*q4time)
        scores+=100-(4*q4time)
        #resetting timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        page="Question 5"
        qmusic.pause()
    #button to show what will happen when choice 2(Infinite Iterations) is clicked in question 4
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 4"):
        scores2=scores2-30
        scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint4"
    #button to show what will happen when choice 3(List of iterations) is clicked in question 4
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 4"):
        scores2=scores2-30
        scores-=30
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint4"
    #button to show what will happen when choice 4(Numebr of iterations) is clicked in question 4
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 4"):
        scores2=scores2-30
        scores-=30
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint4"

    #buttons in question 5
     #button to exit on question 5 if they want to stop doing the quiz
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 5"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 5"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(list.find(search)) is clicked in question 5
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 5"):
        scores2=scores2-30
        scores-=30
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint5"
    #button to show what will happen when choice 2(list.findindex(search)) is clicked in question 5
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 5"):
        scores2=scores2-30
        scores-=30
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint5"
    #button to show what will happen when choice 3(list.index(search)) is clicked in question 5
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 5"):
        #rewinding the sound
        qmusic.rewind()
        #restting sounds
        sf.rewind()
        sf.play()
        #setting and adding time scores
        q5time=time
        q5time=25-q5time
        times2=times2+q5time
        q6time=0
        #adding scores
        scores2+=100-(4*q6time)
        scores+=100-(4*q6time)
        #resetting timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        qmusic.pause()
        page="Question 6"
    #button to show what will happen when choice 4(list.add(search)) is clicked in question 5
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 5"):
        scores2=scores2-30
        scores-=30
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint5"

      #buttons in question 6
     #button to exit on question 6 if they want to stop doing the quiz
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 6"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 6"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(open(filename,w)) is clicked in question 6
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 6"):
        #scores2=scores2-30
        #scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint6"
    #button to show what will happen when choice 2(x=open(w)) is clicked in question 6
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 6"):
        #scores2=scores2-30
        #scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint6"
    #button to show what will happen when choice 3(x=open('w','filename')) is clicked in question 6
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 6"):
        #scores2=scores2-30
        #scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint6"
    #button to show what will happen when choice 4(x='filename,'w')) is clicked in question 6
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 6"):
        #rewinding the sound
        qmusic.rewind()
        #resetting sounds
        sf.rewind()
        sf.play()
        #adding time scores
        q6time=time
        q6time=25-q6time
        times2=times2+q6time
        #$setting and adding scores
        scores2+=100-(4*q6time)
        scores+=100-(4*q6time)
        tottimes+=times2
        qmusic.pause()
        page="Results1"
        
     #button in results1 page results for level 2
    #button to go back to homepage
    elif(mouseX>60 and mouseX<60+250 and mouseY>600 and mouseY<600+120 and page=="Results1"):
        page="Welcome"
    #button to leave game
    elif (mouseX>735 and mouseX<735+250 and mouseY>600 and mouseY<600+120 and page=="Results1"):
        exit()
    #button to start level 3
    elif (mouseX>380 and mouseX<380+250 and mouseY>600 and mouseY<600+120 and page=="Results1"):
        page="Level Three"
    
     #buttons in question 7
     #button to exit on question 7 if they want to stop doing the quiz
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 7"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 7"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(takes out the tab cahracters) is clicked in question 7
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 7"):
        #scores3=scores3-35
        #scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint7"
    #button to show what will happen when choice 2(takes out the escape characters) is clicked in question 7
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 7"):
        #rewinding the sound
        qmusic.rewind()
        #resetting sounds
        sf.rewind()
        sf.play()
        #setting and adding time scores
        q7time=time
        q7time=20-q7time
        times3=times3+q7time
        q8time=0
        #Setting and adding scores
        scores3+=100-(5*q7time)
        scores+=100-(5*q7time)
        #resetting timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        page="Question 8"
        qmusic.pause()
    #button to show what will happen when choice 3(puts the files into a list is clicked in question 7
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 7"):
        #scores3=scores3-35
        #scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint7"
    #button to show what will happen when choice 4(takes out the comments) is clicked in question 7
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 7"):
        #scores3=scores3-35
        #scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint7"

      #buttons in question 8
     #button to exit on question 8 if they want to stop doing the quiz
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 8"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 8"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(list of tokens) is clicked in question 8
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 8"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint8"
    #button to show what will happen when choice 2(search) is clicked in question 8
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 8"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint8"
    #button to show what will happen when choice 3(delimiters) is clicked in question 8
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 8"):
        #rewinding the sound
        qmusic.rewind()
        #resetting sounds
        sf.rewind()
        sf.play()
        #adding and setting time scoress
        q8time=time
        q8time=20-q8time
        times3=times3+q8time
        q9time=0
        #Setting and adding scores
        scores3+=100-(5*q8time)
        scores+=100-(5*q8time)
        #setting timers
        start=millis()-start
        time=20
        duration=20
        start=millis()
        page="Question 9"
        qmusic.pause()
    #button to show what will happen when choice 4(variables) is clicked in question 8
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 8"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint8"
    
      #buttons in question 9
     #button to exit on question 9 if they want to stop doing the quiz
    elif (mouseX>775 and mouseX<775+200 and mouseY>120 and mouseY<120+50 and page=="Question 9"):
        exit()
    #button if they want to return to the hompage/welcome page during quiz
    elif (mouseX>80 and mouseX<80+200 and mouseY>685 and mouseY<685+50 and page=="Question 9"):
        page="Welcome"
        qmusic.pause()
    #button to show what will happen when choice 1(x=open('filename','f')) is clicked in question 9
    elif (mouseX>80 and mouseX<80+400 and mouseY>390 and mouseY<390+100 and page=="Question 9"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint9"
    #button to show what will happen when choice 2(x=open('filename','r')) is clicked in question 9
    elif (mouseX>580 and mouseX<580+400 and mouseY>390 and mouseY<390+100 and page=="Question 9"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint9"
     #button to show what will happen when choice 3(x=open('filename','f')) is clicked in question 9
    elif (mouseX>80 and mouseX<80+400 and mouseY>550 and mouseY<550+100 and page=="Question 9"):
        #rewinding the sound
        qmusic.rewind()
        #resetting sounds
        sf.rewind()
        sf.play()
        #adding and setting time scores
        q9time=time
        q9time=20-q9time
        times3=times3+q9time
        #Setting and adding scores
        scores3+=100-(5*q9time)
        scores+=100-(5*q9time)
        tottimes+=times3
        qmusic.pause()
        page="Results2"
    #button to show what will happen when choice 4(x=open('filename','x')) is clicked in question 1
    elif (mouseX>580 and mouseX<580+400 and mouseY>550 and mouseY<550+100 and page=="Question 9"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint9"
        
    #button in results page 3
    #button to go back to homepage
    elif(mouseX>60 and mouseX<60+250 and mouseY>600 and mouseY<600+120 and page=="Results2"):
        page="Welcome"
    #button to leave game
    elif (mouseX>735 and mouseX<735+250 and mouseY>600 and mouseY<600+120 and page=="Results2"):
        exit()
        
#Making a key pressed function so this quiz can also be done using a keyboard
def keyPressed():
    global page
    global scores
    global highscore
    global high1
    global high2
    global high3
    global scores1
    global scores2
    global scores3
    global time
    global duration
    global start
    global q1time
    global q2time
    global q3time
    global times
    global q4time
    global q5time
    global q6time
    global times2
    global start
    global q7time
    global q8time
    global q9time
    global times3
    global tottimes
    
    #keys on homepage
    #Keys for start button
    if (key=="s" and page=="Welcome"):
        page="Level One"
        #setting time scores  and scores
        times=0
        scores=0
        scores1=0
        tottimes=0
    #Keys for highscore button
    elif (key=="h" and page=="Welcome"):
        page="Highscore"
    #Keys for quit button
    elif (key=="q" and page=="Welcome"):
        exit()
    elif (key=="k" and page=="Welcome"):
        page="Keys"
    elif (key=="p" and page=="Welcome"):
        page="Help"
        
    #keys in highscore pages
    #welcome page button
    elif (key=="w" and page=="Highscore"):
        page="Welcome"
        
    #keys in keys page
     #welcome page button
    elif (key=="w" and page=="Keys"):
        page="Welcome"
        
    #keys in help page
    #keys to go to welcome page
    elif (key=="w" and page=="Help"):
        page="Homepage"
    #key to go to leave game
    elif (key=="q" and page=="Help"):
        exit()
    #key to start level one 
    elif (key=="s" and page=="Help"):
        page="Level One"
        #setting time scores and scores
        times=0
        scores=0
        scores1=0
        tottimes=0
                
    #keys in all the level pages
    #keys in level one
    #start level one
    elif (key=="s" and page=="Level One"):
        #rewinding the sound
        qmusic.rewind()
        #setting up time scores
        q1time=0
        times=0
        #resetting timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        #setting scores
        scores=0
        scores1=0
        page="Question 1"
    #go back to the welcome page
    elif (key=="w" and page=="Level One"):
        page="Welcome"
    #keys in level two
    #key to start level two
    elif (key=="s" and page=="Level Two"):
        #rewinding the sound
        qmusic.rewind()
        #setting time scores
        q4time=0
        times2=0
        #settting scores
        scores2=0
        #resetting timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        page="Question 4"
    #key to go back to the welcome page
    elif (key=="w" and page=="Level Two"):
        page="Welcome"
    #keys in level three
    #key to start level three
    elif (key=="s" and page=="Level Three"):
        #rewinding the sound
        qmusic.rewind()
        #setting time scores
        q7time=0
        times3=0
        #setting scores
        scores3=0
        #resetting timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        page="Question 7"
    #key to go to the welcome page
    elif (key=="w" and page=="Level Three"):
        page="Welcome"
        
    #keys in question 1
    #exit key on question 1 page
    elif (key=="q" and page=="Question 1"):
        exit()
    #homepage key in question 1 page
    elif (key=="w" and page=="Question 1"):
        page="Welcome"
        qmusic.pause()
    #key to press for choice 1 in question 1 
    elif (key=="1" and page=="Question 1"):
        #rewinding the sound
        qmusic.rewind()
        #Setting  and adding up time scores 
        q1time=time
        q1time=30-q1time
        times=times+q1time
        q2time=0
        #adding their scores if they get it right
        scores1+=100-(3.3*q1time)
        scores+=100-(3.3*q1time)
        #resettting soumds
        sf.rewind()
        sf.play()
        #resetting timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        page="Question 2"
        qmusic.pause()
    #key to press for choice 2 in question 1
    elif (key=="2" and page=="Question 1"):
        scores1=scores1-25
        scores-=25
        #resetting the sounds
        wrong.rewind()
        wrong.play()
        page="Hint1"
    #key to press for choice 3 in question 1
    elif (key=="3" and page=="Question 1"):
        scores1=scores1-25
        scores-=25
        #resetting the sounds
        wrong.rewind()
        wrong.play()
        page="Hint1"
    #button for choice 4 in question 1
    elif (key=="4" and page=="Question 1"):
        scores1=scores1-25
        scores-=25
        #restting the soynds
        wrong.rewind()
        wrong.play()
        page="Hint1"
        
    #keys in question 2
    #exit key on question 2 page
    elif (key=="q" and page=="Question 2"):
        exit()
    #homepage key in question 2 page
    elif (key=="w" and page=="Question 2"):
        page="Welcome"
        qmusic.pause()
    #key to press for choice 1 in question 2 
    elif (key=="1" and page=="Question 2"):
        scores1=scores1-25
        scores-=25
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint2"
    #key to press for choice 2 in question 2
    elif (key=="2" and page=="Question 2"):
        #rewinding the sound
        qmusic.rewind()
        #setting and adding time scores
        q2time=time
        q2time=30-q2time
        times=times+q2time
        q3time=0
        #settin up and adding scores
        scores1+=100-(3.3*q2time)
        scores+=100-(3.3*q2time)
        #restting sounds
        sf.rewind()
        sf.play()
        #restting timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        page="Question 3"
        qmusic.pause()
    #key to press for choice 3 in question 2
    elif (key=="3" and page=="Question 2"):
        scores1=scores1-25
        scores-=25
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint2"
    #key to press for choice 4 in question 2
    elif (key=="4" and page=="Question 2"):
        scores1=scores1-25
        scores-=25
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint2"
        
    #keys in question 3
    #exit key on question 3 page
    elif (key=="q" and page=="Question 3"):
        exit()
    #homepage key in question 3 page
    elif (key=="w" and page=="Question 3"):
        page="Welcome"
        qmusic.pause()
    #key to press for choice 1 in question 3 
    elif (key=="1" and page=="Question 3"):
        scores1=scores1-25
        scores-=25
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint3"
    #key to press for choice 2 in question 3
    elif (key=="2" and page=="Question 3"):
        scores1=scores1-25
        scores-=25
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint3"
    #key to press for choice 3 in question 3
    elif (key=="3" and page=="Question 3"):
        scores1=scores1-25
        scores-=25
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint3"
    #key to press for choice 4 in question 3
    elif (key=="4" and page=="Question 3"):
        #rewinding the sound
        qmusic.rewind()
        #settting and adding times scores
        q3time=time
        q3time=30-q3time
        times=times+q3time
        tottimes+=times
        #setting up scores
        scores1+=100-(3.3*q3time)
        scores+=100-(3.3*q3time)
        #restting sounds
        sf.rewind()
        sf.play()
        qmusic.pause()
        page="Results"
        
    #keys in results page for level one
    #key to press to go back to welcome page
    elif (key=="w" and page=="Results"):
        page="Welcome"
    #key to press to exit the game
    elif (key=="q" and page=="Results"):
        exit()
    #key to start level 2
    elif (key=="f" and page=="Results"):
        page="Level Two"
        
    #keys in question 4
    #exit key on question 4 page
    elif (key=="q" and page=="Question 4"):
        exit()
    #homepage key in question 4 page
    elif (key=="w" and page=="Question 4"):
        page="Welcome"
        qmusic.pause()
    #key to press for choice 1 in question 4 
    elif (key=="1" and page=="Question 4"):
        #rewinding the sound
        qmusic.rewind()
        #setting time scores 
        q4time=time
        q4time=25-q4time
        times2=times2+q8time
        q9time=0
        #setting scores
        scores2+=100-(4*q4time)
        scores+=100-(4*q4time)
        #resetting sounds
        sf.rewind()
        sf.play()
        #restting timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        page="Question 5"
        qmusic.pause()
    #key to press for choice 2 in question 4
    elif (key=="2" and page=="Question 4"):
        scores2=scores2-30
        scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint4"
    #key to press for choice 3 in question 4
    elif (key=="3" and page=="Question 4"):
        scores2=scores2-30
        scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint4"
    #key to press for choice 4 in question 4
    elif (key=="4" and page=="Question 4"):
        scores2=scores2-30
        scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint4"
        
    #keys in question 5
    #exit key on question 5 page
    elif (key=="q" and page=="Question 5"):
        exit()
    #homepage key in question 5 page
    elif (key=="w" and page=="Question 5"):
        page="Welcome"
        qmusic.pause()
    #key to press for choice 1 in question 5 
    elif (key=="1" and page=="Question 5"):
        scores2=scores2-30
        scores-=30
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint5"
    #key for choice 2 in question 5
    elif (key=="2" and page=="Question 5"):
        scores2=scores2-30
        scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint5"
    #key to press for choice 3 in question 5
    elif (key=="3" and page=="Question 5"):
        #rewinding the sound
        qmusic.rewind()
        #setting times
        q5time=time
        q5time=25-q5time
        times2=times2+q5time
        q6time=0
        #setting scores
        scores2+=100-(4*q5time)
        scores+=100-(4*q5time)
        #restting sounds
        sf.rewind()
        sf.play()
        #restting timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        page="Question 6"
        qmusic.pause()
    #key to press for choice 4 in question 5
    elif (key=="4" and page=="Question 5"):
        scores2=scores2-30
        scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint5"
        
    #keys in question 6
    #exit key on question 6 page
    elif (key=="q" and page=="Question 6"):
        exit()
    #homepage key in question 6 page
    elif (key=="w" and page=="Question 6"):
        page="Welcome"
        qmusic.pause()
    #key to press for choice 1 in question 6 
    elif (key=="1" and page=="Question 6"):
        scores2=scores2-30
        scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint6"
    #key to press for choice 2 in question 6
    elif (key=="2" and page=="Question 6"):
        scores2=scores2-30
        scores-=30
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint6"
    #key to press for choice 3 in question 6
    elif (key=="3" and page=="Question 6"):
        scores2=scores2-30
        scores-=30
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint6"
    #key to press for choice 4 in question 6
    elif (key=="4" and page=="Question 6"):
        #rewinding the sound
        qmusic.rewind()
        #setting time scores
        q6time=time
        q6time=25-q6time
        times2=times2+q6time
        #setting and adding scores
        scores2+=100-(4*q6time)
        scores+=100-(4*q6time)
        #resetting sounds
        sf.rewind()
        sf.play()
        page="Results1"
        qmusic.pause()
        
  #keys in results page for level two
  #key to press to go to the welcome page
    elif (key=="w" and page=="Results1"):
    #key to press to leave the game
        page="Welcome"
    elif (key=="q" and page=="Results1"):
        exit()
    #key to to start level three
    elif (key=="f" and page=="Results1"):
        page="Level Three"
        
     #keys in question 7
     #key to exit on question 7 if they want to stop doing the quiz
    elif (key=="q" and page=="Question 7"):
        exit()
    #key to press if they want to return to the hompage/welcome page during quiz
    elif (key=="w" and page=="Question 7"):
        page="Welcome"
        qmusic.pause()
    #keyh to press to show what will happen when choice 1 is clicked in question 7
    elif (key=="1" and page=="Question 7"):
        scores3=scores3-35
        scores-=35
        #resettin sounds
        wrong.rewind()
        wrong.play()
        page="Hint7"
    #key to press to show what will happen when choice 2 is clicked in question 7
    elif (key=="2" and page=="Question 7"):
        #rewinding the sound
        qmusic.rewind()
        #setting time scores
        q7time=time
        q7time=20-q7time
        times3=times3+q7time
        q8time=0
        #setting and adding scores
        scores3+=100-(5*q7time)
        scores+=100-(5*q7time)
        #resetting sounds
        sf.rewind()
        sf.play()
        #restting timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        qmusic.pause()
        page="Question 8"
    #key to press to show what will happen when choice 3 is clicked in question 7
    elif (key=="3" and page=="Question 7"):
        scores3=scores3-35
        scores-=35
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint7"
    #key to press to show what will happen when choice 4 is clicked in question 7
    elif (key=="4" and page=="Question 7"):
        scores3=scores3-35
        scores-=35
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint7"
        
     #keys in question 8
     #key to exit on question 8 if they want to stop doing the quiz
    elif (key=="q" and page=="Question 8"):
        exit()
    #key to press if they want to return to the hompage/welcome page during quiz
    elif (key=="w" and page=="Question 8"):
        page="Welcome"
        qmusic.pause()
    #key to press to show what will happen when choice 1 is clicked in question 8
    elif (key=="1" and page=="Question 8"):
        scores3=scores3-35
        scores-=35
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint8"
    #key to press to show what will happen when choice 2 is clicked in question 8
    elif (key=="2" and page=="Question 8"):
        scores3=scores3-35
        scores-=35
        #restting sounds
        wrong.rewind()
        wrong.play()
        page="Hint8"
    #key to press to show what will happen when choice 3 is clicked in question 8
    elif (key=="3" and page=="Question 8"):
        #rewinding the sound
        qmusic.rewind()
        #setting time scores
        q8time=time
        q8time=20-q8time
        times3=times3+q8time
        q9time=0
        #setting and adding scores
        scores3+=100-(5*q8time)
        scores+=100-(5*q8time)
        #resetting sounds
        sf.rewind()
        sf.play()
        #resetting timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        page="Question 9"
        qmusic.pause()
    #key to press to show what will happen when choice 4 is clicked in question 8
    elif (key=="4" and page=="Question 8"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint8"
        
     #keys in question 9
     #key to press to exit on question 9 if they want to stop doing the quiz
    elif (key=="q" and page=="Question 9"):
        exit()
    #key to press if they want to return to the hompage/welcome page during quiz
    elif (key=="w" and page=="Question 9"):
        page="Welcome"
        qmusic.pause()
    #key to press to show what will happen when choice 1 is clicked in question 9
    elif (key=="1" and page=="Question 9"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint9"
    #key to press to show what will happen when choice 2 is clicked in question 9
    elif (key=="2"and page=="Question 9"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint9"
    #key to press to show what will happen when choice 3 is clicked in question 9
    elif (key=="3" and page=="Question 9"):
        #rewinding the sound
        qmusic.rewind()
        #setting times scores
        q9time=time
        q9time=20-q9time
        times3=times3+q9time
        #setting scores
        scores3+=100-(5*q9time)
        scores+=100-(5*q9time)
        #setting sounds
        sf.rewind()
        sf.play()
        page="Results2"
        qmusic.pause()
    #key to press to show what will happen when choice 4 is clicked in question 9
    elif (key=="4" and page=="Question 9"):
        scores3=scores3-35
        scores-=35
        #resetting sounds
        wrong.rewind()
        wrong.play()
        page="Hint9"
        
    #keys in results page 3
    #key to press to go back to homepage
    elif(key=="w" and page=="Results2"):
        page="Welcome"
    #key to press to leave game
    elif (key=="q" and page=="Results2"):
        exit()
        
     #keys in hint pages
    #key to redo question 1
    elif (key=="r" and page=="Hint1"):
        page="Question 1"
    #key to go to the next question
    elif (key=="n" and page=="Hint1"):
        page="Question 2"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        #their scores f they go to the next question
        q1time=30
        times=times+q1time
        q2time=0
        countdown.pause()
        qmusic.pause()
    #key to redo question 2
    elif (key=="r" and page=="Hint2"):
        page="Question 2"
    #key to go to the next question
    elif (key=="n" and page=="Hint2"):
        page="Question 3"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=30
        duration=30
        start=millis()
        #their scores f they go to the next question
        q2time=30
        times=times+q2time
        q3time=0
        countdown.pause()
        qmusic.pause()
    #key to redo question 3
    elif (key=="r" and page=="Hint3"):
        page="Question 3"
    #key to go to the next question
    elif (key=="c" and page=="Hint3"):
        page="Results"
        #rewinding the sound
        qmusic.rewind()
        #their scores f they go to the next question
        q3time=30
        times=times+q3time
        tottimes+=times
        countdown.pause()
        qmusic.pause()
    #key to redo question 4
    elif (key=="r" and page=="Hint4"):
        page="Question 4"
    #key to go to the next question
    elif (key=="n" and page=="Hint4"):
        page="Question 5"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        #their scores if they go to the next question
        q4time=25
        times2=times2+q4time
        q5time=0
        countdown.pause()
        qmusic.pause()
    #key to redo quesion 5
    elif (key=="r" and page=="Hint5"):
        page="Question 5"
    #key to go to the next question 
    elif (key=="n" and page=="Hint5"):
        page="Question 6"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=25
        duration=25
        start=millis()
        #their scores if they go to the next question
        q5time=25
        times2=times2+q5time
        q6time=0
        countdown.pause()
        qmusic.pause()
    #key to redo the question
    elif (key=="r" and page=="Hint6"):
        page="Question 6"
    #key to go to the results for end of level 2
    elif (key=="c" and page=="Hint6"):
        page="Results1"
        #rewinding the sound
        qmusic.rewind()
         #their scores if they go to the results page and skip the question
        q6time=25
        times2=times2+q6time
        tottimes+=times2
        countdown.pause()
        qmusic.pause()
    #key to redo the question
    elif (key=="r" and page=="Hint7"):
        page="Question 7"
    #key to go to the next question
    elif (key=="n" and page=="Hint7"):
        page="Question 8"
        #rewinding the sound
        qmusic.rewind()
        #resettting the timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        #their scores if they go to the next question
        q7time=20
        times3=times3+q7time
        q7time=0
        countdown.pause()
        qmusic.pause()
    #key to redo the question
    elif (key=="r" and page=="Hint8"):
        page="Question 8"
    #key to go to the next question
    elif (key=="n" and page=="Hint8"):
        page="Question 9"
        #rewinding the sound
        qmusic.rewind()
        #resetting the timer
        start=millis()-start
        time=20
        duration=20
        start=millis()
        #their scores if they go to the next question
        q8time=20
        times3=times3+q8time
        q8time=0
        countdown.pause()
        qmusic.pause()
    #key to redo the question
    elif (key=="r" and page=="Hint9"):
        page="Question 9"
    #key to go to the next question
    elif (key=="c" and page=="Hint9"):
        page="Results2"
        #rewinding the sound
        qmusic.rewind()
        #their scores if they go to the results page and skip the question
        q9time=20
        times3=times3+q9time
        tottimes+=times3
        countdown.pause()
        qmusic.pause()
        
        
        
    
    
        
        
        
    
        
        
    
        
    
        
