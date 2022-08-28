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
            print(f"There are {self.tickets} tickets remaining")  
            print(f"There are {self.parkingSpaces} parking spaces remaining")   
            print(self.currentTickets)  
            
        
    def payForParking(self):
        pass
        """
        alex's part 
        
        """

    def leaveGarage(self):
        if self.currentTickets['paid'] == True: 
            print("Thank you, have a nice day!")
            self.tickets[0] += 1
            self.parkingSpaces[0] += 1
            self.currentTickets['paid'] = False
            
        elif self.currentTickets['paid'] == False: 
            print("Please pay for your ticket before leaving")
            self.payForParking()

ticket = Parking_garage()

class Garage:
    def run(self):
        while True:
            nav = input("What would you like to do? (enter/pay/leave)?")
            if nav == 'enter':
                ticket.takeTicket()
                
            elif nav == 'pay':
                pass

            elif nav == 'leave':
                paid = input('have you paid for your ticket (y/n)?')
                if paid == 'y':
                    ticket.leaveGarage()

                elif paid == 'n':
                    ticket.payForParking()
                    

                
            else: 
                print("Invalid Input. Please try again")


garage = Garage()
garage.run()