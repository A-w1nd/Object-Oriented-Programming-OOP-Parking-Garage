class Parking_garage:
    def __init__(self, tickets, parkingSpaces, currentTickets=4):
            self.tickets = tickets
            self.parkingSpaces = parkingSpaces
            self.currentTickets = currentTickets

class Garage:
    def __init__(self):
        self.tickets = []
        self.parkingSpaces = []
        self.currentTickets = {}
            
        
    def takeTicket(self, tickets, parkingSpaces):
        print("Checking for space....")
        if self.parkingSpaces == 0:
            print("We are currently full!")
            
        else:    
            Parking_garage.tickets -= 1
            Parking_garage.parkingSpaces -= 1     
        
    def payForParking(self):
        pass
        """
        alex's part 
        
        """

    def leaveGarage(self, tickets, parkingSpaces):
        pass
#         if currentTicket == True:
#             print("Thank you, have a nice day!")
#             Parking_garage.tickets += 1
#             Parking_garage.parkingSpaces += 1
#             Parking_garage.currentTickets['tickets'] = False
            
#         else:
#             print("Please pay for your ticket before leaving")
#             self.payForParking()

    def run(self):
        while True:
            nav = input("Would you like to enter the garage? (y/n)?")
            if nav == 'y':
                self.takeTicket()
                
            elif nav == 'n':
                print("Maybe next time!")
                break

garage = Garage()
garage.run()