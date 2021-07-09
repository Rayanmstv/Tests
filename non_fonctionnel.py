
from tkinter import *

violet = "#260451"
violet_f = "#14022B"
grey = '#b5b5b5'

def open_add_window():

    right_frame = Tk()

    def submit_new():
        eval_comp = eval_comp_button_variable.get()
        print(eval_comp)

    def clear_eval_comp():
        eval_comp_button_variable.set(3)
        
    eval_comp_frame = LabelFrame(right_frame, bg=violet, bd = 0)
    eval_comp_frame.pack(expand=YES, anchor=W)

    eval_comp_text = Label(eval_comp_frame, text="Évaluation Comportementale:", fg ='white', bg=violet)
    eval_comp_text.grid(row=0, column=0, sticky=W)

    eval_comp_buttons = Frame(eval_comp_frame, bg= violet)
    eval_comp_buttons.grid(row=0, column=1, sticky=W)
    
    eval_comp_button_variable = IntVar(master=right_frame)
    eval_comp_button_variable.set(3)

    yes_eval_comp_button = Radiobutton(eval_comp_buttons, text='oui', bg=violet, fg='#FFFFFF',selectcolor=violet,variable=eval_comp_button_variable,value=1, activebackground= violet, activeforeground='white')
    yes_eval_comp_button.pack(anchor=W)

    no_eval_comp_button = Radiobutton(eval_comp_buttons, text='non', bg=violet, fg='#FFFFFF',selectcolor=violet,variable=eval_comp_button_variable,value=2, activebackground= violet, activeforeground='white')
    no_eval_comp_button.pack(anchor=W)

    clear_button = Button(eval_comp_buttons, text='supprimer selection', bg=violet, fg='#FFFFFF', command=clear_eval_comp)
    clear_button.pack()

    Button(right_frame, text='ajouter', command=submit_new ).pack()



home_window = Tk()



choice_frame = Frame(home_window, bg = violet)
choice_frame.pack()

add_button = Button(choice_frame, text="Ajouter un commercial", font=("Helvetica", 40), bg="white", fg=violet, command=open_add_window)
add_button.pack()

home_window.mainloop()

