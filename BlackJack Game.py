import random

class Card:
    def __init__(self, rank, suits):
        self.rank = rank
        self.suits = suits

    def __str__(self):
        return f"{self.rank['rank']} of {self.suits}"
      
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "K", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "10", "value": 10},
            {"rank": "9", "value": 9},
            {"rank": "8", "value": 8},
            {"rank": "7", "value": 7},
            {"rank": "6", "value": 6},
            {"rank": "5", "value": 5},
            {"rank": "4", "value": 4},
            {"rank": "3", "value": 3},
            {"rank": "2", "value": 2}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        dealt_cards = []
        for _ in range(number):
            if self.cards:
                dealt_cards.append(self.cards.pop())
        return dealt_cards
 
class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)
        self.calculate_value()
  
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self,show_Deal_Cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index,card in enumerate(self.cards):
          if index==0 and self.dealer and not show_Deal_Cards and not self.is_blackjack():
           print("hidden")
          else:
            print(card)
            
        if not self.dealer:
            print("Value:", self.get_value())

class Game():
    def play(self):
        game_num = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many Games You want to Play ?"))
            except:
                print("You Must Enter a Number")

        while game_num < games_to_play:
            game_num += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_num} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()
           
            if self.Check_Winner(player_hand,dealer_hand):
                continue
            
            choice=""
            while player_hand.get_value()<21 and choice not in ["s","stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h","s","hit","stand"]:
                    choice=input("Please Enter 'Hit' or 'Stand' (H/S)")
                    print()
                    if choice in ["hit","h"]:
                        player_hand.add_card(deck.deal(1))
                        player_hand.display()
                    
            if self.Check_Winner(player_hand,dealer_hand):
                continue
            
            player_hand_value=player_hand.get_value()
            dealer_hand_value=dealer_hand.get_value()
            
            while dealer_hand_value<17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()
                
            dealer_hand.display(show_Deal_Cards=True)
            
            if self.Check_Winner(player_hand,dealer_hand):
                continue
            
            print("Final Results")
            print("your hand: ", player_hand_value )
            print("Dealer's hand: ", dealer_hand_value )
            
            self.Check_Winner(player_hand,dealer_hand,True)
            
        print("\nThanks for Playing!")
            
                    
    def Check_Winner(self, player_hand, dealer_hand,game_over=False):
         if not game_over:
            if player_hand.get_value()>21:
                print("You busted, Dealer Wins! 😭")
                return True
            elif dealer_hand.get_value()>21:
                print("Dealer busted, you Win! 😂")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both Players have Black jack! Tie! 😑")
                return True
            elif  player_hand.is_blackjack():
                print("You have Black Jack! You Win! 😂")
                return True
            elif  dealer_hand.is_blackjack():
                print("Dealer has Black Jack! You Lose! 😭")
                return True
         else:
             if player_hand.get_value() > dealer_hand.get_value():
                 print("You Win! 😂")  
                    
             elif player_hand.get_value() == dealer_hand.get_value():
                 print("Tie ! 😑")  
             else: 
                 print("Dealer Wins! 😭")  
                    
         return False

g = Game()
g.play()