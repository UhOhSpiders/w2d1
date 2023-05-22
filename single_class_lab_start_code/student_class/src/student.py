class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        # self.talk = talk
        # self.talk = talk
        # self.fav_lang = fav_lang
    
    def name(self, name):
        self.name = name

    def cohort(self, cohort):
        self.cohort = cohort
    
    def talk(self):
        # self.talk = talk
        return "I can talk!"
    
    def say_favourite_language(self, fav):
        say_fav = "I love " + fav
        return say_fav
