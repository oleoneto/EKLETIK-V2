/*

Language: JavaScript (JQuery)

A snipped of code for displaying a table of songs.
Clicking on a row displays the artwork of the album along with the name of the singer. Sorting works on all present fields.

Source: JavaScript Book
Edited by Leo Neto
Thursday July 20, 2017

*/

// Debugging...
console.log('Loaded: album.js');


/* Start here... */
var album_list = [
'http://is1.mzstatic.com/image/thumb/Music118/v4/dc/66/2f/dc662f3c-c1d4-9b1f-99c5-04f1dc11332a/source/600x600bb.jpg',
'http://is1.mzstatic.com/image/thumb/Music/v4/08/6c/12/086c12ca-2c96-38dd-bc39-504be1da8db8/source/600x600bb.jpg',

'http://is5.mzstatic.com/image/thumb/Music18/v4/f4/9d/8f/f49d8fff-b601-22f5-f6ff-c73c52bdb6ab/source/600x600bb.jpg',
'http://is4.mzstatic.com/image/thumb/Music111/v4/be/72/0d/be720d85-9f89-3fa5-5630-e11cf8737767/source/600x600bb.jpg',

'http://is3.mzstatic.com/image/thumb/Music71/v4/89/01/da/8901dab4-9c40-aff0-2608-c6b6f1717551/source/600x600bb.jpg',
'http://is2.mzstatic.com/image/thumb/Music7/v4/a7/07/c6/a707c6c4-6b12-1d6a-f92d-9814670d2000/source/600x600bb.jpg',

'http://is1.mzstatic.com/image/thumb/Music1/v4/35/38/7e/35387e3f-364b-dfad-5f32-852383900607/source/600x600bb.jpg',
'http://is4.mzstatic.com/image/thumb/Music7/v4/17/9a/2e/179a2ec1-9fe7-65dc-bab4-5d4126d5dad9/source/600x600bb.jpg',

'http://is3.mzstatic.com/image/thumb/Music91/v4/df/fb/ad/dffbad95-0927-6762-3baf-1018d7b0d149/source/600x600bb.jpg',
'http://is1.mzstatic.com/image/thumb/Music4/v4/2f/40/48/2f4048c5-3633-938e-dcbb-7ea3cbb38fb0/source/600x600bb.jpg',

'http://is4.mzstatic.com/image/thumb/Music2/v4/86/42/4a/86424aca-2248-1693-6a3e-9dde096b4eb9/source/600x600bb.jpg',
'http://is4.mzstatic.com/image/thumb/Music118/v4/2d/d4/3d/2dd43d3e-d6e2-ec63-e013-15bc258ef831/source/600x600bb.jpg'
];


// Getting all the songs on the page...
var $songs = $(".song");


function ClickedSong(ref) {
  // The song element that was clicked...
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

  //
  // var $copyright = $('#copyright').text();

  // Replacing the header text...
  $page.textContent = $song_artist.innerText;

  // Replacing the artwork with images from iTunes Api...
  var url = album_list[$song_id-1];
  $('#artwork').attr('src', url);

  // Replacing the title of the HTML page...
  var $html_title = $('title').text();
  // $('title').html($song_title.innerText + " by " + $song_artist.innerText);

  // Replacing the albumHeader....
  $('#albumHeader').html($song_album.innerText);

  // Debugging...
  // console.log($song_id);

};//end of ClickedSong




// Click on the first element of the table when the page loads...
ClickedSong($songs[0]);
// ClickedSong($songs[Math.random()]);
