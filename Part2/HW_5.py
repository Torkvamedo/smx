class personal:
    def __init__(self, pilot, stewardess):
        self.pilot = pilot
        self.stewardess = stewardess

class ticket:
    def __init__(self, ticket_type,ticket_cost):
        self.ticket_type = ticket_type
        self.ticket_cost = ticket_cost

class Airplane:
    def __init__(self,model,gas,gas_cost):
        self.model = model
        self.gas = gas
        self.gas_cost = gas_cost

class Flight:
    def __init__(self):
        self.tickets = []
    def add_ticket(self, tickets):
        self.add_ticket.append(ticket)
    def total(self):
        sum = 0
        for ticket in self.tickets:
            sum +=ticket.cost*ticket.ticket_type
        return sum


def main():
    firs_pilot = personal('James D', 8000)
    second_pilot = personal('Adam H', 7800)
    first_class = ticket('first_class', 700)
    second_class = ticket('second_class',400)
    bioing747 = Airplane('Bioing 747',14580,30)


    Price = Flight()
    Price.add_ticket(firs_pilot)

    Price.add_ticket(second_pilot)
    Price.add_ticket(first_class)
    Price.add_ticket(second_class)
    Price.add_ticket(bioing747)

    print(Price.total())
main()



