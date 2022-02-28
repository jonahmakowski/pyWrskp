class IsItAWord:
    def __init__(self, word):
        self.word = word
        self.word_list = list(word)
        self.rever = ''

    def reverse(self):
        for i in range(len(self.word_list)):
            self.rever += self.word_list[]
            print(self.rever)


is_it_a_word = IsItAWord('add')
is_it_a_word.reverse()
