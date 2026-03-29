function saveAppointment(){
    alert("Appointment Saved!");
}
function removeAppointment(){
    alert("Appointment Removed!");

}
function saveSteps(){
    let steps = document.getElementById("steps").ariaValueMax;
    document.getElementById("stepsResult").innerText = "Steps: " + steps;
}
function stratBreathing(){
    document.getElementById("breathText").innerText = "Inhale...Exhale...";
}
function saveTime(){
    alert("Medicine Reminder Saved!");
}
function clearTime(){
    alert("REminder Removed!");
}