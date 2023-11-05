from NumberGuesser import NumberGuesser

if __name__ == "__main__":
    number_guesser: NumberGuesser = NumberGuesser(UpperLimit = 100, 
                                                  LowerLimit = 1, 
                                                  NumberOfGuesses = 6)
    number_guesser.run()