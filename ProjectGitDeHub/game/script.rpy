# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define tina= Character("tina")
define christy = Character("christy")
define user = Character("[player_name]")
define ryu= Character ("Ryuuji")
define dad= Character ("Dad")
define mei= Character ("Mei")
define you= Character ("Youhei")
define mom= Character ("Mom")
define koji= Character ("Koji")
define hak = Character ("Hakkudoshi")
define kan = Character ("Kaine")
define mys = Character ("?")
define riz = Character("Riza")
define ly = Character("Lyra")
define ryo = Character("Ryouhei")
define eth = Character("Ethna")
define kyo = Character("Kyouhei")
define lu = Character("Luna")
define bl = Character("Blade")
define thu = Character("Thugs")
define atk = Character("Attackers")
define dark = Character("Mysterious Voice")
define merch = Character ("Merchant")
define tut = Character ("Tutorial Sensei")
define lil = Character("Lil Pump")
define kur = Character("Kuroh")
define ran = Character("Randy")
define flo = Character("Florence")
define ren = Character("Ren")
define caf = Character("People in the cafeteria")
define chef = Character("Chefs")
define player = Character("User")


#Game log with customized character color
define log = Character("GAME LOG", who_color="33FFF7")
#image bigryuuji = im.Scale("ryuuji2.jpg", 200, 900)
image ryu1 = "ryuuji6.png"
image girl6 = "girl6.png"
image ryusmall = "ryuuji1.png"

define flash = Fade(0.5, 0.0, 0.5, color="#fff")
define fade2 = Fade( 1, 1, 1, color="#000")
define pixel = pixellate




#Testing out 2nd mana and health bar

label mana_health_bars:
    screen new_health_bar:
        text "Ryuuji Health: [new_hp]/[max_hp]" xalign 0.0 yalign 0.05
        bar value new_hp range max_hp xalign 0.0 yalign 0.1 xmaximum 200

    screen new_mana_bar:
        text "Ryuuji Mana: [new_mana]/[max_mana]" xalign 0.22 yalign 0.05
        bar value new_mana range max_mana xalign 0.22 yalign 0.1 xmaximum 200

    screen tutorial_enemy:
        text "Lil Pump: [pump_hp]/[maxpump_hp]" xalign 0.50 yalign 0.10
        bar value pump_hp range maxpump_hp xalign 0.50 yalign 0.15 xmaximum 200

    screen Igada_clan_fight:
        text "Igada Soldier: [Igada_hp]/[maxIgada_hp]" xalign 0.50 yalign 0.10
        bar value Igada_hp range maxIgada_hp xalign 0.50 yalign 0.15 xmaximum 200

    screen Igada_captain_fight:
        text "Igada Captain: [IgadaCaptain_hp]/[maxIgadaCaptain_hp]" xalign 0.50 yalign 0.10
        bar value IgadaCaptain_hp range maxIgadaCaptain_hp xalign 0.50 yalign 0.15 xmaximum 200

    screen Igada_general_fight:
        text "Igada General: [IgadaGeneral_hp]/[maxIgadaGeneral_hp]" xalign 0.50 yalign 0.10
        bar value IgadaGeneral_hp range maxIgadaGeneral_hp xalign 0.50 yalign 0.15 xmaximum 200

    screen Hakku_hp:
        text "Hakkudoshi: [hak_hp]/[maxhak_hp]" xalign 1.0 yalign 0.10
        bar value hak_hp range maxhak_hp xalign 1.0 yalign 0.15 xmaximum 200

    screen Kaine_hp:
        text "Kaine: [Kaine_hp]/[maxKaine_hp]" xalign 1.00 yalign 0.10
        bar value Kaine_hp range maxKaine_hp xalign 1.0 yalign 0.15 xmaximum 200

    screen Mei_hp:
        text "Mei: [Mei_hp]/[maxMei_hp]" xalign 0.0 yalign 0.05
        bar value Mei_hp range maxMei_hp xalign 0.0 yalign 0.1 xmaximum 200

# ================= 1st Health and Mana =================================
    #This will test out the health bar
    screen hpbar:
        text "Health: [currenthp]/[maxhp]" xalign 0.0 yalign 0.05
        bar value currenthp range maxhp xalign 0.0 yalign 0.1 xmaximum 200

    #Tests our the manaBar
    screen manaBar:
        text "Mana: [currentmana]/[maxmana]" xalign 0.15 yalign 0.05
        bar value currenthp range maxhp xalign 0.15 yalign 0.1 xmaximum 200

    #Gald currency
    screen galdbar:

        text "Gald: [currentgald]" xalign 1.0 yalign 0.05



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    label gald:
        $currentgald = 90000
        show screen galdbar

    #CALL MANA BAR
    label healthbar:
        $currenthp = 30
        $maxhp = 50

        if currenthp >= 50:
           log "MAX HEALTH REACHED"

        show screen hpbar

    #calls the mana bar
    label manaDisplay:
        $currentmana = 30
        $maxmana = 50

        if currentmana >=50:

            log "MAX MANA REACHED"
        show screen manaBar

        hide screen manaBar
        hide screen hpbar


    label new_hp_call:
        $ new_hp = 20
        $ max_hp = 20
        show screen new_health_bar

    label new_mana_call:
        $ new_mana = 20
        $ max_mana = 20
        show screen new_mana_bar

    # These display lines of dialogue.

    stop music fadeout 1.0

    show ryu1 at left


    show ryusmall at center

    hide ryu1
    hide ryusmall

#    show girl6 at center with zoomin


#    hide girl6 with zoomout


    #play music "calm.mp3"
    show tut at left
    tut "Welcome to the game! Here we have an interactive visual novel that always uses 'LEFT CLICK' to
    continue {p}See?! Heres the next line, but we will also have instances where it will open another window, Try it!"




    tut "Given that this is interactive, you'll have series of choices and selections that will
    determine the outcome of the story so make it count and choose wisely, and pay attention!"



    tut "Lets give it a shot shall we?"

    tut "Are you ready to play?" with flash
label tutorial:

    menu:
        "Yes":
            tut "Then Let's get to to it!"
            jump quizzy

        "No":
            tut "That's not what we want to hear!"
            jump tutorial1

        "Kind of":
            tut "Eh, Good enough"
            jump quizzy

        "Do I have to?":
            tut "Yes!, come on, dont be shy"
            jump quizzy

label tutorial1:
    menu:
        "Yes":
            tut "Then let's get to it!"
            jump quizzy
        "Kind of":
            tut "Eh, good enough"
            jump quizzy

        "Do I have to?":
            tut "Yes!, come on, don't be shy!"
            jump quizzy




label quizzy:
    stop music fadeout 1.0
    #play music "vortex.mp3"

    tut "There will also be some trial and error scenarios where you would need a sufficient amount
            of points to progress, lets try it!"

    tut "Dont sweat too much, this is a basic quiz you'll need to score 3 or more to progress!"

    tut "Good luck! Remember, CORRECT answers only! Incorrect answers won't give you points which will
         cause you to restart from the beginning! "

    #User does not see this, but by default the score will be zero



#Start quiz!
label quiz_starts_here:
    $ score = 0
    #First question
    tut "What color is the sky?"

    menu:
        "Question 1 :What color is the sky?{p}{p}Blue":
            tut "I'm blue da be doo a do dye"
            #correct answers will add +1 to the score we called earlier
            $ score +=1

        "Question 1 :What color is the sky?{p}{p}Purple":
            tut "Purple nurplesss"

        "Question 1 :What color is the sky?{p}{p}Red":
            tut "Dead redemption"


    #Second Question
    tut "How many wheels does a car have?"
    menu:

        "Question 2: How many wheels does a car have?{p}{p}6":
            tut "6?!"

        "Question 2: How many wheels does a car have?{p}{p}10":
            tut "10?!"

        "Question 2: How many wheels does a car have?{p}{p}4":
            tut "That's what I thought!"
            $ score +=1

    #3rd question
    tut "What does the ocean consist of?"
    menu:
        "Question 3: What does the ocean consist of?{p}{p}Water":
            tut "I luv me sum h20 bb"
            $ score +=1

        "Question 3: What does the ocean consist of?{p}{p}Blue stuff":
            tut "Yeah, I'll take that"
            $ score +=1

        "Question 3: What does the ocean consist of?{p}{p}Bleach":
            tut "Have you ever been to the beach?"

    #4th question
    tut "Where do you get a college degree from?"
    menu:
        "Question 4: Where do you get a college degree from?{p}{p}School":
            tut " I see you're an intellectual"
            $ score +=1

        "Question 4: Where do you get a college degree from?{p}{p}Internet":
            tut "Er, I guess online certifications count"
            $score +=1

        "Question 4: Where do you get a college degree from?{p}{p}The sky":
            tut "Get drug tested please"


    #5th Question
    tut "What's 1+1?"
    menu:
        "Question 5: What's 1+1?{p}11":
            tut "Wtf"

        "Question 5: What's 1+1?{p}4":
            tut "Did you fail kindergarten or something?"

        "Question 5: What's 1+1?{p}2":
            tut "Phew, had me worried for a second"
            $ score +=1


    #Calculates the score out of 5

    log "You got a score of: [score]/5"

    #if user got 3 or more, passed!
    if score >=3:
        tut "Yay! you passed!!!"

    #If they fail then it restarts the quiz
    else:
        tut "Come on, you can do better than that! Run it again!"
        jump quiz_starts_here


    hide tut
    show tut at left
    stop music fadeout 1.0

