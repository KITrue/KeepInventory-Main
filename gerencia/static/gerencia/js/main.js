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