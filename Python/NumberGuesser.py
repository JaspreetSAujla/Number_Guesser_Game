import random

class NumberGuesser:
    """
    A game where the user thinks of a number and the program has 
    to guess what the number is within a certain number of tries.
    """

    def __init__(self, LowerLimit: int, UpperLimit: int, NumberOfGuesses: int) -> None:
        self.upper_limit: int = UpperLimit
        self.lower_limit: int = LowerLimit
        self.number_of_guesses: int = NumberOfGuesses

    

    def run(self) -> None:
        play: bool = True
        while play:
            print(f"Think of a number between {self.lower_limit} and {self.upper_limit}")
            input("Hit enter once you have thought of the number...")

            self.guess_number(current_lower_limit = self.lower_limit, 
                              current_upper_limit = self.upper_limit)

            play = self.determine_play_again()
    


    def guess_number(self, current_lower_limit: int, current_upper_limit: int) -> None:
        current_number_of_guesses: int = 0
        current_guess: int = random.randint(self.lower_limit, self.upper_limit)

        while current_number_of_guesses < self.number_of_guesses:
            print(f"Guess {current_number_of_guesses+1}: {current_guess}")
            valid_correct_answer: bool = False

            while valid_correct_answer == False:
                correct_answer: str = input("Was this the number you were thinking of? \n(y/n) \n")

                if correct_answer == "y":
                    print(f"Awesome, it took me {current_number_of_guesses+1} attempts to guess it!")
                    valid_correct_answer = True
                    current_number_of_guesses = self.number_of_guesses
                elif correct_answer == "n":
                    valid_correct_answer = True
                    if current_number_of_guesses == self.number_of_guesses-1:
                        print("I did not guess the number in time... \nYou win!")
                        current_number_of_guesses = self.number_of_guesses
                        break
                    print("Let me try again...")
                    valid_higher_or_lower: bool = False
                    
                    while valid_higher_or_lower == False:
                        higher_or_lower: str = input("Is the number higher or lower? \n(h/l) \n")
                        if higher_or_lower == "h":
                            valid_higher_or_lower = True
                            current_lower_limit = current_guess
                            current_guess = self.determine_new_guess(current_lower_limit = current_lower_limit, 
                                                                     current_upper_limit = current_upper_limit, 
                                                                     original_upper_limit = self.upper_limit)
                            if current_guess > self.upper_limit:
                                print("You have thought of a number higher than the range, the game will now end...")
                                current_number_of_guesses = self.number_of_guesses
                        elif higher_or_lower == "l":
                            valid_higher_or_lower = True
                            current_upper_limit = current_guess
                            current_guess = self.determine_new_guess(current_lower_limit = current_lower_limit, 
                                                                     current_upper_limit = current_upper_limit, 
                                                                     original_upper_limit = self.upper_limit)
                            if current_guess < self.lower_limit:
                                print("You have thought of a number below the range, the game will now end...")
                                current_number_of_guesses = self.number_of_guesses
                        else:
                            print("Invalid response, try again.")
                    current_number_of_guesses += 1
                else:
                    print("Invalid response, try again.")
    


    def determine_new_guess(self, lower_limit: int, upper_limit: int, original_upper_limit: int) -> int:
        midpoint: int = (upper_limit - lower_limit)//2
        if midpoint == 0 and upper_limit == original_upper_limit:
            return lower_limit + 1
        else:
            return lower_limit + midpoint
    


    def determine_play_again(self) -> bool:
        while True:
            play_again: str = input("Would you like to play again? \n(y/n) \n")
            if play_again == "y":
                print("Lets play again!")
                return True
            elif play_again == "n":
                print("Thank you for playing!")
                return False
            else:
                print("Invalid response, try again.")