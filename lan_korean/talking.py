import random

class Human:
    def __init__(self, kk=1):
        self.feel = None
        self.name = None
        self.talk = None
        self.names(kk)
        self.feel_score()
        # 보통은 인스턴스 이름을 출력하는 편이 더 유용합니다.
        print(f"{self.name}: {self.talk}")

    def feel_score(self):
        feel_scores = random.randrange(1, 5)  # 1..4
        if feel_scores == 1:
            self.talk = '너무 좋다!'
            self.feel = "매우 좋음"
        elif feel_scores == 2:
            self.talk = '좋아~'
            self.feel = "좋음"
        elif feel_scores == 3:
            self.talk = '난 보통'
            self.feel = '보통'
        elif feel_scores == 4:
            self.talk = '기분 안좋네.'
            self.feel = '안좋음'
        else:
            self.talk = '난 다 망했어!어떡하지?'

    def names(self, kk=1):
        en = list("abcdefghijklmnopqrstuvwxyz")
        if kk <= 1:
            self.name = random.choice(en)
        else:
            self.name = ''.join(random.choices(en, k=kk))