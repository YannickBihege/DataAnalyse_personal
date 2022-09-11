from tkinter import *
import backend

window = Tk()
#add title
window.wm_title("Bookstore")

def convert():
    print('')


def get_selected_row(event):
    try:
        global selected_tuple
        #get the index of the selected row
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
    #print(index)
    #return selected_tuple
    #delete everything from entry
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])

        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])

        er1.delete(0,END)
        er1.insert(END, selected_tuple[3])

        er12.delete(0,END)
        er12.insert(END, selected_tuple[4])

    except IndexError:
        pass
    


def view_command():
    #make sure the list is empty
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)   #every new row is at the end

def search_command():
    #make sure the list is empty
    list1.delete(0, END)
    for row in backend.search(title_value.get(), author_value.get(),year_value.get(),isbn_value.get() ):
        list1.insert(END, row)

def add_command():
    #empty the box
    list1.delete(0, END)
    #insert in the database
    backend.insert(title_value.get(), author_value.get(),year_value.get(),isbn_value.get() )
    list1.insert(END, (title_value.get(), author_value.get(),year_value.get(),isbn_value.get() ) )
    
def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_value.get(), author_value.get(),year_value.get(),isbn_value.get() )
    
    #print(selected_tuple[0], selected_tuple[1],selected_tuple[2],selected_tuple[3] ,selected_tuple[4])



l0 =Label(window , text= "Title" ,height =1, width= 10)
l0.grid(row=0, column = 0) 

title_value=StringVar()
e1 =Entry(window , textvariable= title_value)
e1.grid(row=0, column = 1)   

l1 =Label(window , text= "Author" ,height =1, width= 10)
l1.grid(row=0, column = 2)

author_value=StringVar()
e2 =Entry(window , textvariable= author_value)
e2.grid(row=0, column = 3)  

lr1 =Label(window , text= "Year" ,height =1, width= 10)
lr1.grid(row=1, column = 0) 

year_value=StringVar()
er1 =Entry(window , textvariable= year_value)
er1.grid(row=1, column = 1)   

lr12 =Label(window , text= "Isbn" ,height =1, width= 10)
lr12.grid(row=1, column = 2)

isbn_value=StringVar()
er12 =Entry(window , textvariable= isbn_value)
er12.grid(row=1, column = 3)  


list1 = Listbox(window, height = 6 , width = 32)
list1.grid(row =2 , column = 0, rowspan = 6 ,columnspan = 2)

#create scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2 , rowspan = 6 )
#add to list
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

# eventtype  and function as args
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all" , command = view_command , width = 12 )
b1.grid(row=2, column = 3 )

b2 = Button(window, text="Search entry" , command = search_command , width = 12 )
b2.grid(row=3, column = 3)

b3 = Button(window, text="Add entry" , command = add_command , width = 12)
b3.grid(row=4, column = 3)

b4 = Button(window, text="Update" , command = update_command , width = 12 )
b4.grid(row=5, column = 3)

b5 = Button(window, text="Delete" , command = delete_command , width = 12)
b5.grid(row=6, column = 3)

b6 = Button(window, text="Close" , command = window.destroy , width = 12)
b6.grid(row=7, column = 3)


# t1 =Text(window , height =1, width= 10)
# t1.grid(row=1, column = 0)







window.mainloop()