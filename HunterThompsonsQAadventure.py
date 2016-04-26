invalid_input = True
def start() :
    print('''
    \n\t\t -------------------------------------------
    \t\t Hunter S. Thompson's QA Adventure!!
    \t\t Use the number keys to enter a response!!!!
    \t\t -------------------------------------------
\nWARNING: Very NSFW!!! Make sure nobody's looking over your shoulder!!!
DO NOT CONTINUE if you have no sense of humor or can't take a joke!!!!
\nAlso... all info about chemistry stuff in the game is factually correct!!!
You might even learn something!!!
\nYou, Hunter S. Thompson, have been brought in to the company to help with
QA. You've been working at this office for about a year. With this job,
you've been employing a new strategy to get through the day: DRUGS!!
\nOn your way into work this morning, you overhear a manager
arguing with an executive about the quality system...
Obviously danger is afoot!! Be careful!!!
\nKnowing that today is probably going to be boring and frustrating, pick
your poison:
\n1. LSD - Nothing like a few extra colors to make the day more interesting!
2. Alcohol: the only option that's been through the quality system
3. Weed, man. Those vending machines downstairs have muffins, you know
4. Speed - WAAAAYYY better than coffee!!!
5. Crack, because you have way too many teeth anyway
6. Just coffee. (You're boring.)
    ''')

    drg = input()

