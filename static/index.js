const logIn = document.querySelector('.logIn');
const signUp = document.querySelector('.signUp');
const closeButton = document.querySelectorAll('.modal-close');



const modalClose = () => {
    signUp.classList.remove('fadeIn');
    signUp.classList.add('fadeOut');

    logIn.classList.remove('fadeIn');
    logIn.classList.add('fadeOut');
    setTimeout(() => {
        signUp.style.display = 'none';
        logIn.style.display = 'none';
    }, 500);
}



const openModal_signUp = () => {
    signUp.classList.remove('fadeOut');
    signUp.classList.add('fadeIn');
    signUp.style.display = 'flex';
}

const openModal_logIn = () => {
    logIn.classList.remove('fadeOut');
    logIn.classList.add('fadeIn');
    logIn.style.display = 'flex';
}

for (let i = 0; i < closeButton.length; i++) {

    const elements = closeButton[i];

    elements.onclick = (e) => modalClose();

    signUp.style.display = 'none';
    logIn.style.display = 'none';

    window.onclick = function (event) {
        if (event.target == signUp) modalClose();
        if (event.target == logIn) modalClose();
    }
}

  