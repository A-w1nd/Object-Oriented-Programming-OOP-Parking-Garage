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
        print("~-" * 15)
        print("Checking for space....")
        if self.parkingSpaces[0] <= 0:
            print("~-" * 15)
            print("We are currently full!")
            print("~-" * 15)
            
        else:    
            self.tickets[0] -= 1
            self.parkingSpaces[0] -= 1
            T = self.tickets[0]
            P = self.parkingSpaces[0]
            print("~-" * 15)
            print(f"There are {T} tickets remaining")  
            print(f"There are {P} parking spaces remaining")   
            # print(self.currentTickets)  
            print("~-" * 15)
            
        
    def payForParking(self):
        pay = input("How many tickets (1/2/3)")

        if pay == '1': 
                    self.currentTickets['paid'] = True
                    print("2.00")
                    input("payment method (credit/debit)")
                    print("please leave within 15 minutes")
                    self.tickets[0] += 1
                    self.parkingSpaces[0] += 1
                
                    
        if pay == '2':
                    self.currentTickets['paid'] == True
                    print("4.00")
                    input("payment method (credit/debit)")
                    print("please leave within 15 minutes")
                    self.tickets[0] += 2
                    self.parkingSpaces[0] += 2
            
                    
        if pay == '3':
                    self.currentTickets['paid'] = True
                    print("6.00")
                    input("payment method (credit/debit)")
                    print("please leave within 15 minutes")
                    self.tickets[0] += 3
                    self.parkingSpaces[0] += 3

    def leaveGarage(self):
        if self.currentTickets['paid'] == True: 
            print("~-" * 15)
            print("Thank you, have a nice day!")
            print("~-" * 15)
            self.tickets[0] += 1
            self.parkingSpaces[0] += 1
            self.currentTickets['paid'] = False
            
        elif self.currentTickets['paid'] == False: 
            print("~-" * 15)
            print("Please pay for your ticket before leaving")
            print("~-" * 15)
            self.payForParking()

    def refund(self):
        self.tickets[0] += 1
        self.parkingSpaces[0] += 1
        self.currentTickets['paid'] = True
        print("~-" * 15)
        print('Your refund has been completed')
        print('We are sorry for the inconvenience')
        print("~-" * 15)

ticket = Parking_garage()

class Garage:
    def run(self):
        while True:
            nav = input("What would you like to do? (enter/pay/refund/leave/quit)?")
            if nav == 'enter':
                ticket.takeTicket()
                
            elif nav == 'pay':
                pass

            elif nav == 'leave':
                print('(back)')
                paid = input('have you paid for your ticket (y/n)?')
                if paid == 'y':
                    ticket.leaveGarage()

                elif paid == 'n':
                    print("~-" * 15)
                    print("Please pay for your ticket before leaving")
                    print("~-" * 15)
                    ticket.payForParking()

                elif paid == 'back':
                    garage.run()

            elif nav == 'refund':
                print('(back)')
                ref = input("Would you like a refund (y/n)?")
                if ref == 'y':
                    ticket.refund()

                elif ref == 'n':
                        garage.run()

                elif ref == 'back':
                    garage.run()
                    

            elif nav == 'quit':
                print("~-" * 15)
                print('Thank you, have a nice day!')  
                print("~-" * 15)
                break      

            else: 
                print("~-" * 15)
                print("Invalid Input. Please try again")
                print("~-" * 15)

garage = Garage()
garage.run()
