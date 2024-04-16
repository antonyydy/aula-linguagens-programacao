let palavra = "Antony";

for (let letra of palavra) {
    console.log('letra:', letra);
}

for (let i = 0; i < palavra.length - 1; i++) {
    console.log('letra', i, ':', palavra[i]);
}