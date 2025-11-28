var outputDiv = document.querySelector("#output");
var myButton = document.querySelector("#myButton");
if (myButton && outputDiv) {
    myButton.addEventListener("click", function (event) {
        console.log("Button clicked!", event);
        outputDiv.textContent = 'Button clicked';
    });
}
else {
    console.log('Error during button click');
}
var myInput = document.querySelector("myInput");
if (myInput && outputDiv) {
    myInput.addEventListener('input', function (event) {
        var target = event.target;
        outputDiv.textContent = "You wrote: ".concat(target.value);
    });
}
//Example 3
