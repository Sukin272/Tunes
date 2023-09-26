[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/uO3FBJhb)
# project-ok_17

There is navigation bar on top of each webpage containing link to home, artists and about us page. Hence you can open any html file and go to any webpage of the website. 

src/home.html leads you to the home page with all top charts.

src/artists.html leads you to the artists page listing all the artists.

src/about.html is the about us page. It can be accessed from both the header and the footer.

src/album, src/album2, src/album3, ... are the pages that list the albums of each artist can be accessed through artists page.

src/music01, src/music02, ... are all the pages that list the songs of 25 albums from different artists. These can be accessed by clicking on the respective album.

src/images/ contains all the images that are used in the entire website. 

Artist's images are named with the name of the artist.

Album images are named starting with Al- and then shorthand for the artist of that album followed by the name of the album.

Some songs that have images are named S-"song name".

There are 5 css files each associated with home, about us, artist, album, music.

All the Albums and all the music pages share the same css files i.e. album.css and music.css. 

Phase 3:

To run the website , we should run the app.py file in the src folder and click on the link which is provided. All the images,css files and js files are in images folder,css folder and js folder in static folder respectively and templates folder contains all the html files. 

All the songs in music01-music25 pages have the add to playlist option, and clicking it adds the song to the playlists page which can be accessed in the navbar, through its unique value given by the number xy, where x represents the music page name , 1-25, and y represents the sl no of the songs in it . Ex. value of 37 , represents ,3rd page's 7th song.

Playlist page , contains all the songs which have been added , and it stores it in ascending order with respect to the value.We can delete the song from the playlist by cicking on the delete button next to it.

Spotlight page has the feature by which we can give our reviews , ratings about Ed Sheeran and also displays a countdown to Ed Sheeran's next album.

Search page has a Search bar linked to Itunes API. This uses fetch to get data from Itunes API and displays a max of 10 items. There are filters related to showing only non explicit result and also related to duration of the song. We can also play the preview of the song directly from the result. 

```
.
├── ASSUMPTIONS.md
├── README.md
└── src
    ├── app.py
    ├── music.db
    ├── static
    │   ├── css
    │   │   ├── about.css
    │   │   ├── album.css
    │   │   ├── artists.css
    │   │   ├── home.css
    │   │   ├── music.css
    │   │   ├── playlist.css
    │   │   ├── search.css
    │   │   └── spotlight.css
    │   ├── images
    │   │   ├── Al-1d-Four.jpg
    │   │   ├── Al-1d-MadeintheAM.jpg
    │   │   ├── Al-1d-midnightmemmories.jpg
    │   │   ├── Al-1d-takmehome.jpg
    │   │   ├── Al-1d-upallnight.jpg
    │   │   ├── Al-bsb-AverybackstreetChristmas.jpg
    │   │   ├── Al-bsb-DNA.jpg
    │   │   ├── Al-bsb-Inaworldlikethis.jpg
    │   │   ├── Al-bsb-Thisisus.jpg
    │   │   ├── Al-bsb-unbreakable.jpg
    │   │   ├── Al-Ed-Babies.png
    │   │   ├── Al-Ed-callme.png
    │   │   ├── Al-Ed-divide.jpg
    │   │   ├── Al-Ed-dont.jpg
    │   │   ├── Al-Ed-=.jpg
    │   │   ├── Al-Ed-No.6col.jpg
    │   │   ├── Al-Ed-+.png
    │   │   ├── Al-ED-smoke+mirrors.jpg
    │   │   ├── Al-Ed-x.jpg
    │   │   ├── Al-ID-Evolve.jpg
    │   │   ├── Al-ID-Mercury.jpg
    │   │   ├── Al-ID-NightVisions.jpg
    │   │   ├── Al-ID-Origins.jpg
    │   │   ├── Al-TS-Evermore.jpg
    │   │   ├── Al-TS-Fearless.jpg
    │   │   ├── Al-TS-folklore.jpg
    │   │   ├── Al-TS-midnights.jpg
    │   │   ├── Al-TS-Red.jpg
    │   │   ├── anish.jpg
    │   │   ├── anish.png
    │   │   ├── background.jpg
    │   │   ├── backStreetBoys.jpeg
    │   │   ├── delete.png
    │   │   ├── deluxe.png
    │   │   ├── EdSheeran.jpg
    │   │   ├── images.jpeg
    │   │   ├── ImagineDragons.jpeg
    │   │   ├── logo.png
    │   │   ├── OneDirection.jpg
    │   │   ├── playlist-head.png
    │   │   ├── playlist.png
    │   │   ├── S-believer.jpeg
    │   │   ├── search.png
    │   │   ├── search-red.png
    │   │   ├── shreyas.jpg
    │   │   ├── S-perfect.jpeg
    │   │   ├── S-stealmygirl.jpeg
    │   │   └── TaylorSwift.webp
    │   └── js
    │       ├── about.js
    │       ├── header.js
    │       ├── search.js
    │       └── spotlight.js
    └── templates
        ├── about.html
        ├── album2.html
        ├── album3.html
        ├── album4.html
        ├── album5.html
        ├── album.html
        ├── artists.html
        ├── home.html
        ├── music01.html
        ├── music02.html
        ├── music03.html
        ├── music04.html
        ├── music05.html
        ├── music06.html
        ├── music07.html
        ├── music08.html
        ├── music09.html
        ├── music10.html
        ├── music11.html
        ├── music12.html
        ├── music13.html
        ├── music14.html
        ├── music15.html
        ├── music16.html
        ├── music17.html
        ├── music18.html
        ├── music19.html
        ├── music20.html
        ├── music21.html
        ├── music22.html
        ├── music23.html
        ├── music24.html
        ├── music25.html
        ├── playlist.html
        ├── search.html
        └── spotlight.html

6 directories, 100 files


```
