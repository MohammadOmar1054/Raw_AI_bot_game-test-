import random 
import math 
# import numpy 
break_line = '\n'
log_limit = 0 
ask_log_or_sign = int(input('Log in [1] or Sign Up[2] :'))
if ask_log_or_sign == 1:
    log_pass = "mama12"
    ask_pass = input("Enter Your Password , LunaticXXD :")
    while ask_pass != log_pass and log_limit <= 3:
        print('INCORRECT PASSWORD!!!!!')
        ask_pass = input("Enter Your Password , LunaticXXD :")
        log_limit+=1

else:

    print('We first have to encrypt our conversation by allowing you to create a password')
    list_sug_pass = list(range(1000,1000000))
    random_pass = random.choice(list_sug_pass)
    print('A suggested password: ', random_pass)


    sug_accp= input("Press '0' to accept or '1' to deny the suggested password: ")
    if sug_accp == "0":
        print('Password set to:',random_pass) 
        print('Protected boys')

    #  phase of security ]]      ]
    #  len pass != less 4 digs  
    # go on  

    elif sug_accp == "1" : 
        # print('length of the password should not be less than 4 digits')
        limit = 0
        cr_pass = input('Create a password:  ')
        if len(cr_pass) >= 4 and len(cr_pass) < 7:
            print('Behold thy comrade, We are henceforth secured ')
        while len(cr_pass) < 4 and limit <=4 or len(cr_pass)>7 :
            if limit == 4:
                loser = [
                    'LOSER', 'YOURE A LOSER', 'YOUVE WASTED ALL CHANCES ',
                        'CHANCES WASTED', 'OPPORTUNITY DEEMED SMALL', 'FINE, I WILL DO IT MYSELF'
                        ]
                print(random.choice(loser))
                print('Password is set to : ', random_pass)
                break
            print('lenght of the password should not be less than 4 or greater than 6 digits' , break_line ,'     you have', 4-limit,'more chances left')
            cr_pass = input('    Re-create your password mate : ')
            if len(cr_pass) >= 4 and len(cr_pass) <7:
                print('Behold comrade of mine , We are henceforth secured ')
            limit += 1

        # END OF SECURITY IMPLIMENTATION 
        

                # if len(cr_pass) >= 7:
                #     print('protected boys')
                # elif len(cr_pass) < 7:
                #   
list_ask_name = (
"What's your name ? : ", 'What can i call you? : ', 'Mind telling me your name? : ' , "What's your name pal? : ", "What's your name buddy? : ")
tell_name = input(random.choice(list_ask_name)) 

list_ask_sup = (
'I hope you are good,', 'U look fine today,' , "Hey,", "What's up, ", 'How is it going,', 'Oh Hey,', 'Good day,'
)

print(random.choice(list_ask_sup), tell_name)


    # affirmates = ['yes',"Yes", 'YES', 'ye', 'yep','YEP','Yep','Yeah','YEAH','yeah']
    # stro= ('Same thought[1]', 'Number guessing[2]' )


ask_play = str(input('Would you like to play a game? y or n : '))



    #USSER AFFIRMATES 


