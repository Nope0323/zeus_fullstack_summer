let number = 5;
if (number>0){
        console.log("эерэг тоо");
}

let age = 20
if (age>18){
    console.log("Насанд хүрсэн")
}

let temperature = 35;
if (temperature>30){
    console.log("Халуун өдөр")
}

let score = 75;
if (score>60){
    console.log("Тэнцсэн")
}
else{
    console.log("Тэнцсэнгүй")
}

let time = 14
if(time <12){
    console.log("Өглөө")
}
else {console.log("Орой")}

let grade = 85;
if (90< grade && grade<100){
    console.log("A");
}
else if (80<grade && grade<89){
    console.log("B");
}
else if (grade<70 && grade<79){
    console.log("C");
}
else{
    console.log("F")
}

let i = 1
while (i<=5){
    console.log(i);
    i++;
}

let counter = 10 
while (counter>0){
    console.log(counter);
    counter=counter-1
}

//*ex09
input =""
do {
    input = prompt("ug oruulna uu: ")

}while(input !== "exit");

//*ex10
for(let n=1; n<=10; n++){
    if(n % 2 === 0)  
        console.log(n);
}

//*ex11
function calculateSquare(a){
    let parameter1 = a*a;
    console.log(`parameter:${parameter1}`)
}
calculateSquare(5)

//*ex12
