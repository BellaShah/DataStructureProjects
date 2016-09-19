#  File: Blackjack.py

#  Description: This program will simulate a game of Blackjack

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: February 17, 2016

#  Date Last Modified: February 17, 2016

import random

class Card (object):
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 1):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Player (object):
  # cards is a list of card objects
  def __init__ (self, cards):
    self.cards = cards

  # when a player hits append a card
  def hit (self, card):
    self.cards.append (card)

  def get_points (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    # deduct 10 if Ace is there and and needed as 1
    for card in self.cards:
      if count <= 21:
        break
      elif card.rank == 1:
        count = count - 10

    return count

  # does the player have 21 points or not
  def has_blackjack (self):
    return (len(self.cards) == 2) and (self.get_points() == 21)

  # complete the code so that the cards and points are printed
  def __str__ (self):
    string = ''
    for card in self.cards:
      string += str(card) + ' '
      
    return string

# Dealer class inherits from the Player class
class Dealer (Player):
  def __init__ (self, cards):
    Player.__init__ (self, cards)
    self.show_one_card = True
    
  # over-ride the hit() function in the parent class
  # add cards while points < 17, then allow all to be shown
  def hit (self, deck):
    self.show_one_card = False
    while self.get_points() < 17:
      self.cards.append (deck.deal())

  # return just one card if not hit yet 
  def __str__ (self):
    if self.show_one_card:
      return str(self.cards[0])
    else:
      return Player.__str__ (self)

class Blackjack (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.num_players = num_players
    self.player_list = []

    # create the number of players specified
    # each player gets two cards
    for i in range (self.num_players):
      self.player_list.append (Player ([self.deck.deal(), self.deck.deal()]))

    # create the Dealer object
    # dealer gets two cards
    self.dealer = Dealer ([self.deck.deal(), self.deck.deal()])
  def play (self):
    # print the cards that each player has
    for i in range (self.num_players):
      print ('Player ' + str(i + 1) + ': ' + str(self.player_list[i]) + '- ' \
            + str(self.player_list[i].get_points()) + ' points')

    # print the cards that the dealer has
    print ('Dealer: ' + str (self.dealer))

    # each player hits until he says no
    playerPoints = []
    for i in range (self.num_players):
      if self.player_list[i].has_blackjack():
        playerPoints.append(self.player_list[i].get_points())
        continue
      print()
      while True:
        print('Player ' + str(i + 1) + ', ', end = '')
        choice = input ('do you want to hit? [y / n]: ')
        if choice in ('y', 'Y'):
          (self.player_list[i]).hit (self.deck.deal())
          points = (self.player_list[i]).get_points()
          print ('Player ' + str(i + 1) + ': ' + str(self.player_list[i]) +'- ' + str(points) + ' points')
          if (points >= 21):
            break
        else:
          break
      playerPoints.append ((self.player_list[i]).get_points())

    # Dealer's turn to hit
    self.dealer.hit (self.deck)
    dealerPoints = self.dealer.get_points()
    print ('\nDealer: ' + str(self.dealer) + '- ' + str(dealerPoints)+ ' points \n')

    # determines the outcome for all players
    for j in range (self.num_players):
      if playerPoints[j] > 21:
        print ("Player " + str(j+1) + ' loses')
      elif self.player_list[j].has_blackjack():
        print ('Player ' + str(j+1) + ' wins')
      elif dealerPoints > 21:
        if playerPoints[j] <= 21:
          print('Player ' + str(j+1) + ' wins')
        else:
          print('Player ' + str(j+1) + ' loses')
      elif self.dealer.has_blackjack() or dealerPoints == 21:
        if playerPoints[j] == 21:
          print('Player ' + str(j+1) + ' ties')
        else:
          print('Player ' + str(j+1) + ' loses')
      elif dealerPoints < 21:
        if playerPoints[j] < dealerPoints:
          print('Player ' + str(j+1) + ' loses')
        elif playerPoints[j] > dealerPoints:
          print('Player ' + str(j+1) + ' wins')
        else:
          print('Player ' + str(j+1) + ' ties')

def main():
  print()
  num_players = eval (input ('Enter number of players: '))
  print()
  while (num_players < 1 or num_players > 6):
    num_players = eval (input ('Enter number of players: '))

  # create a Blackjack object
  game = Blackjack (num_players)

  # star the game
  game.play()

main()
