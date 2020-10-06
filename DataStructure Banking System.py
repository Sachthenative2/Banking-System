#Need to fix withdraw and implement deque
from collections import deque
from pythonds.basic import Stack
from pythonds.basic import Queue
from pythonds.basic import Deque
import random
import time
#from pythonds.basic import List

#Declaring our stacks for different bill types
#Stack implementation
hundredsStack = Stack()
fiftiesStack = Stack()
twentiesStack = Stack()
tensStack = Stack()
fivesStack = Stack()
onesStack = Stack()
waiting = Queue()
loanQueue = Deque()

finalAmount = 0
depoAmount = 0
billcounter = 0

hundreds = 0
fifties = 0
twenties = 0
tens = 0
fives = 0
ones = 0

def accountHolder(acctName, acctBal):
  global finalAmount
  finalAmount = acctBal
  global holder
  holder = []
  global holderName
  holderName = acctName
  global holderAcctNum
  holderAcctNum = random.randint(1,100)
  holderAcctNum *= 1324
  holder.append(acctName)
  holder.append(holderAcctNum)
  holder.append(acctBal)
  print("Account name: " + str(acctName))
  print("Account number: " + str(holderAcctNum))
  print("Account balance: $" + str(acctBal))

#Needs to be modified and made shorter
def depobillcounter():
  #Accessing the global variables to use them in the func
  global finalAmount
  global holder
  global hundreds
  global fifties
  global twenties
  global tens
  global fives
  global ones
  global billcounter
  i = 0
  depoAmount = 0
  #Adding ones
  onesinput = int(input("How many 1s would you like to deposit? "))
  while i < onesinput:
    onesStack.push(1)
    i += 1
    ones += 1
    finalAmount = int(finalAmount) + 1
  i = 0
  #Adding fives
  fivesinput = int(input("How many 5s would you like to deposit? "))
  while i < fivesinput:
    fivesStack.push(5)
    i = i + 1
    fives += 5
    finalAmount = int(finalAmount) + 5
  i = 0
  #adding tens
  tensinput = int(input("How many 10s would you like to deposit? "))
  while i < tensinput:
    tensStack.push(10)
    i += 1
    tens += 10
    finalAmount = int(finalAmount) + 10
  i = 0
  #Adding twenties
  twentiesinput = int(input("How many 20s would you like to deposit? "))
  while i < twentiesinput:
    twentiesStack.push(20)
    i += 1
    twenties += 20
    finalAmount = int(finalAmount) + 20
  i = 0
  #Adding fifties
  fiftiesinput = int(input("How many 50s would you like to deposit? "))
  while i < fiftiesinput:
    fiftiesStack.push(50)
    i = i + 1
    fifties += 50
    finalAmount = int(finalAmount) + 50
  i = 0
  #Adding hundreds
  hundredsinput = int(input("How many 100s would you like to deposit? "))
  while i < hundredsinput:
    hundredsStack.push(100)
    i += 1
    hundreds += 100
    finalAmount = int(finalAmount) + 100
  i = 0
  #Printing out the value that the user has in each bill value, then the final
  print("You now have $" + str(hundreds) + " in hundreds, $" + str(fifties) + " in fifties, $"+ str(twenties) + " in twenties, $" + str(tens) + " in tens, $" + str(fives) + " in fives, $" + str(ones) + " in ones")
  print("For a final balance of $" + str(finalAmount))
  #Modifying the amount in the users account
  modbal(getName(), finalAmount)

