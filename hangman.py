from random import randint

def old():
    file = open("words.txt")
    words = file.readlines()
    n=randint(1, 2999)
    word = words[n]
    
    #print(word)
    print("Guess a letter!")

    count_wrong=0

    while count_wrong < 5:
        print("You have got {} wrong".format(count_wrong))
        guess = input()
        if guess in word:
            print("yes")
        else:
            print("NO, YOU R BULI, U SUCK AT THIS D:<")
            count_wrong = count_wrong + 1

    print("Bad luck, loser")
    print("The word was: {}".format(word))


class Hangman:

    def __init__(self):
        self.word = self.get_new_word()

    def get_new_word(self):
        file = open("words.txt")
        words = file.readlines()
        n=randint(1, 2999)
        return words[n]
        
        # what goes here?

    def play(self):
        # play the hangman game!!
        
    def length(self):
        return len(self.word)


def main():
    h = Hangman()
    l = h.length()
    print(l)
    print(h.word)


if __name__ == "__main__":
    main()
