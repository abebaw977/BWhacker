#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <time.h>
#include <string.h>

int main() {
  srand(time(NULL));
  int EX = 0;
  while (EX == 0) {
    int length;
    char g1[]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char g2[]="abcdefghijklmnopqrstuvwxyz";
    char g3[]="0123456789";
    char g4[]="!@#$\%^&*()_-+=[]{}<>?";
    
    printf("Enter password length: ");
    scanf("%d", &length);
    char PassW[length];
    char gA[100] = ""; // Initialize as empty string
    if (length < 4) {
        printf("\nPassword must be greater than 4");
        EX=1;
    }else if (length > 100) {
        printf("\nPassword must be less than 100");
        EX=1;
    }else{
        char U,L,N,S;
        printf("\nInclude uppercase? (Y/N): ");
        scanf(" %c",&U);
        printf("\nInclude lowercase? (Y/N): ");
        scanf(" %c",&L);
        printf("\nInclude numbers? (Y/N): ");
        scanf(" %c",&N);
        printf("\nInclude symbols? (Y/N): ");
        scanf(" %c",&S);
        if (U=='y') {strcat(gA,g1);};
        if (L=='y') {strcat(gA,g2);};
        if (N=='y') {strcat(gA,g3);};
        if (S=='y') {strcat(gA,g4);};
        if (strlen(gA) == 0) {
            printf("\nAt least one character type must be selected.");
            EX=1;
        }
        for (int i=0;i<length;i++){
          PassW[i] =gA[rand() % strlen(gA)];
        };
        printf("\nPassword: %s\n",PassW);
    };
}
  return 0;
}