#==============This scene will begin the first fighting scene of the tutorial!
label tutorial_fight:

    play music "battle.mp3"
    tut "A wild lil pump appeared! Go battle him or we'll die to the Gucci Gang!"
    hide tut
    show lil pump at center with pixel

    $pump_hp = 10
    $maxpump_hp = 10

    show screen tutorial_enemy

    menu:
        "Kill him through overdoes of lean":

            log "CRITICAL HIT" with hpunch
            $pump_hp -=5


    log "*Little Pump launches an album!*"
    $ new_hp -=5
    log "You have taken Damage!" with vpunch


    menu:
        "Disconnect the aux":
            log "CRITICAL HIT x2" with hpunch
            $pump_hp -=5



    if pump_hp <= 0:
        hide lil pump with dissolve
        tut "YAY! My ears have been saved!
        {p}Another good day for a struggling Harvard Student!"
        jump tutorial_end

label tutorial_end:

    hide screen tutorial_enemy
    hide screen new_health_bar
    hide screen new_mana_bar

    stop music fadeout 1.0
    #play music "calm.mp3"

    show tut at right
    tut "That wasn't too bad right?"
    tut "Alright! Looking good, look-ing-good!"
    tut "Remember there are more basic functions located at the bottom of the screen! Check out the
        options for more!"

    hide tut
    show tut at left
    tut "You have completed the tutorial, it brings tears to my eyes to see you progress"
    tut "Now go out there and play away!"
    hide tut





#start of game, dialogue will begin
label game_start:
    log "*****GAME START*****"

    log "How it all started."

    log " *3 Years Ago* "

    log "Inside the Takahara house."

    log "Ryuuji is gazing at his family members while they are discussing about a mission they're about to go on."

    ryu "I really need to talk to dad"

label ryu_start:
    menu:
        "Go speak to him":
           log "*You enter the room*"
           jump dad_chat

        "Sit down and wait":

            ryu "I should really get a move on, it's rare to see dad home since he goes on
                all these missions."
            jump ryu_start2



#after selecting the "sit down and wait" that option will be eliminated the 2nd time"
#This will leave only the  "Go speak to him option" You will use a lot of these throughout the game

label ryu_start2:
    menu:
        "Go speak to him":
            log "*You enter the room and sit down next to Dad*"
            jump dad_chat


label dad_chat:
    ryu "Dad, please let me become a mage. It's always been my dream since I was a kid.
     One day, I want to do what you and everyone else do. So please let me be a mage."

    show dad at right
    dad "What mage? You’re just a mere human. What can you do without powers?
    You can’t do anything so just be good and stay with your mom in the village."

    dad "Let your siblings and I deal with the problems out there. The world is a dangerous place, you're not ready.
    If you can't protect yourself, don't be foolish enough to try and protect others. "


    log "*Ryu gets irritated*"
    hide dad
    ryu "I hate all of you!."

    log "*Ryu runs away*"
    hide ryu

    show mom at left

    mom " Go after him!!"

    show mei at right

    log "Mom looks serious."

    mei "Mom..."

    show you at center

    you "Mei, let's go! It's dangerous for him to be outside!"

#initiates first choice selection for the user.
label getRyu:
        menu:
            "Exit the door to find Ryuuji's tracks":
               log "*The door opens*"
               log "*The Mei and Youhei darts out the house in hopes of obtaining Ryuuji safely*"
               jump Mission

            "Stand Still":
                you "What are you standing around for? Door's that way!"
                jump getRyu

            "Stare at Youhei":
                you "We don't have time for a staring contest!"
                jump getRyu







#user jumps here when they select the correct panel
label Mission:

label find_ryu:
        menu:
            "Let's check by the river bank!" :
                you "Sounds like a good idea!"
                you "There he is!"
                jump found_ryu

            "Let's check the village!" :
                you "Sure!"
                you "Hmm doesn't seem like he's here."
                jump find_ryu2

            "Let's check the backyard." :
                you "I don't know if he'll be there, but sure!"
                you "Hmm I don't see him here."
                jump find_ryu3

label find_ryu2:
        menu:
            "Let's check by the river bank!" :
                you "Sounds like a good idea!"
                you "There he is!"
                jump found_ryu

            "Let's check the backyard." :
                you "I don't know if he'll be there, but sure!"
                you "Hmm I don't see him here."
                jump find_ryu4


label find_ryu3:
        menu:
            "Let's check by the river bank!" :
                you "Sounds like a good idea!"
                you "There he is!"
                jump found_ryu

            "Let's check the village!" :
                you "Sure!"
                you "Hmm doesn't seem like he's here."
                jump find_ryu4

label find_ryu4:
        menu:
            "Let's check by the river bank!" :
                you "Sounds like a good idea!"
                you "There he is!"
                jump found_ryu

label found_ryu:

    you "Ryuuji, let's go home. Mom is worried about you."

    mei "Don't take what father said to heart. He only means well for you."

    log "Ryuuji looks at Youhei and Mei and nods."

    log "After walking back home, Ryuuji's mom runs up to him and gives him a long hug."

    log "The Next Day."

    show mom at left


    mom "Your Father and I are going on a mission and we don't know when we'll be back, but if you come across a group
    of bandits, make sure to run to your siblings and hide immediately"

    mom "After got to Pyre's Guild and they will help you guys out. Make sure to take care of each other."

#Another selection for the user
label mom_convo:
    menu:
        "Sounds good, will do!":
            mom "That's what I like to hear."

        "I've always wanted to fight":
            mom "Don't be stupid."

        "I want to go with you!":
            mom "G rank hostiles are not to be reckoned with, your ensured safety here will give your
            father and I a peace of mind."




#Story continues
    hide mom
    hide you
    hide mei

    log "Ryuuji's parent's leave the house, leaving the siblings to watch after one another."

    log "Three Days Later."

    log "People are screaming in the background and chaos occur. People running for their lives trying to escape the
    ruthless killing and attack that is happening."

    log "In the midst of the chaos, Mei and Youhei is looking for Ryuuji."

        #Allows user to get max mana and health
    #"You reach to your pocket and find an elixir"
    #menu:
    #    "Take the elixir to fully restore health and mana":

    #        $currenthp += 20
    #        $currentmana +=20


    show mei at left

    show you at right

    mei " RYUUJI!!!"

    hide mei

    hide you

    log "*As Youhei and Mei aimlessly look around for Ryuu, Youhei see a shadow in their house, so he runs inside to check and he saw Koji slightly
    injured and proceed to go help him out.*"

    log "As Youhei was carrying Koji out, he spotted Ryuu in the middle of the village and quickly screamed out for him.
    Ryuuji terrified not knowing what to do, finally notice Youhei and Koji in the distance. Ryuu runs to them as fast as he could."

    show ryu at center

    show mei at left

    show you at right

    ryu " Guys! We forgot about Lyra!"

    hide ryu

    hide mei

    hide you

    koji "*Shivers*"

    show ryu at center

    show mei at left

    show you at right

    you "I'll go help her! Mei, look after Koji and Ryuu for me!"

    mei "Youhei, it's fine! She can handle this. I know she'll handle this just fine.
    We can all meet up with her later."

    ryu "Lyra needs me! I promised her I'll be by her side if anything happens!"

    log "*Ryuuji looks worried* "

    you "Mei, go on! I'll let Ethna aid us! "

    mei "No, if you're going to do this, then we are looking for her together. Tsubaki and I will go that way,
    and you and the rest will go that way!"

    log "Points over to the other side of the village"

    mei "If we combine our efforts, I'm sure we'll find Lyra!"

    log "*Ryuuji and Youhei nods*"

    hide mei

    log "Youhei looks and Ryuuji."

    you "Do you know where she could be hiding right now?"

    ryu "We have a secret base that we made together a long time ago, she might be there!"

    you "Alright, Let's go!"

    ryu "Right!"

    hide ryu
    hide you

    log "Youhei, Ryuu, and Koji run towards the secret base. In the meantime, the enemies continue attacking the village.
    Being outnumbered, all the mages tries to fend off the enemies and defend their citizens but they were too strong."

    log "In the distant, the enemies notice a movement making their way across the village and proceed to stop them.
    Without noticing it, Youhei and them were surrounded by enemies."

    show you at left
    show ryu at center

    #Encounter time
label encounter:

    menu:
        "Flee":
            ryu "We can't do that! Go talk to them!"
            jump encounter

        "Speak with attackers":
            jump attackersIntro


label attackersIntro:


    you "W-WHO ARE YOU?!"

    show mys at right

    mys "Since you’re going to die anyways, might as well tell you who we are.{p}
     We’re from the Igada clan!"

    ryu "Igada clan?? Why are you attacking us? Our people never did anything to you guys!"

    mys "Nothing? All these years, all we wanted was to go back to our home, but you people did nothing to help us.
    Instead, you mocked, treated us like rats, and looked down on us!"

    mys "All these years of hatred, we decided to change this pathetic world. You guys are just a bunch of lowly scumbags
    in this world full of magic."

    ryu "Then why do you guys bother to seek vengeance on us? You guys arrive here on your own.
    It's not our fault you can't go back home! Our town isn't responsible for your hatred!"

    log "Youhei looks concern."

    you "There’s no use in arguing, they wouldn't listen to us."

    mys "*tsk* Kill them all and make sure to drain their magic.
    We’ll take all their magic and make it ours and then we’ll be unstoppable! *laugh evilly*"

    hide ryu

    #The enemies started attacking but Youhei fought them off one by one, making sure Ryuuji wasn’t harmed.
    #As soon as they got a chance, Youhei grabbed Ryuuji and made a run for it as soon as they
    #thought there was no more enemies. In the midst of everything, mei caught a glimpse of Ryuuji and Youhei.
    #Implement a fight scene.

#Youhei's head ass
label youhei_health_for_fight:

    screen youhei_vs_igada:

        text "Youhei Health: [youhei_health_igada]/[youhei_max_health_igada]" xalign 0.0 yalign 0.05
        bar value youhei_health_igada range youhei_max_health_igada xalign 0.0 yalign 0.1 xmaximum 200

    $youhei_health_igada = 80
    $youhei_max_health_igada = 80

    show screen youhei_vs_igada

