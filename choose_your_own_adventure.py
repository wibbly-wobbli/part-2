name = input('Type your name: \n')
print ('Welcome', name, 'to the game. It is incredibly important that you follow the instructions to a T, if you do not. The consequences may be dire. Have fun.\n')

answer = input('You are in the middle of a forest. The only items you have on your person are leather armour and a shortsword. The path you are taking splits into two seperate routs. Would you like to go left or right? \n').lower()

if answer == 'left':
    l1 = input('The trees thin after traveling for some time, leading you to a small clearing lit by the sun scattering through the treetops. Enter 1 or 2.\n')
   
    if l1 == '1':
        l2 = input('You enter the clearing carefully keeping an eye on your surroundings. But not steathily enough. An orc spots you, glaring down at you. Enter 1 to flirt, 2 to fight, or 3 to run.\n')
        if l2 == '1':

            l3 = input('You decided to flirt with the orc. He blinks at you, startled by your boldness. "Bold. Commendable." Enter 1 to flirt again or 2 to try to fight him.\n')
            if l3 == '1':
                print('You have successfully seduced the orc. He takes you home and marries you. Some time later, you die in a very bloody battle with an opposing clan.\n')
            elif l3 == '2':
                print('You decided to fight the orc. Too bad you don\'t know how to wield that shortsword you\'re carrying.')
            else: 
                print('You committed scooter ankle because apparently you cannot read instructions.')

        elif l2 == '2':
            l4 = input('You decided to try and fight him. Somehow, you kill him. To your surprise, he also happens to be the chief. That clearing you just entered? Well, it is the sacred grounds of the chieftain. Do you wish to accept the position of the chieftain? (yes/no)')
            if l4 == 'yes':
                print('You become chieftain with no issues. You live for another year before you are slaughtered in your sleep.')
            elif l4 == 'no':
                l5 = input('You leave quickly, making your way down the path hurrying down the path.')
            else:
                print('You leave.')

        elif l2 == '3':
            print('You ran? Pathetic. You lose.')
        else:
            print ('You died. Reread the instructions.\n')

    elif l1 == '2':
        print('You enter the clearing without care. This allows the orc lumbering there to spot you long before you do him. He kills you before you have the opportunity to pull your weapon.\n')
    else: 
        print('You died. You really cannot listen to instructions, can you? \n')


elif answer == 'right':
    print('The pathway leads towards a river. The current is slow enough for you to swim across but there is also a boat. Enter 1 to cross with the boat, 2 to cross by swimming, or 3 to follow the river.')


else:
    print('Dead already? You forgot the instructions, didn\'t you?')

