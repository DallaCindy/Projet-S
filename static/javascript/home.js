const startApp = document.querySelector('.start-app');
const container = document.querySelector('.container');

const buttonSuivant = document.getElementById('Suivant');
const buttonPrecedent = document.getElementById('Precedent');

function activateurDeSection(sectionCourrante, sectionAActiver) {
    document.querySelector('.' + sectionCourrante).classList.remove('active')
    document.querySelector('.' + sectionAActiver).classList.add('active')
}

if (startApp && container) {
    startApp.addEventListener('click', e => {
        e.preventDefault();
        container.style.display = 'flex';
        startApp.style.display = 'none';
    });
}

buttonSuivant.addEventListener('click', (e) => {

    e.preventDefault();
    const elementActif = document.querySelector('.active');
    if (elementActif.classList.contains('Enregitrement')) {
        activateurDeSection('Enregitrement', 'Categories');

    } else if (elementActif.classList.contains('Categories')) {
        activateurDeSection('Categories', 'Priorites');

    } else if (elementActif.classList.contains('Priorites')) {
        activateurDeSection('Priorites', 'Depenses');
    } else if (elementActif.classList.contains('Depenses')) {
       document.querySelector('form').submit();
    }
})

buttonPrecedent.addEventListener('click', (e) => {
    e.preventDefault()
    const elementActif = document.querySelector('.active')
    if (elementActif.classList.contains('Enregitrement')) {
        activateurDeSection('Enregitrement', 'Welcome')
        buttonSuivant.innerText = 'Demarrer'
        buttonPrecedent.style.display = 'none'

    } else if (elementActif.classList.contains('Categories')) {
        activateurDeSection('Categories', 'Enregitrement')

    } else if (elementActif.classList.contains('Priorites')) {
        activateurDeSection('Priorites', 'Categories')

    } else if (elementActif.classList.contains('Depenses')) {
        activateurDeSection('Depenses', 'Priorites')
    }
})
