function mostrarDiv(div_mostrar, div_esconder) {
    div_mostrar.style.display = 'flex'; 
    div_esconder.style.display = 'none';
}

async function entrar() {
    var cpf = cpf_login.value;
    var senha = senha_login.value;

    try {
        const resposta = await fetch("/user/entrar", { 
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "cpf": cpf,
                "senha": senha
            }) 
        });

        if (!resposta.ok) {
            throw new Error("Erro na resposta do servidor");
        }

        const dados = await resposta.json(); 

        if (dados) {
            status_login.innerHTML = "Bem vindo, " + dados.dono.nome + "! <br> Indo para a tela inicial..."; 
            status_login.innerHTML += "<br><div class='loader'></div>";

            sessionStorage.setItem("nome", dados.dono.nome);
            sessionStorage.setItem("cpf", dados.dono.cpf);
            sessionStorage.setItem("renda", dados.dono.renda);  
            sessionStorage.setItem("sexo", dados.dono.sexo);    
            sessionStorage.setItem("saldo", dados.saldo);   
            sessionStorage.setItem("credito_disponivel", dados.credito_disponivel);
            sessionStorage.setItem("fatura", dados.fatura)

            setTimeout(() => {
                window.location.href = "private/home.html";
                status_login.innerHTML = "";
            }, 2000);
            
        } else {
            status_login.innerHTML = "Usuário ou senha incorretos!";
            console.log(dados)
        }
    } catch (erro) {
        console.warn("Erro ao buscar dados:", erro);
        status_login.innerHTML = "Deu ruim!";
    }
}

async function cadastrar() {
    var nome = nome_cadastro.value;
    var sexo = sexo_cadastro.value;
    var cpf = cpf_cadastro.value;
    var renda = Number(renda_cadastro.value);
    var senha = senha_cadastro.value;

    try {
        const resposta = await fetch("/user/cadastrar", { 
            method: "POST",
            headers: {
                "Content-Type": "application/json" // Informando o tipo de conteúdo enviado
            },
            body: JSON.stringify({
                "nome": nome,
                "sexo": sexo,
                "cpf": cpf,
                "renda": renda,
                "senha": senha
            }) 
        });

        if (!resposta.ok) {
            throw new Error("Erro na resposta do servidor");
        }

        const status = await resposta.json();

        if (status) {
            status_cadastro.innerHTML = "Cadastro realizado com sucesso! Redirecionando para o login..."; // Exibindo a mensagem no DOM
            status_cadastro.innerHTML += "<br><div class='loader'></div>";

            setTimeout(() => {
                mostrarDiv('div_login');
                status_cadastro.innerHTML = "";
            }, 2000);

        } else {
            status_cadastro.innerHTML = "Houve um erro ao cadastrar, tente novamente mais tarde...";
        }
    } catch (erro) {
        console.warn("Erro ao cadastrar usuário:", erro);
    }
}