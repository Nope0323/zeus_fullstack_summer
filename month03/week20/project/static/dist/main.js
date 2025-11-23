async function e(){const t=await(await fetch("/api/pokemon/")).json(),o=document.getElementById("list");o.innerHTML=t.map(n=>`<div>${n.name} — ${n.type.join(", ")}</div>`).join("")}e();
