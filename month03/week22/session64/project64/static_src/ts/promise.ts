function makeBatter(): Promise<void> {
    console.log("Mixing ingredients...");
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log("Batter is ready! ");
            resolve();
        }, 1500);
    });
}

function cookPancakes(): Promise<void> {
    console.log("2. Pouring batter on the griddle...");
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const burned = Math.random() < 0.5; // 50% chance to burn
            if (burned) {
                console.log("Pancakes are burned! ");
                reject("Pancake is burned"); //Failure
            } else {
                console.log("Pancakes are cooked! ");
                resolve(); // Success
            }
        }, 2000);
    });
}
function addSyrup(): Promise<void> {
    console.log("3. adding maple syrup...");
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log(" ->Pancakes is ready to eat");
            resolve();
        }, 500);
    });
}
console.log(" lets make pancakes using Promises ");

makeBatter()
    .then(() => {
        // Battrer is done, now cook
        return cookPancakes();
    })
    .then(() => {
        // Pancakes are cooked, now add syrup
        return addSyrup();
    })
    .then(() => {
        console.log("Enjoy your pancakes! ");
    })
    .catch((error) => {
        console.error("Error:", error);
    });

    console.log ("This messgae logs immediately")

    // async/await
    async function makeBreakfast() {
        try {
            console.log(" lets make pancakes using async/await ");
            // step 1: make batter
            await makeBatter();
            // step 2: cook pancakes
            await cookPancakes();
            // step 3: add syrup
            await addSyrup();
            console.log("\n ALL done! Enjoy your breakfast! ");
        }
        catch (error) {
            console.log("\n Breakfast failed:");
            console.error("Error:", error);
        }
    }
    makeBreakfast();
