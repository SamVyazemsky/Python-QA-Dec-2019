import json

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

print(blackjack_hand == decoded_hand)

print(type(blackjack_hand))
print(type(decoded_hand))

print(blackjack_hand == tuple(decoded_hand))
