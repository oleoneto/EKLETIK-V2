/**************************************
 TITLE: helloWorld.js (LN)
 AUTHOR: Leo Neto (LN)
 CREATE DATE: 6 September 2017
 PURPOSE: Display an alert on the screen with javascript
 Based on an example from the Javascript and jQuery book by Jon Duckett
 Also inspired by the example on W3 Schools, (https://www.w3schools.com/js/tryit.asp?filename=tryjs_timing_clock)

 Adapted from a school assignment.
***************************************/

// Variables
// var timeOfDayArray = ["Bom dia, {{user.first_name}}", "Boa tarde, {{user.first_name}}", "Boa noite, {{user.first_name}}", "Hora de dormir, {{user.first_name}}"];
var timeOfDayArray = ["Bom dia!", "Boa tarde!", "Boa noite!", "Hora de dormir!"];
// Functions
// Takes the current time and returns an appropriate greeting.
function DefineTimeOfDay(currentTime){
  if (currentTime >= 22 ){
    greeting = timeOfDayArray[3];
  }
  else if (currentTime > 18){
    greeting = timeOfDayArray[2];
  }
  else if (currentTime >= 12){
    greeting = timeOfDayArray[1];
  }
  else if (currentTime >= 0){
    greeting = timeOfDayArray[0];
  }
  else {
    greeting = "Olá, ";
  }
  return greeting;
}


// Concatenates a zero to either the second or the minute for better presentation.
function ConcatenateZero(secondOrMinute) {
  if(secondOrMinute < 10){
    secondOrMinute = "0"+secondOrMinute;
  }
  return secondOrMinute;
}


// Writes the time on the screen along with a greeting corresponding to the time of the day...
// I am making use of setInterval to help load the part of the page that was written with the javascript from this file.
function WriteGreeting() {
  var greeting;
  var date = new Date();
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var seconds = date.getSeconds();
  minutes = ConcatenateZero(minutes);
  seconds = ConcatenateZero(seconds);
  var hellogreeting = DefineTimeOfDay(hours);
  $('#greeting').html(hellogreeting);
  $('#clock').html(hours + ':'+ minutes + ':'+ seconds);
  var tickingClock = setInterval(WriteGreeting, 1000);
}




// Loading the Javascript after the DOM has fully loaded...
// Future functionality: check if the alert has been shown. If so, do not display it anymore.
$(document).ready(function() {
  WriteGreeting();
});