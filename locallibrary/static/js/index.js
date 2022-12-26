// Changing the text of a button when clicked
// https://bobbyhadz.com/blog/javascript-change-button-text-on-click#:~:text=To%20change%20the%20text%20of,textContent%20%3D%20%27Button%20clicked%27%20.

const theme_btn = document.getElementById('theme_btn');

theme_btn.addEventListener('click', function handleClick() {
const initialHTML = '<i class="fa fa-moon-o" aria-hidden="true"></i>';

    if (theme_btn.innerHTML == '<i class="fa fa-sun-o" aria-hidden="true"></i>') {
        theme_btn.innerHTML = '<i class="fa fa-moon-o" aria-hidden="true"></i>';
    } else {
        theme_btn.innerHTML = '<i class="fa fa-sun-o" aria-hidden="true"></i>';
    }
});

// Function for changing the screen mode
// https://www.geeksforgeeks.org/how-to-make-dark-mode-for-websites-using-html-css-javascript/#:~:text=Steps%20to%20create%20Dark-Mode%20websites%20using%20HTML%2C%20CSS%2C,to%20switch%20between%20dark-mode%20and%20light-mode%20using%20JavaScript
function darkMode() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}

// Index Page

let span = document.getElementsByClassName('slider-arrow');
let product = document.getElementsByClassName('product');
let product_page = Math.ceil(product.length/4);
let l = 0;
let movePer = 25.34;
let maxMove = 203;

// Mobile view
let mobile_view = window.matchMedia("(max-width: 768px)");
if (mobile_view.matches)
{
    movePer = 50.36;
    maxMove = 504;
}

let right_mover = ()=> {
    l = l + movePer;
    if (product == 1) {l = 0;}

    for (const i of product)
    {
        if (l > maxMove) {l = l - movePer}
        i.style.left = '-' + l + '%';
    }
}

let left_mover = ()=> {
    l = l - movePer;
    if (l <= 0) {l = 0;}

    for (const i of product)
    {
        if (product_page > 1)
        i.style.left = '-' + l + '%';
    }
}

span[1].onclick = ()=>{right_mover();}
span[0].onclick = ()=>{left_mover();}