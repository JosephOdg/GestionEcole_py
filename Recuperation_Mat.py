from tkinter import *
from customtkinter import *
import customtkinter as ctk
import mysql.connector
import re
from tkinter import ttk, messagebox
#import page_note
#import importlib

"""modulename = input('page_note:')
importlib.import_module(modulename)"""




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

win = ctk.CTk()
win.title("CONNEXION")
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}+0+0")

inscription = ctk.CTk()
inscription.geometry("1000x850")
frame = ctk.CTkFrame(master=inscription)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#--------------------#Fonctions inscription

def inscription_Profil():
    cleanframe()
    def connexion(email, password, confirm_password):
        if not email or not password or not confirm_password:
            messagebox.showerror("e","Remplir tous les champs")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Adresse mail non valide")
            return
        if(password != confirm_password):
            messagebox.showerror("e","Saisir des password conforme")
            return

        # Enregistrement Database
        User(email, password, confirm_password)

    def User(email, password, confirm_password):
        try:
            # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()

            # Module insertion
            curseur.execute("INSERT INTO compte (email, password, confirm_password) VALUES (%s, %s, %s)",
                            (email, password, confirm_password))
            mabd.commit()

            messagebox.showinfo("Success","Success User Enter")
            
        except mysql.connector.Error as err:
            messagebox.showerror("er",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    """ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    win = ctk.CTk()
    win.title("CONNEXION")
    win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}+0+0")
    inscription = ctk.CTk()
    inscription.geometry("1000x850")
    frame = ctk.CTkFrame(master=inscription)
    frame.pack(pady=20, padx=60, fill="both", expand=True)"""

    label = CTkLabel(master=frame, text="Inscription")
    label.pack(padx=50, pady=100)

    champ_email = CTkEntry(master=frame, placeholder_text="email@gmail.com")
    champ_email.pack(padx=100, pady=20)

    champ_password = CTkEntry(master=frame, placeholder_text="Enter password", show="*")
    champ_password.pack(padx=105, pady=20)

    champ_confirm_password = CTkEntry(master=frame, placeholder_text="Confirm password", show="*")
    champ_confirm_password.pack(padx=105, pady=20)

    button_connexion = CTkButton(master=frame, text="S'inscrire", command=lambda: connexion(champ_email.get(), champ_password.get(), champ_confirm_password.get()))
    button_connexion.pack(padx=70, pady=25)

    def log():
        connexion_Profil()

    connexion_button = CTkButton(master=frame, text="Connect", command=log)
    connexion_button.pack(padx=130, pady=25)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

#---------------------FIN fonctions Inscriiption
##############################################################################""

#--------Fonctions Login 

def connexion_Profil():
    cleanframe()
    def connexion(email, password):
        if not email or not password:
            messagebox.showerror("Error","Remplir tous les champs")
            return
        # Enregistrement Database
        User(email, password)

    def User(email, password):
        try:
            # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            #print(f"{email}, {password}")
            # Module insertion
            curseur.execute("SELECT * FROM compte WHERE email = %s AND password = %s", (email, password)) 
     
            donnees = curseur.fetchall()
            mabd.commit()
            print(donnees)
            messagebox.showinfo("Success","Success User Enter")
            
        except mysql.connector.Error as err:
            messagebox.showerror("Error",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()


    label =ctk.CTkLabel(master=frame, text="Se connecter")
    label.pack(pady=12, padx=10)

    email=ctk.CTkEntry (master=frame, placeholder_text="email@gmail.com")
    email.pack(pady=12)

    password=ctk.CTkEntry (master=frame, placeholder_text="password", show="*")
    password.pack(pady=12)


    button=ctk.CTkButton(master=frame, text="Connexion", command=lambda: connexion(email.get(), password.get()))
    button.pack(pady=12, padx=10)

    checkbox=ctk.CTkCheckBox(master=frame, text="Se souvenir de moi")
    checkbox.pack(pady=12, padx=18)

    def win_insc():
        inscription_Profil()

    button1=ctk.CTkButton(master=frame, text="creer un compte", command=win_insc)
    button1.pack(pady=12, padx=20)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

#--------Fin fonctions Login

####################################################################################

#---------------------------######Note fonctions 

def Modify_note(id_matiere):
    cleanframe()

    def connexion(N_mat, Nom_etud, Prenom_etud, first_note, second_note, note_pond, moyenne):
        if not N_mat or not Nom_etud or not Prenom_etud or not first_note or  not second_note or not note_pond or not moyenne:
            messagebox.showerror("er","Remplir tous les champs")
            return
        try:
            # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{N_mat}, {Nom_etud}, {Prenom_etud}, {first_note}, {second_note}, {note_pond}, {moyenne}")
            # Module insertion
            curseur.execute("UPDATE notes SET N_mat=%s, Nom_etud=%s, Prenom_etud=%s, first_note=%s, second_note=%s, note_pond=%s, moyenne=%s WHERE id_matiere=" + str(id_matiere),
                            (N_mat, Nom_etud, Prenom_etud, first_note, second_note, note_pond, moyenne))
            mabd.commit()

            cleanframe()
            callDisplayNot(id_matiere)
            
        except mysql.connector.Error as err:
            messagebox.showerror("Error",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM notes WHERE id_matiere=" + str(id_matiere))
    x = curseur.fetchone()

    label = CTkLabel(master=frame, text="MODIFICATION DE NOTE", font=("algerian",20,"bold"))
    label.pack(padx=50, pady=20)

    champ_no = CTkEntry(master=frame, placeholder_text="N_mat")
    champ_no.pack(padx=100, pady=20)
    champ_no.insert(0,x[1])

    champ_etud = CTkEntry(master=frame, placeholder_text="Nom_etud")
    champ_etud.pack(padx=105, pady=20)
    champ_etud.insert(0,x[2])

    champ_et = CTkEntry(master=frame, placeholder_text="Prenom_etud")
    champ_et.pack(padx=105, pady=20)
    champ_et.insert(0,x[3])

    F_not = CTkEntry(master=frame, placeholder_text= "first_note")
    F_not.pack(padx=105, pady=20)
    F_not.insert(0,x[4])

    S_not = CTkEntry(master=frame, placeholder_text= "second_note")
    S_not.pack(padx=105, pady=20)
    S_not.insert(0,x[5])

    pondere = CTkEntry(master=frame, placeholder_text= "note_pond")
    pondere.pack(padx=105, pady=20)
    pondere.insert(0,x[6])

    moy= CTkEntry(master=frame, placeholder_text= "moyenne")
    moy.pack(padx=105, pady=20)
    moy.insert(0,x[7])

    button_connexion = CTkButton(master=frame, text="SAVE", command=lambda: connexion(champ_no.get(), champ_etud.get(), champ_et.get(), F_not.get(), S_not.get(), pondere.get(), moy.get()))
    button_connexion.pack(padx=130, pady=20)

def callDisplayNot(id_matiere):
    cleanframe()
     
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM notes WHERE id_matiere=" + str(id_matiere))
            
    x = curseur.fetchone()
    i=0
    label = CTkLabel(master=frame, text="Nom matiere: " + str(x[1]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Nom etudiant: " + str(x[2]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="prenom etudiant: "+ str(x[3]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="1ere Note: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="2e Note: "+ str(x[5]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Note Pondere: "+ str(x[6]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Moyenne: "+ str(x[7]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    #mabd.commit()
    #messagebox.showerror("Success User Enter")


    """for i in range(3):
        label = CTkLabel(master=frame, text="Nom matiere:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""
    """label = CTkLabel(master=frame, text="Nom matiere: " + str(x[1]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient: " + str(x[2]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire: "+ str(x[3]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""

    #Label(root, ="REGISTRE ENSEIGNANTS", width=10, height=2, bg="dark blue",fg="#fff",font="arial 20 bold")
    def retour():
        cleanframe()
        list_notes()

    def Sup():
        mabd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school"
            )
        curseur = mabd.cursor()
        mabd.commit()
        curseur.execute("DELETE FROM notes WHERE id_matiere = " + str(id_matiere))
        cleanframe()
        list_notes()
        callDisplayNot(id_matiere)
   
    i += 1

    label = CTkLabel(master=frame, text="Affichage informations Notes", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    button=ctk.CTkButton(master=frame, text="BACK", command= retour)
    button.place(x=20,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Modifier", command=lambda:Modify_note(id_matiere))
    button.place(x=320,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Supprimer", command= Sup)
    button.place(x=520,y=150 + i*50)
 
def ADD_Note():
    cleanframe()
    def connexion(N_mat, Nom_etud, Prenom_etud, first_note, second_note, note_pond, moyenne):
        if not N_mat or not Nom_etud or not Prenom_etud or not first_note or  not second_note or not note_pond or not moyenne:
            messagebox.showerror("er","Remplir tous les champs")
            return
        try:
                # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{N_mat}, {Nom_etud}, {Prenom_etud}, {first_note}, {second_note}, {note_pond}, {moyenne}")
            # Module insertion
            curseur.execute(" INSERT INTO notes (N_mat, Nom_etud, Prenom_etud, first_note, second_note, note_pond, moyenne) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (N_mat, Nom_etud, Prenom_etud, first_note, second_note, note_pond, moyenne))                            
            mabd.commit()

            cleanframe()
            list_notes()
                
        except mysql.connector.Error as err:
            messagebox.showerror("err",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    label = CTkLabel(master=frame, text="Ajouter les Notes de L'Etudiant Ici", font=("algerian", 20, "bold"))
    label.pack(padx=50, pady=20)

    champ_no = CTkEntry(master=frame, placeholder_text="N_mat")
    champ_no.pack(padx=100, pady=20)

    champ_etud = CTkEntry(master=frame, placeholder_text="Nom_etud")
    champ_etud.pack(padx=105, pady=20)

    champ_et = CTkEntry(master=frame, placeholder_text="Prenom_etud")
    champ_et.pack(padx=105, pady=20)

    F_not = CTkEntry(master=frame, placeholder_text= "first_note")
    F_not.pack(padx=105, pady=20)

    S_not = CTkEntry(master=frame, placeholder_text= "Second_Note")
    S_not.pack(padx=105, pady=20)

    pondere = CTkEntry(master=frame, placeholder_text= "Pondere")
    pondere.pack(padx=105, pady=20)

    moy = CTkEntry(master=frame, placeholder_text= "Moyenne")
    moy.pack(padx=105, pady=20)

        
    button_connexion = CTkButton(master=frame, text="SAVE", command= lambda: connexion(champ_no.get(), champ_etud.get(), champ_et.get(), F_not.get(), S_not.get(), pondere.get(), moy.get()))
    button_connexion.pack(padx=120, pady=20)
        
def list_notes():
    cleanframe()
    label = CTkLabel(master=frame, text="INCRISPTION NOTES", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    #N_mat, Nom_etud, Prenom_etud, first_note, second_note, note_pond, moyenne

    def displayNotes(x,i):
        button=ctk.CTkButton(master=frame, text="Nom matiere: " + str(x[1]) + "   -   Nom etudiant: " + str(x[2]) +"   -   Prenom etudiant: "+ str(x[3]) + "   -   1ere Note: "+ str(x[4]) + "   - 2e Note: "+ str(x[5]) + "   -  Note pondere: "+ str(x[6]) + "   -   Moyenne: "+ str(x[7]), command=lambda: callDisplayNot(x[0]))
        button.place(y=220 + i*50, x=20)

    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM notes")
            
    don = curseur.fetchall()
    i = 0
    for x in don:
        print(x)
        displayNotes(x,i)
        i +=1
    mabd.commit()
    #messagebox.showerror("Success User Enter")
            
    label = ctk.CTkLabel(master=frame, text="LISTE DE NOTES",font=("algerian",30,"bold"),
        text_color="dark blue",bg_color="lightgray",width=win.winfo_screenwidth(),height=100)
    label.place(x=0,y=0)
    button_connexion = CTkButton(master=frame, text="Ajouter", command=ADD_Note)
    button_connexion.place(x=500, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)


    """#barre de defilement
    scroll = ttk.Scrollbar(inscription, orient="vertical", command= inscription.yview)
    inscription.configure(yscrollcommand= scroll.set)
    scroll.pack(side="right", fill="y")"""

    """for i in range(3):
        label = CTkLabel(master=frame, text="Nom matiere:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""

    #Label(root, ="REGISTRE ENSEIGNANTS", width=10, height=2, bg="dark blue",fg="#fff",font="arial 20 bold")

    #button=ctk.CTkButton(master=frame, text="Connexion")
    #button.pack(pady=12, padx=10)

    inscription.mainloop()
    #win.mainloop()

#--------------------FIN fonctions notes


#Matiere fonctions 

def cleanframe():
    for i in frame.winfo_children():
        i.destroy()

def Modify_mat(id_mat):
    cleanframe()
    def connexion(Nom_mat, Coefficient, Vol_horaire, Semestre):
        if not Coefficient or not Vol_horaire or not Semestre or not Nom_mat:
            messagebox.showerror("Remplir tous les champs")
            return

        try:
            # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{Nom_mat}, {Coefficient}, {Vol_horaire}, {Semestre}")
            # Module insertion
            curseur.execute("UPDATE matiere SET Nom_mat=%s, Coefficient=%s, Vol_horaire=%s, Semestre=%s WHERE id_mat="+str(id_mat),
                            (Nom_mat, Coefficient, Vol_horaire, Semestre))
            mabd.commit()

            cleanframe()
            callDisplayMat(id_mat)
            
        except mysql.connector.Error as err:
            messagebox.showerror(f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM matiere WHERE id_mat="+str(id_mat))
    x = curseur.fetchone()

    label = CTkLabel(master=frame, text="MODIFICATION D'UNE MATIERE")
    label.pack(padx=50, pady=20)

    champ_mat = CTkEntry(master=frame, placeholder_text="New_Nom_mat")
    champ_mat.pack(padx=100, pady=20)
    champ_mat.insert(0,x[1])

    champ_coe = CTkEntry(master=frame, placeholder_text="New_Coefficient")
    champ_coe.pack(padx=105, pady=20)
    champ_coe.insert(0,x[2])

    champ_vol = CTkEntry(master=frame, placeholder_text="New_Vol_horaire")
    champ_vol.pack(padx=105, pady=20)
    champ_vol.insert(0,x[3])

    semestre = CTkEntry(master=frame, placeholder_text= "New_semestre")
    semestre.pack(padx=105, pady=20)
    semestre.insert(0,x[4])

    button_connexion = CTkButton(master=frame, text="Save", command=lambda: connexion(champ_mat.get(), champ_coe.get(), champ_vol.get(), semestre.get()))
    button_connexion.pack(padx=130, pady=25)

def callDisplayMat(id_mat):
    cleanframe()
     
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM matiere WHERE id_mat="+str(id_mat))
            
    x = curseur.fetchone()
    i=0
    label = CTkLabel(master=frame, text="Nom matiere: " + str(x[1]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Coefficient: " + str(x[2]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Volume horaire: "+ str(x[3]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Semestre: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    #mabd.commit()
    #messagebox.showerror("Success User Enter")


    """for i in range(3):
        label = CTkLabel(master=frame, text="Nom matiere:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""
    """label = CTkLabel(master=frame, text="Nom matiere: " + str(x[1]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient: " + str(x[2]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire: "+ str(x[3]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""

    #Label(root, ="REGISTRE ENSEIGNANTS", width=10, height=2, bg="dark blue",fg="#fff",font="arial 20 bold")
    def retour():
        cleanframe()
        list_matiere()

    def Sup():
        mabd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school"
            )
        curseur = mabd.cursor()
        mabd.commit()
        curseur.execute("DELETE FROM matiere WHERE id_mat = " + str(id_mat))
        cleanframe()
        list_matiere()
   
    i += 1

    label = CTkLabel(master=frame, text="Affichage informations Matiere", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    button=ctk.CTkButton(master=frame, text="BACK", command= retour)
    button.place(x=20,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Modifier", command=lambda:Modify_mat(id_mat))
    button.place(x=320,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Supprimer", command= Sup)
    button.place(x=520,y=150 + i*50)

def ADD_Mat():
    cleanframe()
    def connexion(Nom_mat, Coefficient, Vol_horaire, Semestre):
        if not Coefficient or not Vol_horaire or not Semestre or not Nom_mat:
            messagebox.showerror("Remplir tous les champs")
            return
        try:
        # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{Nom_mat}, {Coefficient}, {Vol_horaire}, {Semestre}")
            # Module insertion
            curseur.execute("INSERT INTO matiere (Nom_mat, Coefficient, Vol_horaire, Semestre) VALUES (%s, %s, %s, %s)",
                            (Nom_mat, Coefficient, Vol_horaire, Semestre))
            mabd.commit()

            cleanframe()
            list_matiere()

        except mysql.connector.Error as err:
            messagebox.showerror(f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    label = CTkLabel(master=frame, text="Inscription Matiere", font=("algerian", 20, "bold"))
    label.pack(padx=50, pady=20)

    champ_mat = CTkEntry(master=frame, placeholder_text="Nom_mat")
    champ_mat.pack(padx=100, pady=20)

    champ_coe = CTkEntry(master=frame, placeholder_text="Coefficient")
    champ_coe.pack(padx=105, pady=20)

    champ_vol = CTkEntry(master=frame, placeholder_text="Vol_horaire")
    champ_vol.pack(padx=105, pady=20)

    semestre = CTkEntry(master=frame, placeholder_text= "semestre")
    semestre.pack(padx=105, pady=20)

    button_connexion = CTkButton(master=frame, text="Ajouter", command=lambda: connexion(champ_mat.get(), champ_coe.get(),  champ_vol.get(), semestre.get()))
    button_connexion.pack(padx=130, pady=25)

    butbackmat = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    butbackmat.place(x=0, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)


def list_matiere():
    cleanframe()
    label = CTkLabel(master=frame, text="Inscription Matiere", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    def displayMatiere(x,i):
        button=ctk.CTkButton(master=frame, text="Nom matiere: " + str(x[1]) + "   -   Coefficient: " + str(x[2]) +"   -   Volume horaire: "+ str(x[3]) + "   -   Semestre: "+ str(x[4]), command=lambda: callDisplayMat(x[0]))
        button.place(y=220 + i*50, x=20)

    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM matiere")
            
    don = curseur.fetchall()
    i = 0
    for x in don:
        print(x)
        displayMatiere(x,i)
        i +=1
    mabd.commit()
    #messagebox.showerror("Success User Enter")
            
    label = ctk.CTkLabel(master=frame, text="LISTE DE MATIERE",font=("algerian",30,"bold"),
        text_color="dark blue",bg_color="lightgray",width=win.winfo_screenwidth(),height=100)
    label.place(x=0,y=0)
    button_connexion = CTkButton(master=frame, text="Ajouter", command=ADD_Mat)
    button_connexion.place(x=500, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

    """for i in range(3):
        label = CTkLabel(master=frame, text="Nom matiere:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""

    #Label(root, ="REGISTRE ENSEIGNANTS", width=10, height=2, bg="dark blue",fg="#fff",font="arial 20 bold")

    #button=ctk.CTkButton(master=frame, text="Connexion")
    #button.pack(pady=12, padx=10)

#--------------------FIN fonctions matieres

##################################################################################################################
#---------------Fonctions Enseignant


def Modify_ens(id_enseignant):
    cleanframe()

    def connexion(Nom, Prenom, Mat_Ens, Diplomes, Tel, Email_Ens, Filiere):
        if not Nom or not Prenom or not Mat_Ens or not Diplomes or not Tel or not Email_Ens or not Filiere:
            messagebox.showerror("Error","Remplir tous les champs")
            return

        try:
            # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{Nom}, {Prenom}, {Mat_Ens}, {Filiere}, {Diplomes}, {Tel}, {Email_Ens}")
            # Module insertion
            curseur.execute("UPDATE enseignant SET Nom=%s, Prenom=%s, Mat_Ens=%s, Diplomes=%s, Tel=%s, Email_Ens=%s, Filiere=%s WHERE id_enseignant="+str(id_enseignant),
                            (Nom, Prenom, Mat_Ens, Diplomes, Tel, Email_Ens, Filiere))
            mabd.commit()

            cleanframe()
            callDisplayEns(id_enseignant)
            
        except mysql.connector.Error as err:
            messagebox.showerror("Er",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM enseignant WHERE id_enseignant="+str(id_enseignant))
    x = curseur.fetchone()

    label = CTkLabel(master=frame, text="MODIFICATION LISTE ENSEIGNANTS", font=("algerian", 20, "bold"))
    label.pack(padx=50, pady=20)

    champ_N = CTkEntry(master=frame, placeholder_text="Nom")
    champ_N.pack(padx=100, pady=20)
    champ_N.insert(0,x[1])

    champ_P = CTkEntry(master=frame, placeholder_text="Prenom")
    champ_P.pack(padx=105, pady=20)
    champ_P.insert(0,x[2])

    champ_M = CTkEntry(master=frame, placeholder_text="Module")
    champ_M.pack(padx=105, pady=20)
    champ_M.insert(0,x[3])

    Dip = CTkEntry(master=frame, placeholder_text= "Diplome")
    Dip.pack(padx=105, pady=20)
    Dip.insert(0,x[4])

    tel = CTkEntry(master=frame, placeholder_text= "TELEPHONE")
    tel.pack(padx=105, pady=20)
    tel.insert(0,x[5])

    mail = CTkEntry(master=frame, placeholder_text= "Son Mail")
    mail.pack(padx=105, pady=20)
    mail.insert(0,x[6])

    fil = CTkEntry(master=frame, placeholder_text= "Filiere")
    fil.pack(padx=105, pady=20)
    fil.insert(0,x[7])

    button_connexion = CTkButton(master=frame, text="Save", command=lambda: connexion(champ_N.get(), champ_P.get(), champ_M.get(), Dip.get(), tel.get(), mail.get(), fil.get()))
    button_connexion.pack(padx=130, pady=25)

def callDisplayEns(id_enseignant):
    cleanframe()

    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM enseignant WHERE id_enseignant="+str(id_enseignant))
            
    x = curseur.fetchone()
    i=0
    label = CTkLabel(master=frame, text="Nom: " + str(x[1]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Prenom: " + str(x[2]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Module: "+ str(x[3]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Diplome: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="TELEPHONE: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Mail: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Filiere: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
   
    def retour():
        cleanframe()
        list_ens()

    def Sup():
        mabd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school"
            )
        curseur = mabd.cursor()
        mabd.commit()
        curseur.execute("DELETE FROM enseignant WHERE id_enseignant = " + str(id_enseignant))

        cleanframe()
        list_ens()
        callDisplayEns()
   
    i += 1

    label = CTkLabel(master=frame, text="Affichage informations enseignant", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    button=ctk.CTkButton(master=frame, text="BACK", command= retour)
    button.place(x=20,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Modifier", command=lambda:Modify_ens(id_enseignant))
    button.place(x=320,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Supprimer", command= Sup)
    button.place(x=520,y=150 + i*50)

def ADD_Ens():
    cleanframe()
    def connexion(Nom, Prenom, Mat_Ens, Diplomes, Tel, Email_Ens, Filiere):
        if not Nom or not Prenom or not Mat_Ens or not Diplomes or not Tel or not Email_Ens or not Filiere:
            messagebox.showerror("Err","Remplir tous les champs")
            return
        try:
        # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{Nom}, {Prenom}, {Mat_Ens}, {Diplomes}, {Tel}, {Email_Ens}, {Filiere}")
            # Module insertion
            curseur.execute("INSERT INTO enseignant (Nom, Prenom, Mat_Ens, Diplomes, Tel, Email_Ens, Filiere) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (Nom, Prenom, Mat_Ens, Diplomes, Tel, Email_Ens, Filiere))
            mabd.commit()

            cleanframe()
            list_ens()

        except mysql.connector.Error as err:
            messagebox.showerror("Er",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    label = CTkLabel(master=frame, text="Inscription Enseignant", font=("algerian", 20, "bold"))
    label.pack(padx=50, pady=20)

    champ_N = CTkEntry(master=frame, placeholder_text="Nom")
    champ_N.pack(padx=100, pady=20)

    champ_P = CTkEntry(master=frame, placeholder_text="Prenom")
    champ_P.pack(padx=105, pady=20)

    champ_M = CTkEntry(master=frame, placeholder_text="Module")
    champ_M.pack(padx=110, pady=20)

    Dip = CTkEntry(master=frame, placeholder_text= "Diplome")
    Dip.pack(padx=115, pady=20)

    tel = CTkEntry(master=frame, placeholder_text= "TELEPHONE")
    tel.pack(padx=120, pady=20)

    mail = CTkEntry(master=frame, placeholder_text= "Mail")
    mail.pack(padx=125, pady=20)

    fil = CTkEntry(master=frame, placeholder_text= "Filiere")
    fil.pack(padx=130, pady=20)



    button_connexion = CTkButton(master=frame, text="Ajouter", command=lambda: connexion(champ_N.get(), champ_P.get(),  champ_M.get(), Dip.get(), tel.get(), mail.get(), fil.get()))
    button_connexion.pack(padx=130, pady=25)

def list_ens():
    cleanframe()
    label = CTkLabel(master=frame, text="Inscription Enseignant", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    ###########################################################
    def displayEns(x,i):
        button=ctk.CTkButton(master=frame, text="Nom: " + str(x[1]) + "   -   Prenom: " + str(x[2]) +"   -   Mat_Ens: "+ str(x[3]) + "   -   Diplomes: "+ str(x[4]) + "   -   Tel: "+ str(x[5]) +  "  -  Email_Ens: "+ str(x[6]) + "  -  Filiere: " + str(x[4]), command=lambda: callDisplayEns(x[0]))
        button.place(y=220 + i*50, x=20)

    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM enseignant")
            
    don = curseur.fetchall()
    i = 0
    for x in don:
        print(x)
        displayEns(x,i)
        i +=1
    mabd.commit()
    #messagebox.showerror("Success User Enter")
            
    label = ctk.CTkLabel(master=frame, text="LISTE ENSEIGNANTS",font=("algerian",30,"bold"),
        text_color="dark blue",bg_color="lightgray",width=win.winfo_screenwidth(),height=100)
    label.place(x=0,y=0)
    button_connexion = CTkButton(master=frame, text="Ajouter", command= ADD_Ens)
    button_connexion.place(x=500, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

    
    #Label(root, ="REGISTRE ENSEIGNANTS", width=10, height=2, bg="dark blue",fg="#fff",font="arial 20 bold")

    #button=ctk.CTkButton(master=frame, text="Connexion")
    #button.pack(pady=12, padx=10)

    inscription.mainloop()
    #win.mainloop()


#----------Fin fonctions enseignant

###################################################################################################################

#----------fonctions etudiant

def Modify_Stu(id_student):
    cleanframe()

    def connexion(Nom, Prenom, Sexe, Date_naissance, Lieu_naissance, Filiere, L_etude, Contact, SC_tel):
        if not Nom or not Prenom or not Sexe or not Date_naissance or not Lieu_naissance or not  Filiere or not L_etude or not Contact or not SC_tel:
            messagebox.showerror("Error","Remplir tous les champs")
            return

        try:
            # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{Lieu_naissance}, {Sexe}, {Prenom}, {Nom},{Filiere},{Date_naissance},{L_etude}, {Contact}, {SC_tel}")
            # Module insertion
            curseur.execute("UPDATE cours SET Lieu_naissance=%s, Date_naissance=%s, Sexe=%s, Nom=%s, Prenom=%s, Filiere=%s, L_etude=%s, Contact=%s, SC_tel=%s WHERE id_student="+str(id_student),
                            (Nom, Prenom, Sexe, Date_naissance, Lieu_naissance, Filiere, L_etude, Contact, SC_tel))
            mabd.commit()

            cleanframe()
            callDisplayCo(id_cours)
            
        except mysql.connector.Error as err:
            messagebox.showerror("er",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM student WHERE id_student="+str(id_student))
    x = curseur.fetchone()

    label = CTkLabel(master=frame, text="MODIFICATION DU PROGRAMME D'UN COURS")
    label.pack(padx=50, pady=20)

    champ_nom = CTkEntry(master=frame, placeholder_text="Nom ")
    champ_nom.pack(padx=100, pady=20)
    champ_nom.insert(0,x[1])

    champ_p = CTkEntry(master=frame, placeholder_text="Prenom")
    champ_p.pack(padx=105, pady=20)
    champ_p.insert(0,x[2])

    champ_sex = CTkEntry(master=frame, placeholder_text="Sexe")
    champ_sex.pack(padx=105, pady=20)
    champ_sex.insert(0,x[3])

    birth = CTkEntry(master=frame, placeholder_text= "Date de naissance")
    birth.pack(padx=105, pady=20)
    birth.insert(0,x[4])

    local = CTkEntry(master=frame, placeholder_text= "Lieu de naissance")
    local.pack(padx=105, pady=20)
    local.insert(0,x[4])

    fil = CTkEntry(master=frame, placeholder_text= "Filiere")
    fil.pack(padx=105, pady=20)
    fil.insert(0,x[4])

    an = CTkEntry(master=frame, placeholder_text= "Niveau d'etude")
    an.pack(padx=105, pady=20)
    an.insert(0,x[4])

    tel = CTkEntry(master=frame, placeholder_text= "Telephone")
    tel.pack(padx=105, pady=20)
    tel.insert(0,x[4])

    Con = CTkEntry(master=frame, placeholder_text= "Personne à prevenir")
    Con.pack(padx=105, pady=20)
    Con.insert(0,x[4])

    button_connexion = CTkButton(master=frame, text="Save", command=lambda: connexion(champ_nom.get(), champ_p.get(),  champ_sex.get(), birth.get(), local.get(), fil.get(), an.get(), tel.get(), Con.get()))
    button_connexion.pack(padx=130, pady=25)

def callDisplayStu(id_student):
    cleanframe()
     
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM student WHERE id_student="+str(id_student))
            
    x = curseur.fetchone()
    i=0
    label = CTkLabel(master=frame, text="Nom: " + str(x[1]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    label.place(x=20,y=120 + i*20)
    label = CTkLabel(master=frame, text="Prenom: " + str(x[2]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=120 + i*20)
    label = CTkLabel(master=frame, text="Sexe: "+ str(x[3]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=120 + i*20)
    label = CTkLabel(master=frame, text="Date de naissance: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=120 + i*20)
    label = CTkLabel(master=frame, text="Lieu de naissance: "+ str(x[5]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=120 + i*20)
    label = CTkLabel(master=frame, text="Filiere: "+ str(x[6]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=120 + i*20)
    label = CTkLabel(master=frame, text="Niveau d'etude: "+ str(x[7]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=120 + i*20)
    label = CTkLabel(master=frame, text="Telephone: "+ str(x[8]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=120 + i*20)
    label = CTkLabel(master=frame, text="Personne à prevenir: "+ str(x[9]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=120 + i*20)

    #mabd.commit()
    #messagebox.showerror("Success User Enter")

    def retour():
        cleanframe()
        list_student()

    def Sup():
        mabd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school"
            )
        curseur = mabd.cursor()
        mabd.commit()
        curseur.execute("DELETE FROM student WHERE id_student = " + str(id_student))

        cleanframe()
        list_student()
        callDisplayStu()
   
    i += 1

    label = CTkLabel(master=frame, text="Affichage informations Cours", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    button=ctk.CTkButton(master=frame, text="BACK", command= retour)
    button.place(x=20,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Modifier", command=lambda:Modify_Stu(id_student))
    button.place(x=320,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Supprimer", command= Sup)
    button.place(x=520,y=150 + i*50)

def ADD_Stu():
    cleanframe()
    def connexion(Nom, Prenom, Sexe, Date_naissance, Lieu_naissance, Filiere, L_etude, Contact, SC_tel):
        if not Nom or not Prenom or not Sexe or not Date_naissance or not Lieu_naissance or not  Filiere or not L_etude or not Contact or not SC_tel:
            messagebox.showerror("Error","Remplir tous les champs")
            return
        try:
        # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{Lieu_naissance}, {Sexe}, {Prenom}, {Nom},{Filiere},{Date_naissance},{L_etude}, {Contact}, {SC_tel}")
            # Module insertion
            curseur.execute("INSERT INTO student (Nom, Prenom, Sexe, Date_naissance, Lieu_naissance, Filiere, L_etude, Contact, SC_tel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (Nom, Prenom, Sexe, Date_naissance, Lieu_naissance, Filiere, L_etude, Contact, SC_tel))
            mabd.commit()

            cleanframe()
            list_student()

        except mysql.connector.Error as err:
            messagebox.showerror("Error",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    label = CTkLabel(master=frame, text="Inscription Etudiant", font=("algerian", 20, "bold"))
    label.pack(padx=50, pady=20)

    champ_nom = CTkEntry(master=frame, placeholder_text="Nom ETUDIANT")
    champ_nom.pack(padx=100, pady=10)

    champ_p = CTkEntry(master=frame, placeholder_text="Prenom ETUDIANT")
    champ_p.pack(padx=105, pady=10)

    champ_sex = CTkEntry(master=frame, placeholder_text="Sexe")
    champ_sex.pack(padx=105, pady=10)

    birth = CTkEntry(master=frame, placeholder_text= "Date_naissance")
    birth.pack(padx=105, pady=10)

    local = CTkEntry(master=frame, placeholder_text= "Lieu_naissance")
    local.pack(padx=105, pady=10)

    fil = CTkEntry(master=frame, placeholder_text= "Filiere")
    fil.pack(padx=105, pady=10)

    an = CTkEntry(master=frame, placeholder_text= "Anne d'etude")
    an.pack(padx=105, pady=10)

    tel = CTkEntry(master=frame, placeholder_text= "Contact")
    tel.pack(padx=105, pady=10)

    Con = CTkEntry(master=frame, placeholder_text= "Personne à prevenir")
    Con.pack(padx=105, pady=10)

    button_connexion = CTkButton(master=frame, text="Ajouter", command=lambda: connexion(champ_nom.get(), champ_p.get(),  champ_sex.get(), birth.get(), local.get(), fil.get(), an.get(), tel.get(), Con.get()))
    button_connexion.pack(padx=130, pady=15)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

def list_student():
    cleanframe()
    label = CTkLabel(master=frame, text="Liste Student", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    def displayStu(x,i):
        button=ctk.CTkButton(master=frame, text="Nom: " + str(x[1]) + "   -   Prenom: " + str(x[2]) +"   -   Sexe: "+ str(x[3]) + "   -   Date_naissance: "+ str(x[4]) + "   -   Lieu_naissance: "+ str(x[5]) + "   -   Filiere: "+ str(x[6]) + "   -   L_etude: "+ str(x[7]) + "   -   Contact: "+ str(x[8]) + "   -   SC_tel: "+ str(x[4]), command=lambda: callDisplayStu(x[0]))
        button.place(y=220 + i*50, x=20)

    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM student")
            
    don = curseur.fetchall()
    i = 0
    for x in don:
        print(x)
        displayStu(x,i)
        i +=1
    mabd.commit()
    #messagebox.showerror("Success User Enter")
            
    label = ctk.CTkLabel(master=frame, text="LISTE DES ETUDIANTS",font=("algerian", 40,"bold"),
        text_color="dark blue",bg_color="lightgray",width=win.winfo_screenwidth(),height=100)
    label.place(x=0,y=0)
    button_connexion = CTkButton(master=frame, text="Ajouter", command=ADD_Stu)
    button_connexion.place(x=500, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

   
    inscription.mainloop()
    #win.mainloop()



#----------FIN fonctions etudiants
###################################################################################################################

#-------Fonctions cours 


def Modify_cours(id_cours):
    cleanframe()

    def connexion(N_Prof, Vol_hor, Sal_cours, Module):
        if not N_Prof or not Vol_hor or not Sal_cours or not Module:
            messagebox.showerror("Error","Remplir tous les champs")
            return

        try:
            # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{N_Prof}, {Vol_hor}, {Sal_cours}, {Module}")
            # Module insertion
            curseur.execute("UPDATE cours SET N_Prof=%s, Vol_hor=%s, Sal_cours=%s, Module=%s WHERE id_cours="+str(id_cours),
                            (N_Prof, Vol_hor, Sal_cours, Module))
            mabd.commit()

            cleanframe()
            callDisplayCo(id_cours)
            
        except mysql.connector.Error as err:
            messagebox.showerror("er",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM cours WHERE id_cours="+str(id_cours))
    x = curseur.fetchone()

    label = CTkLabel(master=frame, text="MODIFICATION DU PROGRAMME D'UN COURS")
    label.pack(padx=50, pady=20)

    champ_prof = CTkEntry(master=frame, placeholder_text="Nom Professeur")
    champ_prof.pack(padx=100, pady=20)
    champ_prof.insert(0,x[1])

    champ_hor = CTkEntry(master=frame, placeholder_text="Volume Horaire")
    champ_hor.pack(padx=105, pady=20)
    champ_hor.insert(0,x[2])

    champ_sal = CTkEntry(master=frame, placeholder_text="Salle du cours")
    champ_sal.pack(padx=105, pady=20)
    champ_sal.insert(0,x[3])

    module = CTkEntry(master=frame, placeholder_text= "Module")
    module.pack(padx=105, pady=20)
    module.insert(0,x[4])

    button_connexion = CTkButton(master=frame, text="Save", command=lambda: connexion(champ_prof.get(), champ_hor.get(), champ_sal.get(), module.get()))
    button_connexion.pack(padx=130, pady=25)

def callDisplayCo(id_cours):
    cleanframe()
     
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM cours WHERE id_cours="+str(id_cours))
            
    x = curseur.fetchone()
    i=0
    label = CTkLabel(master=frame, text="Nom Cours: " + str(x[1]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Volume Horaire: " + str(x[2]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Salle Cours: "+ str(x[3]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Module: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    #mabd.commit()
    #messagebox.showerror("Success User Enter")


    """for i in range(3):
        label = CTkLabel(master=frame, text="Nom matiere:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""
    """label = CTkLabel(master=frame, text="Nom matiere: " + str(x[1]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient: " + str(x[2]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire: "+ str(x[3]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre: "+ str(x[4]),font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""

    #Label(root, ="REGISTRE ENSEIGNANTS", width=10, height=2, bg="dark blue",fg="#fff",font="arial 20 bold")
    def retour():
        cleanframe()
        list_cours()

    def Sup():
        mabd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school"
            )
        curseur = mabd.cursor()
        mabd.commit()
        curseur.execute("DELETE FROM cours WHERE id_cours = " + str(id_cours))

        cleanframe()
        list_cours()
        callDisplayCo()
   
    i += 1

    label = CTkLabel(master=frame, text="Affichage informations Cours", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    button=ctk.CTkButton(master=frame, text="BACK", command= retour)
    button.place(x=20,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Modifier", command=lambda:Modify_cours(id_cours))
    button.place(x=320,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Supprimer", command= Sup)
    button.place(x=520,y=150 + i*50)

def ADD_Cours():
    cleanframe()
    def connexion(N_Prof, Vol_hor, Sal_cours, Module):
        if not N_Prof or not Vol_hor or not Sal_cours or not Module:
            messagebox.showerror("Error","Remplir tous les champs")
            return
        try:
        # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{N_Prof}, {Sal_cours}, {Vol_hor}, {Module}")
            # Module insertion
            curseur.execute("INSERT INTO cours (N_Prof, Vol_hor, Sal_cours, Module) VALUES (%s, %s, %s, %s)",
                            (N_Prof, Vol_hor, Sal_cours, Module))
            mabd.commit()

            cleanframe()
            list_cours()

        except mysql.connector.Error as err:
            messagebox.showerror("Error",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()

    
    label = CTkLabel(master=frame, text="Inscription Cours", font=("algerian", 20, "bold"))
    label.pack(padx=50, pady=20)

    champ_prof = CTkEntry(master=frame, placeholder_text="Professeur")
    champ_prof.pack(padx=100, pady=20)

    champ_hor = CTkEntry(master=frame, placeholder_text="Volume Horaire")
    champ_hor.pack(padx=105, pady=20)

    champ_sal = CTkEntry(master=frame, placeholder_text="Salle Cours")
    champ_sal.pack(padx=105, pady=20)

    module = CTkEntry(master=frame, placeholder_text= "Module")
    module.pack(padx=105, pady=20)

    button_connexion = CTkButton(master=frame, text="Ajouter", command=lambda: connexion(champ_prof.get(), champ_hor.get(),  champ_sal.get(), module.get()))
    button_connexion.pack(padx=130, pady=25)

def list_cours():
    cleanframe()
    label = CTkLabel(master=frame, text="Liste Cours", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    def displayCours(x,i):
        button=ctk.CTkButton(master=frame, text="Professeur: " + str(x[1]) + "   -   Volume Horaire: " + str(x[2]) +"   -   Salle Cours: "+ str(x[3]) + "   -   Module: "+ str(x[4]), command=lambda: callDisplayCo(x[0]))
        button.place(y=220 + i*50, x=20)

    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM cours")
            
    don = curseur.fetchall()
    i = 0
    for x in don:
        print(x)
        displayCours(x,i)
        i +=1
    mabd.commit()
    #messagebox.showerror("Success User Enter")
            
    label = ctk.CTkLabel(master=frame, text="LISTE DES MODULES",font=("algerian", 40,"bold"),
        text_color="dark blue",bg_color="lightgray",width=win.winfo_screenwidth(),height=100)
    label.place(x=0,y=0)
    button_connexion = CTkButton(master=frame, text="Ajouter", command=ADD_Cours)
    button_connexion.place(x=500, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

    """for i in range(3):
        label = CTkLabel(master=frame, text="Nom matiere:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=20,y=150 + i*50)
        label = CTkLabel(master=frame, text="Coefficient:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=300,y=150 + i*50)
        label = CTkLabel(master=frame, text="Volume horaire:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=600,y=150 + i*50)
        label = CTkLabel(master=frame, text="Semestre:",font=("Times_new_roman",20,"bold"),
        text_color="white")
        label.place(x=900,y=150 + i*50)"""

    #Label(root, ="REGISTRE ENSEIGNANTS", width=10, height=2, bg="dark blue",fg="#fff",font="arial 20 bold")

    #button=ctk.CTkButton(master=frame, text="Connexion")
    #button.pack(pady=12, padx=10)

    inscription.mainloop()
    #win.mainloop()


#---------FIN fonction Cours 

##################################################################################################################

#----------Fonctions Profil


def Modify_profil(id):
    cleanframe()
    def connexion(email, password):
        
        try:
            # Database
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{email}, {password}")
            # Module insertion
            curseur.execute("UPDATE compte SET email=%s, password=%s WHERE id="+str(id),
                            (email, password))
            mabd.commit()

            cleanframe()
            callDisplayP(id)
            
        except mysql.connector.Error as err:
            messagebox.showerror("Err",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()
               

    
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM compte WHERE id="+str(id))
    x = curseur.fetchone()

    label = CTkLabel(master=frame, text="MODIFICATION PROIL")
    label.pack(padx=50, pady=20)

    champ_mail = CTkEntry(master=frame, placeholder_text="email@gmail.com")
    champ_mail.pack(padx=100, pady=20)
    champ_mail.insert(0,x[1])

    champ_password = CTkEntry(master=frame, placeholder_text="Password")
    champ_password.pack(padx=105, pady=20)
    champ_password.insert(0,x[2])


    button_connexion = CTkButton(master=frame, text="Save", command=lambda: connexion(champ_mail.get(), champ_password.get()))
    button_connexion.pack(padx=130, pady=25)

def callDisplayP(id):
    cleanframe()
     
    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM compte WHERE id="+str(id))
            
    x = curseur.fetchone()
    i=0
    label = CTkLabel(master=frame, text="Email: " + str(x[1]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    label.place(x=20,y=150 + i*50)
    label = CTkLabel(master=frame, text="Password: " + str(x[2]),font=("Times_new_roman",20,"bold"),
    text_color="white")
    i+=1
    label.place(x=20,y=150 + i*50)
    
    #mabd.commit()
    #messagebox.showerror("Success User Enter")

    #Label(root, ="REGISTRE ENSEIGNANTS", width=10, height=2, bg="dark blue",fg="#fff",font="arial 20 bold")
    def retour():
        cleanframe()
        list_profil()

    def Sup():
        mabd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="school"
            )
        curseur = mabd.cursor()
        mabd.commit()
        curseur.execute("DELETE FROM compte WHERE id = " + str(id))


        cleanframe()
        list_profil()
        callDisplayP()
   
    i += 1

    label = CTkLabel(master=frame, text="Profil", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)

    button=ctk.CTkButton(master=frame, text="BACK", command= retour)
    button.place(x=20,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Modifier", command=lambda:Modify_profil(id))
    button.place(x=320,y=150 + i*50)
    button=ctk.CTkButton(master=frame, text="Supprimer", command= Sup)
    button.place(x=520,y=150 + i*50)

def ADD_Profil():
    cleanframe()
    def connexion(email, password):
        if not email or not password:
            messagebox.showerror("Error","Remplir tous les champs")
            return
        # Database
        try:
            mabd = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="school"
            )
            curseur = mabd.cursor()
            print(f"{email}, {password}")
            # Module insertion
            curseur.execute("INSERT INTO compte (email, password) VALUES (%s, %s)",
                            (email, password))
            mabd.commit()

            cleanframe()
            list_profil()

        except mysql.connector.Error as err:
            messagebox.showerror("Error",f"Error BD: {err}")

        finally:
            # Database close
            if mabd.is_connected():
                curseur.close()
                mabd.close()
                #cleanframe()
                #import Jo_Odg

    label = CTkLabel(master=frame, text="Ajout Profil", font=("algerian", 20, "bold"))
    label.pack(padx=50, pady=20)

    champ_prof = CTkEntry(master=frame, placeholder_text="Email")
    champ_prof.pack(padx=100, pady=20)

    champ_hor = CTkEntry(master=frame, placeholder_text="Password")
    champ_hor.pack(padx=105, pady=20)

    button_connexion = CTkButton(master=frame, text="Ajouter", command=lambda: connexion(email.get(), password.get()))
    button_connexion.pack(padx=130, pady=25)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

def list_profil():
    cleanframe()

    label = CTkLabel(master=frame, text="Liste Profil", font=("algerian", 25,"bold"))
    label.pack(padx=50, pady=20)
    def displayprofile(x,i):
        button=ctk.CTkButton(master=frame, text="Email: " + str(x[1]) + "   -   Password: " + str(x[2]),  command=lambda: callDisplayP(x[0]))
        button.place(y=220 + i*50, x=20)

    mabd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
        )
    curseur = mabd.cursor()
    mabd.commit()
        # Module insertion
    curseur.execute("SELECT * FROM compte")#WHERE email=%s AND password= %s", (email, password)
            
    don = curseur.fetchall()
    i = 0
    for x in don:
        print(x)
        displayprofile(x,i)
        i +=1
    mabd.commit()
            
    label = ctk.CTkLabel(master=frame, text="Profil",font=("algerian",30,"bold"),
        text_color="dark blue",bg_color="lightgray",width=win.winfo_screenwidth(),height=100)
    label.place(x=0,y=0)
    button_connexion = CTkButton(master=frame, text="Ajouter", command=ADD_Profil)
    button_connexion.place(x=500, y=150)

    but = CTkButton(master= frame, text="Retour", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= home_page)
    but.place(x=0, y=150)

    inscription.mainloop()
    #win.mainloop()



#----------FIN fonctions profil

##################################################################################################################""


#-------------------Home page


def home_page():
    cleanframe()
    label = CTkLabel(master=frame, text="W.School", text_color="blue",font=("algerian", 30,"bold"))
    label.pack(padx=0, pady=20)

    l = CTkLabel(master = frame, text = "*W E L C O M E  * T O  *", text_color = "blue", font=("algerian", 50, "bold"))
    l.pack(expand= True)

    lbl = CTkLabel(master= frame, text=" W E N D P O U L M O M N O N G O  ", text_color = "blue",font=("algerian", 50, "bold"))
    lbl.pack(expand=True)

    lb = CTkLabel(master = frame, text = " * T E C H N O L O G I E *  S C H O O L * ", text_color = "blue",font=("algerian", 50, "bold"))
    lb.pack(expand = True)
    
    but = CTkButton(master= frame, text="Profil", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command =  list_profil)
    but.place(x=0, y=50)
    
    but = CTkButton(master= frame, text="Inscription", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= inscription_Profil)#, command= insc
    but.place(x=0, y=100)
    
    def login():
        connexion_Profil()
    
    but = CTkButton(master= frame, text="Login", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= login)#, command= login
    but.place(x=0, y=150)
    
    but = CTkButton(master= frame, text="Etudiant", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= list_student)
    but.place(x=0, y=200)
    
    but = CTkButton(master=frame, text="Enseignant", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= list_ens)
    but.place(x=0, y=250)
    
    but = CTkButton(master= frame, text="Matiere", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= list_matiere)
    but.place(x=0, y=300)
    
    but = CTkButton(master= frame, text="Notes", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command=list_notes)
    but.place(x=0, y=350)
    
    but = CTkButton(master= frame, text="Cours", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= list_cours)
    but.place(x=0, y=400)
    
    
    but = CTkButton(master= frame, text="Graphique", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2)
    but.place(x=0, y=450)
    
    def exit():
        win.destroy()
        messagebox.showinfo("Error","BONNE SUITE DE PROGRAMME A VOUS ET A LA PROCHAINE CONNEXION POUR PLUS DE MERVEILLE")
    
    but = CTkButton(master= frame, text="Exit", corner_radius = 25, fg_color = "transparent", hover_color = "#4158D0", border_width = 2, command= exit)#, command= exit
    but.place(x=0, y=500)

#-------------FIN home page
############################################################################################

home_page()

inscription.mainloop()
win.mainloop()


