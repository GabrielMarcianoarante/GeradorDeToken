/* ========================
   MAR DE TOKENS — visual
======================== */
const STREAM_COLORS = [
  'rgba(181,212,244,0.55)',
  'rgba(93,202,165,0.45)',
  'rgba(255,255,255,0.28)',
  'rgba(250,199,117,0.35)',
  'rgba(181,212,244,0.38)',
  'rgba(255,255,255,0.20)',
];

const STREAM_ROWS = [
  { top:  5, dur: 17, dy: '-6px'  },
  { top: 13, dur: 22, dy: '-10px' },
  { top: 22, dur: 19, dy: '-5px'  },
  { top: 31, dur: 25, dy: '-8px'  },
  { top: 40, dur: 20, dy: '-12px' },
  { top: 50, dur: 23, dy: '-6px'  },
  { top: 58, dur: 18, dy: '-9px'  },
];

const SAMPLE = [
  'A3F9K2','ZX91QP','M7T4WL','B2R8NV','C5J6DH',
  'K1P3YU','Q8W2EA','L4S7FG','N6V0HJ','X9M1BC',
];

const caracteres = document.getElementById("qtd-caracteres").value;
const quantidade = document.getElementById("qtd-tokens").value;

function buildLine() {
  const parts = [];
  let rem = 55 + Math.floor(Math.random() * 35);
  while (rem > 0) {
    const sz = Math.min(4 + Math.floor(Math.random() * 8), rem);
    parts.push(SAMPLE[Math.floor(Math.random() * SAMPLE.length)]);
    rem -= sz;
  }
  return parts.join(' · ');
}

function initOcean() {
  const ocean = document.getElementById('ocean');

  STREAM_ROWS.forEach(({ top, dur, dy }) => {
    const el = document.createElement('span');
    el.style.top = top + '%';
    el.style.color = STREAM_COLORS[Math.floor(Math.random() * STREAM_COLORS.length)];
    el.style.animationDuration = dur + 's';
    el.style.animationDelay = -(Math.random() * dur) + 's';
    el.style.setProperty('--dy', dy);
    el.textContent = buildLine();
    ocean.appendChild(el);
  });

  setInterval(() => {
    const all = ocean.querySelectorAll('span');
    all[Math.floor(Math.random() * all.length)].textContent = buildLine();
  }, 2800);
}

/* ========================
   LÓGICA DO TOKEN
======================== */
document.addEventListener("DOMContentLoaded", async () => {
  initOcean();

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
  fetch('http://127.0.0.1:5000/receber-valor', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ valor: meuValor })
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