#lsd
    if drg == "1": #done!!!
        print ('''You reach into your pocket for a tab and put it under your tongue,
then go get a cup of coffee while you wait for it to kick in.
\n WAIT!! Did you hear that???
1. YES WTF WAS THAT
2. You're not tripping THAT hard... yet...
        ''')

        lsd = input()

        if lsd == "1":
            print('''You start to listen a little more closely....
It sounds like a train!! Like a very specific train....
You realize that you're having a flashback! You start
to be blinded by the light that keeps getting brighter
and brighter!!!
\nYou're now fully immersed in the flashback...
\nYou're stopped on High Street (HAHAHAHA HIGH STREET),
waiting for the train to go by. You watch your car's clock
ticking, ticking, ticking.....
You know that you're gonna be late for a 9am meeting. You
start getting stressed out! Then you start to hear gunfire
and explosions!!
\nThe train blew up and is permanently stuck on the tracks!!
You have no way of getting to work at all, and ESPECIALLY
no way of getting to the meeting on time!
\nWhat do you do???
1. Freak out
2. REALLY freak out
            ''')

            frk = input() 

            if frk == "1" or "2": #only one choice here
                print('''Yeah, what else can you really do at this point?
You freak out and jump out of the car, doing what looks
to others as some kind of weird lunatic dance. (Because
honestly, that IS what you're doing.) As you're dancing,
you slowly start to realize that you're actually doing the
dance in real life too... and coworkers around you have started
watching and being like wtf are you doing.
\nHow do you react to this madness???
1. Take a bow!!
2. Be all indignant and shit and ask why they can't
respect your privacy, goddammit!!
                ''')

                mad = input()

                if mad == "1":
                    print('''You take a bow. Everyone starts to clap!! They
thought your lunatic dance was great!! You bow
a couple more times, then make a quick acceptance
speech for being the best dancer EVER. Then they leave
and you continue going about your business, hearing
colors and seeing sounds and all. You actually have a fun
day at work, FOR ONCE, once you get there. I think that's considered
a win!
\nYay!!! You win!!!
\nI think I'd recommend trying again and choosing a different
path, since this was one of the shorter ones....
                    ''')

                elif mad == "2":
                    print('''You mouth off to your coworkers, but you can't help
but slur your words cuz you're all fucked up.
They think you're drunk and report you to the boss!
\nBad news....
\nYOU LOSE!!!!
Here, try again.
                    ''')

        elif lsd == "2":
            print ('''You go back to get some more coffee, but when you do,
you notice that your coworkers are looking at you like you
have two heads - but probably only because they don't know how
goddamn good LSD can be. You ignore them and get back to work.
You start to write yet another fucking test case, when the words
begin to come out from the screen and go straight into
your eyeballs!!! YOOUUURRRR EYYYYEEEESSSS!!!! WHAT THE FUCK
DO YOU DO NOW????
1. SCOOP THOSE FUCKERS RIGHT OUT
2. I dunno man, you haven't even really said what the
problem is. They're just words.
            ''')

            lsd2 = input()

            if lsd2 == "1":
                print('''You go into the kitchen area to look for a spoon,
but none of them are sharp enough!! OH NO!!!! You
have to find an alternative now! What other utensil do
you look for??
1. Fork
2. Knife
                ''')

                uti3 = input()

                if uti3 == "1" or "2":
                    print('''That's no good for scooping!! Or are you too messed
up to tell??
\nEither way, you don't find a suitable utensil, so
you give up on your scooping plans.
\nWait a second....
\nYou realize you don't have to give up on your scooping
plans after all! You go to the nearest female coworker,
and go SCOOOOOOOOOOOP!
\nShe screams, because really what else is somebody going
to do when you randomly scoop them without warning.
\nShe reports it to HR immediately, and you get fired for
harrassment.
\nBut on the other hand, no more test cases or SRS's to write!!
It's a win after all!!! There were probably ways to win
without scooping a random person though.... Hmmm....
\nYou get to start over and try again!
                    ''')

            elif lsd2 == "2":
                print('''YEAH, WORDS THAT'LL TURN ON YOU THE FIRST CHANCE THEY GET!!!
YOU GOTTA DO SOMETHING!!!!! WTF YOU GONNA DO MAN???
1. Ok, freak out after all.
2. SCRIBBLE ALL OVER YOUR SCREEN WITH A PERMANENT MARKER.
THAT WAY IT'S PERMANENT.
....PERMANENT.
\nPERMANENT.
                ''')

                scr = input()

                if scr == "1":
                    print('''You freak out after all, but can't do it for too long
because one of the creeper security guys runs over
and tackles you, just because he was bored!
\nWHY YOU??? DOES HE KNOW????
\nYou decide that somehow HE KNOWS, and you promptly freak
out, again but even more, and fight him off. As soon as you
get him off of you, you run for the nearest exit!
\nYou make it outside, but then they sky and all the
buildings start melting!! You don't know what to do!!! But
just as you're deciding your fate, the security guy jumps
out from the bushes and tackles you again! You're forced
to the ground! He's getting his stink all over you!!!
\nThe security stink causes you to wilt into a puddle on
the ground...
\nSoooo you pretty much lose the game...
\nHere, start over and try again!! You don't have a choice!!
                    ''')

                elif scr == "2": 
                    print('''You scribble ALLLL OVER both of your monitors with
a permanent marker! It makes you feel SOOOO good!
But your boss comes over and asks wtf you're doing, and
you tell him that you just got too fucking frustrated and
couldn't deal with life anyore. He understands, and orders
you a couple more monitors, ones that are even newer and
nicer! Then you get the rest of the day off for being
"an honest employee" and go home and continue to trip balls!
\nYOU WIN!!! CONGRATULATIONS!!!
\n1. Wanna quit?
2. ...or try again?
                    ''')

                    scr2 = input()

                    if scr2 == "1":
                        print("Ok then.")
                        exit()

                    elif scr2 == "2":
                        print("Yay, excellent choice!!")

#alcohol
    elif drg =="2": #done
        print ('''Well at least you're using the tried and true QA helper.
You wander over to the QA beer garden. What kind do you choose?
1. IPA
2. Red ale
3. Porter
4. Stout
5. Mead, bitch!
        ''')

        bur = input()

        if bur == "1" or "2" or "3" or "4" or "5":
            print('''Just kidding!!! ALCOHOL!?!??!? You're picking
ALCOHOL for Hunter Thompson's QA Adventure????
\nDo you even know who Hunter Thompson is????
\nStart over and make a more interesting choice.
            ''')

