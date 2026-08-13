#include <stdio.h>
#include <stdlib.h>
void Banner(char filename[50]);
void AnalayseLog();
void File(char filep[50]);
void SearchKey();
void ErrorLine();
void WarnLine();
void Export();
char filep[50];
int R=0;
int main() {
  int exit = 0,ch;
  char value[100];
  char *en;
  File(filep);
  while (!exit) {
    Banner(filep);
    scanf("%99s", value);
    ch=strtol(value ,&en,10);
    if (ch == 1) {
      AnalayseLog();
    } else if (ch == 2) {
      SearchKey();
    } else if (ch == 3) {
      ErrorLine();
    } else if (ch == 4) {
      WarnLine();
    } else if (ch == 5) {
      Export();
    } else if (ch == 6) {
      File(filep);
    } else if (ch == 7) {
      printf("\n GoodBye ");
      break;
    } else {
      printf(" [!] Please Enter valid value \n");
    }
  }
  return 0;
}
void File(char filep[50]) {
  printf("Enter file path: ");
  scanf("%s", filep);
  FILE* file = fopen(filep, "r");
  if (file == NULL) {
    printf("[!] File not found, please enter correct file mame !! .. \n");
    File(filep);
  }
}
void AnalayseLog() {
  FILE* file = fopen(filep, "r");
  char fp[246];
  int info = 0, error = 0, warn = 0, debug = 0, unknown = 0, trace = 0,
      other = 0, total = 0;
  while (fgets(fp, sizeof(fp), file) != NULL) {
    char* resultI = strstr(fp, "INFO");
    if (resultI != NULL) {
      info += 1;
    }
    char* resultW = strstr(fp, "WARNING");
    if (resultW != NULL) {
      warn += 1;
    }
    char* resultE = strstr(fp, "ERROR");
    if (resultE != NULL) {
      error += 1;
    }
    char* resultT = strstr(fp, "TRACE");
    if (resultT != NULL) {
      trace += 1;
    }
    char* resultD = strstr(fp, "DEBUG");
    if (resultD != NULL) {
      debug += 1;
    }
    char* resultU = strstr(fp, "UNKNOWN");
    if (resultU != NULL) {
      unknown += 1;
    }
    if (resultI == NULL && resultW == NULL && resultE == NULL &&
        resultT == NULL && resultD == NULL && resultU == NULL) {
      other += 1;
    }
    total += 1;
  }
  printf("=============================================\n");
  printf("                  LOG REPORT               \n");
  printf("=============================================\n\n");
  printf(" Total events: %d\n\n", total);
  printf(" INFO: %d\n", info);
  printf(" WARNING: %d\n", warn);
  printf(" ERROR: %d\n", error);
  printf(" TRACE: %d\n", trace);
  printf(" DEBUG: %d\n", debug);
  printf(" UNKNOWN: %d\n", unknown);
  printf(" other: %d\n\n", other);
  int arr[7] = {warn, error, debug, other, info, trace, unknown};
  int c = 0;
  int status = 0;
  int a = 0;
  int len = sizeof(arr) / sizeof(0);
  for (int i = 0; i < len; i++) {
    for (int j = 0; j < len; j++) {
      if (arr[i] >= arr[j]) {
        c += 1;
      }
    }

    if (c == 7 || c == 6 || c == 5) {
      if (arr[i] == info) {
        printf("Info %%: %.2f%%\n", ((float)info * 100) / total);
      }
      if (arr[i] == debug) {
        printf("Debug %%: %.2f%%\n", ((float)debug * 100) / total);
      }
      if (arr[i] == warn) {
        printf("Warn %%: %.2f%%\n", ((float)warn * 100) / total);
      }
      if (arr[i] == unknown) {
        printf("Unknown %%: %.2f%%\n", ((float)unknown * 100) / total);
      }
      if (arr[i] == trace) {
        printf("Trace %%: %.2f%%\n", ((float)trace * 100) / total);
      }
      if (arr[i] == other) {
        printf("Other %%: %.2f%%\n", ((float)other * 100) / total);
      }
      if (arr[i] == error) {
        printf("Errors %%: %.2f%%\n", ((float)error * 100) / total);
      }
    }
    c = 0;
  }
  printf("\n=================================\n");
  fclose(file);
}
void SearchKey() {
  FILE* file = fopen(filep, "r");
  char fp[246], search[500];
  printf("Enter search keyword: ");
  scanf("%s", search);
  int line = 0;
  while (fgets(fp, sizeof(fp), file) != NULL) {
    line += 1;
    char* result = strstr(fp, search);
    if (result != NULL) {
        R+=1;
      printf("Line  %4d     |%s", line, result);
    }
  }
  if (R == 0){printf("\n [!] Not match found \n");}
  R=0;
}
void WarnLine() {
  FILE* file = fopen(filep, "r");
  char fp[246];
  printf("              WARNING LINES       ");
  int line = 0;
  while (fgets(fp, sizeof(fp), file) != NULL) {
    line += 1;
    char* result = strstr(fp, "WARNING");
    if (result != NULL) {
        R+=1;
      printf("Line  %4d      |%s", line, result);
    }
  }
    if (R == 0){printf("\n [!] Not match found \n");}
    R=0;
}
void ErrorLine() {
  // char filep[50];
  // File(filep);
  FILE* file = fopen(filep, "r");
  printf("            ERROR LINES       ");
  char fp[246];
  int line = 0;
  while (fgets(fp, sizeof(fp), file) != NULL) {
    line += 1;
    char* result = strstr(fp, "ERROR");
    if (result != NULL) {
        R+=1;
      printf("Line  %4d     |%s", line, result);
    }
  }
    if (R == 0){printf("\n [!] Not match found \n");}
    R=0;
}
void Export() {
  char newf[100];
  FILE* filef = fopen(filep, "r");
  printf("Enter report file name: ");
  scanf("%99s", newf);
  FILE* file = fopen(newf, "w");
  char fp[246];
  int info = 0, error = 0, warn = 0, debug = 0, unknown = 0, trace = 0,
      other = 0, total = 0;
  while (fgets(fp, sizeof(fp), filef) != NULL) {
    char* resultI = strstr(fp, "INFO");
    if (resultI != NULL) {
      info += 1;
    }
    char* resultW = strstr(fp, "WARNING");
    if (resultW != NULL) {
      warn += 1;
    }
    char* resultE = strstr(fp, "ERROR");
    if (resultE != NULL) {
      error += 1;
    }
    char* resultT = strstr(fp, "TRACE");
    if (resultT != NULL) {
      trace += 1;
    }
    char* resultD = strstr(fp, "DEBUG");
    if (resultD != NULL) {
      debug += 1;
    }
    char* resultU = strstr(fp, "UNKNOWN");
    if (resultU != NULL) {
      unknown += 1;
    }
    if (resultI == NULL && resultW == NULL && resultE == NULL &&
        resultT == NULL && resultD == NULL && resultU == NULL) {
      other += 1;
    }
    total += 1;
  }
  fprintf(file,"=============================================\n");
  fprintf(file,"                  LOG analayse                \n");
  fprintf(file,"=============================================\n\n");
  fprintf(file," Total events: %d\n\n", total);
  fprintf(file," INFO: %d\n", info);
  fprintf(file," WARNING: %d\n", warn);
  fprintf(file," ERROR: %d\n", error);
  fprintf(file," TRACE: %d\n", trace);
  fprintf(file," DEBUG: %d\n", debug);
  fprintf(file," UNKNOWN: %d\n", unknown);
  fprintf(file," other: %d\n\n", other);
  
  fprintf(file," [@@@] Persentile \n");
  fprintf(file,"    Info %%: %.2f%%\n", ((float)info * 100) / total);
  fprintf(file,"    Debug %%: %.2f%%\n", ((float)debug * 100) / total);
  fprintf(file,"    Warn %%: %.2f%%\n", ((float)warn * 100) / total);
  fprintf(file,"    Unknown %%: %.2f%%\n", ((float)unknown * 100) / total);
  fprintf(file,"    Trace %%: %.2f%%\n", ((float)trace * 100) / total);
  fprintf(file,"    Other %%: %.2f%%\n", ((float)other * 100) / total);
  fprintf(file,"    Errors %%: %.2f%%\n", ((float)error * 100) / total);
  fprintf(file,"=============================================");
  printf("Report exported successfully. \n");
  printf("Source : %s ",filep);
  fclose(file);
  fclose(filef);
}
void Banner(char filename[]) {
  printf("\n");
  printf("====================================================\n");
  printf("              LOG ANALYZER\n");
  printf("====================================================\n");

  printf("Current file: %s\n", filename);

  printf("----------------------------------------------------\n");
  printf("1. Analyze Log File\n");
  printf("2. Search Keyword\n");
  printf("3. Show ERROR Lines\n");
  printf("4. Show WARNING Lines\n");
  printf("5. Export Report\n");
  printf("6. Change Log File\n");
  printf("7. Exit\n");
  printf("~$ ");
}
