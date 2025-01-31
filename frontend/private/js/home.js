atualizarDados();

function atualizarDados() {
    atualizarNome();
    atualizarSaldo();
    atualizarCreditoDisponivel();
    atualizarFatura();
}

function atualizarNome() {
    h1_nome.innerHTML = "Olá, " + sessionStorage.getItem("nome") + "!";
}

function atualizarSaldo() {
    span_saldo.innerHTML = "Saldo atual: R$ " + sessionStorage.getItem("saldo");
}

function atualizarCreditoDisponivel() {
    span_credito_disponivel.innerHTML = "Crédito disponível: R$ " + sessionStorage.getItem("credito_disponivel");
}


function atualizarFatura() {
    span_fatura.innerHTML = "Fatura atual: R$ " + sessionStorage.getItem("fatura");
}

function mostrarModal(modal) {
    modal.style.display = "block";
}

function fecharModal(modal) {
    modal.style.display = "none";
}