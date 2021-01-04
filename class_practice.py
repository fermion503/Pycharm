class Human():

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        print("{}이의 나이는 {}살이며 몸무게는 {}kg입니다.".format(self.name, self.age, self.weight))

    def shooting(self, item):
        print("{}이/가 {}를 가지고 슛을 합니다~!!".format(self.name, item))

    def walking(self, mountain=None):
        if mountain is not None:
            self.weight -= 1
            print("{}이/가 {}를 올라 몸무게가 {}가 됐습니다.".format(self.name, mountain, self.weight))
        else:
            self.weight -= 0.1
            print("{}이/가 걸어서 몸무게가 {}가 됐습니다.".format(self.name, self.weight))

    def eating(self, food):
        if food in ["피자", "피킨"]:
            self.weight += 0.5
            print("{}이/가 {}를 먹어서 몸무게가 {}kg가 됐습니다.".format(self.name, food, self.weight))
        else:
            self.weight += 0.2
            print("{}이/가 {}를 먹어서 몸무게가 {}kg가 됐습니다.".format(self.name, food, self.weight))

    def study(self, study=15):
        print("{}이는 공부를 평소 1주에 {}시간만큼 합니다.".format(self.name, study))

# person = Human("영훈", 31, 77)
# person.shooting("축구공")
# person.walking()
# person.eating("과자")
# person.study(10)