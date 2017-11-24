/*
 * Created by Leo N. on 2017-08-03.
 */


$(document).ready(function () {
    NewsApi();
});


// Preparing the HTML
function NewsApi() {

    // Variables
    var apikey = 'f355c018b1474aef93c183aebcb3b845'; // get an API Key from 'https://newsapi.org'
    var req = new XMLHttpRequest();

    var news = document.getElementById('news');
    var index = 0;


    req.open('GET', 'https://newsapi.org/v2/top-headlines?sources=bbc-news,associated-press,abc-news,cbc-news,engadget,the-economist,the-guardian-au&apiKey=' + apikey);
    // What happens when the request loads...
    req.onload = function () {
        // console.log(JSON.parse(req.responseText));
        var parsedResponse = JSON.parse(req.responseText);
        var articles = parsedResponse.articles;
        var length = parsedResponse.articles.length;
        var main_source = parsedResponse.source;

        console.log("Number of articles: " + length);
        var article = "";
        var featuredContent = "";
        var featuredAuthor = "";
        var featuredSource = "";
        var link = "";
        var random = Math.round(Math.random() * (length - 1) + 1);

        if (random > length) {
            // console.log(random);
            random = Math.round(Math.random() * (length - 1) - 1);
            if (articles[random].author === "") {
                random = Math.round(Math.random() * (length - 1) / 2);
            }
        }

        for (index; index < length; index++) {
            article += '<div class="p-top-60 p-bottom-40">';
                 article += '<div class="blog-content">';
                    article += '<div class="col-md-9 mr-auto">';
                        article += '<p><span>'+ articles[index].source.id +'</span></p>';
                        article += '<a href="'+ articles[index].url +'" target="_blank">';
                            article += '<h1 class="p-bottom-10">'+ articles[index].title +'</h1>';
                        article += '</a>';
                        article += '<img class="img-fluid" src="'+ articles[index].urlToImage +'">';
                        article += '<div class="p-top-10">'+ articles[index].description +'</div>';
                    article += '</div>';
                 article += '</div>';
            article += '</div>';
        }

        news.innerHTML = article ;
    };
    req.send();

    var requestAPI = setInterval(NewsApi, 120000);
}



