const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Digite seu peso em kg: ', (peso) => {
  rl.question('Digite sua altura em metros: ', (altura) => {
    peso = parseFloat(peso);
    altura = parseFloat(altura);
    
    // Calcula o IMC
    let imc = peso / (altura * altura);

    // Classifica o IMC
    let classificacao = '';
    if (imc < 18.5) {
      classificacao = 'Abaixo do peso';
    } else if (imc < 24.9) {
      classificacao = 'Peso normal';
    } else if (imc < 29.9) {
      classificacao = 'Sobrepeso';
    } else {
      classificacao = 'Obesidade';
    }

    // Imprime o resultado
    console.log(`Seu IMC é ${imc.toFixed(2)} e sua classificação é: ${classificacao}`);
    
    // Fecha a interface `rl`
    rl.close();
  });
});
