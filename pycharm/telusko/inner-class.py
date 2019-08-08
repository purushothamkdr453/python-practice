class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.age)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i3'
            self.memory = '8gb'

        def show(self):
            print(self.brand,self.cpu,self.memory)


s1 = student('Purushotham',28)
s1.show()
