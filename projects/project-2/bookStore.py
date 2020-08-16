from tkinter import *
from databaseService import DatabaseService

class BookStore(Frame):

    """ 
    A Simple GUI application for managing BookStore
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWidgets()
        self.dbService = DatabaseService("books.db")

    def viewAllCommand(self):
        self.displayList.delete(0, END)
        for row in self.dbService.viewAll():
            self.displayList.insert(END, row)

    def searchCommand(self):
        self.displayList.delete(0, END)
        for row in self.dbService.search(self.titleInput.get(), self.authorInput.get(), self.yearInput.get(), self.isbnInput.get()):
            self.displayList.insert(END, row)

    def addCommand(self):
        self.dbService.insert(self.titleInput.get(), self.authorInput.get(), self.yearInput.get(), self.isbnInput.get())
        self.viewAllCommand()

    def updateCommand(self):
        self.dbService.update(self.currentSelected[0], self.titleInput.get(), self.authorInput.get(), self.yearInput.get(), self.isbnInput.get())
        self.viewAllCommand()   

    def deleteCommand(self):
        self.dbService.delete(self.currentSelected[0])
        self.viewAllCommand()  

    def getSelectedCommand(self, event):        
        index = self.displayList.curselection()[0]
        self.currentSelected = self.displayList.get(index)
        
        self.entryTitle.delete(0, END)
        self.entryTitle.insert(END, self.currentSelected[1])

        self.entryAuthor.delete(0, END)
        self.entryAuthor.insert(END, self.currentSelected[2])

        self.entryYear.delete(0, END)
        self.entryYear.insert(END, self.currentSelected[3])

        self.entryIsbn.delete(0, END)
        self.entryIsbn.insert(END, self.currentSelected[4])

    def createWidgets(self):
        self.lbTitle = Label(self.master, text="Title")
        self.lbTitle.grid(row=0, column=0)

        self.titleInput = StringVar()
        self.entryTitle = Entry(self.master, textvariable=self.titleInput)
        self.entryTitle.grid(row=0, column=1)

        self.lbAuthor = Label(self.master, text="Author")
        self.lbAuthor.grid(row=0, column=2)

        self.authorInput = StringVar()
        self.entryAuthor = Entry(self.master, textvariable=self.authorInput)
        self.entryAuthor.grid(row=0, column=3)

        self.lbYear = Label(self.master, text="Year")
        self.lbYear.grid(row=1, column=0)

        self.yearInput = StringVar()
        self.entryYear = Entry(self.master, textvariable=self.yearInput)
        self.entryYear.grid(row=1, column=1)

        self.lbISBN = Label(self.master, text="ISBN")
        self.lbISBN.grid(row=1, column=2)

        self.isbnInput = StringVar()
        self.entryIsbn = Entry(self.master, textvariable=self.isbnInput)
        self.entryIsbn.grid(row=1, column=3)

        self.displayList = Listbox(self.master, height=6, width=35)
        self.displayList.grid(row=2, column=0, rowspan=6, columnspan=2)
        self.displayList.bind("<<ListboxSelect>>", self.getSelectedCommand)

        self.listScrollBar = Scrollbar(self.master)
        self.listScrollBar.grid(row=2, column=2, rowspan=6)

        self.displayList.configure(yscrollcommand=self.listScrollBar.set)
        self.listScrollBar.configure(command=self.displayList.yview)

        self.buttonViewAll = Button(self.master, text="View All", width=12, command=self.viewAllCommand)
        self.buttonViewAll.grid(row=2, column=3)

        self.buttonSearch = Button(self.master, text="Search Book", width=12, command=self.searchCommand)
        self.buttonSearch.grid(row=3, column=3)

        self.buttonAdd = Button(self.master, text="Add Book", width=12, command=self.addCommand)
        self.buttonAdd.grid(row=4, column=3)

        self.buttonUpdate = Button(self.master, text="Update", width=12, command=self.updateCommand)
        self.buttonUpdate.grid(row=5, column=3)

        self.buttonDelete = Button(self.master, text="Delete", width=12, command=self.deleteCommand)
        self.buttonDelete.grid(row=6, column=3)

        self.buttonClose = Button(self.master, text="Close", width=12, command=self.master.destroy)
        self.buttonClose.grid(row=7, column=3)


if __name__ == "__main__":
    root = Tk()
    bookStore = BookStore(root)    
    bookStore.mainloop()