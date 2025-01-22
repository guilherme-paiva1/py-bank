// Arquivo de teste para entendimento da API
async function buscarMensagem() {
    try {
        const resposta = await fetch("/mensagem", { method: "GET" });

        if (!resposta.ok) {
            throw new Error("Erro na resposta do servidor");
        }

        const dados = await resposta.json(); // Resolvendo a Promise
        div_mensagem.innerHTML = dados.mensagem; // Exibindo a mensagem no DOM
    } catch (erro) {
        console.warn("Erro ao buscar dados:", erro);
        div_mensagem.innerHTML = "Deu ruim!";
    }
}

// Chamando a função
buscarMensagem();