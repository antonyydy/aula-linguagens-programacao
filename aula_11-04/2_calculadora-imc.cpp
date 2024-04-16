#include <iostream>
using namespace std;

int main() {
    double peso, altura, imc;
    string classificacao;

    // Solicita ao usuário o peso e a altura
    cout << "Digite seu peso em kg: ";
    cin >> peso;
    cout << "Digite sua altura em metros: ";
    cin >> altura;

    // Calcula o IMC
    imc = peso / (altura * altura);

    // Classifica o IMC
    if (imc < 18.5) {
        classificacao = "Baixo peso";
    } else if (imc < 25) {
        classificacao = "Peso normal";
    } else if (imc < 30) {
        classificacao = "Sobrepeso";
    } else {
        classificacao = "Obesidade";
    }

    // Imprime o IMC e a classificação
    cout << "Seu IMC é " << imc << " e sua classificação é: " << classificacao << endl;

    return 0;
}
