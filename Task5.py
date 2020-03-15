class Act_of_Shooting:

    def __init__(self):
        pass

    def bullets_(self):
        self.bullets = int(input("Количество патронов - "))
        if self.bullets >= 1 and self.bullets <= 30:
            for i in range(1, self.bullets + 1):
                print(f"Бах {i}")
                # if i == self.bullets:   
                #     break

        else:
            print(f"В один магазин нелья поместить больше 30 патронов, а вы хотите поместить {self.bullets} патронов")

class Act_of_Shooting2(Act_of_Shooting):
    def __init__(self):
        pass
    def reloads_(self):
        while 1:
            print("1) Перезаредить обоиму 2) Теперь я хочу мира")
            self.input_bullets = int(input("Выбери вариант - "))
            if self.input_bullets == 1:
                Act_of_Shooting.bullets_(self)
            elif self.input_bullets <= 2:
                break

Ryan = Act_of_Shooting()
reloads = Act_of_Shooting2()
Ryan.bullets_()
reloads.reloads_()