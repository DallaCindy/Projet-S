const StartButton = document.getElementById('StartButton')
StartButton.addEventListener('click', () => {
    const WelcomeSection = document.querySelector('.Welcome')
    const EnregitrementSection = document.querySelector('.Enregitrement')

    WelcomeSection.classList.remove('active')
    EnregitrementSection.classList.add('active')
})
