class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = list()
    
    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            print(self.passengers)
        else:
            print("Capacity is already met")

dubai_flight = Flight(3)
dubai_flight.add_passenger("Memo")
dubai_flight.add_passenger("Vika")
dubai_flight.add_passenger("Luba")
dubai_flight.add_passenger("Nastya")
dubai_flight.add_passenger("Test")
dubai_flight.add_passenger("text")