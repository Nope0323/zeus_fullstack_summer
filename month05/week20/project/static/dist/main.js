let s;async function i(n=""){try{const t=n?`/api/pokemon/?search=${encodeURIComponent(n)}`:"/api/pokemon/",e=await fetch(t);if(!e.ok)throw new Error(`API Error: ${e.status}`);const r=await e.json();c(r)}catch(t){console.error(t);const e=document.getElementById("list");e&&(e.innerHTML="<div>API Error...</div>")}}function c(n){const t=document.getElementById("list");if(t){if(n.length===0){t.innerHTML="<div>No Pokémon found</div>";return}t.innerHTML=n.map(e=>`
                <div class="card">
                    <img src="${e.image??"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"}" alt="${e.name}">
                    <h3>${e.name}</h3>
                    <div>${e.type.map(a=>`<span class='tag'>${a}</span>`).join(" ")}</div>
                </div>
            `).join("")}}i();const o=document.getElementById("myInput");o&&o.addEventListener("keyup",()=>{clearTimeout(s),s=setTimeout(()=>i(o.value),250)});document.getElementById("searchBtn")?.addEventListener("click",()=>{i(o.value)});
