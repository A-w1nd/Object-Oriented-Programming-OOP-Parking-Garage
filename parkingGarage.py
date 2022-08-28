from tkinter import Y


class Parking_garage:
    def __init__(self, tickets  , parkingSpaces, currentTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTickets = currentTickets

    def __init__(self):
        self.tickets = [4]
        self.parkingSpaces = [4]
        self.currentTickets = {"paid" : False}
        
        
    def takeTicket(self):
        print("Checking for space....")
        if self.parkingSpaces[0] == 0:
            print("We are currently full!")
            
        else:    
            self.tickets[0] -= 1
            self.parkingSpaces[0] -= 1
            print(self.tickets)  
            print(self.parkingSpaces)   
            
        
    def payForParking(self):
        pass
        """
        alex's part 
        
        """

    def leaveGarage(self):
        pass
        if self.currentTickets == True:
            print("Thank you, have a nice day!")
            self.tickets += 1
            self.parkingSpaces += 1
            self.currentTickets['tickets'] = False
            
        else:
            print("Please pay for your ticket before leaving")
            self.payForParking()

ticket = Parking_garage()

class Garage:
    def run(self):
        while True:
            nav = input("Would you like to enter the garage? (y/n)?")
            if nav == 'y':
                ticket.takeTicket()
                
            elif nav == 'n':
                print("Maybe next time!")
                break
            
            else: 
                print("Invalid Input. Please try again")


garage = Garage()
garage.run()