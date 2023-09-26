let headButtons=document.querySelectorAll('.navigation div a');

headButtons.forEach((element) => {
    element.addEventListener('mouseover',()=>{
        element.style.color='red';
    });
    element.addEventListener('mouseout',()=>{
        element.style.color='white';
    });
    
});