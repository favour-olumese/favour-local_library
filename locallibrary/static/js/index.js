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

// Side bar
function show() {
    document.getElementById('sidebar').classList.toggle('active');
}