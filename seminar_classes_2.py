class Color:
    def __init__(self, tuple1):
        self.tuple1 = tuple1
        END = '\033[0'
        START = '\033[1;38;2'
        MOD = 'm'
        # Cornflower blue
        red_level = tuple1[0]
        green_level = tuple1[1]
        blue_level = tuple1[2]
        print(f'{START};{red_level};{green_level};{blue_level}{MOD}●{END}{MOD}'
              )
    def __eq__(self, other) -> bool:
        if self.tuple1 == other.tuple1:
            return True
        else:
            return False
    def __add__(self, other):
        return (min(self.tuple1[0]+other.tuple1[0], 255), min(self.tuple1[1]+ other.tuple1[1], 255), min(self.tuple1[2]+other.tuple1[2]), 255)


    @staticmethod
    def br(color, c):
        cl = -256*(1-c)
        F = (259*(cl+255))/(255*(259-cl))
        return F*(self.tuple1[0]-128)+128

    def __mul__(self, c):
        cl = -256*(1-c)
        F = (259*(cl+255))/(255*(259-cl))
        L1 = F*(self.tuple1[0]-128)+128
        L2 = F*(self.tuple1[1]-128)+128
        L3 = F*(self.tuple1[2]-128)+128
        return Color((Color((0, 0, 255)).br(tuple[0], c), Color((0, 0, 255)).br(tuple[1], c), Color((0, 0, 255)).br(tuple[2], c)))


#Color(Color((0, 0, 255)).__add__(Color((0, 255, 0))))
'''
orange1 = Color((255, 165, 0))
red = Color((255, 0, 0))
green = Color((0, 255, 0))
orange2 = Color((255, 165, 0))
color_list = [orange1, red, green, orange2]
set1 = set()
for i in color_list:
    set1.add(i.tuple1)
print(set1)
for i in set1:
    Color(i)
'''
Color((0, 255, 255))*0.1