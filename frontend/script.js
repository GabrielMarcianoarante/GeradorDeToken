document.addEventListener("DOMContentLoaded", async () => {

    const input = document.getElementById("campo-backend");

    const res = await fetch("http://127.0.0.1:5000/tokens");
    const dados = await res.json();

    console.log(dados);

    const indice = Math.floor(Math.random() * dados.length);

    const token = dados[indice].Token; // 👈 AQUI É O FIX

    input.value = token;

});