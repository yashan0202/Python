class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

yashApplication = RailwayForm()
yashApplication.name = "Yash"
yashApplication.train = "Rajdhani Express"
yashApplication.printData()