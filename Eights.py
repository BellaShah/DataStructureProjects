#  File: Eights.py

#  Description: This program will simulate a game of Crazy Eights

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: March 10, 2016

#  Date Last Modified: March 11, 2016
import random

# Creates Class Cards and assigns ranks and suits to cards
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ("C", "D", "H", "S")

# Converts to actual card rank for printing purposes
  def __init__ (self, rank = 12, suit = "S"):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = "S"
      
# Converts rank to value
  def __str__ (self):
    if (self.rank == 14):
      rank = "A"
    elif (self.rank == 13):
      rank = "K"
    elif (self.rank == 12):
      rank = "Q"
    elif (self.rank == 11):
      rank = "J"
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

# Creates a 52 deck of cards
class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  # Randomly shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # Finds the length of deck
  def __len__ (self):
    return len(self.deck)

  # Deals the deck of cards from the top of deck
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

# Creates Player class
class Player (object):
  def __init__ (self, num_cards, deck):
    self.cards = []
    for i in range(num_cards):
      self.cards.append(deck.deal())
    self.cards.sort(reverse = True)

  def draw (self, deck):
    self.cards.append (deck.deal())

  def deal (self, card_index):
    self.cards.pop (card_index)

  # Finds the point total for each player
  def get_points (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 8:
        count += 50
      else:
        count += card.rank
    return count

  # Prints cards appropriately 
  def __str__ (self):
    string = ""
    for card in self.cards:
      string += str(card) + " "
      
    return string

class Eights (object):
  def __init__ (self, num_players = 1):
    num_cards = 5
    self.deck = Deck()
    self.deck.shuffle()
    self.num_players = num_players
    self.gamePlayers = []
    self.discard = []
    self.playing  = True
    self.round = 0

    # Gives each player cards
    for i in range (self.num_players):
      self.gamePlayers.append (Player (num_cards, self.deck))
    self.discard.append(self.deck.deal())

 # def Play runs the game and determines winner
  def play (self):

    round_number = 0
    while self.playing:

      # Prints Round number and the cards of each player
      print("Round " + str(round_number))
      for i in range (self.num_players):
        print ("Player " + str (i + 1) + ": " + str(self.gamePlayers[i]))
      print (self.print_discard())

      # Determines which card to play based on rules
      for j in range(len(self.gamePlayers)):
        played_card = False
        if self.playing :
          for k in range(len(self.gamePlayers[j].cards)):
            if (self.gamePlayers[j].cards[k].suit == self.discard[0].suit and self.gamePlayers[j].cards[k].rank > self.discard[0].rank):
              self.discard.insert(0, self.gamePlayers[j].cards[k])
              self.gamePlayers[j].deal(k)
              played_card = True
              break
          if not played_card:
            for k in range(len(self.gamePlayers[j].cards)):
              if self.gamePlayers[j].cards[k].rank == 8:
                self.discard.insert(0, self.gamePlayers[j].cards[k])
                self.gamePlayers[j].deal(k)
                played_card = True
                break
          if not played_card:
            for k in range(len(self.gamePlayers[j].cards)):
              if self.gamePlayers[j].cards[k].rank == self.discard[0].rank:
                self.discard.insert(0, self.gamePlayers[j].cards[k])
                self.gamePlayers[j].deal(k)
                played_card = True
                break
          if not played_card:
            for k in range(len(self.gamePlayers[j].cards)):
              if (self.gamePlayers[j].cards[k].suit == self.discard[0].suit):
                self.discard.insert(0, self.gamePlayers[j].cards[k])
                self.gamePlayers[j].deal(k)
                played_card = True
                break
          if not played_card:
            if self.deck.__len__() == 0:
              self.Over()
              break
            else:
              self.gamePlayers[j].draw(self.deck)
              self.gamePlayers[j].cards.sort(reverse = True)
          if len(self.gamePlayers[j].cards) == 0:
            self.Over()
            break

      self.round += 1
      round_number +=1

  # String concatination of the discard pile
  def print_discard(self):
    discarded = "Discard: "
    for i in range(len(self.discard)):
      discarded += str(self.discard[i]) + " " 
    return discarded + "\n"

# Determines if the game is over due to hand length
  def Over(self):
    self.playing  = False
    final = self.round + 1

    print("Round "+str(final))
    for i in range (self.num_players):
      print ("Player " + str (i + 1) + ": " + str(self.gamePlayers[i]))
    print (self.print_discard())

    print("Result")
    for i in range(len(self.gamePlayers)):
      print("Player " + str(i+1) + ": " + str(self.gamePlayers[i].get_points()) + " points")

def main():

  # Prompts user for input
  num_players = eval (input ("Enter number of players: "))
  while (num_players < 1 or num_players > 6):
    num_players = eval (input ("Enter number of players: "))
  print()
  
  # Creates a Eights object 
  game = Eights (num_players)

  # Starts the game
  game.play()

main()