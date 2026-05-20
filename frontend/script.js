document.addEventListener("DOMContentLoaded", async () => {

    const input = document.getElementById("campo-backend");

    const res = await fetch("http://127.0.0.1:5000/tokens");
    const dados = await res.json();

    console.log(dados);

    const indice = Math.floor(Math.random() * dados.length);

    const token = dados[indice].Token; // 👈 AQUI É O FIX

    input.value = token;

  // botão copiar - 20/05/25
  btnCopiar.addEventListener("click", async () => {
    await navigator.clipboard.writeText(input.value);

    // muda texto - 20/05/25
    btnCopiar.textContent = "Copiado";

    // muda cor - 20/05/25
    btnCopiar.classList.add("copiado");

    // volta ao normal - 20/05/25
    setTimeout(() => {
      btnCopiar.textContent = "Copiar";
      btnCopiar.classList.remove("copiado");
    }, 2000);
  });
});
