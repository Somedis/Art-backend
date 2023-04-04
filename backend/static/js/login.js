const wrappers = document.querySelector('.wrappers');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');


registerLink.addEventListener('click', ()=> {
    wrappers.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrappers.classList.remove('active');
});
