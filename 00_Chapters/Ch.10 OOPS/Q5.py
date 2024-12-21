'''
Write a class Train which has methods to book a ticket, get status(no of seats)
and get fare information of trains running under Indian Railways.
'''
import random
class Train:
    def book(self, trainNo, fromStation, toStation):
        print(f"Ticket is booked in train no: {trainNo} from {fromStation} to {toStation}")

    def status(self, trainNo):
        print(f"Train no: {trainNo} is running on time and has {random.randint(0, 100)} seats available")

    def fare(self, trainNo, fromStation, toStation):
        print(f"Ticket fare in train no: {trainNo} from {fromStation} to {toStation} is {random.randint(999, 4500)}")

train = Train()
train.book(12345, "Delhi", "Mumbai")
train.status(12345)
train.fare(12345, "Delhi", "Mumbai")

'''
1. Class train define kar do.
2. Usmein teen methods banane hain: book, status, fare.
3. book method mein train no, from station, to station as arguments lena hai.
4. status method mein train no as argument lena hai.
5. fare method mein train no, from station, to station as arguments lena hai.
6. Sabhi methods mein print karke dikhana hai.
7. Random module ka use karke kuch random values generate karke dikhana hai.
8. Ek object banake us object ke through sabhi methods ko call karke dikhana hai.
'''