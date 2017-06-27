class Airlane:
    def __init__(self, airplane_type, salary,ticket_price,gas_price):
        self.airplane_type = airplane_type
        self.salary = salary
        self. ticket_price = ticket_price


class box:
    def __init__(self, volume,coffee):
        self.volume = volume
        self.coffee = coffee

class lorry:
    def __init__(self):
        self.boxes = []
    def add_box(self,box):
        self.boxes.append(box)
    def total(self):
        sum = 0
        for box in self.boxes:
            sum += box.volume * box.coffee.price
        return sum

def main():
    coffee_arabica = coffee('aravica', 200)
    coffee_rabusta = coffee('rabusta', 130)
    box1 = box(40,coffee_arabica)
    box2 = box(50,coffee_rabusta)
    box3 = box(10,coffee_arabica)
    box4 = box(90, coffee_rabusta)

    Lorry = lorry()
    Lorry.add_box(box1)
    Lorry.add_box(box2)
    Lorry.add_box(box3)
    Lorry.add_box(box4)

    print(Lorry.total())
main()
