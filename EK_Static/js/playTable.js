/*
Language: JavaScript (JQuery)
A snipped of code for displaying a table of songs.
Clicking on a row displays the artwork of the album along with the name of the singer. Sorting works on all present fields.

Source: JavaScript Book
Edited by Leo Neto
Thursday July 20, 2017
*/


$(document).ready(function () {
  // Debugging...
  console.log('Loaded: album.js');

  // Getting all the songs on the page...
  var $songs = $(".song");

  // Click on the first element of the table when the page loads...
  HoverSong($songs[0]);

});


// ----------------------------------------------
function HoverSong(ref) {
  // The song element over which you hovered...
  var $song = ref;

  // Adding highlight to the track
  $($song).addClass('song-clicked').siblings().removeClass('song-clicked');

  // The id of the song element...
  var $song_id = ref.id;

  // The title of the song that was clicked
  var $song_title = ref.children[0];

  // The artist of the song that was clicked...
  var $song_artist = ref.children[1];

  // The album of the song that was clicked...
  var $song_album = ref.children[2];

  // Artwork displayed on the screen...
  var $artwork = $('#artwork');

  // The main header of the page, above the artwork
  var $page = $('#artistHeader')[0];

  // Replacing the header text...
  $page.textContent = $song_artist.innerText;

  // Replacing the artwork with images from Spotify Api...
  var $image = $("#album-"+ref.id);
  var imageSource = $image.attr('src');
  $('#artwork').attr('src', imageSource);
  $('#small-artwork').attr('src', imageSource);

  // Replacing the title of the HTML page...
  var $html_title = $('title').text();

  // Replacing the albumHeader....
  $('#albumHeader').html($song_album.innerText);

  // Debugging...
  // console.log($song_id);
  // console.log($artwork);

}; //end of HoverSong
// ----------------------------------------------