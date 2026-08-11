#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/stat.h>
#include <time.h>

void Banner();
void ListCurDir();
void Export();
void Recuresive(char Folder[], int depth);
void Search(char path[], char F_p[],int* count,int* i);
char Folde[1000];
char space[100];
int depth = 1;
int getChoice(void);
int main() {
  int choice, exit = 0,count,i;
  int *Pc=&count;
  int *Pi=&i;
  char path[100],pattern[100];
  while (exit != 1) {
    Banner();
    choice = getChoice();
switch (choice) {

    case 1:
        ListCurDir();
        break;

    case 2:
        printf("Enter directory path: ");
        scanf("%s", path);

        Recuresive(path, 1);
        break;

    case 3:
        printf("Enter directory path: ");
        scanf("%s", path);

        printf("Enter search file text (.txt or file.txt or file): ");
        scanf("%s", pattern);

        Search(path, pattern, &count, &i);

        if (i) {
            printf("\nTotal found: %d\n", count);
        } else {
            printf("\n[!] Not found\n");
        }
        break;

    
    case 4:
        Export();
        break;
    case 0:
        printf("\nBye\n");
        return 0;

    default:
        printf(" [!] Please enter a valid value:\n ");
        break;
}
  }
  return 0;
}

void Banner() {
  printf("╔════════════════════════════════════════╗\n");
  printf("║          FILE MANAGER MENU             ║\n");
  printf("╚════════════════════════════════════════╝\n");
  printf("1. List Directory\n");
  printf("2. Displag Tree\n");
  printf("3. Search File\n");
  printf("4. Export Listing\n");
  printf("0. Exit\n");
  printf("$ ");
}
int getChoice(void)
{
    char input[100];
    char *end;
    long value;
    /*if(fgets(input, sizeof(input), stdin) == NULL) {
        return -1;
    }*/
    scanf("%99s", input);
    errno = 0;
    value = strtol(input, &end, 10);
    if (end == input) {
        return -1;
    }
    while (*end == ' ' || *end == '\t') {
        end++;
    }
    if (*end != '\n' && *end != '\0') {
        return -1;
    }
    if (errno == ERANGE || value < 0 || value > 8) {
        return -1;
    }
    //while(getchar() != '\n');
    return (int)value;
}
void ListCurDir() {
  char FPath[100];
  printf("Enter file path: ");
  scanf("%s",FPath);
  DIR* dir = opendir(FPath);
  if (dir == NULL) {
    perror("opendir");
    exit(0);
  }
  struct dirent* di;
  while ((di = readdir(dir)) != NULL) {
    printf("[*] %s\n", di->d_name);
  }
  closedir(dir);
}

void Recuresive(char Folder[], int depth) {
  DIR* dir1 = opendir(Folder);
  if (dir1 == NULL) {
    perror("opendir");
exit(0);
  }
  struct dirent* di1;
  while ((di1 = readdir(dir1)) != NULL) {
    if (strcmp(di1->d_name, ".") == 0 || strcmp(di1->d_name, "..") == 0) {
      continue;
    }

    char indent[100] = "";
    for (int i = 0; i < depth; i++) {
      strcat(indent, "  ");
    }
    printf("%s[%s] %s\n", indent, di1->d_type == DT_DIR ? "D" : "F",
           di1->d_name);
    if ((di1->d_type == DT_DIR) == 1) {
      char NewFolder[1024];
      snprintf(NewFolder, sizeof(NewFolder), "%s/%s", Folder, di1->d_name);
      Recuresive(NewFolder, depth + 1);
    }
  }
  closedir(dir1);
}

void Search(char path[], char F_p[],int* count,int* i) {
    DIR *S_dir=opendir(path);
    if (S_dir == NULL){
       perror("Error message");
       //exit(0);
    }
    struct dirent* S_Dir;
    //printf("\n Path %s\n ",path);
    while ((S_Dir = readdir(S_dir)) != NULL) {
       char fullP[100];
       snprintf(fullP, sizeof(fullP), "%s/%s", path, S_Dir->d_name);
      if (strcmp(S_Dir->d_name, ".") == 0 || strcmp(S_Dir->d_name, "..") == 0) {
          continue;
        }
       if ((S_Dir->d_type == DT_DIR) == 1) {
           Search(fullP,F_p,count,i);
       }else if(S_Dir->d_type == DT_REG){
           if (strstr(S_Dir->d_name,F_p)){
               printf("Found: %s%s \n",fullP,S_Dir->d_name);
               (*count) +=1;
               (*i)=1;
        }
      }
    }
  closedir(S_dir);
}
void Export(){
  char FPath[100];
  printf("Enter file path: ");
  scanf("%s",FPath);
  char Name[100];
  time_t now = time(NULL);
  struct tm *t = localtime(&now);

  snprintf(Name, sizeof(Name),
             "Export-%04d-%02d-%02d-%02d:%02d:%02d.log",
             t->tm_year + 1900,
             t->tm_mon + 1,
             t->tm_mday,
             t->tm_hour,
             t->tm_min,
             t->tm_sec);

  DIR* dir = opendir(FPath);
  FILE* file=fopen(Name, "w");
  
  if (dir == NULL) {
    perror("opendir");
    exit(0);
  }
  struct dirent* di;
  struct stat st;
  while ((di = readdir(dir)) != NULL) {
    stat(di->d_name,&st);
    fprintf(file,"[*] %s %ld\n", di->d_name,st.st_size);
  }
  printf("The date exported to %s File\n",Name);
  fclose(file);
  closedir(dir);
}