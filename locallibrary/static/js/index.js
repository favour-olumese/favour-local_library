// Changing the text of a button when clicked

// Accessing theme stored in local storage.
theme = localStorage.getItem("theme");

if (theme == null)
{
    theme = localStorage.setItem("theme", "light");
}

var theme_btn = document.getElementById('theme_btn');

if (theme == 'dark'){
    darkMode();
    document.getElementById('theme_btn').onclick = lightMode;
    theme_btn.innerHTML = '<i class="fa fa-sun-o" aria-hidden="true"></i>';  
} else {
    lightMode();
    document.getElementById('theme_btn').onclick = darkMode;
    theme_btn.innerHTML = '<i class="fa fa-moon-o" aria-hidden="true"></i>';
}


// Changing page theme when the change of mode button is clicked.
theme_btn.addEventListener('click', function handleClick() {

    if (theme_btn.innerHTML == '<i class="fa fa-sun-o" aria-hidden="true"></i>') {
        theme_btn.innerHTML = '<i class="fa fa-moon-o" aria-hidden="true"></i>';
        document.getElementById('theme_btn').onclick = darkMode;
        theme = localStorage.setItem("theme", "light");
    } else {
        theme_btn.innerHTML = '<i class="fa fa-sun-o" aria-hidden="true"></i>';
        document.getElementById('theme_btn').onclick = lightMode;
        theme = localStorage.setItem("theme", "dark");
    }
});

// Functions for changing the screen theme.
function darkMode() {
    var element = document.body;
    element.className = "dark-mode";
    theme = localStorage.setItem("theme", "dark");
}

function lightMode() {
    var element = document.body;
    element.className = "light-mode";
    theme = localStorage.setItem("theme", "light");
}

// INDEX PAGE
// For controlling carousels

// let span = document.getElementsByClassName('slider-arrow');
// let product = document.getElementsByClassName('product');
// let product_page = Math.ceil(product.length/3);
// let l = 0;
// let movePer = 50.36;
// let maxMove = 504;

// Mobile view
// let mobile_view = window.matchMedia("(max-width: 768px)");
// if (mobile_view.matches)
// {
//     movePer = 50.36;
//     maxMove = 504;
// }

// let right_mover = ()=> {
//     l = l + movePer;
//     if (product == 1) {l = 0;}

//     for (const i of product)
//     {
//         if (l > maxMove) {l = l - movePer}
//         i.style.left = '-' + l + '%';
//     }
// }

// let left_mover = ()=> {
//     l = l - movePer;
//     if (l <= 0) {l = 0;}

//     for (const i of product)
//     {
//         if (product_page > 1)
//         i.style.left = '-' + l + '%';
//     }
// }

// span[1].onclick = ()=>{right_mover();}
// span[0].onclick = ()=>{left_mover();}