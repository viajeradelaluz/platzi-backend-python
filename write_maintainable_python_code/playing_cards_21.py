import random

SUITS = {"Diamonds": 1, "Hearts": 2, "Spades": 3, "Clubs": 4}

RANKS = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}


class PlayingCard:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def name(self):
        return f"{self.rank} of {self.suit}"

    def is_better_than(self, other):
        if self.rank > other.rank:
            return True
        if self.rank < other.rank:
            return False
        return self.suit > other.suit


class Deck:
    def __init__(self) -> None:
        self.cards = []

        # Create a card for each suit and rank.
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(PlayingCard(suit, rank))
        self.shuffle()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_top_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def card_index(self, index):
        try:
            return self.cards[index]
        except IndexError:
            return None

    def delete_card(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def __str__(self) -> str:
        return f"Hand with {len(self.cards)} cards"


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = Hand()


class View:
    """Presents the information to the user and request inputs from them."""

    def prompt_for_new_player(self):
        new_player = input("Enter name of player: ")
        if new_player == "":
            return None
        return new_player

    def display_player_and_hand(self, player_name, hand):
        print(f"[ {player_name} ]", end=" ")
        for card in hand.cards:
            if card.face_up:
                print(f"{card.name()}")
            else:
                print("card is hidden")

    def prompt_for_flip_cards(self):
        input("\nReady to flip cards? ")
        return True

    def show_winner(self, winner):
        print(f"\n{winner.name} wins!")

    def prompt_for_new_game(self):
        while True:
            new_game = input("Play again? (y/n) ")
            if new_game in ["y", "Y"]:
                return True
            if new_game in ["n", "N"]:
                return False
            print("Invalid input")


class GameController:
    """Control the sequence of user interactions in the game."""

    def __init__(self, deck, view) -> None:
        # Model
        self.players = []
        self.deck = deck

        # View
        self.view = view

    def start_game(self):
        """Create the card deck and deal cards to players."""
        self.deck.shuffle()
        for player in self.players:
            next_card = self.deck.remove_top_card()
            if next_card is not None:
                player.hand.add_card(next_card)

    def evaluate_game(self):
        """Evaluate the game and return the winner."""
        winner = None
        for player in self.players:
            if winner is None:
                winner = player
                continue
            if player.hand.card_index(0).is_better_than(winner.hand.card_index(0)):
                winner = player

        return winner

    def rebuild_deck(self):
        """Put all cards back into the deck and shuffle."""
        for player in self.players:
            while player.hand.cards:
                card = player.hand.delete_card()
                card.face_up = False
                self.deck.add_card(card)
        self.deck.shuffle()

    def add_player(self, player_name):
        """Add a player to the game."""
        self.players.append(Player(player_name))

    def ready(self):
        """Enter player names and start the game."""
        while len(self.players) < 5:
            new_player = self.view.prompt_for_new_player()
            if new_player is None:
                break
            self.add_player(new_player)

        while True:
            self.start_game()
            for player in self.players:
                self.view.display_player_and_hand(player.name, player.hand)

            # Flip over all player's cards, showing what they have.
            self.view.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand.cards:
                    card.face_up = True
                self.view.display_player_and_hand(player.name, player.hand)

            # Show the winner.
            self.view.show_winner(self.evaluate_game())

            # Ask if the players want to play again.
            if not self.view.prompt_for_new_game():
                break
            self.rebuild_deck()


# Create the Deck, View, and GameController, and run the application.
game_controler = GameController(Deck(), View())
game_controler.ready()
