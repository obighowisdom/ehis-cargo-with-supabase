const hamburger_menu = document.querySelector(".hamburger-menu");
const container = document. querySelector(".container");

hamburger_menu.addEventListener("click", () => {
    container.classList.toggle("active");
})


function getValue(){
    // var track_value = document.getElementById("number");
    var input_value = document.getElementById("realNumber");
    alert(input_value.value);

}




// card




