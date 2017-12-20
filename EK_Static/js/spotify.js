/*
// ekos.css
// EKOS Visual Framework.
// EKOS is based on Bootstrap 4 and jQuery.
// Developed by Leo Neto on Dec 18, 2017.
// Ekletik Studios. Open-source License.
*/

var allSongs = $('audio');
var songIcons = $('button > i');
var pageTitle = document.getElementsByTagName('title');
var mainTitle = pageTitle[0].textContent;

// var audio = document.getElementById("song-b3");

$(document).ready(function() {
    console.log("Loaded spotify.js...");
    // console.log(audio);
    //ProcessEndedTrack(audio);
});


function PlayTrack(id) {
    var currentSong = document.getElementById("song-" + id);
    var currentButton = document.getElementById(id);
    var currentIcon = currentButton.children[0];
    var currentTitle = document.getElementById("title-"+id);
    currentTitle = currentTitle.textContent;
    var title = "Now Playing: " + currentTitle;

    // console.log(currentTitle);


    if (currentSong.paused === true) {
        currentSong.play();
        currentIcon.className = "fa fa-circle-o-notch fa-spin";
        UpdatePageTitle(title);
    } else {
        currentSong.pause();
        currentIcon.className = "fa fa-play";
    }

    StopTracks(currentSong, currentIcon, id);
}

function StopTracks(currentSong, currentIcon, id) {
    for (i = 0, len = allSongs.length; i < len; i++) {
        if (allSongs[i]) {
            if (allSongs[i] != currentSong) {
                allSongs[i].pause();
            }
            if (songIcons[i] != currentIcon){
                if (songIcons[i].className != 'fa fa-check'){
                    songIcons[i].className = 'fa fa-play';
                }
            }
        }
    }
}


function ProcessEndedTrack(el) {
    var currentButton = el.parentElement;
    var currentIcon = currentButton.children[0];
    currentIcon.className = "fa fa-check";
    UpdatePageTitle(mainTitle);
    // console.log(el.parentElement);
}

function UpdatePageTitle(title) {
  pageTitle[0].textContent = title;
  // console.log(pageTitle[0].textContent);
}