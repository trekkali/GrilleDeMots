#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define TAILLE_GRILLE 5
#define TAILLE_MOTS 4
#define LONGUEUR_MOTS 6

char grille[TAILLE_GRILLE][TAILLE_GRILLE] = {
    {'B', 'O', 'N', 'N', 'E'},
    {'I', 'G', 'O', 'I', 'J'},
    {'E', 'L', 'I', 'O', 'I'},
    {'N', 'Q', 'R', 'S', 'T'},
    {'S', 'V', 'W', 'X', 'Y'}
};

char motsCaches[TAILLE_MOTS][LONGUEUR_MOTS] = {
    "BONNE",
    "BIENS",
    "LOI",
    "NOIR"
};

bool estMotTrouve(char mot[]) {
    for (int i = 0; i < TAILLE_MOTS; i++) {
        if (strcmp(motsCaches[i], mot) == 0) {
            return true;
        }
    }
    return false;
}

int main() {
    printf("Grille de lettres :\n");
    for (int i = 0; i < TAILLE_GRILLE; i++) {
        for (int j = 0; j < TAILLE_GRILLE; j++) {
            printf("%c ", grille[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    int motsRestants = TAILLE_MOTS;
    int motsCachesCount = TAILLE_MOTS;

    printf("Nombre de mots à trouver : %d\n\n", motsCachesCount);

    while (motsRestants > 0) {
        char mot[LONGUEUR_MOTS];
        printf("Entrez un mot caché : ");
        scanf("%s", mot);
        
        if (estMotTrouve(mot)) {
            motsRestants--;
            printf("Le mot '%s' a été trouvé !\n\n", mot);

            if (motsRestants == 1) {
                printf("Il reste 1 mot à trouver.\n\n");
            } else {
                printf("Il reste %d mots à trouver.\n\n", motsRestants);
            }
        } else {
            printf("Le mot '%s' n'a pas été trouvé.\n\n", mot);
        }
    }

    printf("Résultats :\n");
    for (int i = 0; i < motsCachesCount; i++) {
        if (estMotTrouve(motsCaches[i])) {
            printf("Le mot '%s'\n", motsCaches[i]);
        } else {
            printf("Le mot 'Non trouvé'\n");
        }
    }
    
    return 0;
}

