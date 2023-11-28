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

function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}


//função para chards.js

function renderiza_graph_produtos(){    
    var labels = document.getElementById('labels').textContent;
    var dados = document.getElementById('dados').textContent;

    if (!labels || !dados) {
        console.log("Os dados estão vazios!");
    }else {
        var labels = JSON.parse(labels);
        var dados = JSON.parse(dados);
        // ...
    }
    // Crie o gráfico com Chart.js
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',  // Ou outro tipo de gráfico
        data: {
            labels: labels,
            datasets: [{
                label: 'data de entrada',
                data: dados,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
    });
};    

// function renderiza_graph_produtos(){
//   const ctx = document.getElementById('graph_produtos').getContext('2d');
//   var cores_geradas = gera_cor(qtd=12)
//   const myChart = new Chart(ctx, {
//     type: 'line',

//   });
// }
