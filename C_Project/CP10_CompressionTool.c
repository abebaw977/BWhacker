#include <stdio.h>
#include <string.h>

void dcomp(char comp[50], char dcomp[50]) {
  unsigned char count = 1;
  unsigned char byte;
  unsigned char next;

  FILE* fp = fopen(comp, "rb");
  FILE* dc = fopen(dcomp, "wb");
  if (fp == NULL || dc == NULL) {
    printf("File error\n");
    return;
  }

  while (fread(&next, 1, 1, fp) == 1) {
    if (fread(&byte, 1, 1, fp) != 1) {
      break;
    }
    for (int i = 0; i < next; i++) {
      fwrite(&byte, 1, 1, dc);
      printf("\n%c", byte);
    }
  }
  fclose(dc);
  fclose(fp);

  printf("\nDeompressed secssufully finshed !!.");
}
void comp(char comp[50], char dcomp[50]) {
  unsigned char count = 1;
  unsigned char current;
  unsigned char next;
  FILE* fp = fopen(comp, "rb");
  FILE* dc = fopen(dcomp, "wb");
  if (fp == NULL || dc == NULL) {
    printf("File error\n");
    return;
  }
  fread(&current, 1, 1, fp);
  while (fread(&next, 1, 1, fp) == 1) {
    if (current == next) {
      if (count == 255) {
        printf(" Run:  %c Count: %d \n", current, count);
        fwrite(&count, 1, 1, dc);
        fwrite(&current, 1, 1, dc);
        current = next;
        count = 1;
      }
      count++;
    } else {
      printf(" Run:  %c Count: %d \n", current, count);
      fwrite(&count, 1, 1, dc);
      fwrite(&current, 1, 1, dc);
      current = next;
      count = 1;
    }
  }
  fwrite(&count, 1, 1, dc);
  fwrite(&current, 1, 1, dc);

  fclose(dc);
  fclose(fp);
  printf("\nCompressed secssufully finshed !!.");
}
int main(int argc, char* argv[]) {
  if (argc != 4) {
    printf("Usage:\n");
    printf("  Compress:   %s comp <input> <output>\n", argv[0]);
    printf("  Decompress: %s dcomp <input> <output>\n", argv[0]);
    return 1;
  }
  if (!strcmp(argv[1], "comp")) {
    comp(argv[2], argv[3]);
  } else if (!strcmp(argv[1], "dcomp")) {
    dcomp(argv[2], argv[3]);
  } else {
    printf(
        "Usage: \n       For (compress){%s comp fileInput fileOutput},\n       "
        "For (decompress) {%s dcomp fileInput fileOutput}",
        argv[0], argv[0]);
  }
  return 0;
}
