from flask import Flask,render_template,request,redirect,session
import sqlite3
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)
@app.route("/")
def home():
     return render_template("index.html")

app.secret_key ="elder_app_secret_123"
@app.route('/register',methods=['GET','POST'])
def register():
     if request.method=='POST':
          username = request.form['username']
          password = request.form['password']
          conn = sqlite3.connect("elder.db")
          cursor = conn.cursor()
          cursor.execute("INSERT INTO users(username,password) VALUES(?,?)",(username,password))
          conn.commit()
          conn.close()
          return redirect('/login')
     return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
     if request.method =='POST':
          username = request.form['username']
          password = request.form['password']
          conn = sqlite3.connect("elder.db")
          cursor = conn.cursor()
          user = cursor.execute("SELECT *FROM users WHERE username=? AND password=?",(
               username,password)).fetchone()
          conn.close()
          if user:
               session['user'] = username
               return redirect('/')
          else:
               return "Invalid logic"
     return render_template('login.html')

@app.route('/logout')
def logout():
     session.pop('user',None)
     return redirect('/login')
          
#---------------DATABASE--------
def init_db():
     conn = sqlite3.connect("elder.db")
     cursor = conn.cursor()
     #medicine:
     cursor.execute("""CREATE TABLE IF NOT EXISTS medicines (
                    id INTEGER PRIMARY KEY,
                    name TEXT, time TEXT)
                     """)
     #users:
     cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,username TEXT,
                    password TEXT)
                    """)
     #appointments:
     cursor.execute("""CREATE TABLE IF NOT EXISTS appointments(
                    id INTEGER PRIMARY KEY,
                    doctor TEXT ,date TEXT)""")
     conn.commit()
     conn.close()
#---------------ADD MEDICINES

@app.route('/add_medicine',methods =['POST'])
def add_medicine():
    name = request.form['name']
    time = request.form['time']
    conn = sqlite3.connect("elder.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medicines (name,time)  VALUES(?,?)",(name,time))
    conn.commit()
    conn.close()
    return redirect('/medicine')
#------------------SHOW MEDICINES
@app.route('/medicine')
def medicine():
     conn = sqlite3.connect("elder.db")
     cursor = conn.cursor()
     data = cursor.execute("SELECT * FROM medicines").fetchall()
     conn.close()
     return render_template("medicine.html",medicines= data)

#-----------APPOINTMENTS---------
@app.route('/add_appointment',methods = ['POST'])
def add_appointment():
     doctor = request.form['doctor']
     date = request.form['date']
     conn = sqlite3.connect("elder.db")
     cursor = conn.cursor()
     cursor.execute("INSERT INTO appointments(doctor,date) VALUES(?, ?)",
                    (doctor,date))
     conn.commit()
     conn.close()
     return redirect('/doctor')
@app.route('/doctor')
def doctor():
     conn = sqlite3.connect("elder.db")
     cursor = conn.cursor()
     data = cursor.execute("SELECT * FROM appointments").fetchall()
     conn.close()
     return render_template("doctor.html",appointments=data)

@app.route('/exercise')
def exercise():
     return render_template("exercise.html")

@app.route('/healthcare')
def healthtips():
     return render_template("healthcare.html")

@app.route('/video')
def video():
     return render_template('video.html')

@app.route('/emergency',methods=['POST'])
def emergency():
     lat = request.form['lat']
     lon = request.form['lon']
     print("Emergency Location:",lat,lon)
     return "EMERGENCY alert sent !"

#-----MEDICINE CHECK----
def check_medicines():
     conn = sqlite3.connect("elder.db")
     cursor = conn.cursor()
     meds = cursor.execute("SELECT name,time FROM medicines").fetchall()
     conn.close()
     print("Medicine Reminder:",meds)

#----------APPOINTMENT CHECK--------
def check_appointments():
     conn = sqlite3.connect("elder.db")
     cursor = conn.cursor()
     appointments = cursor.execute("SELECT doctor,date FROM appointments").fetchall()
     conn.close()
     print("Appointment Reminder:",appointments)
#-----SCHEDULER-------
scheduler = BackgroundScheduler()
scheduler.add_job(check_medicines,'interval',minutes=1)
scheduler.add_job(check_appointments,'interval',minutes=1)
scheduler.start()                                                               
if __name__ == "__main__":
   init_db()   
   app.run(host="0.0.0.0",port=5000,debug=True)