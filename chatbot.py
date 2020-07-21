from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot("My Bot")

trainer=ListTrainer(bot)

convo=(["Hii",
    "Hello, Welcome to VIT Bhopal University. How can I help you?",
    "What is the eligibility criteria for getting admission in VIT Bhopal",
    "Can you please specify category : B.Tech / M.Tech or BBA.",
    "B.tech",
    "Minimum 60% Marks in 10+2 and clearing the cutoff in VITEEE 2020.",
    "What are the courses available in VIT Bhopal",
    "We offer all the Future Ready Programmes:"
    "Aerospace Engineering ,"
    "Biotechnology ,"
    "Computer Science and Engineering etc.",
    "Do you offer Career Counseling services",
    "Yes, You can contact here 123456789.",
    "Please share contact details for admission query",
    "You can contact here 7560254500/7560254501/7560254502.",
    "I want to know the location of VIT Bhopal",
    "VIT University, Bhopal , Bhopal-Indore Highway Kothrikalan, Sehore Madhya Pradesh - 466114",
     ])



trainer.train(convo)


main = Tk()

main.geometry("1000x1250")

main.title("My Chatbot")

main.configure(background='gray24')

img = PhotoImage(file="vit.png")
photoL = Label(main, image=img)H



photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"You :"+query)
    print(type(answer_from_bot))
    msgs.insert(END, "Bot :"+str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)



frame=Frame(main)

sc= Scrollbar(frame,activebackground='gray25',bg='peachpuff2')

msgs=Listbox(frame,width=110,height=30,yscrollcommand=sc.set,background='khaki1')

sc.pack(side=RIGHT, fill=Y )

msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

textF=Entry(main, font=("Arial", 20))

textF.pack(fill=X,pady=10)

btn=Button(main, text="Ask Admin",font=("Arial",20 ,"bold"), command=ask_from_bot)

btn.pack()

btn1=Button(main, text="Quit",font=("Arial",20 ,"bold"),background='brown2', command=main.destroy)

btn1.pack()


#creating function

def enter_function(event):
    btn.invoke()

#going to bind main window with enter key

main.bind('<Return>',enter_function)



main.mainloop()
