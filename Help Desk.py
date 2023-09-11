from Ticket import Ticket  # imports Ticket from Ticket class to Test.py


def displayAll():
    for request in bigList:  # go through every ticket in the list (bigList)
        request.display()  # display a ticket


# LIST OF TICKETS SUBMITTED
bigList = []
startNumber = 2000  # TICKET NUMBERS BEGIN FROM 2000-

# MENU SELECTION DISPLAY
while True:  # CONTINUE TO EXECUTE THE MENU
    print(
        '''
            Menu
            1 Submit helpdesk ticket  
            2 Show all tickets
            3 Respond to ticket by number
            4 Re-open resolved ticket
            5 Display ticket statistics
            0 Exit
        '''
    )
    command = input("Enter menu selection ")  # PROMPTING USER TO SELECT MENU OPTIONS

    # EXIT FROM HELP DESK MENU
    if command == "0":
        exit("Request finished ")

    # CREATE TICKET SUBMISSION
    if command == "1":

        submitAgain = True
        while submitAgain:
            startNumber += 1  # ticket number increased by 1
            request = Ticket(startNumber)  # creating a ticket instance from Ticket class
            request.submit()  # using submit method of the Ticket class
            request.display()  # visualises the Ticket using the display method in the Ticket class
            bigList.append(request)  # adding created Tickets to the ticket list (bigList)

            answer = input("Do you have another problem to submit? (Y/N) ")  # prompting user to submit another query
            if answer == "N":
                submitAgain = False  # if answer is No, goes back to menu selection

    # DISPLAY ALL TICKETS
    if command == "2":
        displayAll()

    # DISPLAY TICKET STATISTICS
    if command == "5":
        totalTickets = len(bigList)  # gives length of list as an integer
        print("Number of Tickets Submitted: " + str(totalTickets))  # display number of tickets submitted

        totalOpen = 0  # initial value of totalOpen variable
        totalClosed = 0
        totalReopened = 0
        for request in bigList:
            if request.status == "Open":  # checking for any "open" status tickets
                totalOpen += 1  # adding "open" status tickets to totalOpen by 1
            elif request.status == "Closed":  # checking for any "closed" status tickets
                totalClosed += 1  # adding "closed" status tickets to totalClosed by 1
            elif request.status == "Reopened":  # checking for any "reopened" status tickets
                totalReopened += 1  # adding "reopened" status tickets to totalReopened by 1
        print("Number of Open Tickets " + str(totalOpen))  # display number of open tickets
        print("Number of Closed Tickets " + str(totalClosed))  # display number of closed tickets
        print("Number of Reopened Tickets " + str(totalReopened))  # display number of reopened tickets

    # REOPENING TO TICKET
    if command == "4":
        displayAll()

        userInput = input("What is the ticket number? ")
        for request in bigList:
            if str(request.number) == userInput:
                request.status = "Reopened"

    # RESPONDING TO A TICKET
    if command == "3":
        displayAll()

        userInput = input("What is the ticket number? ")
        for request in bigList:
            if str(request.number) == userInput:
                userInput = input("What is the response? ")
                request.response = userInput
                request.status = "Closed"







