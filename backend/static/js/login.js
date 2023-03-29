const wrappers = document.querySelector('.wrappers');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');

// next
const btnPopup = document.querySelector('.bntLogin-popup');

registerLink.addEventListener('click', ()=> {
    wrappers.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrappers.classList.remove('active');
});

// next
btnPopup.addEventListener('click', ()=> {
    wrappers.classList.remove('active-popup');
});
