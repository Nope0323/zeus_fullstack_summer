
interface Pokemon {
    name: string;
    type: string[];
    image?: string;   // ако backend image өгөхгүй бол placeholder тавина
}

let timeout: number;

// --- FETCH ---
async function loadPokemon(searchText = "") {
    try {
        const url = searchText
            ? `/api/pokemon/?search=${encodeURIComponent(searchText)}`
            : "/api/pokemon/";

        const res = await fetch(url);

        if (!res.ok) throw new Error(`API Error: ${res.status}`);

        const data: Pokemon[] = await res.json();
        renderList(data);

    } catch (error) {
        console.error(error);
        const list = document.getElementById("list");
        if (list) list.innerHTML = "<div>API Error...</div>";
    }
}

// --- RENDER CARDS ---
function renderList(data: Pokemon[]) {
    const list = document.getElementById("list");
    if (!list) return;

    if (data.length === 0) {
        list.innerHTML = "<div>No Pokémon found</div>";
        return;
    }

    list.innerHTML = data
        .map(p => {
            const imgUrl = p.image ?? "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png";

            return `
                <div class="card">
                    <img src="${imgUrl}" alt="${p.name}">
                    <h3>${p.name}</h3>
                    <div>${p.type.map(t => `<span class='tag'>${t}</span>`).join(" ")}</div>
                </div>
            `;
        })
        .join("");
}

// Initial
loadPokemon();

// --- SEARCH INPUT ---
const input = document.getElementById("myInput") as HTMLInputElement;

if (input) {
    input.addEventListener("keyup", () => {
        clearTimeout(timeout);
        timeout = setTimeout(() => loadPokemon(input.value), 250);
    });
}

document.getElementById("searchBtn")?.addEventListener("click", () => {
    loadPokemon(input.value);
});