label fight_W_Igada:


    $Igada_hp = 20
    $maxIgada_hp = 20

    show screen Igada_clan_fight

    menu:
        "Ethna use Sound Slash!":

            log "CRITICAL HIT" with hpunch
            $Igada_hp -=5


    log "*Igada attacks with Fireball!*"
    $ youhei_health_igada -=5
    log "You have taken Damage!" with vpunch


    menu:
        "Ethna use IRON MAIDEN!":
            log "CRITICAL HIT x2" with hpunch
            $Igada_hp -=15



    if Igada_hp <= 0:
        hide mys with dissolve

        jump end_Igada_fight

label end_Igada_fight:

    hide screen Igada_clan_fight

ryu "YOUHEI WATCH IT THERE'S ANOTHER ONE!"

you "Alright Ethna time for round 2."

show mys at center

label fight_captain:

    $IgadaCaptain_hp = 40
    $maxIgadaCaptain_hp = 40

    show screen Igada_captain_fight

    menu:
        "Ethna use Wind tunnel!":
            log "Captain takes massive damage!" with hpunch
            $IgadaCaptain_hp -= 15

    log "Igada Captain uses Fire Blaze!"
    $ youhei_health_igada -= 15
    log "Youhei has taken Damage!" with vpunch

    menu:
        "Ethna finish him off with IRON MAIDEN!":
            log "CRITICAL HIT " with hpunch
            $IgadaCaptain_hp -=25



    if IgadaCaptain_hp <= 0:
        hide mys with dissolve

        hide screen Igada_captain_fight

        jump end_captain

label end_captain:

    ryu "Watch Youhei the General is here!"

    you "Alright Ethna last one. Let's make this one quick!"

label General_fight:

    $IgadaGeneral_hp = 100
    $maxIgadaGeneral_hp = 100

    show screen Igada_general_fight

    menu:
        "Ethna amplify Iron maiden!":
            log "The General took massive damage!" with hpunch
            $IgadaGeneral_hp -= 100

            you "Wow he went down easier than his buddies."

    if IgadaGeneral_hp <= 0:

            hide mys with dissolve

            hide screen Igada_general_fight

            jump end_general

    label end_general:

    hide screen youhei_vs_igada

    hide you

    hide ryu

    hide mys

    show mei at left

    mei " They didn't!"

    show ly at right

    log "*Lyra shivering and looks up to see Ryuuji*"

    ly "RYUU-NII!!"

    show ryu at center

    ryu " Lyra, you're ok!"

    mei " Quiet! "

    hide mei

    hide ryu

    hide ly

    show mys at center

    mys "They're there!"

    show ryu at right

    log "As the group trying to make an escape from the enemies, they hear a cracking sound."

    mei "What's that sound?!"

    hide mys

    log "Before anyone could respond, the floor suddenly collapse and everyone dropped down in this pitch black tunnel."

    #Flash of white light and Ryuuji wakes up in a cell

    hide ryu with flash

    log "As everyone came too, they notice they were in an underground cell."

    ryu " *Wakes up* "

    log "Hakkudoshi and Kaine emerges from the darkness."

    you "Who are you?!"

    log "Youhei gets on his feet."

    hak "I'm the leader of the Igada clan. *Stares at Ryuuji for a moment* You have no magic?
    Ahhh, I see. You're just a mere human. I can use you as my vessel."

    ryu "Vessel?!"

    log "*Ryuuji looks terrified*"

    hak "You make the perfect vessel for me! All these years, I've been searching for a perfect
    vessel to help me with my eternal youth. You're mine!!"

    log "Hakkudoshi and Kaine proceed to attack Ryuuji."

    #Kaine and Hakkudoshi fight for Ryuuji, Youhei, Mei, and Ethna fight them back.

    mei "Don't worry I'll take care of Kaine!"

label hakku_fight:

    $Kaine_hp = 60
    $maxKaine_hp = 60

    show screen Mei_hp

    $Mei_hp = 50
    $maxMei_hp = 50

    $hak_hp = 60
    $maxhak_hp = 60

    show screen Kaine_hp

    menu:
        "Freeze Dust":
            log "Mei uses Freeze Dust on Kaine."
            $Kaine_hp -=20

        "Ice Lance":
            log "Mei uses Ice Lance on Kaine."
            $Kaine_hp -=20

    log "Kaine uses Nightmare Gale on Mei."
    $Mei_hp -=20

    menu:
        "Crystal Mist":
            log "Mei uses Crystal Mist on Kaine."
            $Kaine_hp -=20

        "Crystal Spark":
            log "Mei uses Crystal Spark on Kaine."
            $Kaine_hp -=20

    log "Kaine uses Nightmare Pain on Mei."
    $Mei_hp -=20

    mei "Youehi I need you to take over!"

    you "I will! Just rest up!"

    hide screen Mei_hp

    show screen youhei_vs_igada

    menu:
            "Sound Break":
                log "Youhei uses Sound Break on Kaine."
                $Kaine_hp -=20

            "Static Resonance":
                log "Youhei uses Static Resonance on Kaine."
                $Kaine_hp -=20

    kan "I'm sorry Hakkudoshi, I couldn't take him."

    hide screen Kaine_hp

    hak "Ugh Looks like I have to take over now."

    show screen Hakku_hp

    menu:
            "Sound Break":
                log "Youhei uses Sound Break on Hakkudoshi."
                $hak_hp -=20

            "Static Resonance":
                log "Youhei uses Static Resonance on Hakkudoshi."
                $hak_hp -=20

            "Iron Maiden" :
                log "Youhei uses Iron Maiden on Hakkudoshi."
                $hak_hp -=20

    log "Hakkudoshi attacks with Dark Blade."
    $ youhei_health_igada -= 20

    menu:
            "Sound Break":
                log "Youhei uses Sound Break on Hakkudoshi."
                $hak_hp -=20

            "Static Resonance":
                log "Youhei uses Static Resonance on Hakkudoshi."
                $hak_hp -=20

            "Iron Maiden" :
                log "Youhei uses Iron Maiden on Hakkudoshi."

                $hak_hp -=40

                you "Had enough yet?"

                hak "I must have him as a vessel! This arm is perfect! "

                jump end_hak_fight

    log "Hakkudoshi attacks with Dark Plunge."

    $ youhei_health_igada -= 40

    hak "I must have him as a vessel! This arm is perfect!"

    jump end_hak_fight

label end_hak_fight:


    hide screen youhei_vs_igada

    hide screen Hakku_hp

label ryuuji_health_arm:
    screen ryuuji_low_health:
        text "Ryuuji Health: [low_hp_arm]/[max_hp_arm]" xalign 0.0 yalign 0.05
        bar value low_hp_arm range max_hp_arm xalign 0.0 yalign 0.1 xmaximum 200


    show ryu at left

    show hak at right
    $ low_hp_arm = 30
    $ max_hp_arm = 50

    show screen ryuuji_low_health

    ryu " N-no.... stop no more... please no more..."
    $ low_hp_arm -=2

    log "Hakkudoshi suddenly appears in front of Ryuuji, and quickly dismembers his arm in one motion.
    Before the arm could fall, Hakkudoshi grabs it as Ryuuji falls to the ground."

    ryu " Wha....!"
    $ low_hp_arm -=2

    log  "*Ryuuji looks shocked seeing Hakkudoshi holding his arm*"

    log  "*Just then, Youhei notice Ryuuji deteriorating condition, in anger, he rushes in fend off Hakkudoshi and Kaine at once.
    He hurriedly ran to Ryuuji and picked him up as he desperately tries to find and escape route.*"

    show you at right

    you " RYUU! Don't you dare die on me! Everyone who cares about you are back at the guild, we'll make it alive!
    All of us!"

    $ low_hp_arm -=2

    you " Ethna lend us your strength! CRIMSON MAIDEN!"

    $ low_hp_arm -=2

    eth " YES! "

    hide hak

    log  "*Ethna then uses his power to evade the monsters from behind as they continue to run.*"

    ryu "Where’s my arm?!!? I'm scared Youhei, It hurts.... *crying in pain*"

    $ low_hp_arm -=2

    you "Don’t worry about your arm! We’ll figure out away. I’ll get us out of here so stay strong!"

    show kan at center

    kan "............"

    log  "*Kaine slowly emerges from behind them.*"

    hide kan

    hide ryu

    log "*As everyone was trying to find an escape, Youhei notice a presence from behind and realized it was Kaine who followed them.*"

    you "Forgive me, it looks like I won't be able to return back with you guys... it's up to you now Ryuuji,
    stay strong and remember to take care of everyone for me. You must believe in the path you choose."


    log "*Youhei Placed Ryuuji down near the wall and start chanting a transportation spell.*"

    show ryu at left

    ##  Constant "$ low_hp_arm -=2" will allow the hp to decrease each time #############

    ryu "Nii-san?"

    $ low_hp_arm -=2

    show you at right

    you "This is goodbye.. I'm sorry if.... I wasn't a good brother to you..."

    ryu "*Starts to cry.* N-nii-san! No wait, there's so many things I never got to say to you! Don't go!
    What about us?! Mei-nee?! What do I say to her?! No, please! You promised we'll be out together!"

    $ low_hp_arm -=2

    you "*smiles sadly, bends down to Ryuuji and hugs him* I'm sorry...if I was never a good brother to you."

    $ low_hp_arm -=2

    ryu "*cries* That's not fair! Nii-san! I -"

    $ low_hp_arm -=2

    kan "Give that boy to me!"

    $ low_hp_arm -=2

    you "He doesn't belong to you! He's a human just like everyone else! We're not objects for your experiments! I’m not giving him up!"

    kan "An order is an order! *takes out his sword*"

    $ low_hp_arm -=2

    hide you

    hide ryu

    show kan at right

    ryu "Please don't go! NII-SAN!"

    $ low_hp_arm -=2

    hide kan

    show you at left

    you "*smiles sadly* Goodbye, Ryuuji. I'm sorry, I want you , Mei, your friends, and all the guildmates...
    to live long. I'll soon be with mom and dad. I'm sorry. I'm really sorry, Ryuu.. live on ! "

    $ low_hp_arm -=2

    log "The transportation spell completes and the magic circle appears with a magic crystal in the middle."

    hide you

    ryu "*cries* NOOO! NII-SAN!"

    show kan at right

    # {p} breaks to a new line

    hide ryu

    hide kan

    log "Ryuuji was  thrown into the crystal, he saw the image of his brother takes out his weapon to fight Kaine. It then flashes into a bright light."

    show ryu at left

    ryu "*Cries* I… I didn't even get a chance to apologize and tell him what a good brother he was."

    log "*A scroll suddenly appears from thin air*"

    ryu "A scroll ? *grabs it the scroll and opens it.*"

    log "As Ryuuji opens the scroll, bright light emerges and he then entered in an unconscious state and sees nothing but darkness around him."

