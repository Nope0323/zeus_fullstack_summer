console.log(" Pokemon ")

interface Pokemon {
    name: string;
    id: number;
    sprites: {
        front_default: string;
    };
    types: Array<{
        type: { name: string 

        }
    }>;
}
async function fetchPokemon(pokemonName: string): Promise<void> {
    try {
        console.log(`Fetching data for ${pokemonName}...`);

        const url=`https://pokeapi.co/api/v2/pokemon/${pokemonName.toLowerCase()}`;
        const response = await fetch (url);

        const data = await response.json();
        console.log('Success');
        console.log(`Name: ${data.name.toUpperCase()}`);
        console.log(`ID: ${data.id}`);
        console.log(`Types: ${data.types[0]?.type.name}`);
        console.log(`See the sprite: ${data.sprites.front_default}`);

        // show dom
        const pokemonDiv = document.getElementById("pokemon");
        console.log(pokemonDiv);

        const pokeName:HTMLParagraphElement = document.createElement("p");
        pokeName.textContent = data.name.toUpperCase();
        pokemonDiv?.appendChild(pokeName);

        const pokemonId = document.createElement("p");
        pokemonId.textContent = `ID: ${data.id}`;
        pokemonDiv?.appendChild(pokemonId);

        const pokemonImage = document.createElement("img");
        pokemonImage.src = data.sprites.front_default;
        pokemonDiv?.appendChild(pokemonImage);





    } catch (error) {
        console.error(`Error fetching: ${pokemonName}`, error);
    }
}

fetchPokemon("pikachu");