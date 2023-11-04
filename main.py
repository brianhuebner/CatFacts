from tkinter import *
import requests
import json
import random

response = requests.get(url="https://catfact.ninja/facts?max_length=60&limit=100")
response.raise_for_status()
global data

data = json.loads(response.text)

def get_quote():

    cat_fact_data = data['data']
    all_cat_facts = []
    for i in cat_fact_data:
        
        fact = i["fact"]
        all_cat_facts.append(fact)

    fact_rand = random.randrange(len(all_cat_facts))
    canvas.itemconfig(quote_text, text=all_cat_facts[fact_rand])
    


window = Tk()
window.title("Cat Facts!")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text= 'Get a cat fact', width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

cat_img = PhotoImage(file="cat.png")
cat_button = Button(image=cat_img, highlightthickness=0, command=get_quote)
cat_button.grid(row=1, column=0)



window.mainloop()