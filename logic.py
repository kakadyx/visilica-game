import random

class Logic:
    num_of_errors = 0
    error_list =[]
    max_errors = 7
    error_last = max_errors
    
    file = open("Words.txt",'r',encoding="utf-8")
    words_list=file.readlines()
    file.close()
    word_bad = random.choice(words_list)
    if '\n' in word_bad:
        word = word_bad[:(len(word_bad)-1):].lower()
    else:
        word = word_bad.lower()

    word_lst = [char for char in word]

    word_try_lst = ['_' for i in range(len(word_lst))]

    @classmethod
    def print_word(cls):
        print(Logic.word)

    @classmethod
    def comparison(cls):
        result=0
        if Logic.max_errors==Logic.num_of_errors:
            result=1
        return result

    def check_input(choice):
        i=0
        check_error = 0
        single_char = str(choice).lower()

        if single_char == 'и' or single_char == 'й':
            for char in Logic.word_lst:
                if char == 'и' or char == 'й':
                    if single_char =='и':
                        Logic.word_try_lst[i] = Logic.word_lst[i]
                    check_error=1
                i += 1
            if check_error == 0:
                Logic.num_of_errors += 1
                if single_char not in Logic.error_list:
                    Logic.error_list.append('и')
                    Logic.error_list.append('й')

        elif single_char == 'е' or single_char == 'ё':
            for char in Logic.word_lst:
                if char == 'е' or char == 'ё':
                    Logic.word_try_lst[i] = Logic.word_lst[i]
                    check_error=1
                i += 1
            if check_error == 0:
                Logic.num_of_errors += 1
                if single_char not in Logic.error_list:
                    Logic.error_list.append('е')
                    Logic.error_list.append('ё')

        else:       
            for char in Logic.word_lst:
                if char == single_char:
                    Logic.word_try_lst[i]=single_char
                    check_error=1
                i += 1
            if single_char in Logic.error_list:   
                pass 
            else:
                if check_error == 0:
                    Logic.num_of_errors += 1
                    if single_char not in Logic.error_list:
                        Logic.error_list.append(single_char)

        Logic.error_last = Logic.max_errors-Logic.num_of_errors

    @classmethod
    def ord_check(cls,char):
        if ord(char) > 1039 and ord(char)< 1106:
            return True
        else:
            return False

    @classmethod
    def len_check(cls,char):
        if len(char) == 1:
            return True
        else: 
            return False