#weed
    elif drg == "3": #finished
        print ('''Well, that's kind of a tame choice for this program, but OK.
Good thing you have a card and have access to the good shit.
You reach into your pocket and pull out a strong edible, then eat it.
What do you do while you wait for it to kick in?
1. Practice with Python, duh
2. Go bug one of your underlings about shit they need to get done
        ''')

        wed = input()

        if wed == "1":
            print('''Apparently great minds think alike!! You sit down at your
computer and start Python. You get a crazy idea for what
project to start next... a QA adventure story!! What genius!!
You start to write, and this is what comes out.....
            ''')

        elif wed == "2":
            print('''You head over to talk to your poor fool of a coworker.
You bug him about all the shit that needs to get
done by some ridiculous deadline, and you also bitch
and moan quite a bit because you hate your fucking 9-5 life.
He seems sympathetic though...
\nSympathetic enough to share his secret drug stash with you!!!
\nHe reaches into his backpack and pulls out some white
powder, and hands it to you. You don't ask what it is because
you like surprises. You go back to your desk and take it immediately.
\nYou wait for it to kick in....
\nThen you get a sudden urge to take off all your clothes and
run around in the street, and fight cars with swords!! Your
whole body feels numb and you feel like you have +50 strength!!
\nHmmm, sounds like that might've been PCP...
\nUh oh, you've heard about the crazy shit people do when they're
on PCP.... but you bought the ticket so you gotta take the ride!!!
You only really have one option here...
1. TAKE OFF YOUR FUCKING CLOTHES AND GO FIGHT A CAR WITH A SWORD
\n(TOLD YOU WEED WAS TOO TAME, HAHAHAHAHAHHAHAHAA THIS IS WHAT YOU
GET FOR PICKING IT!!!!)
            ''')

            fgt = input()

            if fgt == "1": 
                print('''You run outside of the building, strip down, and
flex your giant-looking muscles! You grab the sword that
descends from the heavens, just for you!!! You take it and
start attacking the nearest parked car!!!
\nThe car puts up a good fight!! It won't back down or
admit defeat!! All it's doing is screaming a little...
\nSuddenly, in the middle of your attack, you start to hear
a familiar voice....
\nIt's your ex boyfriend/girlfriend/husband/wife!!! They are
inside your head for their revenge for whatever it was you did wrong
that you never exactly figured out!!!
\nWhat on earth do you do??? How do you deal with even MORE of
their bullshit????
1. Just walk away
2. Start screaming at them!!
                ''')

                wlk = input()

                if wlk == "1":
                    print('''I'm not sure why walking somewhere would affect what
you hear, but okay..... you do your best to walk away
nonchalantly....
\nSomehow it works, because that's the kind of logic we're
dealing with here!!
\nYou walk back into the office like nothing happened... then
you realize that you forgot to put your clothes back on!! Sounds
like nightmare fuel to me!! But then because you're all fucked
up & high, you don't really care. So you go to your desk, naked, and
start working on another one of those damn test cases.
\nYou boss comes in and sees you working on a test case naked,
and asks you wtf. What do you tell him??
1. THE TRUTH
2. That all the computers in the QA area just made it too hot and
you just got too fed up to deal with it, plus you want to
establish your dominance by having the best looking ass around.
                    ''')

                    tel = input()

                    if tel == "1":
                        print('''You tell your boss the truth and much to your surprise,
he listens and even seems sympathetic! He shoos (shooes? whatever)
you into his office and shuts the door, then starts telling you
an old story about 'Nam and how soldiers used to take drugs to
say awake & stuff! Then he reaches into his bag and pulls out...
MORE DRUGS!!! He even shares, how nice of him!!
\nNow that you've found an office drug buddy, you finish
out the day and come back the next day with a very optimistic
attitude. You hit him up for more, and he delivers! Looks like
you found yourself a sweet deal!! YOU WIN!!!
Wanna start over or quit?
1. Start over
2. Quit and be a dick
                        ''')

                        tel2 = input()

                        if tel2 == "1":
                            print("Yay, good choice!!")

                        elif tel2 == "2":
                            print("FINE THEN")
                            exit()

                    elif tel == "2":
                        print('''You tell that to your boss, and he laughs, but then
forcefully requests that you put on some fucking clothes.
You do that, and then you finish writing that test case. You
mark it ready for review so your boss can look it over before
it's approved & run.
\nThe day is pretty much over now, so you head home to
CALM THE FUCK DOWN and go to bed.
\nThe next day, you come back into work and try to act like
nothing unusual happened. (Because, let's face it, nothing about
this whole situation was unusual for you.) Your coworkers try
to act normal around you too.
\nEveryone pretends like nothing happened... So now you're left
with a choice. What drug do you pick today???? Start over & pick!
                        ''')

                elif wlk == "2":
                    print('''You start screaming at your ex S.O.!!! They start to
give you their usual bullshit though! But this time,
because you're all high as shit, you know exactly what to
say to get them to shut the hell up!
\nI think you can consider that as winning the game!!!
\nHere, start over and see what other kinds of nonsense
you can find!!!
                    ''')

