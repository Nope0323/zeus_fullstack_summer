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

}while(input == "exit");

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

//ex12

function isEven(num) {
    return num % 2 === 0;
}
console.log(isEven(15))

//ex12.1
input = Number(prompt("Тоогоо оруулна уу: "));

function isItEven(num) {
  return num % 2 === 0;
}

console.log(isItEven(input));

//ex13
//  if b != 0:
//            return(a/b)
//        else:
//            print("0 ээс ялгаатай")
function divide (a,b){
    try{
        if (b===0){
            throw new Error("0-д хувааж болохгүй!");
        }
        return a/b;
    }catch(err){
        console.log("⚠️ Алдаа:", err.message);
        return null;
    }
}
console.log(divide(10,2));
console.log(divide(10,0));

//ex14
function printPattern(n) {
  for (let i = 1; i <= n; i++) {     
    let line = "";                  
    for (let j = 1; j <= i; j++) {   
      line += "*";                   
    }
    console.log(line);              
  }
}
console.log(printPattern(5))

//ex15
console.log("ex15");
function countBackwards(a,b){
    if (a>b){
        for (let i=0; i<=(a-b); i++){
            console.log(a-i);
        }
      
    } else if (b>a){
         for (let i=0; i<=(b-a); i++){
            console.log(b-i);
        }
    }
    
}
console.log(countBackwards(5,12))

//ex16
console.log("ex16");
function convertTemp(celsius){
    let n = celsius; // celsius ийн утгыг n оноож байна
    n=n+32;
    return n;

}
console.log(convertTemp(23))

//ex17
console.log("ex17");
function sumDigits(n){
    let sum = 0 ;
    while(n !==0 ){
        let last = n%10;
        sum+=last;
        n= Math.floor(n/10);
    
    }
    return sum;
}

console.log(sumDigits(123)); 

//ex18

//def is_prime(num):
//    """Тоог анхны тоо мөн эсэхийг шалгана."""
//    if num < 2:
//        return False
//    for i in range(2, num // 2 + 1):
//        if num % i == 0:
//            return False
//    return True

console.log("ex18");
function isPrime(n){
    if (n<2){
    return false
    }
    for (let i = 2; i <= Math.floor(n / 2); i++) {
    if (n %i ==0){
        return false;
    }
    }
     return true;
}
console.log(isPrime(13))

console.log("ex19")
function factorial(n){
    if(n<=0){
        return 0;
    }
    let list=1;
    for( let i=1; i<=n; i++){
    list=list*i
    }
    return list;
}

console.log(factorial(5))

console.log("ex20");

function fibonacci(n) {
  let fnum = [0, 1]; 
  for (let i = 2; i <= n; i++) {
    fnum[i] = fnum[i - 1] + fnum[i - 2];
  }
  return fnum;
}

console.log(fibonacci(5));


console.log("ex21");
function texToNum(input) {
  const n = Number(input);
  if (Number.isNaN(n)) {
    throw new TypeError("Тоо биш утга оруулсан байна!");
  }
  return n;
}


try {
  console.log("Converted:", texToNum("123")); 
} catch (err){
    console.log("Алдаа:", err.message);
}

console.log ("ex22");
function getDateTime(n){
if (n<12) {
    console.log("Өглөө")
}
else if (n>=12 && n<18){
    console.log("Өдөр")
}
else if (n<=18 && n<24){
    console.log("Орой")
}
return n ;
}

console.log(getDateTime(5));

console.log("ex23")
function session(n){
    if(n===12 || n===1 ||n===2){
        console.log("Өвөл")
    }
    else if (n>=3 && n<=5){
        console.log("Хавар")
    }
    else if (n>=6 && n<=8){
        console.log("Зун")
    }
    else if (n>=9 && n<=11){
        console.log("Намар")
    }
    return n;
}

console.log(session(10));


