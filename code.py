import csv
import tkinter as tk
from tkinter import LEFT, W, messagebox
import matplotlib.pyplot as plt
import random

books_path = 'books.csv'

with open(books_path, "r") as csv_file:
    var=csv.reader(csv_file)
    l=[]
    for i in var:
        l.append(i)

def destroy():
    root.destroy()

def unique_l(l):
    '''this function returns a list of all the genres available to a user'''
    ans=[]
	#ityerating through all the values of list
    for i in range(1,len(l)):
	#adding genre to a list if genre was not there in the list
        if l[i][5] not in ans:
            ans.append(l[i][5])
    ans.append("Maybe, IDK")
    return ans

def unique_author(l):
    '''this function returns a list of all authors available'''
    ans=[]
    for i in range(1,len(l)):
	#if name of author is not there in the list then it appends author name
        if l[i][1] not in ans:
            ans.append(l[i][1])
    ans.append("Something")
    return ans

def func():
    '''Entering into the csv'''
    new_window = tk.Toplevel()
    new_window.geometry("200x450")
    new_window.resizable(False,False)
    name = tk.StringVar()        
    author = tk.StringVar()
    language = tk.StringVar()
    year = tk.StringVar()
    sales = tk.StringVar()
    genre = tk.StringVar()
	#initialing entry variables in all of the above lines

    def input_func():
        '''this function can take input of book from the user and add book to the data of csv file'''

        messagebox.showinfo("Confirmation Box","You have successfully entered values into the csv file.")
        l=([name.get(), author.get(), language.get(), year.get(), sales.get(), genre.get()])
        with open(books_path,'a') as csv_file:
            W=csv.writer(csv_file)
            W.writerow(l)

	#creating entry widgets
    l1=tk.Label(new_window, text="Enter book name").pack()
    entry_name = tk.Entry(new_window, textvariable=name).pack()
    l2=tk.Label(new_window, text="\nEnter author name").pack()
    entry_author = tk.Entry(new_window, textvariable= author).pack()
    l3=tk.Label(new_window, text="\nEnter language").pack()
    entry_language = tk.Entry(new_window, textvariable = language).pack()
    l4=tk.Label(new_window, text="\nEnter publishing year").pack()
    entry_year = tk.Entry(new_window, textvariable = year).pack()
    l5=tk.Label(new_window, text="\nEnter sales").pack()
    entry_sales = tk.Entry(new_window, textvariable = sales).pack()
    l6=tk.Label(new_window, text="\nEnter genre").pack()
    entry_genre = tk.Entry(new_window, textvariable = genre).pack()

    button = tk.Button(new_window, text="Input into csv", command = input_func).pack(pady=10)
    button_quit = tk.Button(new_window, text="Quit the program", command = destroy).pack(pady=5)

