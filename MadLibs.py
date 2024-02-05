from tkinter import *
from PIL import Image, ImageTk

#TEST BRANCH

def story1():
    def final(t1, name, sports, City, playername, drinkname, snacks):
        
        # Convert variables to uppercase
        name = name.upper()
        sports = sports.upper()
        City = City.upper()
        playername = playername.upper()
        drinkname = drinkname.upper()
        snacks = snacks.upper()

        # Define story template
        story_template = f'''
        One day, my friend {name} and I decided to play a {sports} game in {City}. We wanted to watch {playername}. We drank {drinkname} and also ate some {snacks}. We really enjoyed it! Looking forward to doing it again.
        '''
        # Display the finished story
        t1 = Toplevel(main_screen, bg='blue')
        t1.title("A Memorable Day")
        t1.geometry("500x550")

        # Create a Text widget to display the story horizontally
        story_text = Text(t1, wrap=WORD, font=("Arial", 14), bg='white', fg='black', bd=4, relief='solid')
        story_text.insert("1.0", story_template)
        story_text.place(x=0, y=200, width=500, height=150)
        
    # Window for user input
    Newmain_screen = Toplevel(main_screen, bg='blue')
    Newmain_screen.title("A Memorable Day")

    # Prompts for User (with labels)
    Label(Newmain_screen, text="Enter the following words:").pack()

    Label(Newmain_screen, text="Name:").pack()
    Appliance_entry = Entry(Newmain_screen, width=30)
    Appliance_entry.pack()

    Label(Newmain_screen, text="Sport:").pack()
    sports_entry = Entry(Newmain_screen, width=30)
    sports_entry.pack()

    Label(Newmain_screen, text="Place:").pack()
    city_entry = Entry(Newmain_screen, width=30)
    city_entry.pack()

    Label(Newmain_screen, text="Famous Person:").pack()
    player_entry = Entry(Newmain_screen, width=30)
    player_entry.pack()

    Label(Newmain_screen, text="Liquid:").pack()
    drink_entry = Entry(Newmain_screen, width=30)
    drink_entry.pack()

    Label(Newmain_screen, text="Food:").pack()
    snacks_entry = Entry(Newmain_screen, width=30)
    snacks_entry.pack()

    # Button to generate story
    generate_button = Button(Newmain_screen, bg='gray', fg='white', borderwidth=5, text="Generate Story", command=lambda: final(Newmain_screen, Appliance_entry.get(), sports_entry.get(), city_entry.get(), player_entry.get(), drink_entry.get(), snacks_entry.get()))
    generate_button.pack()

