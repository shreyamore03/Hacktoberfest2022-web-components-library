const inputEl =document.querySelector(".input")
console.log(inputEl.checked);
const bodyEl =document.querySelector("body")
inputEl.checked =localStorage.getItem("mode");
updatebody()
function updatebody(){
    if(inputEl.checked){
        bodyEl.style.background = " black"
    }
    else{
        bodyEl.style.background = " white"
    }

}
inputEl.addEventListener("input",()=>{
    updatebody()
    updateLocalStorage()
})
function updateLocalStorage(){
    localStorage.setItem("mode",JSON.stringify(inputEl.checked))
}