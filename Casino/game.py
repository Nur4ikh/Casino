from logic import calculate_result
import configparser

def play_game():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    money = int(config['SETTINGS']['MY_MONEY'])
    while True:
        print(f'Your current balance: {money}$')
        bet = int(input('Place your bet: '))

        if money < bet:
            print('Sorry you dont have money')
            break

        selected_slot = int(input('Choose a slot (1-30): '))

        result = calculate_result(bet, selected_slot)
        money += result

        if result > 0:
            print('Congratulations! You won!')
        else:
            print('Sorry, you lose')

        play_again = input('Do you want to play again? (yes/no)')
        if play_again.lower() != 'yes':
            break

    print(f'Game over. Your final balance {money}')