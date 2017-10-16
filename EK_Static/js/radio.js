// radio.js
// Written by Leo N.


var RADIOLUZEIROS = "http://s11.myradiostream.com:14574/;stream";
var song = document.getElementById('radioAudio');



function togglePlay(element){
  console.log(element);
  var i = element.children;
  var audio = i[0];
  console.log(audio);
   if(element.className == 'btn btn-default white'){
       audio.play();
       element.className = 'btn btn-warning';
       element.textContent = 'Está a ouvir em directo';
   } else {
       audio.stop();
       element.className = 'btn btn-default white';
       element.textContent = 'Ouvir em directo';
   }
}//end togglePlay








function AppendSource(){
    var audios = document.getElementsByTagName('audio');
    for(var i = 0, len = audios.length; i < len; i++){
        audios[i].src = RADIOLUZEIROS;
        // Debugging...
        // console.log(audios[i].src);
    }
}//end AppendSource