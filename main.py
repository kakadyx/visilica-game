from logic import Logic
from interface import Interface

Interface.greetings()

while not Logic.comparison():
    Interface.print_main_interface()
    char = input('Введите предполагаемую букву: ')
    if  Logic.len_check(char) and Logic.ord_check(char) :
        Logic.check_input(char)
        print(Logic.word_lst)
        if Logic.word_lst == Logic.word_try_lst:
            print("Поздравляю, вы победили! ")
            break
    else:
        print('\n')
        print('Вы ввели неправильный символ, используйте только русский алфавит ')
    
   

if Logic.comparison():
    print('Вы проиграли( По вашей вине погиб человек')
    Logic.print_word()