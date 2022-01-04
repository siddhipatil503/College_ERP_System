import psycopg2
import tkinter
from tkinter import ttk




def initialize_database():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres", password="22620053", host="127.0.0.1", port="5432",
                                      database="college")
        cursor = connection.cursor()
        cursor.execute(open("D:\\SEM5\\DBMS\\PROJECT\\CollegeMGMT.sql","r+").read())

    except Exception as e:
        print("Error while connecting to PostgreSQL:", e)

    else:
        cursor.close()
        connection.close()
        print("Starting Database created")


class DisplayWindow:
    def __init__(self, items, query, heading) -> None:
        self.window = tkinter.Tk()
        self.window.title(heading)
        self.window.minsize(width=800, height=400)
        self.window.config(padx=150, pady=100)  # add padding

        operations_label = tkinter.Label(self.window, text=query, bg='red', fg='blue', font=("Comic Sans MS", 16, "bold"))
        operations_label.grid(column=0, row=1, pady=(0, 30), columnspan=100)

        for i in range(len(items)):
            for j in range(len(items[i])):
                tkinter.Label(
                    self.window,
                    text=items[i][j],
                    font=("Comic Sans MS", 12, "normal")
                ).grid(
                    column=j,
                    row=(2 + i),
                    pady=(0, 10),
                    padx=(15, 15),
                    sticky="W"
                )




initialize_database()

window = tkinter.Tk()
window.title("College ERP")
window.minsize(width=1000, height=800)
window.configure(background='black')

# window.config(padx=100, pady=50)
Font_tuple = ("Comic Sans MS",10, "bold")
####### Scrollbar stuff #########
main_frame = tkinter.Frame(window)
main_frame.pack(fill="both", expand=1)
main_frame.configure(background='black')

my_canvas = tkinter.Canvas(main_frame)
my_canvas.pack(side="left", fill="both", expand=1)
my_canvas.configure(background='black')
my_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
my_scrollbar.pack(side="right", fill="y")

my_canvas.configure(yscrollcommand=my_scrollbar.set,)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = tkinter.Frame(my_canvas)
second_frame.configure(background='black')
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
# scroll bar stuff ends

operations_label = tkinter.Label(second_frame, text="College ERP", foreground="red", bg='black',
                                 font=("Comic Sans MS", 24, "bold", "underline"))
operations_label.grid(column=2, row=1,
                      pady=(5, 30))  # to actually show the element on screen, my_label.pack(side="left") this works too

queries_label = tkinter.Label(second_frame, text="Custom queries", foreground="red",bg='black',
                              font=("Comic Sans MS", 20, "bold", "underline"))
queries_label.grid(column=0, row=2, columnspan=2, pady=(0, 10), padx=(15, 15))

options_label = tkinter.Label(second_frame, text="Options", foreground="red",bg='black',
                              font=("Comic Sans MS", 20, "bold", "underline"))
options_label.grid(column=3, row=2, pady=(0, 10), padx=(15, 15))

my_input = tkinter.Entry(second_frame, width="60",bg="black",fg="white",font = Font_tuple)
my_input.grid(column=1, row=3, columnspan=2, padx=(15, 15))


def execute_query(query):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres", password="22620053", host="127.0.0.1", port="5432",
                                      database="college")
        cursor = connection.cursor()

        cursor.execute(query)
        connection.commit()
        rows = cursor.fetchall()
        DisplayWindow(rows, query, "Result")

    except Exception as e:
        print("Error while connecting to PostgreSQL", e)

    else:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


def custom_query():
    input_text = my_input.get()
    execute_query(input_text)
    


execute_button = tkinter.Button(second_frame, text="Execute", command=custom_query, foreground='blue',bg='black',font = Font_tuple)
execute_button.grid(column=3, row=3)

print_database = [
    "Student",
    "Teacher",
    "Department",
    "Course",
    "Class",
    "Attendance",
    " Marks",
    "Student Course"
    "Assign",
    "Assign_Time",
]

print_database_sql = [
    "SELECT * FROM Student;",
    "SELECT * FROM Teacher;",
    "SELECT * FROM Dept;",
    "SELECT * FROM Course;",
    "SELECT * FROM Class;",
    "SELECT * FROM Attendance;",
    "SELECT * FROM StudentCourse"
    "SELECT * FROM  Marks;",
    "SELECT * FROM  Assign;",
    "SELECT * FROM  Assign_Time;",
]

start = 5
tkinter.Label(second_frame, text="Relations", foreground="red",bg='black',
              font=("Comic Sans MS", 20, "bold", "underline")).grid(column=1, row=4, pady=(30, 10))


