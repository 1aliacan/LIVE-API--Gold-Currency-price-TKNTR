import tkinter
from html.parser import commentclose
import tkinter as tk
from tkinter.ttk import tclobjs_to_py

import requests
from requests.packages import package

url_address = "https://finans.truncgil.com/v4/today.json"

data_response = requests.get(url_address)



def aud_ALIS():
    response = requests.get(url_address)
    if response.status_code == 200:
        data = response.json()
        value_ALaud = data["AUD"]["Buying"]
        aud_alis_entry.delete(0,tkinter.END)
        aud_alis_entry.insert(0,value_ALaud)


def aud_SATIS():
    if data_response.status_code == 200:
        data = data_response.json()
        print("AUD Dolari Satis: ", data["AUD"]["Selling"])

def usd_ALIS():
    response = requests.get(url_address)
     if data_response.status_code == 200:
        data = requests.json()
        usd_Avalue = data["USD"]["Buying"]
        usd_alis_entry.delete(0, tk.END )  # Clear the one on screen
        usd_alis_entry.insert(0, usd_Avalue)  # insert the new value

def usd_SATIS():
    data = data_response.json()
    usd_Svalue=data["USD"]["Selling"]
    usd_satis_entry.delete(0, tk.END) #mevcut degeri sil
    usd_satis_entry.insert(0, usd_Svalue)

def euro_ALIS():
    
    data= data_response.json()
    euro_Avalue = data["EUR"]["Buying"]
    euro_alis_entry.delete(0,tk.END)#entry deki eski degeri sil
    euro_alis_entry.insert(0,euro_Avalue) #yeni degeri entry e cek


def euro_SATIS():
    if data_response.status_code == 200:
        data = data_response.json()
        euro_Svalue = data["EUR"]["Selling"]
        euro_satis_entry.delete(0,tk.END)
        euro_satis_entry.insert(0,euro_Svalue)

def gram_altin_ALIS():
    if data_response.status_code == 200:
        data= data_response.json()
        gram_alisValue= data["GRA"]["Buying"]
        gram_alis_entry.delete(0,tk.END)
        gram_alis_entry.insert(0,gram_alisValue)


def gram_altin_SATIS():
    if data_response.status_code == 200:
        data = data_response.json()
        gram_SATvalue = data["GRA"]["Selling"]
        gram_satis_entry.delete(0,tkinter.END)
        gram_satis_entry.insert(0, gram_SATvalue)
def ceyrek_altin_ALIS():
    if data_response.status_code == 200:
        data=data_response.json()
        ceyrek_ALvalue = data["CEYREKALTIN"]["Buying"]
        ceyrek_altin_ALentry.delete(0, tkinter.END)
        ceyrek_altin_ALentry.insert(0, ceyrek_ALvalue)

def ceyrek_altin_SATIS():
    if data_response.status_code == 200:
        data= data_response.json()
        ceyrek_SATvalue = data["CEYREKALTIN"]["Selling"]
        ceyrek_altin_SATentry.delete(0,tkinter.END)
        ceyrek_altin_SATentry.insert(0,ceyrek_SATvalue)

def yarim_altin_ALIS():
    if data_response.status_code == 200:
        data = data_response.json()
        yarim_ALvalue = data["YARIMALTIN"]["Buying"] #value olustur
        yarim_altin_alis_entry.delete(0,tkinter.END)
        yarim_altin_alis_entry.insert(0,yarim_ALvalue)#value yi ata

def yarim_altin_SATIS():
    if data_response.status_code == 200:
        data = data_response.json()
        yarim_SATvalue = data["YARIMALTIN"]["Selling"]
        yarim_altin_satis_entry.delete(0,tkinter.END)
        yarim_altin_satis_entry.insert(0,yarim_SATvalue)

def tam_altin_ALIS():
    if data_response.status_code == 200:
        data = data_response.json()
        tam_ALvalue = data["TAMALTIN"]["Buying"]
        tam_altin_AL_entry.delete(0,tkinter.END)
        tam_altin_AL_entry.insert(0,tam_ALvalue)

def tam_altin_SATIS():
    if data_response.status_code ==200:
        data = data_response.json()
        tam_SATvalue = data["TAMALTIN"]["Selling"]
        tam_altin_SAT_entry.delete(0,tkinter.END)
        tam_altin_SAT_entry.insert(0,tam_SATvalue)




#window tkinter
app_window = tkinter.Tk()
app_window.title("DOLAR-ALTIN ANLIK FIYAT")
app_window.minsize(400,600)
app_window.pack_slaves()




#USD ALIS button
USD_ALIS_BUTTON = tkinter.Button(app_window, text="USD ALIS GOSTER", command=usd_ALIS)
USD_ALIS_BUTTON.pack()
USD_ALIS_BUTTON.place(x=10,y=10)
#USD-ALIS-label
usd_alis_entry = tkinter.Entry(app_window,fg="green",width=15,justify="center")
usd_alis_entry.place(x=10,y=40)

