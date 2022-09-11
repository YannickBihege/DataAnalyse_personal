from tkinter import *
from backend import Database
#filepath to database
database = Database("books.db")


class Window(object):

    def __init__(self, window):

        self.window = window
        #add title
        self.window.wm_title("Bookstore")

        self.l0 =Label(window , text= "Title" ,height =1, width= 10)
        self.l0.grid(row=0, column = 0) 

        self.title_value=StringVar()
        self.e1 =Entry(window , textvariable= self.title_value)
        self.e1.grid(row=0, column = 1)   

        self.l1 =Label(window , text= "Author" ,height =1, width= 10)
        self.l1.grid(row=0, column = 2)

        self.author_value=StringVar()
        self.e2 =Entry(window , textvariable= self.author_value)
        self.e2.grid(row=0, column = 3)  

        self.lr1 =Label(window , text= "Year" ,height =1, width= 10)
        self.lr1.grid(row=1, column = 0) 

        self.year_value=StringVar()
        self.er1 =Entry(window , textvariable= self.year_value)
        self.er1.grid(row=1, column = 1)   

        self.lr12 =Label(window , text= "Isbn" ,height =1, width= 10)
        self.lr12.grid(row=1, column = 2)

        self.isbn_value=StringVar()
        self.er12 =Entry(window , textvariable= self.isbn_value)
        self.er12.grid(row=1, column = 3)  

        self.list1 = Listbox(window, height = 6 , width = 32)
        self.list1.grid(row =2 , column = 0, rowspan = 6 ,columnspan = 2)

        #create scrollbar
        self.sb1 = Scrollbar(window)
        self.sb1.grid(row = 2, column = 2 , rowspan = 6 )
        #add to list
        self.list1.configure(yscrollcommand = self.sb1.set)
        self.sb1.configure(command = self.list1.yview)

        # eventtype  and function as args
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = Button(window, text="View all" , command = self.view_command , width = 12 )
        b1.grid(row=2, column = 3 )

        b2 = Button(window, text="Search entry" , command = self.search_command , width = 12 )
        b2.grid(row=3, column = 3)

        b3 = Button(window, text="Add entry" , command = self.add_command , width = 12)
        b3.grid(row=4, column = 3)

        b4 = Button(window, text="Update" , command = self.update_command , width = 12 )
        b4.grid(row=5, column = 3)

        b5 = Button(window, text="Delete" , command = self.delete_command , width = 12)
        b5.grid(row=6, column = 3)

        b6 = Button(window, text="Close" , command = window.destroy , width = 12)
        b6.grid(row=7, column = 3)

    def get_selected_row(self,event):
        try:
            global selected_tuple
        #get the index of the selected row
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
    #delete everything from entry
            self.e1.delete(0,END)
            self.e1.insert(END, self.selected_tuple[1])

            self.e2.delete(0,END)
            self.e2.insert(END, self.selected_tuple[2])

            self.er1.delete(0,END)
            self.er1.insert(END, self.selected_tuple[3])

            self.er12.delete(0,END)
            self.er12.insert(END, self.selected_tuple[4])

        except IndexError:
            pass


    def view_command(self):
        #make sure the list is empty
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)   #every new row is at the end

    def search_command(self):
        #make sure the list is empty
        self.list1.delete(0, END)
        for row in database.search(self.title_value.get(), self.author_value.get(),self.year_value.get(),self.isbn_value.get() ):
            self.list1.insert(END, row)

    def add_command(self):
        #empty the box
        self.list1.delete(0, END)
    #insert in the database
        database.insert(self.title_value.get(), self.author_value.get(),self.year_value.get(),self.isbn_value.get() )
        self.list1.insert(END, (self.title_value.get(), self.author_value.get(),self.year_value.get(),self.isbn_value.get() ) )

    
    
    def delete_command(self):
        database.delete(selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_value.get(), self.author_value.get(),self.year_value.get(),self.isbn_value.get() )
    #   print(selected_tuple[0], selected_tuple[1],selected_tuple[2],selected_tuple[3] ,selected_tuple[4])


window = Tk()
Window(window)
window.mainloop()
