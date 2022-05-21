class parent:
    def __init__(self, name, age, occupation):
        self.name = name 
        self.age = age
        self.occupation = occupation

    def introduce(self):
        print('{} is {} years old and is {}'.format(self.name, self.age, self.occupation))

    def order(self):
        print('{} says do that.'.format(self.name))

P1 = parent('Dan', 55, 'a Laywer')
P1.introduce()
P1.order()

# child has same methods and some of their own 
class child(parent):
    def __init__(self, name, age, occupation, graduation):
        super().__init__(name, age, occupation)
        self.graduation = graduation
    
    def graduate(self):
        print('{} graduated in {}'.format(self.name, self.graduation))
    
    def obey(self):
        print('{} obeys command'.format(self.name))

C1 = child('Alex', 18, 'unemployed', 2020)
C1.introduce()
C1.obey()
C1.graduate()