#USD SATIS button
USD_SATIS_BUTTON = tkinter.Button(app_window,text="USD SATIS GOSTER", command=usd_SATIS)
USD_SATIS_BUTTON.pack()
USD_SATIS_BUTTON.place(x=200,y=10)
#USD SATIS LABEL
usd_satis_entry = tkinter.Entry(app_window, fg="red", width=15, justify="center")
usd_satis_entry.place(x=200, y=40)

#Euro ALIS button
euro_alis_button = tkinter.Button(app_window,text="EURO ALIS GOSTER",command=euro_ALIS)
euro_alis_button.place(x=10,y=70)
#euro alis entry
euro_alis_entry = tkinter.Entry(app_window,fg="lightblue",width=15, justify="center")
euro_alis_entry.place(x=10,y=100)

#euro satis button
euro_satis_button = tkinter.Button(app_window, text="EURO SATIS GOSTER", command=euro_SATIS)
euro_satis_button.place(x=200,y=70)
#euro satis entry
euro_satis_entry = tkinter.Entry(app_window,fg="#bf51bd", width=15,justify="center")
euro_satis_entry.place(x=200,y=100)

#gram altin alis button
gram_alis_button =tkinter.Button(app_window, text="GRAM ALTIN ALIS", command= gram_altin_ALIS)
gram_alis_button.place(x=10,y=130)
#gram altin alis entry
gram_alis_entry= tkinter.Entry(app_window,fg="yellow",width=15,justify="center")
gram_alis_entry.place(x=10,y=160)

#gram altin satis
gram_satis_button = tkinter.Button(app_window, text="GRAM ALTIN SATIS", command=gram_altin_SATIS)
gram_satis_button.place(x=200,y=130)
#gram altin entry
gram_satis_entry = tkinter.Entry(app_window,fg="yellow",width=15,justify="center")
gram_satis_entry.place(x=200,y=160)

#ceyerek altin ALbutton
ceyrek_altin_ALbutton = tkinter.Button(app_window, text="CEYREK ALTIN ALIS", command=ceyrek_altin_ALIS)
ceyrek_altin_ALbutton.place(x=10, y=190)

#ceyrek altin ALentry
ceyrek_altin_ALentry = tkinter.Entry(app_window, fg="yellow", width=15, justify="center")
ceyrek_altin_ALentry.place(x=10, y=220)

#ceyrek altin SATbutton
ceyrek_altin_SATbutton = tkinter.Button(app_window, text="CEYREK ALTIN SATIS", command=ceyrek_altin_SATIS)
ceyrek_altin_SATbutton.place(x=200,y=190)
#ceyrek altin SATentry
ceyrek_altin_SATentry = tkinter.Entry(app_window, fg="orange", width=15,justify="center")
ceyrek_altin_SATentry.place(x=200,y=220)

#yarim altin alis button
yarim_altin_alis_button = tkinter.Button(app_window,text="YARIM ALTIN ALIS", command=yarim_altin_ALIS)
yarim_altin_alis_button.place(x=10,y=250)
#yarim altin alis entry
yarim_altin_alis_entry = tkinter.Entry(app_window,fg="gold",width=15,justify="center")
yarim_altin_alis_entry.place(x=10,y=280)

#yarim_altin_satis_button
yarim_altin_satis_button = tkinter.Button(app_window,text="YARIM ALTIN SATIS",command=yarim_altin_SATIS)
yarim_altin_satis_button.place(x=200,y=250)
#yarim altin satis entry
yarim_altin_satis_entry = tkinter.Entry(app_window,fg="orange",width=15,justify="center")
yarim_altin_satis_entry.place(x=200,y=280)


#tam altin alis button
tam_altin_AL_button = tkinter.Button(app_window, text= "TAM-ALTIN ALIS", command=tam_altin_ALIS)
tam_altin_AL_button.place(x=10,y=310)
#tam altin alis entry
tam_altin_AL_entry = tkinter.Entry(app_window, fg="yellow", width=15, justify="center")
tam_altin_AL_entry.place(x=10,y=340)

#tam altin satis button
tam_altin_SAT_button = tkinter.Button(app_window,text="TAM-ALTIN SATIS", command=tam_altin_SATIS)
tam_altin_SAT_button.place(x=200,y=310)

#tam altin sat entry
tam_altin_SAT_entry= tkinter.Entry(app_window, fg="orange", width=15,justify="center")
tam_altin_SAT_entry.place(x=200,y=340)

#aud alis button
aud_alis_button = tkinter.Button(app_window, text="AUD ALIS FIYATI",command = aud_ALIS)
aud_alis_button.place(x=10,y=370)
#aud alis entry
aud_alis_entry = tkinter.Entry(app_window, fg="lightblue", width=15, justify="center")
aud_alis_entry.place(x=10,y=400)







app_window.mainloop()
#line
#screen
