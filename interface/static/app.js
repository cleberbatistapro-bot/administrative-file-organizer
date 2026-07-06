// =============================
// TEMA CLARO / ESCURO
// =============================
const themeBtn = document.getElementById('themeBtn');
const themeIcon = document.getElementById('themeIcon');

themeBtn.onclick = function() {
  document.body.classList.toggle('light');
  const isLight = document.body.classList.contains('light');
  themeIcon.className = isLight ? 'ti ti-moon' : 'ti ti-sun';
};

// =============================
// SELEÇÃO DE MODO
// =============================
let modoAtual = '1';

document.querySelectorAll('.mode-card').forEach(card => {
  card.onclick = function() {
    document.querySelectorAll('.mode-card').forEach(c => c.classList.remove('active'));
    card.classList.add('active');
    modoAtual = card.dataset.modo;
    document.getElementById('destinoFixoInfo').style.display = modoAtual === '2' ? 'flex' : 'none';
  };
});

// =============================
// SELEÇÃO DE PASTA
// =============================
const folderPath = document.getElementById('folderPath');
const folderInput = document.getElementById('folderInput');

document.getElementById('btnSelecionar').onclick = async function() {
  try {
    const resposta = await fetch('/selecionar-pasta');
    const dados = await resposta.json();
    if (dados.pasta) {
      folderInput.value = dados.pasta;
      folderPath.textContent = dados.pasta;
      folderPath.classList.add('selecionado');
    }
  } catch (e) {
    console.error('Erro ao selecionar pasta:', e);
  }
};

folderInput.addEventListener('input', () => {
  const valor = folderInput.value.trim();
  if (valor) {
    folderPath.textContent = valor;
    folderPath.classList.add('selecionado');
  } else {
    folderPath.textContent = 'Nenhuma pasta selecionada';
    folderPath.classList.remove('selecionado');
  }
});

// =============================
// TOGGLES
// =============================
document.querySelectorAll('.toggle').forEach(toggle => {
  toggle.onclick = function() {
    const ligado = toggle.dataset.state === 'on';
    toggle.dataset.state = ligado ? 'off' : 'on';
    toggle.classList.toggle('on', !ligado);
    toggle.classList.toggle('off', ligado);
  };
});

// =============================
// CORES POR EXTENSÃO
// =============================
const coresPorTipo = {
  pdf:  { barra: '#D85A30', badge: 'badge-pdf' },
  xlsx: { barra: '#639922', badge: 'badge-xlsx' },
  xls:  { barra: '#639922', badge: 'badge-xls' },
  docx: { barra: '#378ADD', badge: 'badge-docx' },
  doc:  { barra: '#378ADD', badge: 'badge-doc' },
  jpg:  { barra: '#D4537E', badge: 'badge-jpg' },
  jpeg: { barra: '#D4537E', badge: 'badge-jpeg' },
  png:  { barra: '#D4537E', badge: 'badge-png' },
  gif:  { barra: '#D4537E', badge: 'badge-gif' },
  txt:  { barra: '#888780', badge: 'badge-txt' },
};

function obterCor(ext) {
  return coresPorTipo[ext] || { barra: '#888', badge: 'badge-outros' };
}

// =============================
// RENDERIZAR CARD DE EXTENSÕES
// =============================
function renderizarExtensoes(porTipo) {
  const extCard = document.getElementById('extCard');
  extCard.innerHTML = '';
  const total = Object.values(porTipo).reduce((a, b) => a + b, 0);
  Object.entries(porTipo).forEach(([ext, quantidade]) => {
    const cor = obterCor(ext);
    const porcentagem = total > 0 ? (quantidade / total) * 100 : 0;
    const label = quantidade === 1 ? 'arquivo' : 'arquivos';
    const row = document.createElement('div');
    row.className = 'ext-row';
    row.innerHTML = `
      <span class="ext-badge ${cor.badge}">${ext}</span>
      <div class="ext-bar-wrap">
        <div class="ext-bar" style="width:${porcentagem}%; background:${cor.barra};"></div>
      </div>
      <span class="ext-count">${quantidade} ${label}</span>
    `;
    extCard.appendChild(row);
  });
}

// =============================
// RENDERIZAR LISTA DE ARQUIVOS
// =============================
function renderizarResultados(resultados) {
  const lista = document.getElementById('listaResultados');
  lista.innerHTML = '';
  resultados.forEach(r => {
    const nomeOriginal = r.original.split(/[\\/]/).pop();
    const nomeDestino  = r.destination.split(/[\\/]/).pop();
    const ext = nomeOriginal.split('.').pop().toLowerCase();
    const cor = obterCor(ext);
    const row = document.createElement('div');
    row.className = 'result-row';
    row.innerHTML = `
      <span class="file-badge ${cor.badge}">${ext}</span>
      <span class="file-name">${nomeOriginal}</span>
      <span class="arrow">→</span>
      <span class="dest">${nomeDestino}</span>
    `;
    lista.appendChild(row);
  });
}

// =============================
// BOTÃO ORGANIZAR
// =============================
const btnOrganizar     = document.getElementById('btnOrganizar');
const statusBadge      = document.getElementById('statusBadge');
const secaoResultados  = document.getElementById('secaoResultados');
const erroBox          = document.getElementById('erroBox');
const erroMensagem     = document.getElementById('erroMensagem');

btnOrganizar.onclick = async function() {
  const pasta   = folderInput.value.trim();
  const backup  = document.getElementById('toggleBackup').dataset.state === 'on';

  if (!pasta) {
    erroBox.style.display = 'flex';
    erroMensagem.textContent = 'Por favor, informe o caminho da pasta antes de continuar.';
    secaoResultados.style.display = 'none';
    return;
  }

  erroBox.style.display = 'none';
  secaoResultados.style.display = 'none';
  btnOrganizar.disabled = true;
  btnOrganizar.innerHTML = '<i class="ti ti-loader"></i> Organizando...';
  statusBadge.className = 'status-badge carregando';
  statusBadge.textContent = '● Processando...';

  try {
    const resposta = await fetch('/organizar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        input_dir: pasta,
        modo: modoAtual,
        backup: backup
      })
    });

    const dados = await resposta.json();

    if (dados.erro) {
      erroBox.style.display = 'flex';
      erroMensagem.textContent = dados.erro;
      statusBadge.className = 'status-badge erro';
      statusBadge.textContent = '● Erro';
      return;
    }

    document.getElementById('statTotal').textContent   = dados.total;
    document.getElementById('statMovidos').textContent = dados.movidos;
    document.getElementById('statErros').textContent   = dados.nao_movidos;

    renderizarExtensoes(dados.por_tipo);
    renderizarResultados(dados.resultados);

    secaoResultados.style.display = 'block';
    statusBadge.className = 'status-badge';
    statusBadge.textContent = '● Concluído';

  } catch (e) {
    erroBox.style.display = 'flex';
    erroMensagem.textContent = 'Não foi possível conectar ao servidor. Verifique se o programa está rodando.';
    statusBadge.className = 'status-badge erro';
    statusBadge.textContent = '● Erro de conexão';

  } finally {
    btnOrganizar.disabled = false;
    btnOrganizar.innerHTML = '<i class="ti ti-player-play"></i> Organizar arquivos agora';
  }
};