def button_trigger3(idx):
    execute_query(print_database_sql[idx])


for query_idx3 in range(len(print_database)):
    tkinter.Label(
        second_frame,
        text=print_database[query_idx3],fg='white',bg="black",
        font=("Comic Sans MS", 12, "normal")
    ).grid(
        column=1,
        columnspan=2,
        row=(start + query_idx3),
        pady=(10, 10),
        padx=(30, 30),
    )
    tkinter.Button(second_frame, text="Show", foreground='blue',bg='black',font = Font_tuple,
                   command=lambda query_idx3=query_idx3: button_trigger3(query_idx3)).grid(column=3,
                                                                                           row=(start + query_idx3))

######################### Simple queries ################################

simple_queries = [
    "Select all the course names offered by the CSE department.(‘A001’).",
    "Display the details of all female students.",
    "Display details of teachers belonging to the Civil department.",
    "Display the section and class_id of classes belonging to the Electrical department.",
    "Display all marks related details of students who obtained an ‘S’ grade.",
    "Display all marks related details of students who scored more than 30/40."
]
simple_queries_sql = [
    "SELECT name FROM Course WHERE deptid='A001';",
    "SELECT * FROM Student WHERE sex='F';",
    "SELECT * FROM Teacher WHERE deptid='C001';",
    "SELECT section,class_id FROM Class WHERE deptid='E001';",
    "SELECT * FROM Marks WHERE grade='S';",
    "SELECT * FROM Marks WHERE marks_scored>=30;"
]

start += len(print_database) + 1
tkinter.Label(second_frame, text="Simple Queries", foreground="red",bg='black',
              font=("Comic Sans MS", 20, "bold", "underline")).grid(column=1, row=(start - 1), pady=(30, 10))


def button_trigger(idx):
    execute_query(simple_queries_sql[idx])


for query_idx in range(len(simple_queries)):
    tkinter.Label(
        second_frame,
        text=simple_queries[query_idx],fg='white',bg="black",
        font=("Comic Sans MS", 12, "normal")
    ).grid(
        column=1,
        columnspan=2,
        row=(start + query_idx),
        pady=(10, 10),
        padx=(30, 30),
    )

    tkinter.Button(second_frame, text="Execute", foreground='blue',bg='black',font = Font_tuple,
                   command=lambda query_idx=query_idx: button_trigger(query_idx)).grid(column=3,
                                                                                       row=(start + query_idx))

######################### Complex queries ################################

complex_queries = [
    "Display Usn, Name and Marks of the students enrolled in course 'Data Structures And Algorithms'",
    "Display the name of the teachers taking classes on Monday's along with the period and course details.",
    "Display NAME, USN details of students who attended CS201 on '11-10-2021'",
    "Display all details of students with failing grade in course Electrical department",
    "Find all courses taken by students in section A",
    
]

complex_queries_sql = [
    """select student.usn, student.name,marks.marks_scored
    from ( marks inner join student on student.usn=marks.student_id)
    where marks.course_id= 'CS201';""",
    """select teacher.name, assign_time.period, assign_time.day,assign.course
    from (( teacher inner join assign on assign.teacher=teacher.teacher_id )
    inner join assign_time on assign_time.assign_id=assign.id) where day='Monday';""",
    """select NAME,USN from student
    inner join attendance on student.usn=attendance.student_id 
    where attendance.date='2021-10-11' and attendance.course_id='CS201' and status='True';""",
    """select * from student 
    join marks on student.usn=marks.student_id
    where marks.grade='F' AND (student.classid='009' OR student.classid='010') ;""",
    """select course.name from course
    join StudentCourse on course.id=StudentCourse.course join student on student.usn=StudentCourse.Student
    where student.classid='001';""",
]

start += len(simple_queries) + 1
tkinter.Label(second_frame, text="Complex Queries", foreground="red",bg='black',
              font=("Comic Sans MS", 20, "bold", "underline")).grid(column=1, row=(start - 1), pady=(30, 10))


def button_trigger2(idx):
    execute_query(complex_queries_sql[idx])


for query_idx2 in range(len(complex_queries)):
    tkinter.Label(
        second_frame,
        text=complex_queries[query_idx2],fg='white',bg="black",
        font=("Comic Sans MS", 12, "normal")
    ).grid(
        column=1,
        columnspan=2,
        row=(start + query_idx2),
        pady=(10, 10),
        padx=(30, 30),
    )
    tkinter.Button(second_frame, text="Execute", foreground="blue",bg='black',font = Font_tuple,
                   command=lambda query_idx2=query_idx2: button_trigger2(query_idx2)).grid(column=3,
                                                                                           row=(start + query_idx2))

window.mainloop()