#Scroll scene opening
label scroll_found:
    menu:
        "Examine the Scroll":

           log "The scroll rolls open slowly"
           jump dark_area



        "Go around the area":
            ryu "Hmm, there doesn't seem much out there, that scroll might come in handy"
            jump scroll_found


label dark_area:
    ryu "Where am I? *looks confused*"
    hide ryu
    show dark at right

    dark "*Just a voice* Young one, do you seek power? Is it your desire to become a mage?"

    menu:
        "I’m just a human. Is that even possible for me to be a mage?":
            show ryu at left
            ryu "yes I do"
            jump power_obtained

        "No":
            show ryu at left
            ryu "On second thought, this might not be a bad idea, I need to become stronger!"
            jump dark_area2



label dark_area2:

    menu:
         "I’m just a human. Is that even possible for me to be a mage?":
            ryu "Yes I do, give me all of it."
            jump power_obtained


label power_obtained:
    show ryu at left
    show dark at right
    dark "Yes, but it comes with a price. Are you willing to sacrifice something?"

    menu:
        "Yes":
            ryu "No matter what, I want to have my revenge! {p}I'll
            take the power no matter if it's good or evil!"

        "Do it":
            ryu "No matter what, I want to have my revenge! {p}I'll
            take the power no matter if it's good or evil!"

        "This doesn't change my decision, give me the damn power.":

            ryu "No matter what, I want to have my revenge! {p}
            I'll take the power no matter if it's good or evil!"

    dark "Even if it means losing your humanity?"

    ryu "I’ll do whatever it takes in order to have my revenge! No matter if it's good magic or evil magic. I need to be stronger. I’ll do whatever it takes! "

    dark "As you desire. Let the games...begin. * laughs evilly and slowly fades out* *this scene fades out as well*" with fade

    log "With gaining power, Ryuuji along with his new profound power gained a new arm."

    #wrote multiple in case there duplicates
    hide dark
    hide dark
    hide dark
    hide dark
    hide ryu
    hide ryu
    hide ryu
    hide ryu
    hide screen ryuuji_low_health


    #####Gives the user full regen in health and mana######
    $ currenthp +=10
    $ currentmana +=95
    $ maxhp +=10
    if currenthp >= 60:

        hide screen hpbar
        hide screen manabar
        hide screen ryuuji_low_health



    $ maxmana +=50
    if currentmana >=50:

        #Calls new mana and hp here


        #new hp and mana
        label healthbar1:

            $currenthp = 60
            $maxhp = 60

            if currenthp >= 60:

               log "******{p}MAX HEALTH REACHED{p}******"

            show screen hpbar

            #calls the mana bar
        label manaDisplay1:

            $currentmana = 100
            $maxmana = 100

            if currentmana >=100:

               log "******{p}MAX MANA REACHED{p}******"

            show screen manaBar



label merchantscene:


    log  "7 years later in the town of Hirochimatsu, {p}
    The main city that's full of magic." with flash

    #Opening scene - *scene opens up on a busy street market*

    log  "While walking down the street market, Mei ran into a street merchant who sold fascinating weapons which caught her eyes.
    Ryuuji on the other hand, was carrying Mei's boxes with the help of other guild members to help do a task that Mei ask Ryuuji to do."

    mei "Not bad! *Lifts up the weapon*"

    ryu "Sis! *sigh* "

    log "Kyouhei who was helping Ryuu carry the boxes stares at Mei nervously as she's picking up weapon goods that could be a scam."

    show merch at left

    merch "Nice goods, eh? These are limited and rare weapons that are hard to find in regular towns."

    show mei at right

    ryu "*Looks at them and sighs* Sis... We got enough weapons already."

label weapon1:

    menu:
        "Steel Axe":
            ryu "That looks a bit big on you Mei, let's try something smaller."
            jump weapon2

        "Dual Swords":
            kyo "Dual isn't really your style, pick the other one."
            jump weapon3

        "Crimson Sword":
            mei "I think I'm going to go with this one!"
            jump weapon_obtained


label weapon2:

    menu:
        "Crimson Sword":
            mei "Oh! The crimson sword looks nice!"
            jump weapon_obtained

        "Dual Swords":
            kyo "Dual isn't really your style, pick the other one."
            jump finalweapon

label weapon3:

    menu:

        "Steel Axe":
            ryu "That looks a bit big on you Mei, let's try something smaller."
            jump weapon2

        "Crimson Sword":
            mei "Oh! The crimson sword looks nice!"
            jump weapon_obtained

label finalweapon:
    menu:
        "Crimson Sword":
            mei "Oh! The crimson sword looks nice!"
            jump weapon_obtained




label weapon_obtained:

    #Mei lifting up a weapon

    merch "Indeed it does! For you, only 5,000 gald!"

    hide merch

    hide mei

    kyo "How in the world can be the selling price?!"

    " *Ryuuji looks at Mei and the Merchant and sighs* "

    ryu " You don't even use the weapons you buy either! At this rate all our food ration savings will be gone!! {p}
        We will starve to death, with only your weapons keeping us warm..."

    mei " OO this looks nice! *looks happy* "

    ryu " Hey, are you listening to me? "

    kyo " General..... "

    mei "Yeah??"

    kyo "You do know that you're being scammed.. {p}
    Right? "

    merch "Wh-What do you mean?!? *looks confused* "

    ryu " Oh boy, here we go again. "

    log  " *Ryuuji gets irritated* {p}

    *Mei Smiles* "

    mei "You do know I am the general of the Pryre Guild, right?"

    merch "Who wouldn’t have known? Your uniform made it pretty obvious."

    mei "You;re not lying... right? Lying and scamming these weapons can
    be a big deal if you're selling it for a half-decent price."

    mei " You're not lying.....right?
    Lying and scamming these weapons can be a big deal
    even if you're selling it for a half-decent price"

    merch "Of course nooooootttt.. *saying it suspiciously*"

    log  " *A group of men surrounded them; holding weapons and smirking.* "

    log  " *Ryuuji flinches* "

    ryu " S-sis! I knew this would happen! "

label mei_fight:
    menu:
        "Fight the group of men":
            kyo "We can't really catch a break can we? I still wanted to do some
                 Holiday Shopping."

        "Whip out the almighty sword you bought":
            kyo "You just bought the sword and want to get it dirty? Ok, Mei."

        "Place a battle stance to get position yourself to battle":
            kyo "Here we go, I didn't even get a chance to stretch.
                 {p} *draws weapon* "

        "Place hand on the sword and look menacingly at the hostiles":
            kyo "I can't believe you'd want to fight at a time like this."



    kyo "She's the general, she can handle these goons right?
    {p}Come on let's move along."

    kyo "*She's the general, She can handle these goons all on her own.
    Come on, let's move along.*"

    log "*pushes Ryuuji away so they can escape*"

    ryu "sighs"

    log "Kyouhei and Ryuuji started to run away as Mei stayed back to deal with these goons."

    mei "I'm going easy on you fellas since you're not mages."

    log  "*Thugs get mad*"

    thu "capture those boys for me!"

    ryu "Us too?!"

    kyo "Er, run back to the guild!!"

    log  "*The two dashes back, carrying Meis belongings along the way and arrived inside the guild safely.
    {p}Kyouhei and Ryuuji both felt exhausted. Another mage comes by and looks at them. He walks over with a smile and pats Ryuuji's head.*"

    ryo "Oh.... Bro, you're back! {p}
    Where's your sister, Ryuuji??"

    ryu "Getting into trouble again...."

    thu " Damn it!! {p}
    It's Pryre for real!!"

    log "Moments later, the thugs arrived in front of the guild."

    thu "Damn it! It's Prye for real! They weren't kidding."

    thu "We're still going after them!"

    log "Ryuuji notice some strangers outside the window and saw that it was the thugs from earlier."

    ryu " Eeeeh?! Did they manage to follow us? {p}
    What the heck is sis doing the whole time?"

    log "*Meanwhile back to Mei*" with flash

#Will provide health and mana screen calls for the thugs and mei
label mei_battle_with_thugs:
    screen mei_health1:
        text "Mei's Health: [mei_current_hp1]/[mei_max_hp1]" xalign 0.0 yalign 0.05
        bar value mei_current_hp1 range mei_max_hp1 xalign 0.0 yalign 0.1 xmaximum 200


    screen thug_health:
        text "Thug Health: [thug_current_hp]/[thug_max_hp]" xalign 0.90 yalign 0.10
        bar value thug_current_hp range thug_max_hp xalign 0.90 yalign 0.15 xmaximum 200



