class Horse:

    def __init__(self, x_distance=0, sound='Frrr', y_distance=0, sound1='I train, eat, sleep, and repeat'):
        self.distance = x_distance
        self.sound = sound
        super().__init__(y_distance, sound1)


    def run(self, dx):
        isinstance(self.distance, int)
        self.distance = self.distance + dx
        return self.distance


class Eagle:

    def __init__(self, y_distance=0, sound1='I train, eat, sleep, and repeat'):
        self.distance1 = y_distance
        self.sound = sound1

    def fly(self, dy):
        isinstance(dy, int)
        self.distance1 = self.distance1 + dy
        return self.distance1


class Pegasus(Horse, Eagle):

    def __init__(self, x_distance, sound, y_distance, sound1):
        super().__init__(x_distance, sound, y_distance, sound1)

    def move(self, dx, dy):
        return super().run(dx), super().fly(dy)

    def get_pos(self):
        return f'длина: {self.distance}, высота: {self.distance1}'

    def voice(self):
        return print(self.sound)


#p1 = Pegasus(0, 0, 'Hop hey la la lay')
#p1 = Pegasus(0,0,'hey')
#print(p1.get_pos())
p1 = Pegasus(0, 'Frrrr', 0, 'I train, eat, sleep, and repeat')
#print(p1.mro())
print(Pegasus.mro())
print(Horse.mro())
print(Eagle.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
