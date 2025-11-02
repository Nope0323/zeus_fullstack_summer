console.log("Hello from scrift.js");

// const mainElement = document.getElementByTagName("main");
const mainElement = document.getElementsByTagName("main");
console.log(mainElement);

//list element nemeh


//chinese foods
const ulElement = document.createElement("ul");

const liElOne = document.createElement("li");
liElOne.textContent = "Noodles";
const liElTwo = document.createElement("li");
liElTwo.textContent = "Dumplings";

const liElThree = document.createElement("li");
liElThree.textContent = "Fried Rice";

ulElement.appendChild(liElOne);
ulElement.appendChild(liElTwo);
ulElement.appendChild(liElThree);

const main = mainElement[0];



main.appendChild(ulElement);

const sectionElement = document.getElementsByTagName("section");
console.log(sectionElement);

const aOne = document.createElement("a");
aOne.scr ='https://github.com/'
aOne.textContent = 'Github'

const aTwo = document.createElement("a");
aTwo.scr ='https://classroom.google.com/'
aTwo.textContent = 'Classroom'

const aThree = document.createElement("a");
aThree.scr ='https://github.com/'
aThree.textContent = 'Github'



const h1Element = document.createElement('h1')
h1Element.textContent = 'My Favourite Movies'

const section = sectionElement[0];
section.appendChild(h1Element)
section.appendChild(aOne)
section.appendChild(aTwo)
section.appendChild(aThree)

const mongolianNationSports = ['wrestling','Archery', 'Horse Rise'];

const nationSportSection = document.createElement('section');
const nationalSportListUl = document.createElement('ul')
nationSportSection.appendChild(nationalSportListUl);

for(let i = 0; i< mongolianNationSports.length; i++){
    const liElement = document.createElement('li');
    liElement.textContent = mongolianNationSports[i];
    nationalSportListUl.appendChild(liElement);
}

main.appendChild(nationSportSection);