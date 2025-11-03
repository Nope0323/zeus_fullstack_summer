const outputDiv = document.querySelector<HTMLDivElement>("#output");

const myButton = document.querySelector<HTMLButtonElement>("#myButton");

if (myButton && outputDiv) {
    myButton.addEventListener("click", (event: MouseEvent) => {
        console.log("Button clicked!", event);
        outputDiv.textContent ='Button clicked';
    });
} else {
    console.log('Error during button click');
} 

const myInput = document.querySelector<HTMLInputElement>("#myInput");

if (myInput && outputDiv) {
    myInput.addEventListener('input', (event: Event) => {
        const target = event.target as HTMLInputElement;
        outputDiv.textContent = `You wrote: ${target.value}`;
    });
}

//Example 3
// ...existing code...
const myForm = document.querySelector<HTMLFormElement>("#my-form");

if (myForm && myInput && outputDiv) {
    myForm.addEventListener('submit', (event: SubmitEvent) => {
        event.preventDefault();
        console.log('form sent');

        outputDiv.textContent = `Form sent: ${myInput.value}`;
        myInput.value = '';
    });
}
// ...existing code...                           