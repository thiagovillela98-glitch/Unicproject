#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Função que analisa e converte cada caractere para hexadecimal
void analisarCaractere(char c) {
    printf("'%c' -> 0x%02X ", c, (unsigned char)c);
    
    if (isalpha(c)) {
        if (isupper(c)) {
            printf("(letra maiúscula)\n");
        } else {
            printf("(letra minúscula)\n");
        }
    } else if (isdigit(c)) {
        printf("(número)\n");
    } else if (c == ' ') {
        printf("(espaço)\n");
    } else {
        printf("(caractere especial)\n");
    }
}

int main() {
    char texto[256];
    
    printf("Digite um texto: ");
    fgets(texto, sizeof(texto), stdin);
    
    // Remove o '\n' que o fgets adiciona
    texto[strcspn(texto, "\n")] = '\0';
    
    printf("\n=== CONVERSÃO PARA HEXADECIMAL ===\n\n");
    
    // Percorre cada caractere do texto
    for (int i = 0; i < strlen(texto); i++) {
        analisarCaractere(texto[i]);
    }
    
    // Mostra o texto completo em hexadecimal
    printf("\n=== TEXTO COMPLETO EM HEXADECIMAL ===\n");
    for (int i = 0; i < strlen(texto); i++) {
        printf("%02X ", (unsigned char)texto[i]);
    }
    printf("\n");
    
    return 0;
}