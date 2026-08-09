#include <stdio.h>

int KEY;
int ch;
char K[255];
char Ifile[50];
char Ofile[50];
void Key(char key[255]);
void Bann();
void onlyNum(char key[255]);
void enterFile();
int main() {
  Bann();
  return 0;
}
void Bann() {
  printf("Choose operation:\n");
  printf("1. Encrypt\n");
  printf("2. Decrypt\n");
  printf("$ ");
  onlyNum(K);
  if (ch == 1 || ch == 2) {
    enterFile();
  }else {
    printf("please! Enter vaild value\n");
  }
}
void enterFile() {
  printf("Input file : ");
  scanf("%49s", Ifile);
  while (getchar() != '\n');
  printf("Output file : ");
  scanf("%49s", Ofile);
  while (getchar() != '\n');
  printf("Enter key: ");
  Key(K);
  FILE* fi = fopen(Ifile, "rb");
  FILE* en = fopen(Ofile, "wb");
  if (fi == NULL || en == NULL) {
    printf("Cannot open file.\n");
    return;
  }
  int byte;
  
  while ((byte = fgetc(fi)) != EOF) {
    unsigned char enc = byte ^ KEY;
    fputc(enc, en);
  }
  printf("%s",ch==1 ? "Encryption completed successfully.":"Decryption completed successfully.");
  fclose(en);
  fclose(fi);
}
void onlyNum(char key[255]) {
  while (fgets(key, 255, stdin)) {
    if (sscanf(key, "%d", &ch) == 1) {
      break;
    } else {
      printf("Enter only number ,Try Again: ");
    }
  }
}
void Key(char key[255]) {
  while (fgets(key, 255, stdin)) {
    if (sscanf(key, "%d", &KEY) == 1) {
      if (KEY >= 1 && KEY <= 255) {
        break;
      } else {
        printf("Please! enter only in 1...255: ");
      }
    } else {
      printf("Please! enter only 1...255,Try again: ");
    }
  }
}