if ask_play == 'Y' or 'y':
    print('perfect')
    ask_which_game = int(input('Which game would you choose to play with me? Same thought[1], Programming Outputs [2] :'))

        
        #SAME THOUGHT   
    if ask_which_game == 1:
        replay_limit = int(
            input(
                'How many times would you like to play this game :  '
                )
                ) #5 

                
        print('You will chosse a number from a range depending on the difficulty and I will guess it ;)')
        ask_difficulty = int(input('Chose your difficulty Easy[1] Normal[2]  or Hard[3]: ')) 
        if ask_difficulty == 1:
            print(' Seems like you need Experiance :) ')
                
            replay_count = 1
                #CREATE LEVEL 1 SAME THIUGHT GAME 


            while replay_limit >= replay_count:
                pick_lvl_1 = int(input('Pick a number from in between 1-50 :' ))      #USERS PICK

                if pick_lvl_1 > 50:
                    list_of_out_of_range = (
                        'That is out of the range', 'that is beyond thy limit', 'that range is not for level 1 difficulty '
                        )
                    print(random.choice(list_of_out_of_range))
                    continue
                if type(pick_lvl_1) == str:
                    print('Thats not a number')
                print('Your pick is :', pick_lvl_1)
                    
                ai_guess_lvl_1 = random.choice(range(1,51))        #BOT guess
                print('My guess is :', ai_guess_lvl_1)
                    
                    # replay_limit+=1
                if pick_lvl_1 == ai_guess_lvl_1:
                    list_of_victory = (
                        'Oh yeah ! i guesed it right ', 'Bingo!' , 'Well Well Well','easy peasy',  'Here you go','Yeshhhh' ,' I am loving it'
                        ) 
                    print(random.choice(list_of_victory))

                        #### ########################################################################################################################## NORMAL DIFFICULTY  #####################################################################################
                        #############################################################################################

        elif ask_difficulty == 2:
            print('You seem like an experianced person')

            replay_count = 1 
            while replay_limit >= replay_count:
                pick_lvl_2= int(
                    input('Pick a number from in between 1-100 :'))  # USERS PICK

                if pick_lvl_2 > 100:
                    list_of_out_of_range = (
                        'That is out of the range', 'that is beyond thy limit', 'that range is not for level 2 difficulty '
                    )
                    print(random.choice(list_of_out_of_range))
                    continue
                if type(pick_lvl_2) == str:
                    print('Thats not a number')
                print('Your pick is :', pick_lvl_2)

                ai_guess_lvl_2 = random.choice(range(1, 101))  # BOT guess
                print('My guess is :', ai_guess_lvl_2)

                    # replay_limit+=1
                if pick_lvl_2== ai_guess_lvl_2:
                    list_of_victory = (
                        'Oh yeah ! i guesed it right ', 'Bingo!', 'Well Well Well', 'easy peasy',  'Here you go', 'Yeshhhh', ' I am loving it'                        )
                    print(random.choice(list_of_victory))

                else:
                    list_of_defeats = (
                        'Uhh', 'better luck next time ', 'i am pissed' , 'why are they so far away' , 'So close' , 'NOOOO'
                        )
                    print(random.choice(list_of_defeats))
                if replay_limit == replay_count:
                    print('Hence we have arrived at the play limit you chose, Choose a longer play limit next time :) ')
                    list_of_goodbyes = (
                            'See you soon pal !!', 'Was a fun time playing with you '
                            )
                    print(
                            random.choice(list_of_goodbyes)
                        )
                replay_count+=1


                        #### ########################################################################################################################## hard DIFFICULTY  #####################################################################################
                                            #############################################################################################
        else:
            print('I am afraid of your expertise ;-;')

            replay_count = 1
            while replay_limit >= replay_count:
                pick_lvl_3 = int(
                        input('Pick a number from in between 1-500:'))  # USERS PICK
                if pick_lvl_3 > 500:
                    list_of_out_of_range = (
                            'That is out of the range', 'that is beyond thy limit', 'that range is not for level 3 difficulty '
                        )
                    print(random.choice(list_of_out_of_range))
                    continue
                if type(pick_lvl_3) == str:
                    print('Thats not a number')
                print('Your pick is :', pick_lvl_3)

                ai_guess_lvl_2 = random.choice(range(1, 501))  # BOT guess
                print('My guess is :', ai_guess_lvl_2)

                    # replay_limit+=1
                if pick_lvl_3 == ai_guess_lvl_2:
                    list_of_victory = (
                            'Oh yeah ! i guesed it right ', 'Bingo!', 'Well Well Well', 'easy peasy',  'Here you go', 'Yeshhhh', ' I am loving it'
                        )
                    print(random.choice(list_of_victory))

                else:
                    list_of_defeats = (
                            'Uhh', 'better luck next time ', 'i am pissed', 'why are they so far away', 'So close', 'NOOOO'
                        )
                    print(random.choice(list_of_defeats))
                if replay_limit == replay_count:
                    print(
                            'Hence we have arrived at the play limit you chose, Choose a longer play limit next time :) ')
                    list_of_goodbyes = (
                            'See you soon pal !!', 'Was a fun time playing with you '
                        )
                    print(
                            random.choice(list_of_goodbyes)
                        )
                replay_count += 1
    if ask_which_game == 2:
        print('its a difficult game ! \n you will have to solve programming questions!')        
        LIST_OF_PROGRAMMING_QUESTIONS = (1)  
if ask_play == 'n' or 'N':
    print('ok','fine') 
# CRAVE = 1,2,34,5,63
# LISTOS = list(CRAVE)
# DESIRED = int(input('Enter the number you want to find !! : '))
# for i in LISTOS: 
#     if i == DESIRED:
#         print(i ,':',i-1,i-2 )