#speed
    elif drg == "4":
        print ('''You hit up one of the guys with an Adderall prescription and offer
to trade the rest of your real Sudafed for a couple pills. He seems
reluctant to accept your trade though. What do you offer to sweeten
the deal?
\n1. Bring him a cup of coffee
2. Bring him a beer from the QA beer garden 
3. Mention that pseudo can undergo a simple reduction reaction
to make something much more interesting.
        ''')

        dlt = input()

        if dlt == "1":
            print ('''You offer to bring him a cup of coffee. He says no.
Then you offer to bring him coffee for the rest of the week
whenever he emails you... this works. He gives you a couple
caps!! You take them all because you're Hunter Thompson
and that's what you do!!
\nAfter 30-45 minutes, you start to feel it kick in. You
feel like you could DO ALLLL THE SRS'S!! ALLLLLL THE
DOCUMENTATION!!! ALLLL THE THINGS!!!
\nSo what's your next move?
1. DO ALL THE FUCKIN THINGS
2. DO ALLLL THE FUCKIN THINGS
3. DO ALLLLLLL THE FUCKIN THINGS
            ''')

            fin = input()

            if fin == "1" or "2" or "3":
                print('''YOU GO SIT AT YOUR DESK AND START DOING ALL THE
THINGS. AS SOON AS YOU GET STARTED THOUGH, AN EXECUTIVE
COMES INTO YOUR OFFICE BEING ALL CRANKY & SHIT!!!
WHAT THE FUCK DO YOU DO?????
1. GO RAMBO ON THEIR ASS BECAUSE THEY DESERVE IT
2. YELL AT THEM FOR SETTING RIDICULOUS RELEASE DATES
SO EVERYONE CAN HEAR!!! SOMEONE'S GOTTA DO IT!!!
                ''')

                yel = input()

                if yel == "1" or "2":
                    print ('''HELL YES SOMEBODY'S GOTTA DO IT. FINALLY!!!!
\nThe executive starts talking shit to you about how
we're not gonna make the release date for one of the
products, but you GIVE NO SHITS!!!! YOU YELL AT THEM
FOR BEING A DUMBASS!!!
\nAfter you're done yelling, the executive stares at you
like a deer in the headlights... nobody's ever yelled at
them quite like this before!! They actually admit that the
release date they set is totally NOT GONNA HAPPEN!!!
\nI think you can pretty much consider that as winning the
game. Congratulations!!!
\nWanna start over or exit?
1. Start over!
2. Exit!
                    ''')

                    yel2 = input()

                    if yel2 == "1":
                        print("Good choice!!!")

                    elif yel2 == "2":
                        print("FINE, at least you won!!!")
                        exit()
                              
        elif dlt == "2":
            print ('''You bring the Adderall guy a beer from the majestic QA
beer garden. It works!! He gives you a couple caps!!
You take them immediately, because DUH
\nYou start to feel them kick in, then you write
ALLLLL THE SRS'S!! ALLLL THE DOCUMENTATION!!! ALLLLL THE
TEST CASES!!!!
\nAnd now your workday is done. You get to leave early!! You
go home and do whatever you like to do when you get high.
YOU WIN!!!
\nI'm gonna force you to start over now, because this was one of
the shorter possible outcomes. Try a new path!!
            ''')

        elif dlt == "3":
            print ('''THAT'S THE SPIRIT! SCIENCE, BITCH!!!
You describe the reduction reaction to him, mentioning
that it would make Walter White proud. Walter White is your
alter ego, you see.
\nYour coworker is wary of the noxious fumes that would
be produced though. So you tell him about the hazardous
materials equipment you already own! He's convinced!
\nYou tell him to meet you after work so you can show him how
to do the reaction. Looks like those organic chemistry classes
you took are finally coming in handy!
\nYour coworker gives you a couple caps, and you plan to meet
after work. So you go about finishing your boring day, but on
speed. What do you suggest when you meet him after work?
1. Go out to that abandoned RV you know of & do the reaction
2. Go to your house to do the reaction, where all of
your equipment is.
                   ''')

            met = input()

            if met == "1":
                print ('''Walter White would be proud. You both head out
to the abandoned RV. And because it's abandoned and
out in the middle of nowhere, you don't get caught and the
noxious fumes can just escape through the convenient
ventilation system that happens to be already installed!!
\nIt's almost like you've been here before....
\nWhat do you do once the reaction is done?
\n1. Sample the product, of course!!!
2. Test for purity & contaminants first!!
                       ''')
                pur = input()

                if pur == "1":
                    print ('''After the recrystallization is finished, you use a 
Buchner funnel (which also just HAPPENS to already be in the RV)
to vacuum dry the crystals. Then you have a little taste.
\nIt seems pretty good, but kind of stings your nose a little.
You wait for a while, but feel only a little more energetic -
definitely not as much as you were expecting. What do you do to
troubleshoot??
\n1. Do spectroscopy to check for the presence of unwanted stereoisomers
2. Do thin-layer chromatography to check for the presence of the
desired product
                    ''')

                    pur2 = input()

                    if pur2 == "1":
                        print ('''And where the hell do you think you're going to
get that spectroscopy equipment in an abandoned RV??
\nDUH.
\nStart over and try thin-layer chromatography instead maybe?
\nOr just quit. I don't care.
\n1. Start over!
2. Quit and be a dick
                        ''')

                        pur3 = input()

                        if pur3 == "1":
                            print("OK!! Good choice!!")

                        elif pur3 == "2":
                            exit()

                elif pur == "2":
                    print ('''You quickly put together a TLC rig and dot
the product on the baseline of the silica plate. Then
you put the plate in a jar with the correct solvent. (Which
you ALSO just HAPPEN to know and have around.) You wait a few
minutes for the solvent to creep up the silica plate & separate the
product, then you evaluate the chromatogram. You visualize it under
regular light, UV light, and with iodine too, just to be thorough.
\nYou realize that what you made is mostly composed of one of
the unwanted stereoisomers, propylhexedrine!
\nWhat on earth do you do????
1. Just eat the stuff instead
2. Throw it out and go buy the Adderall guy a beer, & admit failure.
                    ''')

                    pro = input()

                    if pro == "1":
                        print ('''Now that's some good thinking! Propylhexedrine
does work as a stimulant when taken orally.
\nEveryone's happy now!!! You win the day!!!
\nI'd suggest starting over and taking a different route, as this
was one of the shorter ones.
\n1. OK!!
2. No way man this is way too sketchy for work
                            ''')

                        ext2 = input()

                        if ext2 == "1":
                            print ("Yay! Here you go!!")

                        elif ext2 == "2":
                            print ('''Well what did you think you were getting into when
you signed up for Hunter Thompson's QA adventure?!?!
Just for that I'm going to make you KILL my precious
program. Murderer.
                                ''')
                            exit()

                    elif pro == "2":
                            print ('''You throw out all of your product and go get beers
from the QA beer garden, because that way they're free.
When you're sipping on your wonderful porter though, you realize
something....
\nThe stereoisomer you found in the product, called propylhexedrine,
is active when taken orally!! Uh oh!! You just wasted some potentially
good shit!!!
\nAfter realizing that you kind of failed a little with your
pharmacology knowledge, you get a second, then a third, then a
fourth beer from the QA beer garden.
Probaboy would've been easier to just go for beers in the first place,
since that's where you ended up.....
\nYou fail.... Try starting over.
                            ''')
                            
            elif met == "2":
                print ('''Good choice. It's always smart to do your work
with the proper equipment available. That's what you
home lab is for, of course!! You guys make the stuff from
the pseudo with the iodine and phosphorus that you just HAPPEN
to have around, then you check out your product before you sample
it. You perform spectroscopy and thin-layer chromatography to
check for the presence of unwanted stereoistomers.
You find nothing unusual! Your product is pure! Congratulations!
\nWhat's your next step??
1. Celebrate & do a dance! Then take it!
2. Have a celebratory beer, then take it!
3. JUST TAKE IT GODDAMMIT
                ''')

                stp = input()

                if stp == "1" or "2" or "3":
                    print ('''You give yourself a pat on the back for successfully
finishing the reaction without blowing anything up, although
that could've been fun too. You divide the stuff carefully
between you and the Adderall guy, then you take that shit because
that's what it's for.
\nYou begin to feel the effects almost immediately. You feel
like you could defeat Sauron in a single blow! What's your next
move, now that you're feeling so good?
1. Run around like a maniac
2. Stay up for 3 days straight, writing code the whole time
3. Quit Hunter Thompson's QA Adventure, because mission accomplished!!
                    ''')

                    fel = input()

                    if fel == "1":
                        print ('''YOU RUN AROUND THE RV LIKE A MANIAC!!!
SO DOES THE ADDERALL GUY!!! YOU ARE BOTH HIGH AS SHIT!!!
You head back to work and get a bunch of shit totally
done!!! The boss doesn't notice anything unusual about
you guys, because you're normally pretty weird anyway,
and gives you both promotions & raises!!
\nMoral of the story: Drugs are good if used properly!!!
\nCongratulations, you win at life!!! (Or at least this game.)
\nWanna start over or exit?
1. Start over
2. Exit
                        ''')

                        prt = input()

                        if prt == "1":
                            print ("Excellent choice!!")

                        elif prt == "2":
                            print ("FINE THEN")

                    elif fel == "2":
                        print ('''You leave the RV and go home. You start up
Python. You decide to write a drug-themed choose your
own adventure story!! What a wonderful idea!! Unlike
this one though, you finish yours in only 24 hours.
You use the rest of your high time to RUN AROUND LIKE
A MANIAC because what else is there to do?? Maybe go
shopping and spend all your money? Maybe go make some extra
$$ hooking downtown?? Practice more Python??? QUIT
THIS GAME???? START THE GAME OVER????
\n1. Quit
2. Start over!
                        ''')

                        prt2 = input()

                        if prt2 == "1":
                            print ("Well ok")
                            exit()

                        elif prt2 == "2":
                            print ("Yay!! Have another adventure!!!")

                    elif fel == "3":
                        print ("OK! Now go defeat Sauron and save the world!!!")
                        exit()

