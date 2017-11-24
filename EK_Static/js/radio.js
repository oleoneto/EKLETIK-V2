// radio.js
// Written by Leo N.


var RADIOLUZEIROS = "http://s11.myradiostream.com:14574/;stream";
var radio = document.getElementById('radioAudio');
var radiobutton = radio.parentElement;

var playingClass = "btn btn-danger";
var playingText = "Está a ouvir em directo";
var stoppedClass = "btn btn-success";
var stoppedText = "Ouvir em directo";


function PlayRadio(){
  if(radiobutton.className == stoppedClass){
       radio.play();
       radiobutton.className = playingClass;
       radiobutton.textContent = playingText;
  } else {
       radio.pause();
       radiobutton.className = stoppedClass;
       radiobutton.textContent = stoppedText;
  }
}//end PlayRadio








function AppendSource(){
    var audios = document.getElementsByTagName('radio');
    for(var i = 0, len = audios.length; i < len; i++){
        audios[i].src = RADIOLUZEIROS;
        // Debugging...
        // console.log(audios[i].src);
    }
}//end AppendSource