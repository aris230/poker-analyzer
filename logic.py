def evaluate_hand(hole_cards, board_cards):
    if "A♠" in hole_cards and "K♠" in hole_cards:
        return "Top hand - Go All In!"
    elif "5♣" in board_cards and board_cards.count("5♣") > 1:
        return "Pair on the board - Check or Fold"
    else:
        return "Weak hand - Check or Fold"
