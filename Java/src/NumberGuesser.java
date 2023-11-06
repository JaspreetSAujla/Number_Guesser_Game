import java.util.Random;
import java.util.Scanner;

/**
 * A game where the user thinks of a number and the program has
 * to guess what the number is within a certain number of tries.
 */
public class NumberGuesser {

    private final int upperLimit;
    private final int lowerLimit;
    private final int numberOfGuesses;
    private final Scanner scanner;
    private final Random random;

    /**
     * Construct the number guesser game object with the
     * starting variables.
     * @param lowerLimit is the smallest guessable number.
     * @param upperLimit is the largest guessable number.
     * @param numberOfGuesses is the number of guesses the program has.
     */
    public NumberGuesser(int lowerLimit, int upperLimit, int numberOfGuesses) {
        this.lowerLimit = lowerLimit;
        this.upperLimit = upperLimit;
        this.numberOfGuesses = numberOfGuesses;
        this.scanner = new Scanner(System.in);
        this.random = new Random();
    }

    /**
     * This method starts the game with the args that were passed
     * into the constructor.
     */
    public void run() {
        boolean play = true;
        while (play) {
            System.out.println("Think of a number between " + this.lowerLimit + " and " + this.upperLimit);
            System.out.println("Hit enter once you have thought of a number...");
            this.scanner.nextLine();

            guessNumber(this.lowerLimit, this.upperLimit);

            play = playAgain();
        }
    }

    private void guessNumber(int currentLowerLimit, int currentUpperLimit) {
        int currentNumberOfGuesses = 0;
        int currentGuess = this.random.nextInt(this.lowerLimit, this.upperLimit+1);

        while (currentNumberOfGuesses < this.numberOfGuesses) {
            System.out.println("Guess " + (currentNumberOfGuesses+1) + ": " + currentGuess);
            boolean validCorrectAnswer = false;

            while (!validCorrectAnswer) {
                System.out.println("Was this the number you were thinking of? \n(y/n)");
                String correctAnswer = this.scanner.nextLine();

                if (correctAnswer.equals("y")) {
                    validCorrectAnswer = true;
                    System.out.println("Awesome, it took me " + (currentNumberOfGuesses+1) + " attempts to get it!");
                    currentNumberOfGuesses = this.numberOfGuesses;
                } else if (correctAnswer.equals("n")) {
                    validCorrectAnswer = true;
                    if (currentNumberOfGuesses == this.numberOfGuesses-1) {
                        System.out.println("I did not guess the number in time... \nYou win!");
                        currentNumberOfGuesses = this.numberOfGuesses;
                        break;
                    }
                    System.out.println("Let me try again...");
                    boolean validHigherOrLower = false;

                    while (!validHigherOrLower) {
                        System.out.println("Is the number higher or lower? \n(h/l)");
                        String higherOrLower = this.scanner.nextLine();
                        if (higherOrLower.equals("h")) {
                            validHigherOrLower = true;
                            currentLowerLimit = currentGuess;
                            currentGuess = determineNewGuess(currentLowerLimit, currentUpperLimit);
                        } else if (higherOrLower.equals("l")) {
                            validHigherOrLower = true;
                            currentUpperLimit = currentGuess;
                            currentGuess = determineNewGuess(currentLowerLimit, currentUpperLimit);
                        } else {
                            System.out.println("Invalid response, try again.");
                        }
                    }
                    currentNumberOfGuesses++;
                } else {
                    System.out.println("Invalid response, try again.");
                }
            }
        }
    }

    private int determineNewGuess(int lowerLimit, int upperLimit) {
        int midpoint = (upperLimit - lowerLimit)/2;
        return lowerLimit + midpoint;
    }

    private boolean playAgain() {
        while (true) {
            System.out.println("Would you like ot play again? \n(y/n)");
            String playAgain = this.scanner.nextLine();
            if (playAgain.equals("y")) {
                System.out.println("Lets play again!");
                return true;
            } else if (playAgain.equals("n")) {
                System.out.println("Thank you for playing!");
                return false;
            } else {
                System.out.println("Invalid response, try again.");
            }
        }
    }
}
