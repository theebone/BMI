from tkinter import *
import psycopg2


root = Tk()
root.title("Výpočet BMI")
root.geometry("450x250")
root.resizable(False,False)
#druhé okno
def open_window():
    root1 = Toplevel(root)
    root1.title("Historie")
    root1.geometry("450x250")
    root1.resizable(False, False)
    root1.grid_rowconfigure(0, weight=1)
    root1.grid_columnconfigure(0, weight=1)

    # Scrollbar
    scrollbar = Scrollbar(root1)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Listbox
    listbox = Listbox(root1, yscrollcommand=scrollbar.set)
    listbox.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
    scrollbar.config(command=listbox.yview)
    refresh_history(listbox)
    
def open_meal_plan(file_name):
    # Vytvoříme nové okno pro zobrazení jídelníčku
    root1 = Toplevel(root)
    root1.title("Jídelníček")
    root1.geometry("450x250")
    root1.resizable(False, False)

        # Scrollbar
    scrollbar = Scrollbar(root1)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Listbox
    listbox = Listbox(root1, yscrollcommand=scrollbar.set, selectmode=SINGLE)
    listbox.pack(fill=BOTH, expand=True, padx=10, pady=10)  
    scrollbar.config(command=listbox.yview)

    # Otevření souboru s jídelníčkem
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            meal_plan = file.readlines()

        # Zobrazení jídel v listboxu
        for meal in meal_plan:
            listbox.insert(END, meal.strip())  
    except FileNotFoundError:
        listbox.insert(END, "Soubor nebyl nalezen!")

def meal_window():
    root2 = Toplevel(root)
    root2.title("Jídelníček")
    root2.geometry("150x330")
    root2.resizable(False, False)

    # Tlačítka pro různé kategorie jídelníčku
    extreme_obesity_button = Button(root2, text="Extrémní obezita", width=20, height=3, command=lambda: open_meal_plan("Extrémní obezita.txt"))
    extreme_obesity_button.grid(row=0, column=1)
    
    obesity_button = Button(root2, text="Obezita", width=20, height=3, command=lambda: open_meal_plan("Obezita.txt"))
    obesity_button.grid(row=1, column=1)
    
    overweight_button = Button(root2, text="Nadváha", width=20, height=3, command=lambda: open_meal_plan("Nadváha.txt"))
    overweight_button.grid(row=2, column=1)
    
    normal_button = Button(root2, text="Normální", width=20, height=3, command=lambda: open_meal_plan("Normální.txt"))
    normal_button.grid(row=3, column=1)
    
    under_weight_button = Button(root2, text="Podváha", width=20, height=3, command=lambda: open_meal_plan("Podváha.txt"))
    under_weight_button.grid(row=4, column=1)
    
    close_button = Button(root2, text="Zpět/Zavřít", width=20, height=3, command=root2.destroy)
    close_button.grid(row=5, column=1)



def refresh_history(listbox):
    # Vyčistit listbox
    listbox.delete(0, END)
    # Načíst všechna data z databáze
    data = show_all()
    for row in data:
        listbox.insert(END, row)


#fce


def calculate_bmi(name,age,weight,height):
    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        label_user_result_1["text"] = "chyba"
        label_user_result_2["text"] = "chyba"
        return None

    bmi = round(weight /height**2,2)
    if bmi < 18.5:
        text_result = "Podváha"
    elif bmi < 24.9:
        text_result = "Normální"

    elif bmi < 29.9:
        text_result = "Nadváha"
    elif bmi < 34.9:
        text_result = "Obezita"
    elif bmi >= 34.9:
        text_result = "Extrémní obezita"
    label_user_result_1["text"] = bmi
    label_user_result_2["text"] = text_result

    insert_data(name,age,bmi,text_result)

def check_dot(number):
    number_string = str(number)
    return number_string.replace(",",".") if "," in number_string else number_string


def insert_data(name,age,bmi_n,bmi_t):
    query = """INSERT INTO bmi(jmeno,vek,bmi_number,bmi_text) VALUES (%s,%s,%s,%s)"""
    with psycopg2.connect(dbname="health",
    user ="postgres",
    password="admin",
    host="localhost",
    port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute(query,(name,age,bmi_n,bmi_t))
            conn.commit()
    label_count_number.config(text=count_all_data())


   

def count_all_data():
    query = """SELECT COUNT(bmi_id) FROM bmi"""
    with psycopg2.connect(dbname="health",
    user ="postgres",
    password="admin",
    host="localhost",
    port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchone()[0]
        
def show_all():
    query = """SELECT * FROM bmi"""
    with psycopg2.connect(dbname="health",
    user ="postgres",
    password="admin",
    host="localhost",
    port="5432") as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            all_data = cur.fetchall()
            return all_data

            




#hlavní label
label_general = Label(root,text="Výpočet BMI")
label_general.grid(row=0,column=1)

#váha
label_weight = Label(root,text="Zadejte váhu v KG: ")
label_weight.grid(row=1,column=0)


entry_weight = Entry(root)
entry_weight.grid(row=1,column=1)

#výška

label_height = Label(root,text="Zadejte výšku v metrech: ")
label_height.grid(row=2,column=0)

entry_height = Entry(root)
entry_height.grid(row=2,column=1)
#Jméno
label_name = Label(root,text="Zadejte své jméno ")
label_name.grid(row=3,column=0)
entry_name = Entry(root)
entry_name.grid(row=3,column=1)
#věk
label_age = Label(root,text="Zadejte svůj věk")
label_age.grid(row=4,column=0)
entry_age = Entry(root)
entry_age.grid(row=4,column=1)


#tlačítka

button = Button(root,text="Spočítej",command=lambda:calculate_bmi(entry_name.get(),entry_age.get(),check_dot(entry_weight.get()),check_dot(entry_height.get())))
button.grid(row=5,column=1)

button_history = Button(root,text="Historie",command=open_window)
button_history.grid(row=9,column=1)

button_meal_plan = Button(root,text="Jídelníček",command=meal_window)
button_meal_plan.grid(row=5,column=3)

#výsledky

label_result_1 = Label(root,text="Číselný výsledek")
label_result_1.grid(row=6,column=0)

label_user_result_1 = Label(root)
label_user_result_1.grid(row=6,column=1)

label_result_2 = Label(root,text="Text výsledek")
label_result_2.grid(row=7,column=0)

label_user_result_2 = Label(root)
label_user_result_2.grid(row=7,column=1)

label_count_text = Label(root,text="Počet uživatelů: ")
label_count_text.grid(row=8,column=0)

label_count_number = Label(root,text=count_all_data())
label_count_number.grid(row=8,column=1)

label_history = Label(root,text="Historie")
label_history.grid(row=9,column=0)


root.mainloop()