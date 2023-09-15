class Ticket:
    def __init__(self, number=None, creator="", staffID="", email="", issue="", status="Open", response="Not Yet Provided"):        # default settings for each object
        self.number = number        # initialise ticket number
        self.creator = creator      # initialise ticket creator name
        self.staffID = staffID      # initialise staff ID
        self.email = email          # initialise email
        self.issue = issue          # initialise issue description
        self.response = response    # initialise ticket response
        self.status = status        # initialise ticket status

    # Method for display basic ticket info
    def display(self):
        print("Ticket Number: "+str(self.number))       # display the ticket number
        print("Ticket Creator: "+self.creator)          # display the name of the ticket creator
        print("Staff ID: "+self.staffID)                # display the staff ID associated with the ticket
        print("Email Address: "+self.email)             # display the email address of the ticket creator
        print("Issue: "+self.issue)                     # display the issue description in the ticket
        print("Response: "+self.response)               # display the response for the ticket
        print("Status: "+self.status)                   # display the current status of ticket
        print("--------------------------------------")

    # Change Password - Method
    def changepassword(self):
        password = self.staffID[0:2] + self.creator[0:3]        #  generate a new password using first 2 characters of StaffID and 3 characters of creator's name
        self.response = "User password was set to: " + password     #  update the ticket's response to the new password
        print(self.response)        # display the updated password message to the user
        self.status = "Closed"      # set the ticket status to 'Closed' after password change


    # Ticket submission - Method
    def submit(self):
        self.creator = input("Enter Your Name ")        # staff will enter their own name
        self.staffID = input("Please Enter Your Staff ID ")     # staff will enter their staff ID
        self.email = input("Please Enter your Email Address ")      # staff will enter their email
        self.issue = input("Please Enter the Description of Your Problem ")     # staff to enter the description of the problem
        if self.issue == "Password Change":         # check if the issue is related to 'Password Change' and call the 'changepassword' method if it is
            self.changepassword()


