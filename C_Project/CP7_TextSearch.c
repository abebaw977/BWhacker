#include <stdio.h>
void Search(char Fname[50], char search[50]);
int main() {
  char Fname[50], search[50];
  printf("Enter file name: ");
  scanf("%s", Fname);
  printf("Enter search pattern: ");
  scanf("%s", search);
  Search(Fname,search);
  return 0;
}
void Search(char Fname[50], char search[50]) {
  FILE* fp = fopen(Fname, "r");
  if (fp == NULL) {
    perror("Error message");
  }
  char fs[256];
  int line = 0;
  char F = 0;
  printf("[?] Finding with : %s\n", search);
  while (fgets(fs, sizeof(fs), fp) != NULL) {
    line += 1;
    char* result = strstr(fs, search);
    if (result != NULL) {
      printf("[%d] %s\n", line, fs);
      F = 1;
    }
  }
  if (F == 0) {
    printf("[!] Not Found with search: %s", search);
  }
  fclose(fp);
}

