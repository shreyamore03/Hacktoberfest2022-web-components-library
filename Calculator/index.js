const result = document.querySelector('#value');

const sign = document.querySelectorAll('.sign-btn');
const number = document.querySelectorAll('.number-btn');

const equal = document.querySelector('.eql-btn');
const del = document.querySelector('.del-btn');
const clear = document.querySelector('.ac-btn');
const dot = document.querySelector('.pt-btn');

let isSign = false;
let isPoint = false;

for (let i = 0; i < number.length; i++) {
  number[i].addEventListener('click', (e) => {
    result.innerText += e.target.innerText;
    isPoint = false;
    isSign = false;
  });
}
for (let i = 0; i < sign.length; i++) {
  sign[i].addEventListener('click', (e) => {
    if (!isSign) {
      result.innerText += e.target.innerText;
      isSign = true;
      isPoint = false;
    }
  });
}

clear.addEventListener('click', () => {
  result.innerText = '';
});

dot.addEventListener('click', () => {
  if(!isPoint) {
      result.innerText += '.';
      isPoint = true;
      isSign = false;
  }
});

del.addEventListener('click', () => {
  const expression = result.innerText.slice(0,-1); 
  result.innerText = expression;
});

equal.addEventListener('click', () => {
  if (result.innerText !== '') {
    result.innerText = eval(result.innerText);
    isPoint = false;
    isSign = false;
  }
});