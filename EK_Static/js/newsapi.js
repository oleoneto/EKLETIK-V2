/*
 * Created by Leo N. on 2017-08-03.
 */


function NewsApi() {

// Variables
    var apikey = 'f355c018b1474aef93c183aebcb3b845'; // get an API Key from 'https://newsapi.org'
    var req = new XMLHttpRequest();

    var news = document.getElementById('news');
    var featuredTitle = document.getElementById('main-title');
    var featuredDesc = document.getElementById('main-desc');

    var author = document.getElementById('author');
    var source = document.getElementById('source');
    var index = 0;


req.open('GET', 'https://newsapi.org/v1/articles?source=bbc-news&apiKey=' + apikey);
    // req.open('GET', 'https://newsapi.org/v1/articles?source=the-guardian-uk&sortBy=top&apiKey=' + apikey);

// Onload...
    req.onload = function () {
console.log(JSON.parse(req.responseText));
        var parsedResponse = JSON.parse(req.responseText);
        var articles = parsedResponse.articles;
        var length = parsedResponse.articles.length;
        var main_source = parsedResponse.source;

// console.log("Number of articles: " + length);
        var article = "";
        var featuredContent = "";
        var featuredAuthor = "";
        var featuredSource = "";
        var random = Math.round(Math.random() * (length - 1) + 1);

        if (random > length) {
            // console.log(random);
            random = Math.round(Math.random() * (length - 1) - 1);
            if (articles[random].author === "") {
                random = Math.round(Math.random() * (length - 1) / 2);
            }
        }

        for (index; index < length; index++) {
            article += '<tr>';
            article += '<td>' + (index + 1) + '</td>'; // Row index
            article += '<td><a href="'+articles[index].url+'">' + articles[index].title + '</a><td>'; // Headline...
            article += '<td>' + articles[index].author + '<td>'; // Source...
            article += '</tr>';

            featuredContent = articles[random].description;
            featuredAuthor = articles[random].title;
            featuredSource = main_source;
        }

        news.insertAdjacentHTML('beforeend', article);
        featuredTitle.innerText = featuredAuthor;
        featuredDesc.innerText = featuredContent;

        //author.innerText = featuredAuthor;
        //source.innerText = featuredSource;
    };
    req.send();

    var requestAPI = setInterval(NewsApi, 60000);
}

NewsApi();