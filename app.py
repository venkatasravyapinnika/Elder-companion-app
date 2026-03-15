from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/medicine')
def medicine():
     return """
     <h2>Medicine Reminder</h2>
     <p>Set the time to take your medicine (only once):</p>

     <input type = "time" id="medtime">
     <button onclick="saveTime()">Save Reminder</button>
     <button onclick="clearTime()">Remove Time</button>
     <br><br>
     <a href="/">Back to Home</a>
     <script>
     function saveTime(){
     var time =document.getElementById("medtime").value;
     localStorage.setItem("medicine_time",time);
     alert("Medicine reminder saved at " + time);
     }
     function clearTime(){
     document.getElementById("medtime").value="";
     localStorage.removeItem("medicine_time");
     alert("Medicine reminder removed");
     }
     function checkReminder(){
        var savedTime=localStorage.getItem("medicine_time");
        if(savedTime){
        var now = new Date();
        var hours = now.getHours().toString().padStart(2,'0');
        var minutes= now.getMinutes().toString().padStart(2,'0');
        var current = hours + ":" + minutes;
          if(current==savedTime){
          alert("💊Time to take  your medicine !");
          var audio = new Audio("https://www.soundjay.com/buttons/sounds/beep-07.mp3");
          audio.loop = true;
          audio.play();
        }

        }
     }
     setInterval(checkReminder,60000);
     </script>
    """
@app.route('/doctor')
def doctor():
     return"""
     <h2>Doctor Appointment</h2>
     <p>Set your doctor appointment:</p>
     Appointment Date:<br>
     <input type ="date" id="date"><br><br>
     Appointment Time:<br>
     <input type="time" id="time"><br><br>
     <button onclick = "saveAppointment()">SaveAppointment</button>
     <button onclick="removeAppointment()">RemoveAppointment</button>
     <br><br>
     <a href="/">Back to Home</a>
     <script>
     function saveAppointment(){
     var date = document.getElementById("date").value;
     var time = document.getElementById("time").value;
     localStorage.setItem("appointment_date", date);
     localStorage.setItem("appointment_time", time);
     alert("Doctor appointment saved on" + date + "at" + time);
     }
     function removeAppointment(){
     localStorage.removeItem("appointment_date");
     localStorage.removeItem("appointment_time");
     alert("Appointment removed");
     }
     function checkDoctorReminder(){
     var savedDate = localStorage.getItem("appointment_date");
     var savedTime = localStorage.getItem("appointment_time");
     if(savedDate && savedTime){
     var now = new Date();
     var today = now.toISOString().split("T")[0];
     var hour = now.getHours().toString().padStart(2,'0');
     var minutes = now.getMinutes().toString().padStart(2,'0');
     var currentTime = hours + ":" + minutes;
     if (today === savedDate && curentTime ===savedTime){
     alert("🔔Time for your doctor appointment!");
     var audio = new
     audio("https://www.soundjay.com/buttons/sounds/beep-07.mp3");
     audio.loop = true;
     audio.play();
            }
        }
     }
     setInterval(checkDoctorReminder, 60000);
     
     </script>
     """


@app.route('/exercise')
def exercise():
     return """
    <h2>Healthy Activities for Elderly</h2>
    <h3>🚶 Walking</h3>
    <p>walk for 15-20 minutes daily to improve circulation and joint mobility.</p>
    <h3>🫁 Breathing Exercise</h3>
    <p>slow deep breathing for 5 minutes helps lung capacity and relaxation.</p>
    <h3>❤️ Heart Tracking </h3>
    <p>normal resting heart rate: 60-100 BPM.</p>
    <br>
    <a href="/">Back to Home</a>
    """

@app.route('/healthcare')
def healthtips():
     return"""
    <h2>🩺 Health Tips for Elderly</h2> 
    <ul>
    <li>💧 Drink enough water</li>
    <li>🚶‍♂️ walking daily</li>
    <li>💊 Take medicines on time</li>
    </ul>
    <a href="/">Back</a>
    """
                                                                                                                       
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
