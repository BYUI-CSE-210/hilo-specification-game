from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 300
        self.total_score = 0

        for i in range(1):
            card = Card()
            self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.higher_or_lower()
            self.do_outputs()
            self.get_inputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        draw_card = input("Play again? [y/n] ")
        self.is_playing = (draw_card == "y")
        print("")
        if self.score <= 0:
            self.is_playing = False
            print("Sorry you have score of 0. Game Over!")

    def higher_or_lower(self):
        """Roll the first and second die then show the first die ask the user for a higher or lower guese then show them the second die.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        
        values1 = ""
        values2 = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            card.draw()
            values1 += f"{card.value}"
            values2 += f"{card.value1}"

        print(f"The card is: {values1} ")

        guess = input("Higher and Lower? [h/l] ")

        if guess == "h":
            if card.value1 > card.value:
                self.score += 100
            elif card.value1 < card.value:
                self.score += (-75)
            else:
                self.score += 0
        elif guess == "l":
            if card.value1 < card.value:
                self.score += 100
            elif card.value1 > card.value:
                self.score += (-75)
            else:
                self.score += 0
        self.total_score = self.score

        print(f"The next card was: {values2} ")

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.score > 0)