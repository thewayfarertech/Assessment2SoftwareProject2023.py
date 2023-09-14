class Ticket:
    def __init__(self, number=None, creator="", staffID="", email="", issue="", status="Open", response="Not Yet Provided"):
        self.number = number
        self.creator = creator
        self.staffID = staffID
        self.email = email
        self.issue = issue
        self.response = response
        self.status = status

    # Method for display basic ticket info
    def display(self):
        print("Ticket Number: "+str(self.number))
        print("Ticket Creator: "+self.creator)
        print("Staff ID: "+self.staffID)
        print("Email Address: "+self.email)
        print("Issue: "+self.issue)
        print("Response: "+self.response)
        print("Status: "+self.status)
        print("--------------------------------------")

    # Change Password - Method
    def changepassword(self):
        password = self.staffID[0:2] + self.creator[0:3]
        self.response = "User password was set to: " + password
        print(self.response)
        self.status = "Closed"


    # Ticket submission - Method
    def submit(self):
        self.creator = input("Enter Your Name ")
        self.staffID = input("Please Enter Your Staff ID ")
        self.email = input("Please Enter your Email Address ")
        self.issue = input("Please Enter the Description of Your Problem ")
        if self.issue == "Password Change":
            self.changepassword()


