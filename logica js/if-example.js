const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Digite um número: ', (input) => {
    const a = parseInt(input);

    if (a > 50) {
        console.log('maior que 50');
    } else {
        console.log('menor ou igual a 50');
    }

    readline.close();
});