#crack
    elif drg == "5":
        print ('''Yeah, teeth are overrated. Dentists can just rebuild them nowadays.
Besides, you're going for that Richard Pryor look.
You sneak into the bathroom that nobody ever uses and light up.
You finish smoking, and then go to your desk to start the day.
\nWhen you get back to your desk, you get a brilliant idea!!
You think that if you automate some of the tests for one of the hot new
company products, you could release it a month early, easy!
\nDo you implement the automation and tell everyone about your idea?
1. Yes!! \n2.No way man, not yet
        ''')

        crk = input()

        if crk == "1":
            print ('''You start writing the code, but then you get another brilliant idea!
You could write a choose your own adventure QA story!
(Oh yeah, I just went meta on your ass)
But really, do you finish the automation code or write the QA story?
1. Finish the code \n2. Write the QA story
            ''')

            sty = input()

            if sty == "1":
                print ('''You finish the code for automating the product testing,
and you're so confident in it that you don't even email it to
your boss first for him to check it over. You send it to
the whole company because all of these poor fools need to
get ahold of themselves and learn how to get shit done
around here. \nA few minutes later, your boss walks in to
your office with a weird look on his face....
1. Tackle him & show him who the boss really is!!!
2. Jump up onto your desk and beat your chest like a gorilla,
because you ALSO sipped on a little of that pink adrenaline...
                ''')

                jmp = input()

                if jmp == "1":
                    print ('''You tackle him and take him down!!
But then you realize that you didn't really think any
farther ahead than that... so you decide to roll around
on the ground for a while, then write an SRS about it.
\nThe SRS turns out to be brilliant, and even though your
boss didn't fare so well, you get a promotion for your
BRILLIANT writing!!!! \nWanna start over and choose another drug?
1. OF COURSE!! \n2. Naw man enough of that crack
                    ''')

                    ext = input()

                    if ext == "1":
                        print ("You're apparently my kind of person.")

                    elif ext == "2":
                        print ('''Well, I guess that's it then... could've been better...
At least I got mine...
THE END!!!
                        ''')
                        exit()

                elif jmp == "2":
                    print ('''You jump up onto your desk and LET IT OUT! RRAAAWWWWRRRRR!
Your boss continues to look at you funny...
What do you do this time???
1. Hit him over the head with a SRS
2. Hit him over the head with an old bug report
3. Hit him over the head with an old beer bottle from the
QA beer garden
                    ''')

                    lok = input()

                    if lok == "1" or lok == "2":
                        print ('''You grab the documentation and strike!!
Your boss appears dazed... What do you do now?
\n1. Leave the area, since you've done your job.
2. Strike again!! Show no mercy when it comes to documentation!
                        ''')

                        ske = input()

                        if ske == "1":
                            print ('''You leave the area, documentation in hand.
On your way out, your boss throws a surprise SRS at you.
WHAT IS THIS MADNESS???? You thought you'd finished that SRS!!
\nHow do you react???
1. Visit the QA beer garden & drown your sorrows
2. Curl up in the fetal position and rock back & forth
                            ''')

                            fet = input()

                            if fet == "1":
                                print ('''Good choice! You visit the QA beer garden and
pick out a strong IPA and drink it.
What now?
1. Start over and choose another drug!!
2. Quit because you had too much to drink in the QA
beer garden.
                                ''')

                                ipa = input()

                                if ipa == "1":
                                    print ("Yay! Here you go!")

                                elif ipa == "2":
                                    print ("FINE THEN.")
                                    exit()
                                
    
                            elif fet == "2":
                                print (''' You do just that, but then an executive comes in and
sees you! You get yelled at for not being productive
and not doing somebody else's job well enough!!
You decide that enough is enough and you resign right
then and there.
\nNow the madness is finally over.
\nYou're finally FREE!!!!!
\nYou win!!!!!
Wanna start over?
                                ''')

                                stt = input()

                                if srt == "1":
                                    print ("Yay!! Here you go!!")

                                elif srt == "2":
                                    print ("FINE.")
                                    exit()

                        elif ske == "2":
                            print ('''You force the outdated documentation on him again!!
He winces for a split second, but then his QA stoicism sets in!
He is unaffected by the outdated documentation!!
\nYou just lose.
Sorry. Just start over and might I recommend CHOOSING SOMETHING
BESIDES CRACK. Just a suggestion.
                            ''')
                        
                    elif lok == "3":
                        print ('''Well that's kinda harsh, jeez.
Maybe start over and try something other than f*cking CRACK?!?!?
Now there's an idea! \nWant to start over?
1. Yes! No more crack for me! \n2. Nope, crack rules!
                        ''')

                        stt = input()

                        if stt == "1":
                            print ("Yay! Here you go!!")

                        elif stt == "2":
                            print ('''Well too bad, you're going to start over anyway.
I have a feeling that forcing reason upon you isn't a
terribly bad idea.
                            ''')

            elif sty == "2":
                print ('''You open up Python and start to write a choose your own
adventure story. What's going to be the theme of your story?
1. DRUGS, DUH \n2. Just daily life in the QA department
                ''')

                qa = input()

                if qa == "1":
                    print ('''Well you're in the right place!!!
....Here you are!
Would you like to start over and choose a different drug??
\n1. Yes!! \n2. Nope.
                    ''')

                    qut = input()

                    if qut == "1":
                        print ("Yay!!")

                    elif qut == "2":
                        print ('''Well you're just a bucket of fun aren't you.
Maybe check out Ariel's QA Adventure?
THE END
                        ''')
                        exit()

                elif qa == "2":
                    print ('''WELL I GUESS THIS IS OVER THEN ISN'T IT.
THE END!!!!
Would you like to start over again and try to make more
reasonable choices you twat? \n1. Ok!! \n2. Nope
                    ''')

                    ext = input()

                    if ext == "1":
                        print ("GOOD!!!")

                    else:
                        print ("Are you serious??")
                        print ("THE END!!!!")
                        exit()

        elif crk == "2":
            print ('''You test out the code at your desk first, and it seems to work.
But then you start to feel a wave of energy come over you...
You jump up onto your desk and beat your chest like a gorilla
to celebrate your code victory!!!
Your boss hears the  commotion and steps out of his office to
see what the hell you're doing. He doesn't catch you until you've
jumped off of your desk and stopped, but he looks at you like
HE KNOWS EVERYTHING.
\nWhat do you do???
1. Intensely stare back at him until your dominance is established
2. Offer him some of what you had.
            ''')

            ofr = input()

            if ofr == "1":
                print ('''You stare, you stare, and you stare some more....
Your boss eventually gets the idea that something's up with
you, and asks wtf you're on.
You tell him the truth because in your current state of mind,
you can't tell that saying you're on crack is a bad idea.
He stares at you for a second, then suddenly says, 'Well
wtf are you doing not sharing that shit?'
Now you stare at him for a while... again...
\nWhat do you do next?
1. Keep staring
2. Share the wealth, because you have such a kind heart
...And also you think it would just be fun to see your
boss on crack.
                ''')

                shr = input()

                if shr == "1":
                    print ('''After even more awkward staring at your boss, he eventually
just walks slowly back into his office, backwards, and then
turns and sits in his chair. He shakes his head and starts
typing something... going about his regular business.
\nThat's it.
\nYou know why that's it? Cuz you chose CRACK. I mean come on.
\nCRACK.
\nYou chose crack. For a Hunter Thompson QA adventure story.
\nWhat's wrong with you????
\nTHE END!!!!
\nNow I'm gonna make you KILL my PRECIOUS PROGRAM in order
to close it! Because that's the kind of thing you probably
enjoy, you sick bastard!
                    ''')
                    exit()

                elif shr == "2":
                    print ('''You give you boss a rock. He thanks you and goes into
his office and shuts the door. Five minutes later, you
see an executive go into your boss's office. Five more
minutes after that, your boss comes out and asks you to
come into his office to talk.
\nLong story short, you're FIRED!!!
Did you really think crack was a good idea? I mean come
on, there are so many better choices.
YOU LOSE!!!!
THE END!!!!
                    ''')
                    exit()

            elif ofr == "2":
                print ('''Are you f*cking serious?? Offering your boss crack???
But much to your surprise, he accepts the offer!!!
You have an office crack party and then you write
an SRS on it, because THAT'S WHAT YOU DO AROUND HERE.
\nThe SRS turns out brilliantly, because you and your
boss were both all energized and you actually used
some fucking TEAMWORK for once!
Great job!!! You win!!! \nWanna start over and go again?
1. Yes \n2. Nope
                ''')

                qit = input()

                if qit == "1":
                    print ("That's the spirit!!!")

                elif qit == "2":
                    print ("Well fine then. Be that way.")
                    exit()

    #coffee
    elif drg == "6": #DONE!!!!
        print ('''So yeah, you're apparently kinda boring. This was
supposed to be about a drug-fueled QA adventure, and
you just ruined it. \nTHANKS.
\nNow start over and pick a more reasonable option.
        ''')

    else: #DONE!!!
        print ('''Are you already too messed up to pick one of the valid numbers???
SHIT SON!!! Make sure you share some of that!
Here, start over and try again.
        ''')

while invalid_input :
    start()
