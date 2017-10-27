/*
playMe.js
Written by Leo N.

Adapted from:
http://stackoverflow.com/questions/27368778/
how-to-toggle-audio-play-pause-with-one-button-or-link

*/

// 1. Start here...
var playButton;
var paused = true;
var song;


/*
2. Second...
    originId is the id of the audio we just clicked
    song is the element with the specified contatenated id
    if the audio is playing, pause it and change the icon from pause to play
    else, play it. Then, change the button icon from play to pause
*/
function togglePlay(originId){
  song = document.getElementById("faixa-"+originId);
  playButton = song.parentElement;

  if (playButton.className === "btn black fa fa-pause") {
    paused = true;
    playButton.className = "btn black fa fa-play";
    song.pause();
  } else {
    paused = false;
    StopTracks(originId);
    playButton.className = "btn black fa fa-pause";
    song.play();
    //StopAudio(originId);
  }
}//end togglePlay


/*
3. Stop all here...
    originId is the id of the audio just clicked
    audios is an array of all audio elements on the page
    len, in the for-loop, is for the length of the array
    in the if statement all audio is paused (as long as it is not the audio that we clicked on)
*/
function StopTracks(originId){
    var audios = document.getElementsByTagName('audio');
    for(var i = 0, len = audios.length; i < len;i++){
        if (audios[i]) {
            if(audios[i].id != originId) {
                audios[i].pause();
            }
            if(audios[i].parentElement.className != "btn pale fa fa-check") {
                audios[i].parentElement.className = "btn black fa fa-play";
            }
            // Debugging...
            // console.log(audios[i].parentElement);
        }
    }
}//end StopTracks


// 4. Stop just-played track...
function StopAudio(originId) {
    var button = document.getElementById(originId);
    playButton.className = "btn pale fa fa-check";
}


function GetCurrentTime(e) {
    var el = e;
    console.log(el.currentTime);
    var time = setInterval(GetCurrentTime(el), 3000);
}