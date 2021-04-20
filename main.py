import requests

class snowman():
    def __init__(self):
        self.url = 'https://random-words-api.vercel.app/word'
        self.active_game = False
        self.wrong = 0
        self.game_word = ''
        self.game_display = list()
        self.snowman_show = ['     ___     ','    |   |    ','   _|___|_   ','    (~ ~)    ','---(     )---','  (   *   )  ',' (    *    ) ']

    def pick_word(self):
        res = requests.get(self.url)
        if res.status_code != 200:
            print("Error - Status Code: ",res.status_code)
        else:
            self.game_word = res.json()

    def setGame(self):
        word = self.game_word[0]['word']
        for i in range(0,len(word)):
            self.game_display.insert(i,'_')
    
    def checkLetter(self,letter=False):
        if len(letter) == 1:
            for i in range(10):
                if str(i) == letter:
                    letter = False
            if letter == '' or letter == ' ':
                letter = False
            if letter:
                return letter
            else:
                print('Please enter in a letter')
                return False
        else:
            if len(letter) > 1:
                print('Please enter in one letter at a time')
    
    def printGame(self):
        if self.wrong > 0:
            for i in range(self.wrong):
                print(self.snowman_show[i])
            print('\n')
        if len(self.snowman_show)-self.wrong != 0:
            print("You have",len(self.snowman_show)-self.wrong,"tries left before you lose!",'\n'*2)
            for i in range(len(self.game_display)):
                if i != len(self.game_display)-1:
                    print(self.game_display[i].upper(),end=' ')
                else:
                    print(self.game_display[i].upper())
        else:
            print("So you made it this far:\n\n")
            for i in range(len(self.game_display)):
                if i != len(self.game_display)-1:
                    print(self.game_display[i].upper(),end=' ')
                else:
                    print(self.game_display[i].upper())
            print("\n\nBut that wasn't good enough, Sorry Game Over.\n\nThe word to guess was",self.game_word[0]['word'].upper(),'\n\n')
    
    def right_or_wrong(self,letter=False):
        right = 0
        if letter:
            word = self.game_word[0]['word']
            for i in range(len(word)):
                if letter.lower() == word[i].lower():
                    right = right + 1
                    self.game_display[i] = letter
            if right == 0:
                self.wrong = self.wrong + 1
            if len(self.snowman_show)-self.wrong == 0:
                print("Game Over, You Lose!!!")
                self.active_game = False

    def init(self):
        self.pick_word()
        self.setGame()
        self.active_game = True

    def play(self,let):
        lett = game.checkLetter(let)
        self.right_or_wrong(lett)
        self.printGame()


game = snowman()
while True:
    while game.active_game == False:
        answer = input("Would you like to start a game?(y/n)")
        if answer.lower() == 'y' or answer.lower() == 'yes':
            game.init()
    while game.active_game == True:
        yourLetter = input('Please enter a letter:')
        game.play(yourLetter)    

        