#  File: Poker.py

#  Description: This program will simulate a game of Poker

#  Student's Name: Bella Shah

#  Student's UT EID: BHS533

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: February 9, 2016

#  Date Last Modified: February 10, 2016

import random

# Creates Class Cards and assigns ranks and suits to cards
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ("S", "D", "H", "C")


  def __init__ (self, rank, suit):
    self.rank = rank
    self.suit = suit

# Converts to actual card rank for printing purposes
  def __str__ (self):
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit


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
        self.deck.append(card)

  def shuffle (self):
    random.shuffle (self.deck)

  def __len__ (self):
    return len (self.deck)

  # Deals cards from top of deck 
  def deal (self):
    if len(self) == 0:
      return None
    else:
      return self.deck.pop(0)


class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  # def Play runs the game and determines winner or ties
  def play (self):      
    points_hand = [] 

    # Prints out the player and their cards
    print()
    for i in range (len (self.players) ):
      # Sort hand in order of decreasing rank
      sortedHand = sorted (self.players[i], reverse = True)  
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + " "
      print ("Player " + str(i + 1) + ": " + hand)
      points_hand.append(self.handResult(sortedHand))
      
    # Gives type of each hand for each player 
    print()
    for j in range (len(self.players)):
        print("Player " + str(j + 1) + ': ' + points_hand[j][1])

    
    # Gets total points for each player and outputs winner
    Points = []
    for i in range (0, len(points_hand)):
      Points.append(points_hand[i][0])
    max_points = max(Points)
    print()
    if Points.count(max_points)==1:
        print("Player", Points.index(max_points)+1, "wins.")
    elif Points.count(max_points)>1:
        for i in range (0, len(Points)):
            if Points[i] == max_points:
                print("Player",i+1, "ties.")

  # Returns result
  def handResult(self, hand):

      handType = ''
      
      if self.is_royal(hand) > 0:
          score = self.is_royal(hand)
          handType = "Royal Flush"
          
      elif self.is_straight_flush(hand) > 0:
          score = self.is_straight_flush(hand)
          handType = "Straight Flush"
          
      elif self.is_four_kind(hand) > 0:
          score = self.is_four_kind(hand)
          handType = "Four of a Kind"

      elif self.is_full_house(hand) > 0:
          score = self.is_full_house(hand)
          handType = "Full House"

      elif self.is_flush(hand) > 0:
          score = self.is_flush(hand)
          handType = "Flush"

      elif self.is_straight(hand) > 0:
          score = self.is_straight(hand)
          handType = "Straight"

      elif self.is_three_kind(hand) > 0:
          score = self.is_three_kind(hand)
          handType = "Three of a Kind"

      elif self.is_two_pair(hand) > 0:
          score = self.is_two_pair(hand)
          handType = "Two Pair"

      elif self.is_one_pair(hand) > 0:
          score = self.is_one_pair(hand)
          handType = "One Pair"

      else:
          score = self.is_high_card(hand)
          handType = "High Card"

      result = [score, handType]

      return result

  # Checks if hand is royal flush
  def is_royal (self, hand):
      is_straight = False
      is_flush = False
      score = 0

      # Check for a straight
      for i in range(4):
          if hand[i].rank == hand[i+1].rank + 1:
              is_straight = True
          else:
              is_straight = False
              break

      # Check for a flush           
      for j in range(4):
          if hand[j].suit == hand[j+1].suit:
              is_flush = True
          else:
              is_flush = False
              break

      # Hand must also contain an Ace
      if is_flush and is_straight and hand[0].rank == 14:  
          score += 9 * 13**5
          for j in range(5):
              score += hand[j].rank * 13**(4 - j)
        
      return score

  # Checks if hand is Straight flush
  def is_straight_flush (self, hand):
      is_straight = False
      is_flush = False
      score = 0

      # Checks for a straight
      for i in range(4):
          if hand[i].rank == hand[i+1].rank + 1:
              is_straight = True
          else:
              is_straight = False
              break

      # Checks for a flush           
      for j in range(4):
          if hand[j].suit == hand[j+1].suit:
              is_flush = True
          else:
              is_flush = False
              break

      if is_flush and is_straight:
          score += 9 * 13**5
          for j in range(5):
              score += hand[j].rank * 13**(4 - j)
        
      return score

  # Checks if hand is four of a kind
  def is_four_kind (self, hand):
      is_four_kind = False
      score = 0

      if hand[1].rank == hand[2].rank == hand[3].rank:
          if hand[4].rank == hand[3].rank:
              is_four_kind = True
              notFour = hand[0].rank  
              
          elif hand[0].rank == hand[1].rank:
              is_four_kind = True
              notFour = hand[4].rank

      if is_four_kind:
          score += 8 * 13**5
          if notFour == hand[0].rank:
              score += hand[1].rank * (13**4 + 13**3 + 13**2 + 13)
              score += hand[0].rank
          elif notFour == hand[4].rank:
              score += hand[0].rank * (13**4 + 13**3 + 13**2 + 13)
              score += hand[4].rank
    
      return score

  # Checks if hand is full house
  def is_full_house (self, hand):
      is_full_house = False
      score = 0

      if hand[0].rank == hand[1].rank:
          if hand[2].rank == hand[3].rank == hand[4].rank:
              is_full_house = True
              pairRank = hand[0].rank
              threeRank = hand[2].rank
          elif hand[1].rank == hand[2].rank and \
          hand[3].rank == hand[4].rank:
              is_full_house = True
              pairRank = hand[3].rank
              threeRank = hand[0].rank

      if is_full_house:
          score += (7 * 13**5) + threeRank * (13**4 + 13**3 + 13**2)
          score += pairRank * (13 + 1)

      return score

  # Checks if hand is Flush 
  def is_flush (self, hand):
      is_flush = False
      score = 0

      # Check if all cards have the same suit
      for i in range(4):
          if hand[i].suit == hand[i+1].suit:
              is_flush = True
          else:
              is_flush = False
              break

      if is_flush:
          score += 6 * 13**5
          for j in range(5):
              score += hand[j].rank * 13**(4 - j)
            
      return score

  # Checks if hand is Straight
  def is_straight (self, hand):
      is_straight = False
      score = 0

      # Checks if all cards are different by  one rank
      for i in range(4):
          if hand[i].rank == hand[i+1].rank + 1:
              is_straight = True
          else:
              is_straight = False
              break

      if is_straight:
          score += 5 * 13**5 
          for j in range(5):
              score += hand[j].rank * 13**(4 - j)
          
      return score

  # Checks if hand is three of a kind
  def is_three_kind (self, hand):
      is_three_kind = False
      score = 0
      notThree = []

      # Check if three of the cards have the same rank
      for i in range(3):
          if hand[i].rank == hand[i+1].rank == hand[i+2].rank:
              threeRank = hand[i].rank
              is_three_kind = True

      if is_three_kind:
          for j in range(5):
              if hand[j].rank != threeRank:
                  notThree.append(hand[j].rank)  # Cards not in the
                                                 #   three of a kind
          score += (4 * 13**5) + threeRank * (13**4 + 13**3 + 13**2)
          score += (notThree[0] * 13) + notThree[1]

      return score

  # Checks if hand is two of a kind
  def is_two_pair (self, hand):
      is_two_pairPair = False
      score = 0
      if hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank:
          pair1 = hand[0].rank
          pair2 = hand[2].rank
          is_two_pairPair = True
          notTwoPair = hand[4].rank
      elif hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank:
          pair1 = hand[1].rank
          pair2 = hand[3].rank
          is_two_pairPair = True
          notTwoPair = hand[0].rank
      elif hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank:
          pair1 = hand[0].rank
          pair2 = hand[3].rank
          is_two_pairPair = True
          notTwoPair = hand[2].rank

      if is_two_pairPair:
          score += (3 * 13**5) + pair1 * (13**4 + 13**3)
          score += pair2 * (13**2 + 13) + notTwoPair
          
      return score

  # Checks if hand has one pair
  def is_one_pair (self, hand):
      isPair = False
      score = 0
      notPair = []   # list of cards that are not in the pair

      # Check to see if there is exactly one pair of matching ranks
      for i in range(4):
          if hand[i].rank == hand[i+1].rank:
              pairRank = hand[i].rank
              isPair = True

      if isPair:
          for j in range(5):
              if hand[j].rank != pairRank:
                  notPair.append(hand[j].rank)  # The cards not in the pair
          score += (2 * 13**5) + pairRank * (13**4 + 13**3)
          score += (notPair[0] * 13**2) + (notPair[1] * 13) + notPair[2]
  
      return score
      
  # Checks for high card 
  def is_high_card (self, hand):

      score = 13**5 + (hand[0].rank * 13**4)
      score += (hand[1].rank * 13**3) + (hand[2].rank * 13**2)
      score += (hand[3].rank * 13) + hand[4].rank

      return score

def main ():

    # prompt user to enter the number of players
    num_players = int(input ("Enter number of players: "))
    while (num_players < 2 or num_players > 6): # Makes sure there is 2-6 players only
        num_players = int( input ("Enter number of players: "))

    # Creates Poker object
    game = Poker (num_players)

    # Play the game (poker)
    game.play()

main()