import requests
from wiktionaryparser import WiktionaryParser
import tkinter as tk 
from tkinter import ttk 
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
import googletrans
import os 



def word_finder():
    global word
    textbox1.delete('1.0', tk.END)
    textbox2.delete('1.0', tk.END)
    textbox3.delete('1.0', tk.END)
    textbox4.delete('1.0', tk.END)
    textbox5.delete('1.0', tk.END)
    
    user=tk.StringVar()
    user=entry.get()
    parser=WiktionaryParser()
    word=parser.fetch(user,"english")

   # parser.set_default_language("")
     

    definitonlist=[]
    synonyms_list=[]
    antonyms_list=[]
    example_list=[]
    # print(word[0]["definitions"][0]["text"])

    # Definitions
    for i in range(len(word[0]["definitions"][0]["text"])):
        definitonlist.append(word[0]["definitions"][0]["text"][i])

    # SYNONYMS
    
    if len(word[0]["definitions"][0]["relatedWords"])>1:
        for i in range(len(word[0]["definitions"][0]["relatedWords"][0]["words"])):
            synonyms_list.append(word[0]["definitions"][0]["relatedWords"][0]["words"][i])

    # ANTONYMS
    if len(word[0]["definitions"][0]["relatedWords"])>1:
        for i in range(len(word[0]["definitions"][0]["relatedWords"][1]["words"])):
            antonyms_list.append(word[0]["definitions"][0]["relatedWords"][1]["words"][i])
            

    for i in range(len(word[0]["definitions"][0]["examples"])):
        example_list.append(word[0]["definitions"][0]["examples"][i])
    
    written=False
    for i in range(len(antonyms_list)):
        if written==False:
            textbox1.insert(tk.END,"  ANTONYMS " +"\n")
            written=True
        textbox1.insert(tk.END, antonyms_list[i]+"\n")
    
    written2=False
    for i in range(len(synonyms_list)):
        if written2==False:
            textbox3.insert(tk.END,"  SYNONYMS " +"\n")
            written2=True
        textbox3.insert(tk.END, synonyms_list[i]+"\n")
    
    written3=False
    for i in range(len(definitonlist)):
        if written3==False:
            textbox2.insert(tk.END," DEFINITIONS " + "\n")
            written3=True
        textbox2.insert(tk.END,definitonlist[i]+"\n")
    
    written4=False
    for i in range(len(example_list)):
        if written4==False:
            textbox4.insert(tk.END," EXAMPLES " + "\n")
            written4=True
        textbox4.insert(tk.END,example_list[i]+"\n")
    
def voice():
    text=entry.get()
    language="en"
    speech=gTTS(text=text,lang=language,slow=False)
    os.remove('text.mp3')
    speech.save("text.mp3")
     
    playsound('text.mp3')

def translate():
    translator = Translator(service_urls=['translate.googleapis.com'])
    sentence=str(entry.get())
    print(sentence)
   
    
    translated_word=translator.translate(sentence,dest="tr").text
    textbox5.insert(tk.END,translated_word)


window=tk.Tk()
window.geometry("1920x1080")
window.configure(bg='gray')
window.grid()

window.columnconfigure(0,weight=2,uniform="a")
window.columnconfigure(1,weight=3,uniform="a")
window.columnconfigure(2,weight=2,uniform="a")
 


window.rowconfigure(0,weight=1,uniform="a")
window.rowconfigure(1,weight=1,uniform="a")
window.rowconfigure(2,weight=6,uniform="a")
window.rowconfigure(3,weight=6,uniform="a")
window.rowconfigure(4,weight=1,uniform="a")
window.rowconfigure(5,weight=1,uniform="a")
window.rowconfigure(6,weight=1,uniform="a")
window.rowconfigure(7,weight=1,uniform="a")
window.rowconfigure(8,weight=1,uniform="a")

entry=ttk.Entry(window)
entry.grid(row=0,column=1)

color="green"

button=ttk.Button(window,command=word_finder,text="touch me fellow")
button.grid(row=1,column=1,pady=(0,10))

soundbutton=ttk.Button(window,command=voice,text="touch me hear me ")
soundbutton.grid(row=5,column=0)
 

textbox1=tk.Text(window)
textbox1.grid(row=2,column=0,pady=(20,0))
textbox1.config(background=color)

textbox2=tk.Text(window)
textbox2.grid(row=2,column=1,pady=(20,0))
textbox2.config(background=color)

textbox3=tk.Text(window)
textbox3.grid(row=2,column=2,pady=(20,0))
textbox3.config(background=color)

textbox4=tk.Text(window)
textbox4.grid(row=3,column=1,pady=(5,0))
textbox4.config(background=color)

textbox5=tk.Text(window)
textbox5.grid(row=6,column=1,pady=(5,0))
textbox5.config(background=color)

# translate it 
transbutton=ttk.Button(window,command=translate,text="i am a loser")
transbutton.grid(row=5,column=1)

window.mainloop()


