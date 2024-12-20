import threading

def parse_input(inp, word, word_correct, word_wrong_place, word_wrong):
    word_lis = list(word)
    index = 0
    for letter in inp:
        if letter.lower() == "c":
            word_correct[index] = word_lis[index]
        elif letter.lower() == "s":
            if word_wrong_place.get(word_lis[index]) is not None:
                word_wrong_place[word_lis[index]].append(index)
            else:
                word_wrong_place[word_lis[index]] = [index]
        elif letter.lower() == "w":
            if word_lis not in word_wrong:
                word_wrong.append(word_lis[index])
        else:
            print('There was an invalid input, terminating')
            exit()
        index += 1
    return word_correct, word_wrong_place, word_wrong

def check_valid_word(word, word_correct, word_wrong_place, word_wrong):
    word_lis = list(word)
    index = 0

    for letter in word_lis:
        if letter.lower() != word_correct[index] and word_correct[index] != '':
            #print("Word {} doesn't work at letter {} for not being in correct list, correct was {}"
                  #.format(word, letter, word_correct[index]))
            #print(word_correct, word_wrong_place, word_wrong)
            return False
        elif letter.lower() in word_wrong:
            #print("Word {} doesn't work at letter {} for letter in wrong list".format(word, letter))
            return False
        elif word_wrong_place.get(word_lis[index]) is not None:
            if index in word_wrong_place[word_lis[index]]:
                #print("Word {} doesn't work at letter {} for having letter in wrong spot".format(word, letter))
                return False
        index += 1

    for letter in word_wrong_place.keys():
        if letter not in word_lis:
            # print("Word {} doesn't work at letter {} for not having a letter in the semi wrong list".format(word,letter))
            return False

    return True

def find_all_valid(words:list, ranks, word_correct:list, word_wrong_place:dict, word_wrong:list):
    index = 0
    while index < len(words):
        word = words[index]
        if not check_valid_word(word, word_correct, word_wrong_place, word_wrong):
            words.pop(index)
            if ranks is not None:
                ranks.pop(index)
        else:
            index += 1
    return words.copy(), ranks

def give_rank(word_list, word_correct, word_wrong_place, word_wrong, threads=100):
    lists = []
    seperator = len(word_list) // threads
    remainder = len(word_list) % threads
    for cur in range(threads):
        lists.append(word_list[seperator*cur:seperator*(cur+1)])
    lists[-1].extend(word_list[-remainder:])

    running_threads = []
    lock = threading.Lock()
    worker_out = []

    for worker, list in enumerate(lists):
        x = threading.Thread(target=rank_helper, args=(list, word_list, word_correct, word_wrong_place, word_wrong, worker, worker_out, lock), daemon=True)
        x.start()
        running_threads.append(x)
        print('Started worker {} with {} words'.format(worker, len(list)))

    for thread in running_threads:
        thread.join()

    ranks = []

    for cur in range(threads):
        for dic in worker_out:
            if dic['worker'] == cur:
                ranks.extend(dic['output'])
                break

    return ranks

def rank_helper(this_word_list, word_list, word_correct, word_wrong_place, word_wrong, worker, worker_output, lock):
    ranks = []
    for index, word in enumerate(this_word_list):
        word_correct, word_wrong_place, word_wrong = parse_input('WWWWW', word, word_correct, word_wrong_place, word_wrong)
        word_list_copy, _ = find_all_valid(word_list.copy(), None, word_correct, word_wrong_place, word_wrong)
        ranks.append(len(word_list) - len(word_list_copy))
        #print('\nWorker {}: Running word {}. Score {} ({} of {})'.format(worker, word, len(word_list) - len(word_list_copy), index, len(this_word_list)))
    print('\nWorker {} complete'.format(worker))
    with lock:
        worker_output.append({'worker': worker, 'output': ranks})
    return ranks

def find_highest_points(words, ranks):
    high = 0
    high_index = -1
    for index, _ in enumerate(words):
        if ranks[index] > high:
            high = ranks[index]
            high_index = index

    return high_index


def solver(starting_word="crane"):
    with open('../five_letter_words.txt', 'r') as file:
        words_temp = file.readlines()

    words = []
    for word in words_temp:
        words.append(word.strip().lower())

    words = list(set(words))
    words.sort()

    word_correct = ['', '', '', '', ''] # Letters in correct place
    word_wrong_place = {} # Give letter, and then a list of places with incorrect location
    word_wrong = [] # Letters that aren't in the word at all

    if starting_word in words:
        words.pop(words.index(starting_word))

    print('Correct (in correct place): C, semi-correct (in wrong place): S, Wrong (not in word): W')

    print('Guess 1: {}'.format(starting_word))
    (word_correct,
     word_wrong_place,
     word_wrong) = parse_input(input(), starting_word, word_correct, word_wrong_place, word_wrong)

    ranks = ['' for word in words]

    guess = 2
    while True:
        if len(words) == 0:
            print("The word isn't on the list")
            break


        words, ranks = find_all_valid(words, ranks, word_correct, word_wrong_place, word_wrong)
        ranks = give_rank(words, word_correct, word_wrong_place, word_wrong, threads=int(len(words)/3) if int(len(words)/3) > 0 else 1)

        word = words[find_highest_points(words, ranks)]

        print('Guess {}: {}, Value: {}, Words Left: {}'.format(guess, word, ranks[words.index(word)], len(words)))
        inp = input()
        if inp == 'n':
            ranks.pop(words.index(word))
            words.pop(words.index(word))
            continue
        (word_correct,
         word_wrong_place,
         word_wrong) = parse_input(inp, word, word_correct, word_wrong_place, word_wrong)

        if word_correct == list(word):
            print('{} is the correct word. Worked at guess {}'.format(word, guess))
            break
        guess += 1

solver()
