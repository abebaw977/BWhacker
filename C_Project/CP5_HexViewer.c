#include <stdio.h>

int main() {
  char fileN[50];
  int exist = 1;
  printf("=====================================\n");
  printf("            Hex Viewer\n");
  printf("=====================================\n");
  while (exist != 0) {
    printf("Enter file name: ");
    scanf("%s", fileN);
    FILE* file = fopen(fileN, "rb");
    if (file == NULL) {
      perror("Error");
    } else {
      int byte;
      printf("\n  [?] File = %s => Hex data ====> \n\n ", fileN);
      while ((byte = fgetc(file)) != EOF) {
        printf("%02X ", byte);
      }
      fclose(file);
      exist = 0;
    }
  }
  return 0;
}
