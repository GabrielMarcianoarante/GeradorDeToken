document.addEventListener("DOMContentLoaded", async () => {

    const input = document.getElementById("campo-backend");

    const res = await fetch("http://127.0.0.1:5000/tokens");
    const dados = await res.json();

    console.log(dados);

    const indice = Math.floor(Math.random() * dados.length);

    const token = dados[indice].Token; 

    input.value = token;


// O valor que você deseja passar para o Python
const meuValor = "Este texto veio do JavaScript!";

// Dispara a requisição para o servidor Flask
fetch('http://127.0.0', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ valor: meuValor }) // Envia como um objeto JSON
})
.then(resposta => resposta.json())
.then(dados => console.log("Resposta do Flask:", dados))
.catch(erro => console.error("Erro ao enviar:", erro));

  // botão copiar - 20/05/25
  const btncopiar = document.getElementById("btn-copiar");
  btncopiar.addEventListener("click", async () => {
    await navigator.clipboard.writeText(input.value);

    // muda texto - 20/05/25
    btncopiar.textContent = "Copiado";

    // muda cor - 20/05/25
    btncopiar.classList.add("copiado");

    // volta ao normal - 20/05/25
    setTimeout(() => {
      btncopiar.textContent = "Copiar";
      btncopiar.classList.remove("copiado");
    }, 2000);
  });
});

const btnGerar = document.getElementById("btn-gerar");
btnGerar.addEventListener("click", async () => {
    const res = await fetch("http://127.0.0.1:5000/gerar-token", {
        method: "POST"
    });
    const dados = await res.json();
    console.log(dados);
});
