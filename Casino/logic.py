from random import choice

def calculate_result(bet, selected_slot):
    winning_slot = choice(range(1, 31))
    if selected_slot == winning_slot:
        return bet * 2
    else:
        return -bet