label healthmana_for_mei_and_thugs:

    #health variables for Mei
    $ mei_current_hp1 = 70
    $ mei_max_hp1 = 70

    #health variables for the thugs
    $ thug_current_hp = 65
    $ thug_max_hp = 65

    hide screen hpbar

    hide screen manaBar

    hide screen new_health_bar

    hide screen new_mana_bar

    show screen mei_health1

    show screen thug_health

    show mei at left

    show thug at right

    stop music fadeout 1.0

    play music "battle.mp3"

    mei "My oh my, let's get this started shall we?"
    menu:
        "Mei:\n Swing your sword at the thugs":
            log "*THUG TOOK SOME DAMAGE!*"  with hpunch
            $ thug_current_hp -=5
            mei "Wow this sword packs a punch!"
            #Thug hp is down to 55

        "Mei:\n Hold Stance to gain power":
            mei "Charging up!
                \n*MEI'S ATTACK INCREASED!*!"
            #This will increase Mei's damage but wont


    log "*THUG RUSHES YOU WITH HIS SWORD*"
    $mei_current_hp1 -= 5
    log "**MEI TOOK SOME DAMAGE**!" with vpunch


    menu:
        "Mei:\n Use Increased Power to attack":
            mei "Get a load of this, Ugly!" with hpunch
            $ thug_current_hp -=10
            log "**THUG TOOK SOME DAMAGE**"


        "Mei:\n Try to dodge some attacks":
            mei "Come at me!"
            log "*THUG RUSHES YOU WITH HIS SWORD*"
            log "*MEI DODGES!*"


    log "*THUG RUSHES YOU WITH HIS SWORD*"
    $mei_current_hp1 -=10
    log "*MEI TOOK SOME DAMAGE!" with vpunch


    menu:

        "Mei:\n Sword Slash":
            mei "Take this!" with hpunch
            $ thug_current_hp -=5

        "Mei:\n Defend and Build Power":

            $ mei_current_hp1 -=10
            log "*DEFEND FAILED!

              \nCRITICAL HIT ON MEI!*/" with vpunch

    log "*THUG RUSHES YOU WITH HIS SWORD*"
    $ mei_current_hp1 -=20
    log "*CRITICAL HIT!*" with vpunch

    menu:
        "Mei: \n Sword Slash":
            mei "Get a load of this!"

            $ mei_current_hp1 -=5
            log "*Mei get's distracted by the crowd and loses focus
              \n Thug counters!*
              \n *Mei Takes Damage!*" with vpunch

        "Mei:\n Charge Power":
            $ mei_current_hp1 -=5
            log "*Mei get's distracted by the crowd and loses focus
            \n Thug counter attacks
            \n *Mei Takes Damage!*" with vpunch

            log "*THUG RUSHES YOU WITH HIS SWORD*"
            $ mei_current_hp1 -=15
            log "*CRITICAL HIT SINCE MEI WAS DISTRACTED!*"
            log "*MEI TOOK SOME DAMAGE!*" with vpunch


    menu:
        "Mei \n Sword Slash":
            mei "Get a load of this!"  with hpunch
            $thug_current_hp -=5
            log "*THUG TOOK SOME DAMAGE!*"

        "Mei \n Power Hit":
            mei "You've done it now!"
            $thug_current_hp -=9




    log "*THUG LUNGES WITH MAX POWER WHILE MEI WAS DISTRACTED BY THE CROWD*"
    $ mei_current_hp1 -=10
    log "*MEI TOOK SOME DAMAGE!*" with vpunch

    #When Mei's health reaches 25 or below, it'll jump to the next scene
    if mei_current_hp1 <= 25:
        mei "Oh man I gotta get back to the guild!"
        jump after_mei_battle
        hide mei with dissolve
        hide thug


label after_mei_battle:

    stop music fadeout 1.0

    hide mei with dissolve

    hide thug

    hide screen thug_health

    hide screen mei_health1

    show mei at left

    mei "*talking out loud to herself* Oh crap.. Ican't believe I got lost in the crowd."

    show riz at right
    hide mei

    riz "General?"

    mei "Oh Riza!"

    log "*Riza then comes up to her with a smile.*"

    # Riza, the toy mage and the master of her own toy shop.
    # She also joined Pryre guild in order to make more cash.

    riz "The guild's back there. *said jokingly and giggles as she pointed to the right direction*"
    hide mei

    log "*Riza giggles as she points out the direction to the guild*"

    mei "Oh Shush! I'll be back! I can't believe they tried to scam me!"
    hide mei
    show riz at right

    riz "Who tried to scam you? *gets suspicious*"

    hide riz
    show mei at left

    show riz at right

    mei "I was just trying to find new weapons for my collection, but can't talk now! See ya!
    *runs and waves*"

    riz "As usual.*chuckles*"
    hide mei
    hide riz

    log "* Back to the guild *" with flash

    ryo "What did you guys do?"

    kyo "It was the general!"

    ryu "Sis got herself scam when she was caught up by some merchant trying to flash some fake weapons."

    ryo "Seriously, again?"

    log "*Ryouhei hears someone walk over*"

    ryo "Oh, Blade, you're awake?"

    log " *Blade walks overlooking quite tired. He then realizes the situation of what's happening and decides to handle the situation himself.* "

    bl "*Looks annoyed* It was getting quite rowdy."

    log " *Blade walk outside.* "

    ryu "(He reminds me of someone.)"

    log " *Ryuuji peaks through the wall and watches as Blade fought the thugs.* "

    ryo "Oh boy... here we go again."

    kyo "At least he's here."

    log " *Blade procceds to throw out the thugs* "

    bl "And stay out!*throws the thugs out*"

    thu "It's.... I can't believe it's him!"

    thu "He's scary! Let's get out of here!"

    bl "*Yawns and walks back in* I'm going back to bed. I don't feel so well."

    kyo "Oh ok Blade. Make sure you get your rest."

    bl "Yep."

    ryu "Wait, isn't that guy..... from the guild's magazine?"

    menu:
        "Inspect Blade":

            log "*You go closer to Blade*"

        "Pull out the Magazine":
            log "*You pull out the magazine and rustle the pages*"



    bl "....."

    log "* Blade sweats a little and runs away *"

    ryu "H-huh?"

    kyo "He doesn't like fans who read the magazine. Don't mind by it. "

    ryu "What's up with that? "

    log "* Back to mei *" with flash

    mei "Don't go on stealing people's hard working made weapons! Especially making a General or anyone else pay for a higher price?
    \nIt's on sale? HAHAHA you almost got me there. "

    log "*The group of thugs got tied up and thrown into the local jail.* "

    log "later in the day."

    log "*Ryuuji decides to head to the guild's bar because his aunt Luna wants him to test a new food that she created called Luna's Beef hot pot.*"

    show ryuuji at left

#Luna scene
#Cooking time for the user!!! It's litty titty mcgritty

label cook_luna:
    hide ryu
    show lu at left
    lu "Let's see what we can serve for Ryuuji and the others"

    lu "Ah! Some beef stew, Hmm, lets see, here's the ingredients we'll need"
    show lu at left

# We'll need to label the ingredients just in case
# the user wants to refer back to this
label broth_ingredients:
    show lu at left
    log "INGREDIENTS NEEDED:
        \n -Broth, Salt, Beef,

        \nPotatoes, Mushrooms
        "




    lu "Let's make sure we get the ingredients first!"
label kitchen:
    show lu at left


    lu "Let's go get some mushrooms!"
    log " * You head to the garden * "

label mushroom:
    show lu at left
    menu:
        "Pick the Mushroom":
            lu "Nice and Fresh Mushrooms!"
            jump salt

        "Pick up the Cucumber":
            lu "I don't think we'll need cucumbers, let's stick with the mushrooms."
            jump mushroom


label salt:
    show lu at left
    lu "Now let's go get some salt!"

    menu:
        "Grab the Salt":
            lu "Ah, there's the salt!"
            jump get_beef

        "Grab the Pepper":
            lu "Pepper won't mix well with my stew, let's stick with salt"
            jump salt2


label salt2:
    show lu at left

    menu:
        "Grab the Salt":
            lu "Ah, there's the salt!"
            jump get_beef


label get_beef:
    show lu at left
    lu "We'll need some Beef!"

    menu:
        "Grab Beef from counter":
            lu "Nice and tender beef coming right up!"
            jump get_potatoes

        "Grab Fish":
            lu "I don't think they'll enjoy fish with their stew"
            jump get_beef

label get_potatoes:
    show lu at left
    lu "Time to get some potatoes!"

    menu:
        "Pick up the tomatoes":
            lu "Oh wait, potatoes, not tomatoes"
            jump get_potatoes

        "Pick up celery":
            lu "I don't think we'll need celery, potatoes are what we're looking for"
            jump get_potatoes

        "Pick up Potatoes":
            lu "Now this wil go great with my signature broth!"
            jump get_broth

label get_broth:
    lu "Let's see where that broth is located"

    menu:
        "Pick up Tamarind Sauce":
            lu "This is not broth"
            jump get_broth

        "Pick up hot sauce":
            lu "I don't think Ryuuji likes spicy stew"
            jump get_broth


        "Pick up the Broth":
            lu "Yay! This is the broth!"
            jump stove


#This will be after the stew is made
label stove:

    lu "Now that we have all the ingredients let's make the stew!"
    lu "Let's keep the flame low to let it simmer"


label low_flamez:
    menu:
        "Fire up the Stove on high":
            lu "This will burn the veggies!"
            jump low_flamez

        "Fire up the Stove on low":
            lu "Ah yes, just right"
            jump serve_dat_boi


