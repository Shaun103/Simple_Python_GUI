import tkinter as tk

class BankAccount:
    def __init__(self, first_name='xxxxxx', last_name='xxxxxx', type='xxxxxx', number=0, interestRate=0):
        self.accFirstName = first_name
        self.accLastName = last_name
        self.accType = type
        self.accNumber = number
        self.accInterestRate = interestRate

# creating instances of the class
a = BankAccount() 

def set_variables():

    first = a.accFirstName.get()
    last = a.accLastName.get()
    type = a.accType.get()
    number = a.accNumber.get()
    interestRate = a.accInterestRate.get()
    
    # checking variables 
    print("First name: ", first)
    print("Last name: ", last)
    print("Account type: ", type)
    print("Account number: ", number)
    print("Account interest rate: ", interestRate)
    return (
        first, last, type, number, interestRate
    )

def main() -> None:



    mainWindow = tk.Tk()
    mainWindow.geometry("600x400")

    # class variables that tkinter with manipulate 
    a.accFirstName=tk.StringVar() # string
    a.accLastName=tk.StringVar()
    a.accType=tk.StringVar()
    a.accNumber=tk.IntVar() # integers
    a.accInterestRate=tk.DoubleVar() # double

    # assigning what is in labels and fields
    first_name_label = tk.Label(mainWindow, text='First name', font=('Times New Roman',10, 'bold'))
    first_name_entry = tk.Entry(mainWindow, textvariable = a.accFirstName, font=('Times New Roman',10,'normal'))

    last_name_label = tk.Label(mainWindow, text='Last name', font=('Times New Roman',10, 'bold'))
    last_entry = tk.Entry(mainWindow, textvariable = a.accLastName, font=('Times New Roman',10,'normal'))

    type_label = tk.Label(mainWindow, text='Account Type', font=('Times New Roman',10, 'bold'))
    type_entry = tk.Entry(mainWindow, textvariable = a.accType, font=('Times New Roman',10,'normal'))

    number_label = tk.Label(mainWindow, text='Account number', font=('Times New Roman',10, 'bold'))
    number_entry = tk.Entry(mainWindow, textvariable = a.accNumber, font=('Times New Roman',10,'normal'))

    interest_label = tk.Label(mainWindow, text='Interest rate', font=('Times New Roman',10, 'bold'))
    interest_entry = tk.Entry(mainWindow, textvariable = a.accInterestRate, font=('Times New Roman',10,'normal'))

    sub_btn=tk.Button(mainWindow,text='Show', command=set_variables) # when button clicked

    # displaying fields labels
    first_name_label.grid(row=0,column=0)
    first_name_entry.grid(row=0,column=1)

    last_name_label.grid(row=1,column=0)
    last_entry.grid(row=1,column=1)

    type_label.grid(row=2,column=0)
    type_entry.grid(row=2,column=1)

    number_label.grid(row=3,column=0)
    number_entry.grid(row=3,column=1)

    interest_label.grid(row=4,column=0)
    interest_entry.grid(row=4,column=1)
    
    sub_btn.grid(row=5,column=1)

    tk.mainloop()

if __name__ == "__main__":
    main()