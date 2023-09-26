const typingEffect = document.querySelector(".head");
const text = typingEffect.textContent;
typingEffect.textContent = "";

const typingDelay = 100; 
const newTextDelay = 400; 
let textIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < text.length) {
    typingEffect.textContent += text.charAt(charIndex);
    charIndex++;
    setTimeout(type, typingDelay);
  } else {
    setTimeout(erase, newTextDelay);
  }
}


setTimeout(type, newTextDelay);
