class IsItAWord:
    def __init__(self, word):
        self.word = word
        self.word_list = list(word)
        self.rever = ''
        self.reverse()

    def reverse(self):
        for i in range(len(self.word_list) -1, -1, -1):
            self.rever += self.word_list[i]
            #print(self.rever)
            #print(i)
    def check(self):
        if self.rever == self.word:
            print('If you reverse the word {} you will get the same word'.format(self.word))
        else:
            print('If you reverse the word {} you get {}'.format(self.word, self.rever))
            print('So it does not work')


is_it_a_word = IsItAWord('add')
is_it_a_word.check()
