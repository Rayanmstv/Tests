import mysql.connector as sql

from tkinter import *
from tkcalendar import Calendar, DateEntry

cnx = sql.connect(host='localhost', user='root', database='referentiel_commerciaux', password='mdpmdpmdp')

violet = "#260451"
violet_f = "#14022B"
grey = '#b5b5b5'

fonction_liste=['SDR', 'Business Developer', 'Sales Managger', 'Account Manager', 'Autre']
annees_exp_liste=['0-2', '3-5', '6-10', '11-15', '16+']
marche_liste=['Banque','Energie','Retail','Assurance','Marchés Publiques']
entry_list=['nom','prenom','tel_1','tel_2','adresse','linkedin','cv','commentaire']

nb_px_decallage = 20


home_window = Tk()
home_window.title("Gestionnaire Base de données commerciaux Sigma Up") #C hoisir le nom de la fenêtre
home_window.config(background=violet) # Fond
width = home_window.winfo_screenwidth()
height = home_window.winfo_screenheight()
home_window.geometry( "%dx%d+0+0" % ( width, height ) )

def open_add_window():
    add_window = Tk()
    add_window.title("Ajout de commerciaux")
    add_window.config(background=violet)
    add_window.geometry( "%dx%d+0+0" % ( width, height ) )

    def submit_new():
        for e in entry_list:
            entry = e+'_entry'
            e = entry.get()
            print('%s:' + e % e)
        eval_comp = eval_comp_button_variable.get()
        print('evaluation comportementale: '+eval_comp)


    main_frame = Frame (add_window, bg=violet)
    main_frame.pack()

    title = Label (main_frame, text="AJOUTER UN COMMERCIAL", font=("Helvetica", 40), bg=violet, fg='white',)
    title.pack()

    middle_frame = Frame(main_frame, bg = violet)
    middle_frame.pack()
    left_frame = Frame (middle_frame, bg=violet)
    left_frame.grid(row=0, column=0, sticky=W)
    right_frame = Frame(middle_frame, bg=violet)
    right_frame.grid(row=0, column=2, sticky=W)
    middle_space = Frame (middle_frame, width= 150, bg = violet)
    middle_space.grid(row=0, column=1, sticky=W)
    
    nom_frame = LabelFrame(left_frame, bg=violet, text='Nom: *', fg ='white', bd = 2)
    nom_frame.pack(pady=nb_px_decallage)
    nom_variable = StringVar()
    nom_entry = Entry(nom_frame, bd=5, width=50, textvariable= nom_variable)
    nom_entry.pack()

    prenom_frame = LabelFrame(left_frame, bg=violet, text='Prénom: *', fg ='white', bd = 2)
    prenom_frame.pack(pady=nb_px_decallage)
    prenom_variable = StringVar()
    prenom_entry = Entry(prenom_frame, bd=5, width=50, textvariable= prenom_variable)
    prenom_entry.pack()

    tel_1_frame = LabelFrame(left_frame, bg=violet, text='Téléphone 1: *', fg ='white', bd = 2)
    tel_1_frame.pack(pady=nb_px_decallage)
    tel_1_variable = StringVar()
    tel_1_entry = Entry(tel_1_frame, bd=5, width=50, textvariable= tel_1_variable)
    tel_1_entry.pack()

    tel_2_frame = LabelFrame(left_frame, bg=violet, text='Téléphone 2:', fg ='white', bd=0)
    tel_2_frame.pack(pady=nb_px_decallage)
    tel_2_variable = StringVar()
    tel_2_entry = Entry(tel_2_frame, bd=5, width=50, bg=grey, textvariable= tel_2_variable)
    tel_2_entry.pack()

    adresse_frame = LabelFrame(left_frame, bg=violet, text='Adresse:', fg ='white', bd = 0)
    adresse_frame.pack(pady=nb_px_decallage)
    adresse_variable = StringVar()
    adresse_entry = Entry(adresse_frame, bd=5, width=50, bg= grey, textvariable= adresse_variable)
    adresse_entry.pack()

    linkedin_frame = LabelFrame(left_frame, bg=violet, text='LinkedIn:', fg ='white', bd = 0)
    linkedin_frame.pack(pady=nb_px_decallage)
    linkedin_variable = StringVar()
    linkedin_entry = Entry(linkedin_frame, bd=5, width=50, bg= grey, textvariable= linkedin_variable)
    linkedin_entry.pack()

    fonction_frame = LabelFrame(left_frame, bg=violet, bd = 0)
    fonction_frame.pack(expand=YES, anchor=W)
    fonction_text = Label(fonction_frame, text="Fonction:", fg ='white', bg=violet)
    fonction_text.grid(row=0, column=0, sticky=W)
    fonction_buttons = Frame(fonction_frame, bg= violet)
    fonction_buttons.grid(row=0, column=1, sticky=W)
    fonction_button_variable = IntVar()
    i=1
    for f in fonction_liste:
        a = Radiobutton(fonction_buttons, text=f, bg=violet, fg='#FFFFFF',selectcolor=violet, variable=fonction_button_variable, value = i, activebackground= violet, activeforeground='white')
        a.pack(anchor=W)
        a.select()
        i+=1

    



    conaissance_it_frame = LabelFrame(left_frame, bg=violet, bd = 0)
    conaissance_it_frame.pack(expand=YES, anchor=W, pady=10)
    conaissance_it_text = Label(conaissance_it_frame, text="conaissances en informatique:", fg ='white', bg=violet)
    conaissance_it_text.grid(row=0, column=0, sticky=W)
    conaissance_it_buttons = Frame(conaissance_it_frame, bg= violet)
    conaissance_it_buttons.grid(row=0, column=1, sticky=W)
    yes_connaissance_it_button_variable = IntVar()
    yes_connaissance_it_button = Checkbutton(conaissance_it_buttons, text='Oui', bg=violet, fg='#FFFFFF',selectcolor=violet, variable = yes_connaissance_it_button_variable, activebackground= violet, activeforeground='white')
    yes_connaissance_it_button.pack(anchor=W)
    no_connaissance_it_button_variable = IntVar()
    no_connaissance_it_button = Checkbutton(conaissance_it_buttons, text='Non', bg=violet, fg='#FFFFFF',selectcolor=violet, variable = no_connaissance_it_button_variable, activebackground= violet, activeforeground='white')
    no_connaissance_it_button.pack(anchor=W)


    date_rdv_frame = LabelFrame(right_frame, bg=violet, text='Date de Rendez-Vous: *', fg ='white', bd = 2)
    date_rdv_frame.pack(pady=nb_px_decallage)
    date_rdv_variable = StringVar()
    date_rdv_entry = DateEntry(date_rdv_frame, font=("Helvetica", 10), width= 42, background=violet_f, Variable=date_rdv_variable)
    date_rdv_entry.pack()

    date_dispo_frame = LabelFrame(right_frame, bg=violet, text='Date de Disponibilité: *', fg ='white', bd = 2)
    date_dispo_frame.pack(pady=nb_px_decallage)
    date_dispo_variable = StringVar()
    date_dispo_entry = DateEntry(date_dispo_frame, font=("Helvetica", 10), width= 42, background=violet_f, variable= date_dispo_variable)
    date_dispo_entry.pack()

    cv_frame = LabelFrame(right_frame, bg=violet, text='Chemin CV: *', fg ='white', bd = 2)
    cv_frame.pack(pady=nb_px_decallage)
    cv_variable = StringVar()
    cv_entry = Entry(cv_frame, bd=5, width=50, textvariable=cv_variable)
    cv_entry.pack()

    annees_exp_frame = LabelFrame(right_frame, bg=violet, bd = 0)
    annees_exp_frame.pack(anchor=W)
    annees_exp_text = Label(annees_exp_frame, text="Années d'expérience:", fg ='white', bg=violet)
    annees_exp_text.grid(row=0, column=0, sticky=W)
    annees_exp_buttons = Frame(annees_exp_frame, bg= violet)
    annees_exp_buttons.grid(row=0, column=1, sticky=W)
    annees_exp_button_variable= IntVar()
    ii=1
    for f in annees_exp_liste:
        a = Radiobutton(annees_exp_buttons, text=f, bg=violet, fg='#FFFFFF',selectcolor=violet, variable = annees_exp_button_variable, value = ii, activebackground= violet, activeforeground='white')
        a.pack(anchor=W)
        a.select()
        a = f+'_button'   
        ii+=1


    marche_frame = LabelFrame(right_frame, bg=violet, bd = 0)
    marche_frame.pack(anchor=W)
    marche_text = Label(marche_frame, text="Marché", fg ='white', bg=violet)
    marche_text.grid(row=0, column=0, sticky=W)
    marche_buttons = Frame(marche_frame, bg= violet)
    marche_buttons.grid(row=0, column=1, sticky=W)
    buttons = {}
    for f in marche_liste:

        buttons[f+'_button'] = Checkbutton(marche_buttons, text=f, bg=violet, fg='#FFFFFF',selectcolor=violet, activebackground= violet, activeforeground='white')
        buttons[f+'_button'].pack(anchor=W)

    eval_comp_frame = LabelFrame(right_frame, bg=violet, bd = 0)
    eval_comp_frame.pack(expand=YES, anchor=W)
    eval_comp_text = Label(eval_comp_frame, text="Évaluation Comportementale:", fg ='white', bg=violet)
    eval_comp_text.grid(row=0, column=0, sticky=W)
    eval_comp_buttons = Frame(eval_comp_frame, bg= violet)
    eval_comp_buttons.grid(row=0, column=1, sticky=W)


    eval_comp_button_variable = StringVar(master=add_window)
    eval_comp_button_variable.set('non')


    yes_eval_comp_button = Radiobutton(eval_comp_buttons, text='Oui', bg=violet, fg='#FFFFFF',selectcolor=violet, value = 'oui', variable=eval_comp_button_variable, activebackground= violet, activeforeground='white')
    yes_eval_comp_button.pack(anchor=W)
    no_eval_comp_button = Radiobutton(eval_comp_buttons, text='Non', bg=violet, fg='#FFFFFF',selectcolor=violet, value = 'non',variable=eval_comp_button_variable, activebackground= violet, activeforeground='white')
    no_eval_comp_button.pack(anchor=W)
    



    commentaire_frame = LabelFrame(right_frame, bg=violet, text='Commentaires:', fg ='white', bd = 0)
    commentaire_frame.pack(pady=nb_px_decallage)
    commentaire_variable = StringVar()
    commentaire_entry = Entry(commentaire_frame, bd=5, width=50, bg= grey, textvariable= commentaire_variable)
    commentaire_entry.pack()







    submit_button = Button(main_frame, text="Ajouter", font=("Helvetica", 40), bg="white", fg=violet, command=submit_new)
    submit_button.pack()

    add_window.mainloop()


    

def open_modify_window():
    modify_window = Tk()
    modify_window.title("Modification") 
    modify_window.config(background=violet) 
    modify_window.geometry( "%dx%d+0+0" % ( width, height ) )

def open_search_window():
    search_window = Tk()
    search_window.title("Recherche")
    search_window.config(background=violet)
    search_window.geometry( "%dx%d+0+0" % ( width, height ) )

choice_frame = Frame(home_window, bg = violet)

add_button = Button(choice_frame, text="Ajouter un commercial", font=("Helvetica", 40), bg="white", fg=violet, command=open_add_window)
add_button.pack()

modify_button = Button(choice_frame, text="Modifier un commercial", font=("Helvetica", 40), bg="white", fg=violet, command= open_modify_window)
modify_button.pack()

search_button = Button(choice_frame, text="Rechercher", font=("Helvetica", 40), bg="white", fg=violet, command=open_search_window)
search_button.pack()

choice_frame.pack(expand=YES)

home_window.mainloop()
cnx.close()

# supprimer tout: SET SQL_SAFE_UPDATES = 0; DELETE FROM commerciaux;

