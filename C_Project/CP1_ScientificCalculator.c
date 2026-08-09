#include <stdio.h>
#include <string.h>
int main() {
  int EX = 1;
  while (EX) {
    printf("Enter first number: ");
    int num1;
    scanf("%d", &num1);
    printf("Enter second number: ");
    int num2;
    scanf("%d", &num2);
    char op[2];
    printf("Enter op: ");
    scanf("%1s", op);

    if (!strcmp("+", op)) {
      printf("%d\n", (num1 + num2));
    } else if (!strcmp("-", op)) {
      printf("%d\n", (num1 - num2));
    } else if (!strcmp("*", op)) {
      printf("%d\n", (num1 * num2));
    } else if (!strcmp("/", op)) {
      if (num2 == 0)
        printf("Cannot divide by zero\n");
      else
        printf("%d\n", num1 / num2);
    } else {
      printf("[!] == > Please Enter valid value < == []\n");
    }
    char x[100];

    printf("Enter 0 to exit or any other key to continue: ");
    scanf("%99s", x);
    if (!strcmp("0", x)) {
      printf("Bye\n");
      EX = 0;
    }
  }
  return 0;
}
