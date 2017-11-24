/**
 * Created by Leo N. on 2017-08-03.
 * Updated on September 13, 2017
 */

// Global variables...
var audios = 'https://ekletik.com/api/audios';
// var audios = 'http://127.0.0.1:8089/api/audios';
var sonzito = document.getElementById('sonzito');
var pedido = new XMLHttpRequest();
pedido.open('GET', audios);


$(document).ready( function () {

    console.log(pedido);

    //Onload...
    pedido.onload = function () {
        var dados = JSON.parse(pedido.responseText);
        prepararHTML(dados);
    };
    pedido.send();

});

// How to process the HTML
function prepararHTML(dados) {
    var audiosource = "";

    if(dados.length > 0){
          for(var i=0; i < dados.length; i++) {
                if(dados[i]){

                  audiosource += '<tr class="audio-item">';
                    audiosource += '<th scope="row">'+ dados[i].id +'</th>';
                    audiosource += '<th>'+ dados[i].title +'</th>';
                    audiosource += '<th class="text-center">';
                        audiosource += '<button id="'+ dados[i].id +'" class="btn black fa fa-play" type="button" onclick="togglePlay(this.id)">';
                            audiosource += '<audio id="faixa-'+ dados[i].id +'" class="audio" src="'+dados[i].source+'" onended="StopAudio(this.parentElement.id)" onplaying="GetCurrentTime(this)"></audio>';
                        audiosource += '</button>';
                    audiosource += '</th>';
                  audiosource += '</tr>';
           }
         }
    } else {
         audiosource += '<tr class="audio-item">';
         audiosource += '<th scope="row">0</th>';
         audiosource += '<th>No data</th>';
         audiosource += '<th class="text-center">No data</th>';
         audiosource += '</tr>';
    }
    sonzito.insertAdjacentHTML('beforeend', audiosource);
}