def recom():
    window_recom= tk.Toplevel()
    window_recom.geometry("275x150")

    def recom_func():
        '''this function is our recommandation algorithm which will use the previous user data and recommand the books based on the previous user choice'''
        user=username.get()+".csv"

        f=open(user, "a")
        f.close()

        with open(user, "r") as csv_file:
		#opening the csv file which contains the data of books
            var1=csv.reader(csv_file)
            k=[]
            for i in var1:
                k.append(i[0])

            if len(k)==0:
		#if the previous record of the user is empty then top5 best selling books will be recommanded, else it choose any genre from the database of the user and will recommand other genres based on the genre
                for i in range(1,6):
                    k.append(l[i][0])
                textrecom1=''
                ke=[]
                for i in k:
                    textrecom1= textrecom1+i+"\n"
                    ke.append([i])

                recom_window= tk.Toplevel()
                recom_window.geometry("300x200")
                label_title = tk.Label (recom_window, text="Recommended books are ", font = ("Arial", "13")).pack()
                recom_label=tk.Label(recom_window, text=textrecom1, justify=tk.LEFT).pack(anchor=tk.W, padx = 5, pady = 6)
                recom_close = tk.Button(recom_window, text = "Close the program",width = 25, command=destroy).pack()

                with open(user, "a") as csv_file:
                    write_csv = csv.writer(csv_file)
                    for j in ke:
                        write_csv.writerow(j)


            else:
                samplebook=k[random.randint(0,len(k)-1)]
                for i in l:
                    if(i[0]==samplebook):
                        samplegenre=i[5]
                        break
                dicts={"Mystery":["Thriller","Horror"],"Thriller":["Mystery","Horror"],"Horror":["Mystery","Thriller"],
       "Novel":["Historical Novel","Biographical Novel","War Novel"],"Historical Novel":["Biographical Novel","War Novel","Novel"],"Biographical Novel":["War Novel","Novel","Historical Novel"],
       "War Novel":["Crime Novel","Coming Of Age"],"Coming Of Age":["Crime Novel","War Novel"],"Crime Novel":["War Novel","Coming Of Age"],
       "Erotica":["Sexology","Romance","Pregnancy Guide"],"Sexology":["Erotica","Romance","Pregnancy Guide"],"Romance":["Erotica","Romance Novel","Young Adult Fiction","Pregnancy Guide"],
       "Romance Novel":["Romance","Young Adult Fiction"],"Young Adult Fiction":["Romance","Romance Novel"],
       "Children's Fiction":["Children's Novel","Children's Literature"],"Children's Literature":["Children's Novel","Children's Fiction"],"Children's Novel":["Children's Fiction","Children's Literature"],
       "Autobiograhy":["Biographical Novel","Memoir"],"Biographical Novel":["Autobiograhy","Memoir"],"Memoir":["Biographical Novel","Autobiograhy"],
       "Fiction":["Science Fiction","Historical Fiction","Popular Science","Fantasy"],"Historical Fiction":["Historical Novel","Science Fiction","Fiction","Fantasy"],"Science Fiction":["Historical Fiction","Popular Science","Fantasy","Fiction"],"Popular Science":["Science Fiction","Fiction","Fantasy"],"Fantasy":["Science Fiction","Historical Fiction","Popular Science"],"Historical Novel":["Historical Fiction"],
       "Social Science":["Self-Help", "Family Saga"],"Self-Help":["Social Science", "Family Saga"], "Family Saga":["Self-Help", "Social Science"],
       "Literature":["Travel Literature","Historical Literature","Christian Literature"],"Historical Literature":["Literature","Historical Novel","Travel Literature"],"Travel Literature":["Literature","Historical Literature"],"Christian Literature":["Historical Literature"],
       "Pregnancy Guide":["Romance","Children's Literature","Children's Picture Book"],
       "Children's Picture Book":["Children's Fantacy Novel","Children's Fiction"],"Children's Picture Book":["Children's Fantacy Novel","Children's Fiction"],"Children's Fantacy Novel":["Children's Picture Book","Children's Fiction"]}
	#this dictionary will provide the genre which will be used for furthur recommandation
                
                recomlist=dicts[samplegenre]
                recomgenre=recomlist[random.randint(0,len(recomlist)-1)]
                ri=[]
                for i in l:
                    if(i[5]==recomgenre):
                        ri.append(i[0])    

                if(len(ri)<=5):
                    ri=ri
                else:
                    ri=ri[0:4]
                textrecom=''
                rie=[]
                for i in ri:
                    textrecom=textrecom+i+"\n"
                    rie.append([i])

                recom_window= tk.Toplevel()
                recom_window.geometry("300x200")
                label_title = tk.Label (recom_window, text="Recommended books are ", font = ("Arial", "13")).pack()
                recom_label=tk.Label(recom_window, text=textrecom, justify=tk.LEFT).pack(anchor=tk.W, padx = 5, pady = 6)
                recom_close = tk.Button(recom_window, text = "Close the program",width = 25, command=destroy).pack()


                with open(user, "a") as csv_file:
                    write_csv = csv.writer(csv_file)
                    for j in rie:
                        write_csv.writerow(j)

    def recom_manual():
        user = username.get() + ".csv"

        window_genre = tk.Toplevel()
        window_genre.geometry("500x400")
        window_genre.resizable(False,False)

        main_frame = tk.Frame(window_genre)
        main_frame.pack(fill=tk.BOTH, expand = True)

        my_canvas = tk.Canvas(main_frame)
        my_canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True )
	#a canvas in which the scrollbar will fit
        my_scrollbar = tk.Scrollbar(main_frame, orient= tk.VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
	#this makes the scrollbar

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind("<Configure>", lambda event: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = tk.Frame(my_canvas)

        my_canvas.create_window((0,0), window = second_frame, anchor = "nw")
	#this whole above thing is for making the scrollbar in the desired window we want here it is for window_genre which contents list of all the genre

        def func1():
            "'To get radiobuttons of genre'"

            label = radio_genre.get()
            radio_author = tk.StringVar()

            def func2(genre):
                "'For getting radiobuttons of author'"
                label1 = radio_author.get()
                n_book=[]
                n_sales=[]
		#this all if ,else will take care of all the cases in which the user can choose any genre or none and any author or none
                if label1 != "Something" and genre!='Maybe, IDK':
		#if any genre and author are selected
                    for i in range(len(l)):
                        if(l[i][1]==label1 and l[i][5]==genre):
                            n_book.append(l[i][0])
                            n_sales.append((int(l[i][4]))/10**6)

                elif(genre!='Maybe, IDK' and label1=='Something'):
		#if any genre and none author are selected
                    for i in range(1,len(l)):
                        if(l[i][5]==genre):
                            n_book.append(l[i][0])
                            n_sales.append((int(l[i][4]))/10**6)
        
                elif(genre=='Maybe, IDK' and label1!='Something'):
		#if none genre and any author are selected
                    for i in range(1,len(l)):
                        if(l[i][1]==label1):
                            n_book.append(l[i][0])
                            n_sales.append((int(l[i][4]))/10**6)

                else:
		 #if none genre and none author are selected
                    for i in range(1,len(l)):
                            n_book.append(l[i][0])
                            n_sales.append((int(l[i][4]))/10**6)

                books=""
                list_book = []
                for i in n_book:
                    books=books+i+"\n"
                    list_book.append([i])
            
                window2= tk.Toplevel()
                window2.geometry("500x250")
                main_frame = tk.Frame(window2)
                main_frame.pack(fill=tk.BOTH, expand = True)

                my_canvas = tk.Canvas(main_frame)
                my_canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True )
		#a canvas in which the scrollbar will fit

                my_scrollbar = tk.Scrollbar(main_frame, orient= tk.VERTICAL, command = my_canvas.yview)
                my_scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
		#this makes the scrollbar

                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind("<Configure>", lambda event: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

                second_frame = tk.Frame(my_canvas)
		#this whole above thing is for making the scrollbar in the desired window we want here it is for window1 which contents list of all the authors


                my_canvas.create_window((0,0), window = second_frame, anchor = "nw")
                label_books = tk.Label(second_frame, text="Books according to your selection(" + genre+" - "+label1+ ") are", font=("Arial", "11")).pack(padx=35, pady =10)
                new = tk.Label(second_frame, text = books, justify=tk.LEFT).pack(anchor=tk.W, padx =6)
                button_quit = tk.Button(second_frame, text="To quit the program", command=destroy).pack(padx=40, pady =10)

                fig=plt.figure()
                #plotting graph of n_books and n_sales
                plt.plot(n_book,n_sales)
                #setting label
                plt.ylabel('Books sold in millions')
                #setting title
                plt.title('BOOKS SOLD BY GENRE AND AUTHOR')
                #rotating x ticks
                plt.xticks(rotation=30)
                #displaying plot
                plt.show()

                f=open(user, "a")
                f.close()
                
                with open(user, "a") as csv_file:
                    write_csv = csv.writer(csv_file)
                    for j in list_book:
                        write_csv.writerow(j)

            window1=tk.Toplevel()
            window1.geometry("500x200")
            main_frame = tk.Frame(window1)
            main_frame.pack(fill=tk.BOTH, expand = True)

            my_canvas = tk.Canvas(main_frame)
            my_canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True )
		#a canvas in which the scrollbar will fit
            my_scrollbar = tk.Scrollbar(main_frame, orient= tk.VERTICAL, command = my_canvas.yview)
            my_scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
		#this makes the scrollbar
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind("<Configure>", lambda event: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
		#a canvas in which the scrollbar will fit

            second_frame = tk.Frame(my_canvas)
		#this whole above thing is for making the scrollbar in the desired window we want here it is for window1 which contents list of all the authors

            my_canvas.create_window((0,0), window = second_frame, anchor = "nw")
		#this whole above thing is for making the scrollbar in the desired window we want here it is for window_genre which contents list of all the genre
            if label != "Maybe, IDK":
                author = []
                for i in l:
                    if label == i[5]:
                        if i[1] not in author:
                            author.append(i[1])
                author.append("Something")
                label_author = tk.Label(second_frame, text = "List of available authors of genre " + label, font= ("Arial", "13")).pack(padx =55, pady = 10)

                for i in author:
		#to get list of all authors in form of radiobuttons if user chooses none of the genres
                    textm=str(i)
                    text1=tk.Radiobutton(second_frame, text=textm, variable = radio_author, value = i)
                    text1.pack(anchor=tk.W, padx=4)

                enter_author = tk.Button(second_frame, text="Enter the value", command =lambda: func2(label), width =25).pack(padx =55, pady =20)

            else:
                label_author = tk.Label(second_frame, text = "List of available authors of all genres", font= ("Arial", "13")).pack(padx =75, pady = 10)
                for i in unique_author(l):
		#to get list of all authors of the respective genre choosen by the user in form of radiobuttons
                    textm=str(i)
                    text1=tk.Radiobutton(second_frame, text=textm, variable = radio_author, value = i)
                    text1.pack(anchor=tk.W, padx = 4)

                enter_author = tk.Button(second_frame, text="Enter the value", command =lambda: func2(label), width =25).pack(padx= 75, pady =20)
		#Button to select the desired author and move to the next window



        genre_label = tk.Label(second_frame, text="List of available Genres", font =("Arial", "13")).pack(pady=10, padx= 150)
        radio_genre = tk.StringVar()
	#variable for storing the selected genre

        for i in unique_l(l):
	#to get list of all genres in form of radiobuttons'''
            textm=str(i)
            text1=tk.Radiobutton(second_frame, text=textm, variable = radio_genre, value = i)
            text1.pack(anchor=tk.W, padx= 4)

        enter_genre = tk.Button(second_frame, text="Enter the value", command = func1, width = 25).pack(padx = 150, pady =20)



    username = tk.StringVar()
    label_username = tk.Label(window_recom, text = "Enter your username", font = ("Arial", "12")).pack(pady= 3)
    entry_username = tk.Entry(window_recom, textvariable=username, width =28).pack()
    enter_recom = tk.Button(window_recom, text="For Automatic Recommendation", command=recom_func, width =25).pack(pady= 10)
    enter_manual = tk.Button(window_recom, text = "For Manual Recommendation", command=recom_manual, width = 25).pack()




root = tk.Tk()
root.title("Book Recommendation System")
root.geometry("310x150")
root.resizable(False,False)

main_label = tk.Label(root, text = "Book Recommendation System", font=("Arial", "15", "bold italic")).pack(pady=12)
#Button to select the desired genre and move to the next window
enter_button = tk.Button(root, text="To enter into csv", command = func, relief=tk.RAISED, width = 25).pack(pady=8)
#Button to go to a window where the user can add new books to the existing list.
enter_bookrecom = tk.Button(root, text="To get book recommendation", command=recom, relief=tk.RAISED, width= 25).pack()
#button to get the recommandation of list by using previous user data 
root.mainloop()
