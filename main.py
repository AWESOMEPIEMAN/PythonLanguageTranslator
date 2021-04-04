from tkinter import *
from tkinter.ttk import Combobox
from textblob import TextBlob
from tkinter import messagebox

root = Tk()
root.geometry("500x300")
root.title("Python Translator")
root.configure(bg="grey")


langlist = {'afrikaans': 'afrikaans', 'albanian': 'albanian', 'amharic': 'amharic', 'arabic': 'arabic', 'armenian': 'armenian', 'azerbaijani': 'azerbaijani', 'basque': 'basque', 'belarusian': 'belarusian', 'bengali': 'bengali', 'bosnian': 'bosnian', 'bulgarian': 'bulgarian', 'catalan': 'catalan', 'cebuano': 'cebuano', 'chichewa': 'chichewa', 'chinese (simplified)': 'chinese (simplified)', 
'chinese (traditional)': 'chinese (traditional)', 'corsican': 'corsican', 'croatian': 'croatian', 'czech': 'czech', 'danish': 'danish', 'dutch': 'dutch', 'english': 'english', 'esperanto': 'esperanto', 'estonian': 'estonian', 'filipino': 'filipino', 'finnish': 'finnish', 'french': 'french', 'frisian': 'frisian', 'galician': 'galician', 'georgian': 'georgian', 'german': 'german', 'greek': 'greek', 'gujarati': 'gujarati', 'haitian creole': 'haitian creole', 'hausa': 'hausa', 'hawaiian': 'hawaiian', 'hebrew': 'hebrew', 'hindi': 'hindi', 'hmong': 'hmong', 'hungarian': 'hungarian', 'icelandic': 'icelandic', 'igbo': 'igbo', 'indonesian': 'indonesian', 'irish': 'irish', 'italian': 'italian', 'japanese': 'japanese', 'javanese': 'javanese', 'kannada': 'kannada', 'kazakh': 'kazakh', 'khmer': 'khmer', 'korean': 'korean', 'kurdish (kurmanji)': 'kurdish (kurmanji)', 'kyrgyz': 'kyrgyz', 'lao': 'lao', 'latin': 'latin', 'latvian': 'latvian', 'lithuanian': 'lithuanian', 'luxembourgish': 'luxembourgish', 'macedonian': 
'macedonian', 'malagasy': 'malagasy', 'malay': 'malay', 'malayalam': 'malayalam', 'maltese': 'maltese', 'maori': 'maori', 'marathi': 'marathi', 'mongolian': 'mongolian', 'myanmar (burmese)': 'myanmar (burmese)', 'nepali': 'nepali', 'norwegian': 'norwegian', 'odia': 'odia', 'pashto': 'pashto', 'persian': 'persian', 'polish': 'polish', 'portuguese': 'portuguese', 'punjabi': 'punjabi', 'romanian': 'romanian', 'russian': 'russian', 'samoan': 'samoan', 'scots gaelic': 'scots gaelic', 'serbian': 'serbian', 'sesotho': 'sesotho', 'shona': 'shona', 'sindhi': 'sindhi', 'sinhala': 'sinhala', 'slovak': 'slovak', 'slovenian': 'slovenian', 'somali': 'somali', 'spanish': 'spanish', 'sundanese': 'sundanese', 'swahili': 'swahili', 'swedish': 'swedish', 'tajik': 'tajik', 'tamil': 'tamil', 'telugu': 'telugu', 'thai': 'thai', 'turkish': 'turkish', 'ukrainian': 'ukrainian', 'urdu': 'urdu', 'uyghur': 'uyghur', 'uzbek': 'uzbek', 'vietnamese': 'vietnamese', 'welsh': 'welsh', 'xhosa': 'xhosa', 'yiddish': 'yiddish', 'yoruba': 
'yoruba', 'zulu': 'zulu'}

#binding functions
def onEnter(e):
    e1['bg'] = 'bisque'
def onleaveEnter(e):
    e1['bg'] = 'white'

def on2Enter(r):
    e2['bg'] = 'bisque'
def on2leaveEnter(r):
    e2['bg'] = 'white'

def onEnterbtn(b):
    butn1['bg'] = 'bisque'
def onleaveEnterbtn(b):
    butn1['bg'] = 'grey'

def on2Enterbtn(b):
    butn2['bg'] = 'bisque'
def on2leaveEnterbtn(b):
    butn2['bg'] = 'grey'
#functions

def enter():
    textw = TextBlob(name.get())
    langd = textw.detect_language()

    lang_ = languages.get()
    lang2 = langlist[lang_]
    textw = textw.translate(from_lang=langd,to=lang2)
    lab3.configure(text=textw)


def exitfunc():
    e = messagebox.askyesnocancel('Hey', "Do you wish to exit?",parent=root)
    if e == True:
        root.destroy()


#combobox section
languages = StringVar()
labg_bo = Combobox(root,width=20,textvariable=languages,state='readonly')
labg_bo['values'] = [e for e in langlist.keys()]
labg_bo.current(57)
labg_bo.place(x=360,y=0)
#buttons
name  = StringVar()
e1 = Entry(root,width=30,textvariable=name,font=('impact',13))
e1.place(x=150,y=70)
name2  = StringVar()
e2 = Entry(root,width=30,textvariable=name2,font=('impact',13))
e2.place(x=150,y=140)
#labels for the boxes
lab1 = Label(root,text="Enter text : ",font=('impact',13,),bg="grey")
lab1.place(x=10,y=66)

lab2 = Label(root,text="Translated Text : ",font=('impact',13,),bg="grey")
lab2.place(x=10,y=136)

lab3 = Label(root,text=" ",font=('impact',13,),bg="grey")
lab3.place(x=10,y=160)
#buttons

butn1 = Button(root,text="Submit",bd=10,bg='Grey',activebackground='white',width=9,font=('impact',13),command=enter)
butn1.place(x=80,y=190)

butn2 = Button(root,text="Exit",bd=10,bg='Grey',activebackground='white',width=9,font=('impact',13),command=exitfunc)
butn2.place(x=200,y=190)

#bindings
e1.bind('<Enter>',onEnter)
e1.bind('<Leave>',onleaveEnter)

e2.bind('<Enter>',on2Enter)
e2.bind('<Leave>',on2leaveEnter)

butn1.bind('<Enter>',onEnterbtn)
butn1.bind('<Leave>',onleaveEnterbtn)

butn2.bind('<Enter>',on2Enterbtn)
butn2.bind('<Leave>',on2leaveEnterbtn)
root.mainloop()
