function pesquisa_produto() {
    let input = document.getElementById('barra_de_pesquisa').value
    input = input.toLowerCase();
    let x = document.getElementsByClassName('produto');

    for (i = 0; i < x.length; i++) {
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="";
        }
    }
}

function AbrirModal(nome, preco, descricao, quantidade, imagem){

    document.getElementById('modal').style.display = 'block'
    document.getElementById('imagem').src = '../' + imagem
    document.getElementById('nome').innerHTML = 'Nome: ' + nome
    document.getElementById('descricao').innerHTML = descricao
    document.getElementById('preco').innerHTML = 'R$ ' + preco
    document.getElementById('quantidade').innerHTML = 'Quantidade: ' + quantidade
}

function FuncaoModal(tipo){
    if (tipo == "editar"){
        
    }
}