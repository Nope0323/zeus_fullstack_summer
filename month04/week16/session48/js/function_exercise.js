console.log('Remove code duplication');

// rectangle 1

let length1 = 10;
let width1 = 5
let area1 = length1*with1;
let perimeter1 = 2*(length1+with1);

console.log('====Rectangle 1 Resalt===');
console.log(`Area:${area1}`);
console.log(`Premeter:${perimeter1}`)
console.log("");

// rectangle 2

let length2 = 20;
let width2 = 8
let area2 = length2*with2;
let perimeter2 = 2*(length2+with2);

console.log('====Rectangle 2 Resalt===');
console.log(`Area:${area2}`);
console.log(`Premeter:${perimeter2}`);
console.log("");

function calculateAndPrintRectangle(length, width){
    let area = length*width;
    let  premeter = 2 *(length+width);
    console.log('====Rectangle  Resalt===');
    console.log(`Area:${area2}`);
    console.log(`Premeter:${perimeter2}`);
    console.log("");
}

calculateAndPrintRectangle(10,5);
calculateAndPrintRectangle(20,8);