def withbillcounter():
  global finalAmount
  global holder
  #Monetary value that is incrementing for each bill being deposited
  hundreds = 0
  fifties = 0
  twenties = 0
  tens = 0
  fives = 0
  ones = 0
  i = 0
  withAmount = 0
  #Checking to see if the stacks are empty. If they are empty, give the user an error
  if onesStack.isEmpty() and fivesStack.isEmpty() and tensStack.isEmpty() and twentiesStack.isEmpty() and fiftiesStack.isEmpty() and hundredsStack.isEmpty():
    print("There are no bills to take out. Returning you to the main menu")
  #If the stacks are nto empty, go through with the withdraw func
  elif onesStack.size() >= 1 or fivesStack.size() >= 1 or tensStack.size() >= 1 or twentiesStack.size() >= 1 or fiftiesStack.size() >= 1 or hundredsStack.size() >= 1:
    #Asking the user for bills, adding them to the correct stack, and adding to the final monetary value for that bill
    onesinput = int(input("How many 1s would you like to withdraw? "))
    while i < onesinput:
      onesStack.pop()
      i += 1
      ones -= 1
      withAmount = int(withAmount) + 1
    i = 0
    fivesinput = int(input("How many 5s would you like to withdraw? "))
    while i < fivesinput:
      fivesStack.pop()
      i += 1
      fives -= 5
      withAmount += 5
    i = 0
    tensinput = int(input("How many 10s would you like to withdraw? "))
    while i < tensinput:
      tensStack.pop()
      i += 1
      tens -= 10
      withAmount += 10
    i = 0
    twentiesinput = int(input("How many 20s would you like to withdraw? "))
    while i < twentiesinput:
      twentiesStack.pop()
      i += 1
      twenties -= 20
      withAmount += 20
    i = 0
    fiftiesinput = int(input("How many 50s would you like to withdraw? "))
    while i < fiftiesinput:
      fiftiesStack.pop()
      i += 1
      fifties -= 50
      withAmount += 50
    i = 0
    hundredsinput = int(input("How many 100s would you like to withdraw? "))
    while i < hundredsinput:
      hundredsStack.pop()
      i += 1
      hundreds -= 100
      withAmount += 100
    i = 0
    
    finalAmount = int(finalAmount) - int(withAmount)
    print("You now have $" + str(hundreds) + " in hundreds, $" + str(fifties) + " in fifties, $"+ str(twenties) + " in twenties, $" + str(tens) + " in tens, $" + str(fives) + " in fives, $" + str(ones) + " in ones")
    print("For a final balance of $" + str(finalAmount - withAmount))
    modbal(getName(), finalAmount - withAmount)

def subtracting(valinput, billstack, billcounter, bill):
  #Accesses the depositAmount and the finalamount
  global depoAmount
  global finalAmount
  i = 0
  #Adds the bills to the stack for each bill
  while i < valinput:
    billstack.push(bill)
    #Increments the counter
    i -= 1
    #Adds the bill to the counter for that bill
    billcounter -= bill
    #Adds the bill to the finalAmount in the account
    finalAmount = billcounter
  #Returns how much is being added in this function
  return billcounter

def waitingTransactions(value):
  global finalAmount
  nameofholder = input("Please input your name: ")
  modbal(nameofholder, finalAmount - value)
  waiting.enqueue(value)
  finalAmount -= value
  print("Current amount of money within the account is " + str(finalAmount))
  print("Current list of transactions: " + str(waiting.size()))

def returnTransaction():
  for x in range (waiting.size()):
    print(waiting.dequeue())

def getName():
  return holderName

def getAcctNum():
  return "Account number: " + str(holderAcctNum)

def getBal():
  return "Account balance: $" + str(finalAmount)

def positionForLoan():
  loanQueue.addFront("Jimmy")
  loanQueue.addFront("Timmy")
  loanQueue.addFront(name)
  loanQueue.addFront("Freddie")
  loanQueue.addFront("Smith")
  for x in range (loanQueue.size()):
    f = loanQueue.removeFront()
    if f == name:
      print("You are in position " + str(x))

#List implementation
def getAcctInfo(nameOfAccount):
  tmp = holder.index(nameOfAccount)
  nameindex = holder.index(nameOfAccount)
  while nameindex <= nameindex + 2:
    if nameindex is not len(holder):
      if nameindex == tmp:
        print("Account name: " + str(holder[nameindex]))
      elif nameindex == tmp + 1:
        print("Account number: " + str(holder[nameindex]))
      elif nameindex == tmp + 2:
        print("Account balance: $" + str(holder[nameindex]))
      nameindex += 1
    elif nameindex == len(holder):
      break

def modbal(name, amount):
  tmp = holder.index(name)
  balindex = holder.index(name) +2
  holder[balindex] = amount

#Not written by us, taken from GeeksforGeeks with modification
def countdown(t):
  t = t * 5
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d} seconds'.format(secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
  print("You can now start your transactions")

#Main menu
print("Welcome, we will now create your account.")
print("Your account will be given a random account number that will be displayed")
name = input("Please enter your name: ")
bal = int(input("Please enter your account balance: "))
accountHolder(name, bal)
before = random.randint(1,10)
print("You are in a queue waiting for the bank teller, there are " + str(before) + " people in front of you")
#countdown(before)

x = 0
while(x == 0):
  answer = input("What would you like to do? (deposit, withdraw, account info, transaction, position, or exit)")
  if answer == "deposit":
    depobillcounter()
  elif answer == "withdraw":
    withbillcounter()
  elif answer == "account info":
    Chungus = input("Please put in your account name: ")
    getAcctInfo(Chungus)
  elif answer == "transaction":
    Chunga = input("Do you want to input a transaction or transaction history? (transaction or history) ")
    if Chunga == "transaction":
      Chooga = int(input("Input most recent transaction: "))
      waitingTransactions(Chooga)
    elif Chunga == "history":
      returnTransaction()
  if answer == "position":
    positionForLoan()
  elif answer == "exit":
    x =1