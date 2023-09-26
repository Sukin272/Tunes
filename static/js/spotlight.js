var zoom = document.getElementById("artist-image");
var scale = 1;
 
setInterval(function() {
  if (scale == 1) {
    scale = 1.2;
  } else {
    scale = 1;
  }
  zoom.style.transform = "scale(" + scale + ")";
}, 1000);

const ratingForm = document.getElementById('rating-form');
const ratingTableBody = document.querySelector('.songs');
const tick =document.querySelector('.submit');
const mainbody=document.querySelector('.review-table');
tick.addEventListener('click', (event) => {
  event.preventDefault();
  
  const artistName = document.getElementById('artist-name').value;
 let rating='';
 if(document.querySelector('input[name="rating"]:checked')){
  rating = document.querySelector('input[name="rating"]:checked').value;
 }

  const review = document.getElementById('review').value;
  if(artistName!='' && rating!='' && review!=''){
  mainbody.innerHTML+=`<div class="songs">
  <div class="snum">
      ${artistName}
  </div>
  <div class="song-name">
      ${rating} &#9733;
  </div>
  <div class="duration">
      ${review}
  </div>
</div>
<hr style="margin:0 450px 0 450px;border-color: gray;">`;
document.getElementById('artist-name').value='';
document.querySelector('input[name="rating"]:checked').checked=0;
document.getElementById('review').value='';
  }
else{
  alert('Enter all the given fields');
}

});
window.onload = function() {
  var checkbox = document.getElementById('star-1');
  var checkbox2 = document.getElementById('star-2');
  var checkbox3 = document.getElementById('star-3');
  var checkbox4 = document.getElementById('star-4');
  var checkbox5 = document.getElementById('star-5');
  checkbox.checked = false;
  checkbox2.checked = false;
  checkbox3.checked = false;
  checkbox4.checked = false;
  checkbox5.checked = false;
  document.getElementById('artist-name').value='';
  document.getElementById('review').value='';
}



const releaseDate = new Date('June 30 , 2023 00:00:00').getTime();


const countdown = setInterval(() => {

  
  const now = new Date().getTime();

 
  const timeRemaining = releaseDate - now;

 
  const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

  let cntdwn=document.querySelector(".countdown");
  cntdwn.innerHTML=(`Upcoming Album: ${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`);

  if (timeRemaining <= 0) {
    clearInterval(countdown);
    cntdwn.innerHTML=(`The album/song is now released!`);
  }
}, 1000);
