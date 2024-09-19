#include <stdio.h>

int main() {
  int INDICE = 13, SOMA = 0, K = 0;

while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}

printf("O valor da soma é:%d\n", SOMA); 

return 0;

}


//Explicação:

K começa com 0 e é incrementado até 13.
A cada iteração, o valor de K é somado a SOMA.
Após o término, o valor de SOMA será a soma de todos os números de 1 a 13, ou seja:

SOMA=1+2+3+⋯+13=91
Resultado: O valor de SOMA será 91. //