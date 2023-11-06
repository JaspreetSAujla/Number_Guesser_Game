from NumberGuesser import NumberGuesser

if __name__ == "__main__":
    number_guesser: NumberGuesser = NumberGuesser(LowerLimit = 1, 
                                                  UpperLimit = 100, 
                                                  NumberOfGuesses = 7)
    number_guesser.run()