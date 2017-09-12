
$(function() {
  var $gallery = $('#gallery');
  var $gallery_divs = $('#gallery div');
  var $gallery_anchors = $('#gallery a');
  var $gallery_images = $('#gallery img');
  var $buttons = $('#buttons');
  var tagsArray = {};

  $gallery_images.each(function(){
    var single_image = this;
    var single_image_div = this.parentElement;
    var single_image_anchor = single_image_div.parentElement;
    var tags = $(this).data('tags');

    if(tags){
        tags.split(',').forEach(function(tagName){
          if(tagsArray[tagName] == null){
            tagsArray[tagName] = [];
          }
          tagsArray[tagName].push(single_image_anchor);
        });
    }
});

// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================
// ======================================


// Create a button with the ability to show ALL images.
// In the event of a click, make the button active, make the other buttons inactive.
// Make the button able to show the gallery.

$('<button/>', {
  text: 'Todos',
  class: 'btn btn-active',
  click: function(){
    $(this).addClass('btn-active').siblings().removeClass('btn-active');
    $gallery_anchors.show();
  }
}).appendTo($buttons);

// Get each tag name and create a button with the given text.
// In the event of a click, make the button active and the others inactive.
// Show the images under the clicked tag.
$.each(tagsArray, function(tagName) {
  $('<button/>',{
    text: tagName,
    class: 'btn',
    click: function(){
      $(this).addClass('btn-active').siblings().removeClass('btn-active');
      $gallery_anchors.hide().filter(tagsArray[tagName]).show();
    }
  }).appendTo($buttons);
});

}());
// C'est fini




// Blurry images
$(function(){
  var $gallery = $("#gallery");
  var $gallery_images = $('.gallery-item img');
  var gallery = document.getElementById('gallery');
  var divs = gallery.children;
  var $divs = gallery.children;
  var count= divs.length;
  var imgs = {};
  var i;


  for (i in divs){
    divs[i].onmouseover = function(){
      // console.log(this);
    }
  }

}); //end function...