label serve_dat_boi:
    log "* The pot simmers and the aroma fills the room * "
    show lu at left

    lu "The food should be complete!"

    ryu "*Eating*"

    show lu at right

    log "*Luna fixes up Ryuuji a bowl of beef stew* "

    lu "How is it?"
    show ryu at right

    ryu "It's delish!!"

    lu "*smiles* Oh, you're so cute!! *hugs him*"

    ryu "A-auntie... stop that! I'm already 19!"

    lu "Now, now just call me Luna. I'm not that old to be called auntie yet."

    hide lu
    hide ryu
    hide kyo

    log "*Mei then walks in and streches her arms as she continues her duties. She noticed Ryuuji was with Luna and Kyouhei is with his brother, Ryouhei and smiles as she walks toward them.
    She notice that Ryuuji was already eating.*"

    show mei at left

    mei "Yo! *waving* Hey, I got an interesting idea for you Ryuu."

    show ryu at right
    hide mei
    show ryu at right

    ryu "Can I finally go on a mission?"

    mei "Not that."

    ryu "Awhhh, even Lyra and Koji get to do easy missions from their class. Why can't I do the same?"

    lu "He's already 19 Mei. I think it's almost time to let him do what he wants."

    ryu "See? Even Auntie said so."

    mei "*thinks hard* Which is why I would like you to come with me. I got an interesting thing for you to work on. How's your arm doing by the way."

    ryu "*stares at his covered arm and looks at her* Not too bad for now. It's been good so far, but I still have a hard time controlling it during training..
    *looks dishearten*"

    mei "The first time you got it, it freaked me out and had me worried sick."

    ryu "*looks down sadly* I'm....sorry."

    mei "No worries, I'm just glad you're still alive. That's all that matters to me."

    ryu "Alive..."

    mei "Well, follow me. *looks at Luna* Thanks as usual Luna."

    lu "Of course! *smiles* You're always welcome to drop by anytime."

    mei "Ryuu, come on."

    ryu "Thanks for the food Auntie! I'll make you something later!"

    lu "I told you to call me Luna! I'm not that old yet but I'll be waiting for that meal!"

    log "*The two sibiling walked into Mei's room. Ryuuji sits down on a chair as Mei sat at her table.* "

    ryu "So what is it that you would like me to do?"

    mei "Training with an S class mage."

    ryu "H-huh? More babysitting? But sis, I would like to see the outside for once."

    mei "That can wait till you get yourselef stronger. You wanted to be a mage, yeah?"

    ryu "I still do!"

    mei "Good, good. I'll call him over then."

    ryu "Huh? But… *Mei interrupts*"

    mei "Don't worry, he's quite reliable. He's one of my good childhood friends."

    log "*There was a knock on the door* "

    mei "Looks like he's here. Come on in!"

    log "A mage walks into Mei's room and sighs nervously"

    bl "I'm here, general Mei."

    mei "Please enough, just drop the formalities."

    menu:
        "Ryu: Wait. I've seen you before!":
            ryu "Wait. I've seen you before!"

        "Ryu: Well I'll be damned":
            ryu "Well I'll be damned"


    ryu "Ah, you're from this morning!"

    bl "*gets nervous and chuckles anxiously*"

    mei "You promised didn't you, Blade?"

    bl "*scratches his head and sighs* A promise is a promise. I've watched Ryuuji grow up ever since he joined the guild. "

    menu:
        "Ryu: How can you say something like that?":
            ryu "How can you say something like that"

        "Ryu: Wow Blade, really?":
            ryu "Wow Blade, really?"


    log "*Ryuuji gets upset*(He looks down being all upset and has a sulky expression.) "

    bl "Oh... my bad. I didn't mean it."

    mei "*sigh* Oh geez, I hope you guys can work well. "

    bl "Since I did promise, I'll make sure to train Ryuuji to the best of my abilities."

    log " *Ryuuji still pouting* "

    bl "...??*looks confused*"

    ryu "I guess... I'm really that useless compared to my Sis and father."

    mei "*Sighs and looks at Blade* Blade..."

    bl "Just leave it to me general."

    log " *Blade walks over to Ryuu, bending down and scruffles Ryuu's head* "

    ryu "Wh-what? What are you doing?! Stop it!"

    bl "I wish I can have another younger sibiling. *saying sadly*"

    ryu "Another?"

    bl "Nothing. *smiles sadly* I'm just glad I get to pay your guy's debt now. And Mei?"

    mei "Yeah?"

    bl "Did you manage to teach him everything he needs to know?"

    mei "*looking slightly offended* Of course!  Why else I would want you to train him?"

    bl " *stands up* Starting tomorrow, I expect great things from you. "

    ryu "? *Looks up*"

    bl " *nods* "

    menu:
        "I think I've seen your face before":
            ryu "I think I've seen your face before"
            jump blade_scene

        "Have we met? I'm pretty sure we did.":
            ryu "Have we met? I'm pretty sure we did."
            jump blade_scene


label blade_scene:

    ryu "Oh wait! *pause and ponder for a moment* I recognize you from before!"

    bl "Ah, from this morning?"

    ryu " Aren't you the white fang from the magazine guild's paper?!  "

    bl " *cracks and sighs* "

    ryu "I guess I'm right! You are The White Fang! *smiles* "

    bl "Please do not call me that!"

    ryu "Blade...sensei?"

    bl "You don't have to be so formal. I'm not really used to it... *feeling shy* "

    ryu "Then I'll just call you sensei!"

    bl "I can't..understand what your brother's thinking *facepalm*"

    mei " *laughs* Don't worry, he's getting fond of you. He had always admired mages but ever since he got his power, he's still struggling to control it, but ever
    since he got his power."

    mei "He's still struggling to control it, but with some training, he'll be a fine mage one day, won't he?"

    bl "Of course, leave it to me. *stares at Ryuuji* "

    ryu " *gleams* "

    bl "Alright, alright! Stop it already. *smiles and scruffles Ryuu's hair*"

    ryu "Ahhhhhh... stop doing that sensei!"

    bl "You want to be a mage, right?"

    menu:
        "Ryu: well":
            ryu "well"

        "Ryu: I mean,":
            ryu "I mean,"

        "Ryu: Blade, you know what?...":
            ryu "Blade, you know what?..."


    ryu "Yeah."

    bl "Then starting tomorrow, let's get some training done."

    ryu "Alright!"

    bl "We will meet up at 4 am."

    ryu "EEEH?! *stunned*"

    mei "What's there to be surprised about? That's his usual training schedule."

    ryu "You're insane."

    bl "I'm not an S class by title you know? I worked hard to get it."

    mei "The man isn't wrong."

    ryu "*stares at Mei* I can see it in sensei but….. you??? Not so much. *starts laughing*"

    mei "HUH?!"

    bl " *coughs* More importantly, get some sleep. I'll see you in the morning."

    ryu "4 am...? *faints* "

    log "Scene moves into Ryuuji's room, as he then lays down on the nearby couch and begins to snore loudly as he falls asleep slowly. Mei slowly approach Ryuu."

    mei "Ryuu?"

    ryu "Goodnight sis.... *snores* "

    mei "Don't sleep on the couch, and what about dinner?! *shakes him*"

    ryu "Yeaaaah, there’s cup noodles...in the cupboarddddd.... *doze off and passes out again*"

    mei "Hey! That's not even a dinner! (Mei grab Ryuu's shoulders) *shakes him* Wake up!"

    bl "Oh geez. *scratches his head and then smiles* This will be interesting." with flash



    #Ch 2  Training Regiment Begins
    log "Scene opens up inside Ryuuji bedroom as he's sleeping."

    log "-Inside of Ryuu's dreams-" with flash

    you "I'm sorry..."

    ryu "Nii-san, don't go!"

    log "A mist then surrounded him. When he turns around he faced a demon unseeable as it opens its eyes, glaring at him."

    #Fight scene between Ryuuji and demon...


label ryuuji_hp_demon:

    screen ryuuji_demon_fight:

        text "Ryuuji : [ryuuji_health_demon]/[ryuuji_max_health_demon]" xalign 0.0 yalign 0.05
        bar value ryuuji_health_demon range ryuuji_max_health_demon xalign 0.0 yalign 0.1 xmaximum 200

label dream_demon_hp:

    screen demon_health_fight:

        text "Demon : [demon_health]/[maxdemon_health]" xalign 1.0 yalign 0.1
        bar value demon_health range maxdemon_health xalign 1.0 yalign 0.15 xmaximum 200



    show screen ryuuji_demon_fight
    show screen demon_health_fight

    $ryuuji_health_demon = 60
    $ryuuji_max_health_demon = 60

    $demon_health = 100
    $maxdemon_health = 100


    menu:
        "Zakai Vortex" :
            log "Creates a vortex that makes the Demon dizzy"

        "Zakai fist" :
            log "Punches the demon multiple times."
            $demon_health -=1

    log "Demon roars, inflicting fear in Ryuuji."
    $ryuuji_health_demon -= 10

    menu:
        "Zakai Vortex" :
            log "Creates a vortex that makes the Demon dizzy"

        "Zakai fist" :
            log "Punches the demon multiple times."
            $demon_health -=1

    log "Demon slashes Ryuuji."
    $ryuuji_health_demon -= 30

    menu:
        "Zakai Vortex" :
            log "Creates a vortex that makes the Demon dizzy"

        "Zakai fist" :
            log "Punches the demon multiple times."
            $demon_health -=1

    log "Demon slashes Ryuuji."
    $ryuuji_health_demon -=20

