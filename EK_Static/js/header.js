// Based on an example by Traversy Media
// Edited by Leo Neto
// September 10, 2017

$(document).ready(function () {
    var wrapper = $('#wrapper');
    var topLayer = $('#wrapper .top');
    var handle = $('.handle');
    var skew = 0;
    var delta = 0;
    if(wrapper.hasClass('skewed')){
        skew = 1000;
    }
    wrapper.on('mousemove', function(e) {
        delta = (e.clientX - window.innerWidth/2) * 0.5;
        handle.css("left", e.clientX+delta+'px');
        topLayer.css("width", e.clientX+skew+delta+'px');
    });
});