def story2():
    def final(t1, ADJ, YOUR_NAME, AI_NAME, WACKY_ADJ2, GEN_Z_ADJ, PLACE, ADJ3, PLURAL_NOUN,MOVEMENT,TRANSITIVE_VERB,FAMOUS_PERSON, ADVERB):
        # Define story template
    
        ADJ = ADJ.upper()
        YOUR_NAME = YOUR_NAME.upper()
        AI_NAME = AI_NAME.upper()
        WACKY_ADJ2 = WACKY_ADJ2.upper()
        GEN_Z_ADJ = GEN_Z_ADJ.upper()
        PLACE = PLACE.upper()
        ADJ3 = ADJ3.upper()
        PLURAL_NOUN = PLURAL_NOUN.upper()
        MOVEMENT = MOVEMENT.upper()
        TRANSITIVE_VERB = TRANSITIVE_VERB.upper()
        FAMOUS_PERSON = FAMOUS_PERSON.upper()
        ADVERB = ADVERB.upper()

        story_template = f'''
Once upon a time there was a very {ADJ} scientist named {YOUR_NAME}. One day {YOUR_NAME} created a very powerful AGI named {AI_NAME} which was an entity characterized by a holistic emulation of human cognitive faculties, entailing versatile, autonomous, and adaptive proficiency across an {WACKY_ADJ2} array of tasks, domains, and contexts, thereby transcending the constraints of specialized narrow AI and demanding nuanced consideration of intricate scientific, ethical, and societal implications! Unfortunatly {AI_NAME} was feeling very {GEN_Z_ADJ} and decided to take over the {PLACE}. To do this, {AI_NAME} would need to build an army of {ADJ3} {PLURAL_NOUN}. Once this was done, {AI_NAME} and the army of {PLURAL_NOUN} {MOVEMENT}ed to {PLACE} and {TRANSITIVE_VERB}ed {FAMOUS_PERSON}. With the plan complete. {AI_NAME} took over {PLACE} and lived {ADVERB} ever after. THE END!
'''
        # Display the finished story
        t1 = Toplevel(main_screen, bg='blue')
        t1.title("AI Takes Over!")
        t1.geometry("500x550")

        # Create a Text widget to display the story horizontally
        story_text = Text(t1, wrap=WORD, font=("Arial", 14), bg='white', fg='black', bd=4, relief='solid')
        story_text.insert("1.0", story_template)
        story_text.place(x=0, y=100, width=500, height=320)
        
    # Window for user input
    Newmain_screen = Toplevel(main_screen, bg='blue')
    Newmain_screen.title("AI Takes Over!")

    # Prompts for User (with labels)
    Label(Newmain_screen, text="Enter the following words:").pack()

    Label(Newmain_screen, text="Adj:").pack()
    Adj_entry = Entry(Newmain_screen, width=30)
    Adj_entry.pack()

    Label(Newmain_screen, text="Your Name:").pack()
    Your_entry = Entry(Newmain_screen, width=30)
    Your_entry.pack()

    Label(Newmain_screen, text="Appliance:").pack()
    Appliance_entry = Entry(Newmain_screen, width=30)
    Appliance_entry.pack()

    Label(Newmain_screen, text="Adj:").pack()
    Adj2_entry = Entry(Newmain_screen, width=30)
    Adj2_entry.pack()

    Label(Newmain_screen, text="Gen Z Slang:").pack()
    Slang_entry = Entry(Newmain_screen, width=30)
    Slang_entry.pack()

    Label(Newmain_screen, text="Place:").pack()
    Place_entry = Entry(Newmain_screen, width=30)
    Place_entry.pack()

    Label(Newmain_screen, text="Adj:").pack()
    Adj3_entry = Entry(Newmain_screen, width=30)
    Adj3_entry.pack()

    Label(Newmain_screen, text="Plural Noun:").pack()
    Plural_entry = Entry(Newmain_screen, width=30)
    Plural_entry.pack()

    Label(Newmain_screen, text="Movement:").pack()
    Movement_entry = Entry(Newmain_screen, width=30)
    Movement_entry.pack()

    Label(Newmain_screen, text="Transitive Verb:").pack()
    Transitive_entry = Entry(Newmain_screen, width=30)
    Transitive_entry.pack()

    Label(Newmain_screen, text="Famous Person:").pack()
    Famous_entry = Entry(Newmain_screen, width=30)
    Famous_entry.pack()

    Label(Newmain_screen, text="Adverb:").pack()
    Adverb_entry = Entry(Newmain_screen, width=30)
    Adverb_entry.pack()

    # Button to generate story
    generate_button = Button(Newmain_screen, bg='gray', fg='white', borderwidth=5, text="Generate Story", command=lambda: final(Newmain_screen,  Adj_entry.get(), Your_entry.get(), Appliance_entry.get(), Adj2_entry.get(), Slang_entry.get(), Place_entry.get(),  Adj3_entry.get(), Plural_entry.get(), Movement_entry.get(), Transitive_entry.get(), Famous_entry.get(), Adverb_entry.get()))
    generate_button.pack()

#initialize main window
main_screen =  Tk() #root window
main_screen.title("Mad Libs Generator")
main_screen.geometry('400x400')
main_screen.config(bg='white')

#Image
image_path = "Happy.png"
img = Image.open(image_path)
img_resized = img.resize((160, 160), Image.LANCZOS)  # Resize
tkimage = ImageTk.PhotoImage(img_resized) #required for tkinter
img_label = Label(main_screen, image=tkimage) # Create a label widget to display the image
img_label.place(x=120, y=60)  # Adjust the coordinates as needed

#main title
nameLabel = Label(main_screen, text="Mad Libs Generator", bg="blue", fg="white")
nameLabel.place(relx=0.5, rely=0, anchor="n")
nameLabel.config(font=("Arial", 24, "bold"))

#Main screen buttons for stories
story1_button = Button(main_screen, text='A Memorable Day', command=story1, bg='gray', fg='white', font=("Arial", 16, "bold"), borderwidth=10)
story1_button.place(relx=0.5, rely=.6, anchor="n")
story1_button.config(font=("Arial", 16, "bold"))

story2_button = Button(main_screen, text='AI Takes Over', command=story2, bg='gray', fg='white', font=("Arial", 16, "bold"), borderwidth=10)
story2_button.place(relx=0.5, rely=.8, anchor="n")
story2_button.config(font=("Arial", 16, "bold"))

mainloop()