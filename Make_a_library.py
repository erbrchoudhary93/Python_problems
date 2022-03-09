class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displatbook(self):
        print(f"We have following book in the library : {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book-Database has been updated . You can take this book now ")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addbook(self, book):
        self.booklist.append(book)
        print(f"Book has been added to the booklist ")

    def returnbook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    harry = Library(['Python', "Rich Daddy poor dady", 'Harry potter', 'C++',"Algorithms by CLRS"], "Codewithharry")
    while (True):
        print(f"Welcome to the {harry.name} library . Enter your choise to continue ")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choise = int(input())

        if user_choise == 1:
            harry.displatbook()
        elif user_choise == 2:
            book = input("Enter the name of book you want to lend :  ")
            user = input('Enter your name : ')
            harry.lendbook(user)

        elif user_choise == 3:
            book = input("Enter the name of book you want to add :  ")
            harry.addbook(book)

        elif user_choise == 4:
            book = input("Enter the name of book you want to return :  ")
            harry.returnbook(book)
        else:
            print("Not a valid optin")
        print("press q to quit and c to continue ")
        user_choise2 = ""
        while (user_choise2 != "c" and user_choise2 != "q"):
            user_choise2 = input()
            if user_choise2 == "q":
                exit()
            if user_choise2 == "c":
                continue


