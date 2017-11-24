/**
 * Created by Leo N. on 2017-08-03.
 * Updated on September 13, 2017
 */


// Global variables...
var portfolio = 'https://ekletik.com/api/portfolio';
var galeria = document.getElementById('gallery');
var pedido = new XMLHttpRequest();
pedido.open('GET', portfolio);


$(document).ready( function () {

    //Onload...
    pedido.onload = function () {
        var dados = JSON.parse(pedido.responseText);
        prepararHTML(dados);
    };
    pedido.send();

});

// How to process the HTML
function prepararHTML(dados) {
    var galeriaTitle = "";
    var galeriaImg   = "";
    var galeriaDesc  = "";
    var galeriaFull  = "";

    if(dados.length > 0){
          for(var i=0; i < dados.length; i++) {
                if(dados[i]){
                  galeriaTitle += dados[i].title;
                  galeriaFull += '<div class="col-xs-12 col-sm-6 col-md-6 col-lg-4">';
                  galeriaFull += '<img class="padding img-fluid" src="' + dados[i].artwork + '">';
                  galeriaFull += '</div>';
           }
         }
    } else {
         galeriaTitle += "Sem dados do API";
         galeriaFull += '<div class="col-md-12">';
         galeriaFull += '<h1 class="text-center">404... Sem dados!</h1>';
         galeriaFull += '</div>';
    }
    galeria.insertAdjacentHTML('beforeend', galeriaFull);
}
