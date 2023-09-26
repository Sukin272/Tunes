const form = document.querySelector('form');
const userInput = document.querySelector('#userInput');
const submitButton = document.querySelector('.search-button');
const durationMax=document.querySelector('#durationInput');
const mainContent=document.querySelector(".mainContent");
let durval;
const resetButton=document.querySelector(".reset");
const explicit=document.querySelector('.Expliciness');
if(durationMax.value=="")
    durval=10000;
else
    durval=durationMax.value;
submitButton.addEventListener('click',func);
userInput.addEventListener('keydown',(event) => {
    if (event.key === 'Enter') {
        event.preventDefault();
        func();
    }
  });

function func() {
    let flag=0;
    const durationMax=document.querySelector('#durationInput');
    let durval;

    if(durationMax.value=="")
        durval=10000;
    else
        durval=durationMax.value;
    let count=0;

    let inputText = userInput.value; 
    inputText=inputText.replace(' ','+');
    console.log(inputText);
    mainContent.innerHTML='<hr style="margin:0 450px 0 450px;border-color: gray;">'
    fetch(`https://itunes.apple.com/search?term=${inputText}`)
        .then(response => response.json())
        .then(data => {
            for(let i=0;i<data.resultCount;i++){
                if(count>=10)
                    break;
                if(data.results[i].trackTimeMillis<durval*60000 && (!explicit.checked||data.results[i].trackExplicitness!='explicit')){
                    flag=1;
                    mainContent.innerHTML+=`<div class="songs">
                    <div class="snum">
                        <img src=${data.results[i].artworkUrl100}>
                    </div>
                    <div class="song-name">
                        ${data.results[i].trackName} &#x2022; ${data.results[i].artistName}
                    </div>
                    <div class="duration">
                        <audio controls>
                            <source src="${data.results[i].previewUrl}",type="audio/mp3">
                        </audio>
                    </div>
                </div>
                <hr style="margin:0 450px 0 450px;border-color: gray;">`
                count++;
                }
            }
            if(flag===0)
            mainContent.innerHTML+='<center style="margin-top:10 px; font-size:40px;">NO RESULTS</center>';
            mainContent.innerHTML+='<div style="height:100px"></div>'
        
            

        })
        .catch(error => {
        
        console.error(error);
        });

};

resetButton.addEventListener('click',()=>{
    explicit.checked=0;
    durationMax.value="";
});