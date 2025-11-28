// Тоо (Number)
let age: number = 25;
let price: number = 99.99;
console.log(age)
console.log(price)
// Текст мөр (String)
let firstName: string = "John";
let message: string = `Сайн уу, ${firstName}`;
console.log(firstName, message)
// Логик утга (Boolean)
let isActive: boolean = true;
console.log(isActive)
// Массив (Array)
let numbers: number[] = [1, 2, 3, 4, 5];
let names: string[] = ["John", "Jane", "Bob"];
console.log(names, numbers);

// Tuple - Тогтмол урттай массив
let person: [string, number] = ["John", 25];
// Тоолох төрөл (Enum)
enum Color {
Red,
Green,
Blue
}
let favoriteColor: Color = Color.Blue;
// Any (аль болох хэрэглэхгүй байх)
let notSure: any = 4;
notSure = "магадгүй текст";
// Void - Хоосон утга
function logMessage(): void {
console.log("Сайн уу!");
}
// Null ба Undefined
let nothing: null = null;
let unassigned: undefined = undefined;