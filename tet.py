playing = True
while playing:
    x = input('Hit or Stand? Enter h or s: ')

    if x[0].lower() == 's':
        print('h')

    elif x[0].lower() == 'h':
        print("Player stands. Dealers turn")
        #playing = False

    # else:
    #     print("Sorry, I did not understand that, Please enter either h or s")
    #     continueh