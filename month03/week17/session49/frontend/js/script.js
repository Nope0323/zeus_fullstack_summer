console.log('jsObjects')
//problem
// хүн гэдэг
// Removed unused variable declarations

let Khangaihuu = {
    firstName: 'Khangaihuu',
    lastName: 'Uvgunhuu',
    age: 43,
    weigth: 80
};

console.log(Khangaihuu);

let boldErdene = {
    firstName: 'Bold-Erdene',
    lastName: 'Enhktsetseg',
    age: 24,
    weigth: 73
};
console.log(boldErdene)

const bugatti = {
    horsePower: 1001,
    brand: "Bugatti",
    model: "Buggatti Veron16.4",
    producedYear: 2015
};
console.log(bugatti)

const porsche = {
    horsePower: 379,
    brand:'porsche',
    model: "porsche carerra",
    producedYear:2026
} ;
console.log(porsche)

const audi = {
    horsePower: 113,
    brand:'audi',
    model: "audi q3",
    producedYear:2016
} ;
console.log(audi)

//object properties - horse power, brand, model,poduce year
//object values - 113.8
//object access properties - do notation
console.log(audi.horsePower);
console.log(audi.brand);
console.log(audi.model);
console.log(audi.producedYear);
//object access properties
console.log(bugatti['horsePower']);
console.log(bugatti['brand']);
console.log(bugatti['model']);
console.log(bugatti['producedYear']);
//dot notation vs bracket notation
constdotaTwoTroll = {
    'ultimate- ability': 'Berserker',
    'health-generation':'2 hp per second',
    'stun':'2 seconds'
};
//console.log(constdotaTwoTroll.ultimate- ability); --this is fordidden
console.log(constdotaTwoTroll['ultimate- ability']); //Berserker

//change object property value
audi.producedYear = 2018
console.log(audi);

//change object property value
constdotaTwoTroll['stun'] = '2 seconds per 7 punch';

//addd new property to object
console.log(boldErdene);
boldErdene.skill = ['HTML','CSS','JS', 'python', 'database'];
console.log(boldErdene);
