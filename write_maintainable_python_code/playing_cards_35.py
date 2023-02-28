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

# Models
class PlayingCard:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.face_up = False

    def name(self):
        return f"{self.rank} of {self.suit}"


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


# Views

class PromptView:
    """Request information from the user."""

    def prompt_for_new_player(self):
        new_player = input("Enter name of player: ")
        if new_player == "":
            return None
        return new_player

    def prompt_for_flip_cards(self):
        input("\nReady to flip cards? ")
        return True

    def prompt_for_new_game(self):
        while True:
            new_game = input("Play again? (y/n) ")
            if new_game in ["y", "Y"]:
                return True
            if new_game in ["n", "N"]:
                return False
            print("Invalid input")


class ShowView:
    """Presents the game to the user."""

    def show_player_and_hand(self, player_name, hand):
        print(f"[ {player_name} ]", end=" ")
        for card in hand.cards:
            if card.face_up:
                print(f"{card.name()}")
            else:
                print("card is hidden")

    def show_winner(self, winner):
        print(f"\n{winner.name} wins!")


class BroadcastView(ShowView):
    def show_player_and_hand(self, player_name, hand):
        """Meaningful code goes here."""
        return super().show_player_and_hand(player_name, hand)

    def show_winner(self, winner):
        """Meaningful code goes here."""
        return super().show_winner(winner)


class InternetView(ShowView):
    def show_player_and_hand(self, player_name, hand):
        """Meaningful code goes here."""
        return super().show_player_and_hand(player_name, hand)

    def show_winner(self, winner):
        """Meaningful code goes here."""
        return super().show_winner(winner)


class PlayerView(PromptView, ShowView):
    def prompt_for_new_player(self):
        return super().prompt_for_new_player()

    def prompt_for_flip_cards(self):
        return super().prompt_for_flip_cards()

    def prompt_for_new_game(self):
        return super().prompt_for_new_game()

    def show_player_and_hand(self, player_name, hand):
        return super().show_player_and_hand(player_name, hand)

    def show_winner(self, winner):
        return super().show_winner(winner)


class MultiView:
    """Interface that combines the prompt and show views."""

    def __init__(self) -> None:
        self.prompt = PlayerView()
        self.show = BroadcastView(), InternetView(), PlayerView()

    def prompt_for_new_player(self):
        return self.prompt.prompt_for_new_player()

    def prompt_for_flip_cards(self):
        return self.prompt.prompt_for_flip_cards()

    def prompt_for_new_game(self):
        return self.prompt.prompt_for_new_game()

    def show_player_and_hand(self, player_name, hand):
        for view in self.show:
            view.show_player_and_hand(player_name, hand)

    def show_winner(self, winner):
        for view in self.show:
            return view.show_winner(winner)


# Controller

class GameController:
    """Control the sequence of user interactions in the game."""

    def __init__(self, deck, multiview, high_card_winner) -> None:
        # Model
        self.players = []
        self.deck = deck

        # View
        self.views = multiview

        # Controller
        self.winner = high_card_winner

    def start_game(self):
        """Create the card deck and deal cards to players."""
        self.deck.shuffle()
        for player in self.players:
            next_card = self.deck.remove_top_card()
            if next_card is not None:
                player.hand.add_card(next_card)

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
            new_player = self.views.prompt_for_new_player()
            if new_player is None:
                break
            self.add_player(new_player)

        while True:
            self.start_game()
            for player in self.players:
                self.views.show_player_and_hand(player.name, player.hand)

            # Flip over all player's cards, showing what they have.
            self.views.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand.cards:
                    card.face_up = True
                self.views.show_player_and_hand(player.name, player.hand)

            # Show the winner.
            self.views.show_winner(self.winner.find_winner(self.players))

            # Ask if the players want to play again.
            if not self.views.prompt_for_new_game():
                break
            self.rebuild_deck()


class HighCardWinner:
    def find_winner(self, players):
        """Return the player with the best card."""
        best_card_rank = None
        best_card_suit = None
        best_player = None

        for player in players:
            player_card_rank = player.hand.card_index(0).rank
            player_card_suit = player.hand.card_index(0).suit
            if (
                best_card_rank is None
                or player_card_rank > best_card_rank
                or (
                    player_card_rank == best_card_rank
                    and player_card_suit > best_card_suit
                )
            ):
                best_card_rank = player_card_rank
                best_card_suit = player_card_suit
                best_player = player

        return best_player


# Create the Deck, View, and GameController, and run the application.

game_controler = GameController(Deck(), MultiView(), HighCardWinner())
game_controler.ready()
