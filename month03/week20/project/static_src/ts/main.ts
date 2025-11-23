async function loadPokemon() {
  const res = await fetch("/api/pokemon/");
  const data = await res.json();

  const list = document.getElementById("list");
  list!.innerHTML = data.map((p: any) =>
    `<div>${p.name} — ${p.type.join(", ")}</div>`
  ).join("");
}

loadPokemon();
