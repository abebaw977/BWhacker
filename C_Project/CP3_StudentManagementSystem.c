#include <stdio.h>

struct Student {
  int ID;
  char Name[100];
  int Age;
  char Department[100];
  float CGPA;
};
int check=0;
int count = 0;

void validation(int Id);
void DisplaySTD(struct Student s[50], int st[], int c);
int main() {
  struct Student student[50];
  int EX = 1;
  int id;
  int choice;
  int st[50];
  while (EX) {
    printf("\n==============================\n");
    printf("Student Management System\n");
    printf("==============================\n");
    printf("1. Add Student\n");
    printf("2. Display Students\n");
    printf("3. Search Student\n");
    printf("4. Update Student\n");
    printf("5. Delete Student\n");
    printf("0. Exit\n");
    printf("$ ");
    scanf("%d", &choice);
    if (choice == 3) {
      printf("Enter Student ID: ");
      scanf("%d", &id);    
      validation(student[id].ID);
      if (student[id].ID>0) {
        printf("Student ID: %d\n", student[id].ID);
        printf("Student Name: %s\n", student[id].Name);
        printf("Student Age: %d\n", student[id].Age);
        printf("Student Department: %s\n", student[id].Department);
        printf("Student CGPA: %.2f\n", student[id].CGPA);
      } else {
        printf("Student not found \n");
      }
    } else if (choice == 1) {
      count += 1;
      printf("Enter Student ID: ");
      scanf("%d", &id);
      student[id].ID = id;
      st[count] = id;
      printf("Enter Student Name: ");
      scanf("%s", student[id].Name);
      printf("Enter Student Age: ");
      scanf("%d", &student[id].Age);
      printf("Enter Student Department: ");
      scanf("%s", student[id].Department);
      printf("Enter Student CGPA: ");
      scanf("%f", &student[id].CGPA);
    } else if (choice == 2) {
      DisplaySTD(student, st, count);
    } else if (choice == 4) {
      printf("Enter Student ID: ");
      scanf("%d", &id);
      validation(student[id].ID);
      if (check) {
        printf("Enter Student Name: ");
        scanf("%s", student[id].Name);
        printf("Enter Student Age: ");
        scanf("%d", &student[id].Age);
        printf("Enter Student Department: ");
        scanf("%s", student[id].Department);
        printf("Enter Student CGPA: ");
        scanf("%f", &student[id].CGPA);
      } else {
        printf("Student not found\n");
      }
    } else if (choice == 0) {
      printf("\nBye");
      EX = 0;
    }
  }
  return 0;
}

void validation(int Id) { check = (Id > 0 ? 1 : 0); }
void DisplaySTD(struct Student s[50], int st[], int c) {
  if (c == 0) {
    printf("No students found.\n");
  } else {
    printf("------------------------------------------------------------\n");
    printf("ID       Name                 Age    Department         CGPA\n");
    for (int i = 1; i < (c + 1); i++) {
      printf("%d        %s                 %d          %s            %d\n",
             s[st[i]].ID, s[st[i]].Name, s[st[i]].Age, s[st[i]].Department,
             s[st[i]].CGPA);
    }
    printf("------------------------------------------------------------");
  }
}