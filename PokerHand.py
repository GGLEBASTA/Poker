class PokerHand():
    """
    Класс для идентификации покерной комбинации,введённой пользователем.
    P.S. Старшая карта не является комбинацией!
    """
    mast_ = ['S','H','D','C']       #список мастей(пики,черви,буби,крести)
    suits_ = ['A','2','3','4','5','6','7','8','9','J','Q','K','T',] #достоинства карт
    st2 = [['2', '3', '4', '5','A'],            #вариации комбинаций на СТРИТ
           ['2', '3', '4', '5', '6'],
           ['3', '4', '5', '6', '7'],
           ['4', '5', '6', '7', '8'],
           ['5', '6', '7', '8', '9'],
           ['6', '7', '8', '9', 'T'],
           ['7', '8', '9', 'J', 'T'],
           ['8', '9', 'J', 'Q', 'T'],
           ['9', 'J', 'K', 'Q', 'T'],
           ['A', 'J', 'K', 'Q', 'T']]

    ##### ИТОГОВЫЙ ТИП КОМБИНАЦИИ #####
    type_of_hand = ''
    ###################################

    def __str__(self):          #строковый метод выводы для пользователя
        if self.type_of_hand:
            return str(self.start + self.type_of_hand)          #заданная комбинация + её тип
        else:               #если не собрали комбинацийы
            return 'СТАРШАЯ КАРТА'

    def __init__(self, start):
        self.start = start      #заданная комбинация
        self.ls_ = list(self.start)     #список из строки с комбинацией для детального анализа
        PokerHand.main(self)    #запускаем АНАЛИЗ!!!

    #Функция проверки Роял-Флэш
    def royal_flash(self):
        royal_list = str(self.start).split()
        royal_count = 0
        for r in royal_list:
            if(r in ['AS','KS','QS','JS','TS']):
                royal_count += 1
            else:
                return False
        if royal_count == 5:
            return True



    #Функция проверки Пары,Двух Пар,Сета,Фулл-Хауса и Каре
    def power(self):
        without_ = [x for x in self.ls_ if (x not in self.mast_ and x != ' ')]      #убираем масти
        max = 0     #кол-во карт первого достоинства
        max2 = 0    #кол-во карт второго достоинства(если будут)
        w_check = []  #список предотвращающий просмотр одних и тех же достоинств в цикле
        for w in without_:
            if(w not in w_check): #проверяем не берём ли мы одинаковые достоинства
                w_check.append(w)
                checkr = without_.count(w)  #считаем количество
                if(checkr == 4): #каре
                    if(max<checkr):
                        max = checkr
                        return max,max2
                elif(checkr == 3 or checkr == 2): #пара,две пары,сет или фул-хаус
                        if(max == 0):
                            max = checkr
                        elif(max!=0):
                            max2 = checkr
            else:
                continue
        return max,max2 #выводим кортеж из 2 значениий

    #Функция проверки Стрит
    def stret(self):
        without_ = [x for x in self.ls_ if (x not in self.mast_ and x != ' ')]  #убираем масти
        without_.sort()         #сортируем
        if without_ in self.st2: #если комбинация совпала с комбинацией в базе СТРИТОВ
            return True
        else:
            return False

    #### АНАЛИЗ КОМБИНАЦИИ ####
    def main(self):
        #Проверка на РОЯЛ-ФЛЭШ
        if PokerHand.royal_flash(self):
            self.type_of_hand = '- РОЯЛ-ФЛЭШ'
        else:
            #Проверка на флэш
            for i in self.mast_:
                check = self.ls_.count(i)
                if(check==5):
                    #проверка на стрит флэш
                    bool_ = PokerHand.stret(self)
                    if bool_:
                        self.type_of_hand = '- СТРИТ-ФЛЕШ'
                        break
                    else:
                        self.type_of_hand = '- ФЛЕШ'
                        break

            #проверяем обычный стрит
            bool_2 = PokerHand.stret(self)
            if bool_2:
                self.type_of_hand = '- СТРИТ'
            #проверка пары,двух пар,сета и каре
            else:
                bool_3 = PokerHand.power(self)
                if 0 in bool_3: #если не было 2 повторяющихся достоинств
                    for element in bool_3:
                        if(element==4):
                            self.type_of_hand = '- КАРЕ'
                            break
                        elif(element == 3):
                            self.type_of_hand = '- СЕТ'
                            break
                        elif(element == 2):
                            self.type_of_hand = '- ПАРА'
                            break
                else:
                    if(bool_3[0] != bool_3[1]):
                        self.type_of_hand = '- ФУЛЛ-ХАУС'
                    else:
                        self.type_of_hand = '- ДВЕ ПАРЫ'




str_ = input('Введите комбинацию для индентификации:\n')
cl = PokerHand(str_)
print(cl)