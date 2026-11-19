// JavaScript do cliente - Prova Pratica Individual de DW2.
//
// Este arquivo e carregado em todas as paginas, pela base. Por isso o
// codigo confere se os elementos existem antes de usa-los.

var lista = document.getElementById("lista");
var botaoAtualizar = document.getElementById("atualizar");


// Escreve uma mensagem na tela, sem recarregar a pagina.
function mostrarAviso(texto) {
  var aviso = document.getElementById("aviso-js");

  if (aviso) {
    aviso.textContent = texto;
  }
}


// Esvazia a lista e a redesenha com os dados recebidos.
// "dados" e um array de objetos, como o que a API devolve.
function desenharLista(dados) {
  lista.innerHTML = "";

  for (var i = 0; i < dados.length; i = i + 1) {
    var item = document.createElement("li");
    item.textContent = dados[i].nome + " — " + dados[i].bloco;
    lista.appendChild(item);
  }

  mostrarAviso(dados.length + " registro(s) lido(s) sem recarregar a página.");
}


if (botaoAtualizar && lista) {

  botaoAtualizar.addEventListener("click", function () {

    // ===== ITEM 8 ===================================================
    // Ao clicar no botao, peca a lista a API, no endereco
    // /api/salas, e redesenhe a lista da pagina com o que chegar,
    // SEM recarregar. Use as funcoes que ja existem neste arquivo.
    // Se nao for possivel falar com o servidor, avise na tela.
    // ================================================================

  });

}
