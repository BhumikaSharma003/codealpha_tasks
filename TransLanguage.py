from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root=tk.Tk() 
root.title('Language Translator')
root.geometry('1000x600')

frame1=Frame(root, width=1000, height=600, relief=SOLID, borderwidth=8, bg='#808080')
frame1.place(x=0,y=0)

Label(root, text="Language Translator", font=("Times New Roman ",20, "bold"), fg="white", bg='#120F3E').pack(pady=10)

def translate():
    lang_1= text_entry1.get("1.0", "end-1c")
    cl= choose_language.get()

    if lang_1=='':
        messagebox.showerror('Language Translator','Enter the text to translate.')
    else:
        text_entry2.delete(1.0,'end')
        translator= Translator()
        output=translator.translate(lang_1,dest=cl)
        text_entry2.insert('end',output.text)

def clear():
    text_entry1.delete(1.0,'end')
    text_entry2.delete(1.0,'end')

a=tk.StringVar()


auto_select=ttk.Combobox(frame1, width=20, textvariable=a, state='randomly', font=('Times New Roman',18, 'bold'))

auto_select['values']=(
                        'Auto Select',
                    )

auto_select.place(x=200,y=90)
auto_select.current(0)

l=tk.StringVar()
choose_language=ttk.Combobox(frame1, width=20, textvariable=l, state='randomly', font=('Times New Roman',18,'bold'))

choose_language['value']=(
                        'Afrikaans',
                        'Albanian',
                        'Amharic',
                        'Arabic',
                        'Armenian',
                        'Azerbaijani',
                        'Basque',
                        'Bengali',
                        'Bosnian',
                        'Bulgarian',
                        'Catalan',
                        'Cebuano',
                        'Croatian',
                        'Czech',
                        'Danish',
                        'Dutch',
                        'English',
                        'Estonian',
                        'Finnish',
                        'French',
                        'Galician',
                        'Georgian',
                        'German',
                        'Greek',
                        'Gujarati',
                        'Haitian Creole',
                        'Hausa',
                        'Hebrew',
                        'Hindi',
                        'Hmong',
                        'Hungarian',
                        'Icelandic',
                        'Igbo',
                        'Indonesian',
                        'Irish',
                        'Italian',
                        'Japanese',
                        'Javanese',
                        'Kannada',
                        'Kazakh',
                        'Khmer',
                        'Korean',
                        'Kyrgyz',
                        'Lao',
                        'Latvian',
                        'Lithuanian',
                        'Luxembourgish',
                        'Macedonian',
                        'Malagasy',
                        'Malay',
                        'Malayalam',
                        'Maltese',
                        'Maori',
                        'Marathi',
                        'Mongolian',
                        'Nepali',
                        'Norwegian',
                        'Odia',
                        'Pashto',
                        'Persian',
                        'Polish',
                        'Portuguese',
                        'Punjabi',
                        'Romanian',
                        'Russian',
                        'Samoan',
                        'Serbian',
                        'Shona',
                        'Sindhi',
                        'Sinhala',
                        'Slovak',
                        'Slovenian',
                        'Somali',
                        'Spanish',
                        'Swahili',
                        'Swedish',
                        'Tajik',
                        'Tamil',
                        'Telugu',
                        'Thai',
                        'Turkish',
                        'Ukrainian',
                        'Urdu',
                        'Uyghur',
                        'Uzbek',
                        'Vietnamese',
                        'Welsh',
                        'Xhosa',
                        'Yiddish',
                        'Yoruba',
                        'Zulu'
                        )

choose_language.place(x=550,y=90)
choose_language.current(0)

text_entry1= Text(frame1, width=35, height=12, borderwidth=5, relief=SOLID, font=('Times New Roman', 15))
text_entry1.place(x=125,y=200)

text_entry2= Text(frame1, width=35, height=12, borderwidth=5, relief=SOLID, font=('Times New Roman', 15))
text_entry2.place(x=525,y=200)

btn1=Button(frame1,command=translate, text="Translate", relief=RAISED, borderwidth=3, font=('Times new Roman', 12, 'bold'), bg='#248aa2' )
btn1.place(x=410,y=150)

btn2=Button(frame1, command=clear, text="Clear", relief=RAISED, borderwidth=3, font=('Times new Roman', 12, 'bold'), bg='#248aa2' )
btn2.place(x=515,y=150)

root.mainloop()