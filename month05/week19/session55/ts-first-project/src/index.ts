interface Greeting {
    message: string;
    name: string;
}

function greet(greeting: Greeting): void {
    console.log(`${greeting.message}, ${greeting.name}!`);
}

const myGreeting: Greeting = {
    message: "Сайн байна уу",
    name: "TypeScript"
};

greet(myGreeting);

let myName: string = "Boldoo";
let age: number = 25;
let isStudent: boolean= true;

let count: string = "ten";
 count= "ten"; 

function add(n:number ,m: number){
    
    let number = n+m
    console.log(number)
    return number;
}
add (3,9)

function logMessage(message: string): void {
    console.log(message);
}

logMessage("Сайн байна уу!");

logMessage(" ");

 let hobbies:string[] = [];
hobbies.push("n");
hobbies.push("l");
hobbies.push("uu");
hobbies.push("100");

