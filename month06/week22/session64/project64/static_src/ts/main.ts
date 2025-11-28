console.log("TypeScript-ээс мэндчилье! 🚀 ");
// call back function
// js synchron 
function funcA() {
    setTimeout(() => {
        console.log("A");
    }, 3000);
}

function funcB() {
    setTimeout(() => {
        console.log("B");
    }, 2000);
}

function funcC() {
    setTimeout(() => {
        console.log("C");
    }, 1000);
}

// callback 
type simpleCallback = () => void;
//  step 1: prepare ingredients
function makeBatter (callback: simpleCallback) {
    console.log("Mixing ingredients...");
    setTimeout(() => {
        console.log("Batter is ready! ");
        callback();
    }, 1500);
}
// step 2: simulates cook pancakes
function cookPancakes (callback: simpleCallback) {
    console.log("Cooking pancakes... ");
    setTimeout(() => {
        console.log("Pancakes are ready! ");
        callback();
    }, 2000);
}
// step 3: serve pancakes
function addSyrup(callback: simpleCallback) {
    console.log("3. adding maple syrup...");
    setTimeout(() => {
        console.log(" ->Pancakes is ready to eat");
        callback();
    }, 500);
}
//  promise
let myPromise = new Promise<string>((resolve, reject) => {
    const isApproved = false; // эсвэл false
    if (isApproved) {
        console.log("ok");
        resolve("ok");
    } else {
        console.log("failed");
        reject("failed");
    }
});

console.log(myPromise)

    function main() {
    // funcA();
    // funcB();
    // funcC();
}
// make pancakes
console.log("Let's make pancakes! ");
// step 1
makeBatter(() => {
    // step 2
    cookPancakes(() => {
        // step 3
        addSyrup(() => {
            console.log("Enjoy your pancakes! ");
        }); // End of addSyrup
    });
});
console.log(myPromise);
myPromise
document.addEventListener('DOMContentLoaded', main);

// function main() {
// const header = document.querySelector('h1');
// if (header) {
// header.style.color = 'blue';
// console.log('<h1> тагийг олж, өнгийг нь цэнхэр болголоо.');
// }
// }
// document.addEventListener('DOMContentLoaded', main);