label dream_demon_fight_done :

    hide screen ryuuji_demon_fight

    hide screen demon_health_fight

    ryu "*wakes up and gasps*" with flash

    log "Ryuuji woke up and covers his face with a sigh. He turns off the alarm clock with an annoyed look at his face."

    ryu "3 am... was it ?"

    log "-He tries to remember from what happened yesterday-"

    bl "We meet in the training room starting at 4."

    log "-back to the current day in Ryuu's room-"

    ryu "1 ...hour... {p}*went back to rest*"

    log "Out nearby Ryuu's window, Kuroh, the crow; woke itself up as it sneezes from it's sleep."
    log "Ryuu's messenger, Kuroh, quickly flies over to Ryuu's house so fast it hit itself at Ryuu's own window to wake Ryuu up."

    kur "*flies and slams onto the window* {p}C-caaw!"

    ryu "Bah! {p}*wakes up* {p}H-huh?"
    ryu "*looks at the window* {p}K-kuroh?"

    log "Ryuuji gets up and opens the window."

    kur "Caw ! Ryuu! {p}*looks at him*"

    ryu "Ah right, I did asked you to wake me up for this morning."
    ryu "*pets him* {p}Good Kuroh. "

    kur "Caw! Meat?"

    ryu "This ..this  early in the morning? {p}*looks worried*"
    ryu "I'm a bit worried about your health if you just keep on eating meat all the time."

    kur "Caw! Hungry! Food! Caw!"

    ryu "*looks at the time and sweated*"
    ryu "If I could've just woken up earlier...*sigh*. I guess you can come to the guild with me."

    kur "Caw?"

    ryu "But you better promise me to head back to look after sis when you finish your food."

    kur "Roger!"

    ryu "-sigh-"

    log "Ryuuji and Kuroh came into the guild. As Ryuu walks over to the bar, he felt relieved
    to see Luna already preparing meals for the day."
    log "He quickly went to her and asks to make a meal for Kuroh as he's running late to class.
    She agrees and start making Kuroh's food."

    lu "*hums and makes some chicken*"

    ryu "Sorry about this Auntie."

    lu "I told you to call me Luna!"

    ryu "Y-yes Luna."

    lu "No worries, I'm glad I can help. *gives some meat to Kuroh*"

    kur "Yay! Caw! *eats*"

    lu "He sure is a lively bird."

    ryu "Ah what time is it?"

    lu "3:50 am."

    ryu "I'll be late! Kuroh, fly back to the house after your done! I need to meet up with sensei today! {p}*runs*"

    kur "Roger! Caw! Your meat was good, caw! Can I have more? Caw!"

    lu "Sure but this will be your last for the day. I need to save some for the other customers."

    kur "R-roger.. caw!"

    lu "*giggled* {p}What an odd demon crow you are. Yet at least you're a friendly one."

    kur "Caw?"

    lu "Go on eat up."

    kur "Roger! *eats*"

    lu "*smiles*"

    kur "Ryuu's was 10 times better though..."

    lu "HUH?!"

    kur "N-nothing! C-caw...! *sweated*"

    log "-at the training hall-"

    log "Blade was already waiting out at the door. He then turns to his right as he saw Ryuu in front of him."

    bl "Oh, you're a few minutes late. I guess I'll let it slide."

    ryu "I forgot to make meat for Kuroh...so I kinda made Auntie feed him for me today."

    bl "Luna?"

    ryu "Y-yeah."

    bl "I see...now, let's start some training for today. What does Mei usually teach you?"

    ryu "*shivered and looks scared* {p}Please don't let me work on her drills ever again...!"

    bl "Was it that traumatizing for you?"

    ryu "I can't help it whenever Tsubaki would throw icicles above my head!"

    bl "*imagines it and laughs* I see, no wonder."

    ryu "Huh?"

    bl "I used to fight with Tsubaki also. As part of training."

    ryu "I'm really not fond of fighting against Tsubaki at all! *sobs*"

    bl "I'm not going to ask Tsubaki to help. She belonged to your sister, right?"
    bl "Just cuz I'm your teacher, I'm not going to force Mei to bring out Tsubaki all the time. It'll be tiring for her as well."

    ryu "*phew* Oh...that's also true. Mei-nee does get exhausted after she always used her in battles. Not too sure why."

    bl "Quick question."

    ryu "Huh?"

    bl "Do you remember anything before you arrive to the guild?"

    ryu "N-no....not much. All I can remember was You-nii's disappearance."

    bl "(Thank god for that....I hope he doesn't need to remember it.)"

    ryu "Sensei?"

    bl "Uh Blade is just fine, you don't need to be so formal."

    ryu "I'm already used to being formal."

    bl "*sigh* Alright, suit yourself but this is my first time teaching kids to be honest."

    ryu "Really?"

    bl "I'm just only doing it because I made a promise to you guys; so a fair warning, don't expect everything out of me."
    bl "You can learn other things from others in the guild as well. There will be times that I always can't be with you when I wish I could."

    ryu "I don't really need a baby sitter anyways."

    bl "That's not what this is about!"

    ryu "I know. *looks annoyed*"

    bl "Urk! (I honestly can't tell what he's thinking at times! This kid...!)"

    ryu "So what do we do now? {p}*yawns*"

    bl "Ah right...it's already almost 4:10 am.... wow, time flies so fast today."
    bl "Let's just wrap things up from here. I'm not the greatest teacher of all times but I'll do the best I can to get you stronger."
    bl "Here's what you're going to do. {p}*shows Ryuuji the list*"

    ryu "-!? *reads Blade's list* {p}I'm going to die at this rate! I don't have magic you know!"

    bl "This is nothing compare to fighting demons in the outside world."
    bl "If you wanna go outside, learn how to defend yourself. This is what you'll be learning for today."
    bl "I already set up the match for you. Mind you, I've been working on this regiment routine ever since I joined this guild."

    ryu "Huh?! That's insane!"

    bl "That's how it is if you wanna get stronger."

    ryu "Aw man.. I can't even pick my own?"

    log "*Ryuuji walks up to the game set*"

    bl "I'm also going to time you so whenever you're ready!"

    ryu "Right! {p}*gulps*"

    log "-after 10 tries-"
    log "Ryuu saw the monster flying high up in the sky. He then fell to his knees and turns blue."

    bl "?"

    ryu "*throws up*"

    bl "What? *gets worried and turns the system off*"

    ryu "S-sorry...I can't take this much longer."

    bl "You managed to do the other 9 quite fine.."

    ryu "Urngh... m-my stomach..."
    log "*Ryuu fainted*"

    bl "R-ryuu?!"

    "Ryuuji's stomach then growls."

    bl "...eh?"

    ryu "H-hungry... no food...since....I woke up for this...."

    bl "*sigh*"

    ryu "S-sensei...dying...."

    bl "*smiles* I'll let it go this time but you better make sure you pass this 10th exercise so we can move on."

    ryu "*turns blue* Ungh..."

    log "Blade picks Ryuu up as he decides it's time for a break. As he looks up at the clock he realize how fast training went by."

    bl "It's already lunch huh? Might as well. Let's go to the cafeteria and get some grub. *carries him on his back*"

    ryu "Sensei... {p}*sleeps*"
    log "-As the two arrive at the cafeteria-"

    bl "Hey, we're here. Wake up."

    ryu "Urngh...can't hold. {p}*nods up and down with his head as he's trying to stay awake*"

    bl "Hey Randy, thanks as usual for the food. Starting today, he'll be my student if you're wondering why we're here together."

    log "The chef peers through his window and opens it. He let's out  a gasp once he sees Ryuu."

    ran "Aw what a sweet new small member we have!"

    ryu "*gets mad* {p}I ain't small! I'm 19! We've saw each other couple times already!"

    ran "I'm just playing with you Ryuuji. And a teacher you say?! That's the first!"

    #People in the cafeteria
    caf "Hmmn? *looks at the front*"

    bl "Quiet down, I don't want a lot of others to know. *whispers nervously*"

    ryu "Why?"

    bl "If they find out, I won't even have my sleep anymore. One student is enough. *sigh* I promised you guys didn't I?"

    ryu "*stare*"

    bl "W-what's with that stare?"

    ryu "Oh nothing. I was dozing off a bit. {p}*yawns*"

    ran "Hmmn suit yourself. {p}Now what would you two like? {p}The usual? Hmn?"

    ryu "Is he always like this?"

    bl "Pretty much."

    ran "White fang will -"

    bl "*gets mad and stares at Randy* I swear if you keep using that nickname, I'll shred your face into pieces."

    ran "If you do that, I can't even cook for you guys for awhile."

    bl "Bah! *looks embarrassed* Y-you're right. *face palmed and looks away* Yeah, sure the usual."

    ryu "Everything all on this list!"

    bl "Don't pass out on me if you can't finish it all."

    ryu "I won't!"

    ran "Hear that chefs? Hurry it up and chop chop!"

    #Chefs
    chef "Yes sir!"

    log "-The chefs scurries all over the kitchen to prepare Blade and Ryuu's meals-"

    log "As Blade and Ryuuji finds a table to sit down, the chefs bring over their food to them due to Ryuu's order.
    Blade and the other mages around Ryuuji were surprised by Ryuuji's appetite."

    bl "I'm really surpised. I guess food is everything to you huh?"

    ryu "*eats and munches on a salad* Hmn?"

    bl "I mean, is this your usual appetite? *stares surprisingly* {p}You don't get sick over eating or anything?"

    ryu "Ever since the raid incident, for some reason I won't have enough energy if I don't eat enough.
    {p}*quickly drinks some tea and eats a rice ball and skewers as he munches down*"

    bl "I ... I see. {p}(Could it be due to Ryuuji's arm he has?)"
    bl "Is your arm doing ok?"

    ryu "You know about it as well?"

    bl "Heard it all from your sister."

    ryu "It's been pretty quiet but at night...I felt it's sensation for some weird reason. It gives me nightmares and I can't really sleep well."

    bl "No wonder why your eyes looks so baggy."

    ryu "Sensei , I'm not the only one who has them too."

    bl "But you're still young."

    ryu "Doesn't really matter does it? *eats some pork with rice* Mmn Randy's cooking never seems to surprise me."

    bl "What about Luna's?"

    ryu "Hers is good too but I need to balance my diet every now and then, right?"

    bl "True, you made a very good point. Luna's cooking is all about meat and desserts. Randy does everything."

    ryu "See? *eats* Eh though I think I still rather cook at home though. Or else Mei keeps complaining... Kuroh too. *mumbles*"

    bl "Then why -"

    ryu "With the recent training schedule you've just gave me, it won't let me have time to cook at all.
    At this rate sleep also won't exist in my schedule. *looks tired*"

    bl "*laughs weakly* You kinda got a point."

    ryu "*looks at Blade's lunch* So that's your 'usual' meal you have?"

    bl "There's nothing wrong having curry right?  *looks defensive*"

    ryu "I guess not. I don't mind eating curry also. {p}*eats noodles*"

    bl "Man you sure do eat a lot."

    ryu "I got a huge appetite. I can't really control myself until it's satisfied. {p}*quickly eats a hamburger*"

    bl "I...I see."

    ryu "It's just....*stops* I don't want to let it take blood..."

    bl "Blood?"

    ryu "Uh.... I'm not so sure myself. If I go out of control....my hand will...just somehow take blood from demons instead if it were to go berserk."
    ryu "It happend after the raid when I can't control it at all... {p}Mei was absolutely terrified... {p}I was too."
    ryu "But I'm not letting it doing it no longer. I'm not a monster... *gets upset*"

    bl "I see. No you're not but, we need to learn how to stop it before it gets worse."

    ryu "Okay.... Huh?  *looks up*"

    bl "Hmn?"

    log "Ryuu sees a person looming behind Blade, grinning evilly. She then noticed Ryuu and secretely lifts her finger."

    mys "*lifts her finger to her mouth and smiled* ....."

    ryu "Uh nothing."

    bl "Well hurry up and let's go . We need to -?!"

    log "The girl  jumps on Blade's back and lands as she place over her arms on his shoulders."

    mys "I found you ! *jumps on him*"

    bl "N-not when I'm eating! Cut it out! *gets up and tries to shake her off* Stop it already!"

    log "She jumps back and lands on one foot and caught her balance. She looks at Ryuuji and waves at him with a smile on her face."

    ryu "Who's that?"

    bl "Crud, we spend here too long. I guess I got no choice..."

    mys "Hey Ren! I found him!"

    ren "*walks over* There you are, I was wondering where you went all this morning. I was worried."

    bl "I thought I left a note on the table before I left. *sigh*"

    ren "Who's this?"

    bl "..... *looks away*"

    ryu "Sensei?"

    bl "*looks embarrassed*"

    #? and Ren
    #mys and ren
    ren "Sensei? *laughs*"

    ryu "*looks surprised*"

    ren "I can't believe that you're now a teacher! So that's what this is all about!"

    bl "Geez man, shut up will you?"

    ren "Huh? *gets irritated*"

    flo "*smiles* Now, now."

    bl "Ryuuji, meet my team mates. {p}We've been working together ever since we've joined here."
    bl "This is Ren, he's a childhood friend of mine ever since we're kids. {p}He uses wind magic."
    bl "Florence is part of the team and a good guandao user. {p}She use illusions as part of her magic skill."
    bl "We're one of the S class rank mages in this guild."

    ryu "R-really?! *gleams*"

    flo "Ah, a newbie huh? What kind of mage is he?"

    bl "He's trying to figure out his magic still, give him time. Also he's related to Mei."

    #Florence and Ren
    flo "*looks surprised*"

    ryu "You guys didn't know?"

    flo "Well we heard about you all the time we just hardly ever seen you around."

    ren "Oh wait, I had seen you hanging around with Luna though."

    ryu "Auntie?"

    ren "Yep."

    bl "It's propably due to his training with Mei. It's usually in the mornings, just not at 4 am like mine.
    Yet during that time we would always be on missions until this started."

    ryu "You know about that ?!"

    bl "Your sister tells me everything in order for me to figure out what I can help you on."

    ryu "I...I see."

    flo "Oh yeah we only came by because I thought you can take an S rank mission with us."

    bl "Today?"

    flo "Don't you want the cash?!"

    ren "So what now? Are you going to teach him starting today?"

    bl "I made a promise to them. I can't turn back now, it'll disrespect my honor to them and to their parents...especially him."

    ren "That's surprising coming from someone like you."

    bl "You know how it goes."

    ren "Yeah, yeah. Just let us know when you can take missions with us."

    bl "Sure thing."

    ryu "*looks down* You-nii..."

    bl "Geh! Anyways, Ryuu, hurry up with your meal."

    ryu "Oh Right! {p}*eats*"

    ren "Wow, he sure does eat a lot."

    bl "I hope I'll still have some savings left. *checks his wallet and looks at Ryuu's meals*"
    bl "-!! {p}*turns white* ....."

    log "*Blade slowly closes his wallet and looks defeated*"

    ryu "S-sensei?"

    ren "I'll help. *pats Blade's shoulder*"

    bl "REN! *covers his eyes with his right arm as he sobs into tears *"

    ryu "???"

    flo "You kinda destroyed his wallet."

    ryu "E-eh?! *looks surprised* Yo-you're paying for all of this?! I was planning to pay my portion! *gets embarrassed*"

    bl "H-huh? You are?!"

    ryu "I mean, since I do eat a lot. If I can't cook my own due to things... I usually just transfer the bill to Mei... *turns red*"

    bl "-! {p}*tries not to laugh but then looks serious*"
    bl "No! This will disrespect my honor! I'll face the judgement of this bill and...!"
    bl "Huh? *looks at his left*"

    ryu "What?"

    bl "Someone is coming this way."

    ryu "Hmmn? -! {p}*shivered* ( This familiar sensation..!)"

    log "The girl suddenly jumps and interrupts Ryuu's conversation."

    mys "Ryuu-nii! *hugs Ryuuji on the side*"

    ryu "Gah! *his face falls onto the plate* {p}L-Lyra?! *gets up*"

    ly "It's been so long!"

    ryu "Man, you made me got food all over my face. *wipes the food off*"

    ly "Koji and I finally get to see you though!"

    log "Ryuuji recalls part of their past and looks a bit nervous."

    bl "This seems similar."

    ren "I can see an resemblance."

    flo "Hey we're not alike!"

    log "Another friend besides Lyra comes up to them and bows respectively. He opens his notebook and flips through a blank paper and writes."

    ren "Hmn?"

    koji "*shows them his notebook* Sorry to intrude. {p}I'm Koji.... {p}she's Lyra, we're Ryuu's friends."

    ren "Ah, don't mind. We're about to leave soon. So are those two."

    koji "-?"

    ryu "Lyra, please get off. I'm still trying to eat...."

    ly "Aw. *then looks at Blade in confusion*"

    bl "*nods*"

    ly "Who are they?"

    ryu "Sensei and his friends."

    ly "-! Sorry to intrude."

    log "Lyra bows to Blade politely."

    bl "Don't mind, I take it you hadn't managed to see them yet?"

    ryu "*nods and looks upset* After that day, I was just scared and confused.
    Even though they tried to help me but back then...I can't recognize anyone at all."
    ryu "It was all blank... {p}But it feels like you guys are more worried then I am.... {p}I'm sorry."

    ly "No what are you saying? We're just glad you're finally you again. Right Koji?"

    koji "*nods in relief*"

    bl "See? Not all that bad."

    ryu "I guess not."

    ly "Hey after your lessons why not check out the academy with us?"

    ryu "The academy?"

    bl "She made a good point. It's a place were you get to meet all your mages at the same age you kids are now.
    {p}It's also great to get to know more and understanding teamwork."
    bl "In this guild if you want to take on missions, you'll need to form a team."
    bl "Sometimes even the two of your other friends need to be with someone else if things get rough. Three people is the max rule to join a mission."

    ryu "Is that so?"

    bl "But before that all started, let's head back to training. I need to toughen up your defense skills."

    ryu "Right!"

    ly "Aw you're leaving?"

    ryu "Sorry Lyra, it's really important."

    ly "Koji and I will be always waiting for you."

    koji "*nods*"

    ryu "Koji, I want you to look after her for us."

    koji "*nods and shows Ryuuji a paper* (You can count on me, be careful.)"

    ryu "I know. Thanks man."

    log "Koji then stares at Lyra and pulls her as he grabs her hood from behind. He then tries to drag her so they can leave."

    ly "K-koji? What are you doing? Oh man! Bye Ryuu-nii! Check out the academy sometime!"

    ryu "You better not get into much trouble, follow Koji you hear?"

    ly "I know!"

    bl "Who's the girl if I might can ask?"

    ryu "Lyra...she's kind of spoiled."

    bl "Spoiled?"

    ryu "Koji and I helped her out when she was being bullied by the kids in our neighborhood before the incident."
    ryu "She doesn't have a family to begin with so I decided to take her in as an adoptive sister I guess."

    bl "That's surprising coming from you."

    ryu "It's not wrong is it?"

    bl "*smiles* Nope, not at all. Sorry Ren and Florence, looks like your mission have to wait."

    ren "We'll just take an easy one then."

    flo "No fair! Ryuu let's battle next time!"

    ren "In your dreams, he's not ready yet. We'll wait for you Ryuu. Since you're a student of Blade's you're welcome to train with us as well. Just say the word."

    ryu "T-thanks!"

    bl "*smiles*"

    ryu "Is she strong?"

    bl "Sure is...they're my team mates after all."

    ryu "*gets excited* I can't wait any longer. Let's hurry up and train! I'm full already, let's go!"

    bl "*smies* Alright let the training finally resumes."


    #Chapter 3



    # This ends the game.

    return
