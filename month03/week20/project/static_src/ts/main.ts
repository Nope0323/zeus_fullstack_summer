interface Pokemon {
    name: string;
    type: string[];
}

async function loadPokemon(searchText = "") {
    const url = searchText
        ? `/api/pokemon/?search=${encodeURIComponent(searchText)}`
        : "/api/pokemon/";

    const res = await fetch(url);
    const data: Pokemon[] = await res.json();

    const list = document.getElementById("list");
    if (list) {
        list.innerHTML = data
            .map((p: Pokemon) => `<div>${p.name} — ${p.type.join(", ")}</div>`)
            .join("");
    }
}

loadPokemon();

const input = document.getElementById("myInput") as HTMLInputElement | null;
if (input) {
    input.addEventListener("keyup", () => {
        loadPokemon(input.value);
    });
}
