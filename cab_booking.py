import time

class CabBooking:

    def __init__(self):

        self.users = {}

        self.rides = {}

        self.current_user = None
        
    def register(self):

        username = input("Enter username: ")

        if username in self.users:

            print("Username already exists! Try again.")

            return
        
        password = input("Enter password: ")

        self.users[username] = password

        self.rides[username] = []

        print("Registration Successful ! ")

    def login(self):

        username = input("Enter username: ")

        password = input("Enter password: ")

        if self.users.get(username) == password:

            self.current_user = username

            print("Login Successful ! ")

        else:

            print("Invalid credentials ! Try again. ")
            
    def book_ride(self):

        if not self.current_user:

            print("You need to log in first ! ")

            return
        
        pickup = input("Enter pickup location: ")

        destination = input("Enter destination: ")

        ride_details = {"pickup": pickup, "destination": destination, "status": "Confirmed"}

        self.rides[self.current_user].append(ride_details)

        print("Ride booked successfuly!\nwaiting for driver confirmation...")

        time.sleep(2)

        print("Driver assigned. Ride in progress...")

        time.sleep(2)

        ride_details["status"] = "Completed"

        print("Ride completed succesfully!")

    def view_rides(self):

        if not self.current_user:

            print("You need to log in first! ")

        if not self.rides[self.current_user]:
            
            print("no rides found! ")

            return

        for index, ride in enumerate(self.rides[self.current_user], start=1):

            print(f"Ride {index}: {ride}")

    def logout(self):

                if self.current_user:

                    print(f"Logged out from {self.current_user}")

                    self.current_user = None

                else:

                    print("No user is logged in!")

    def menu(self):

        while True:

            print("\n CAB BOOKING SYSTEM")

            print("1. Register")

            print("2. Login")

            print("3. Book a Ride")

            print("4. View Ride History")

            print("5. Logout")

            print("6. Exit")

            choice = input("Enter your chpoice: ")

            if choice == "1":
                
                self.register()

            elif choice == "2":

                self.login()

            elif choice == "3":

                self.book_ride()

            elif choice == "4":

                self.view_rides()

            elif choice == "5":

                self.logout()
                
            elif choice == "6":

                print("Exiting... Thank you for using our service!")

                break

            else:

                print("Invalid choice! Please try again.")

if __name__ == "__main__":

    app = CabBooking()

    app.menu()
    
