#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{
    char command[100];
    char path[100];
    char history[1000][5000];
    int a = 0;

    while (1)
    {
        printf("%s~$ ", getcwd(path, sizeof(path)));
        fflush(stdout);

        if (fgets(command, sizeof(command), stdin) == NULL)
            break;

        command[strcspn(command, "\n")] = '\0';

        if (strlen(command) == 0)
            continue;

        if (a < 1000)
        {
            strcpy(history[a], command);
            a++;
        }

        char *args[50];
        int i = 0;

        char *p = strtok(command, " ");

        while (p != NULL && i < 49)
        {
            args[i] = p;
            i++;
            p = strtok(NULL, " ");
        }

        args[i] = NULL;

        if (args[0] == NULL)
            continue;

        if (strcmp(args[0], "exit") == 0)
        {
            exit(0);
        }

        if (strcmp(args[0], "cd") == 0)
        {
            if (args[1] == NULL)
            {
                printf("cd: missing directory\n");
            }
            else if (chdir(args[1]) == -1)
            {
                perror("cd");
            }

            continue;
        }

        if (strcmp(args[0], "history") == 0)
        {
            for (int h = 0; h < a; h++)
            {
                printf("%d  %s\n", h + 1, history[h]);
            }

            continue;
        }

        pid_t pid = fork();

        if (pid == -1)
        {
            perror("fork");
            continue;
        }

        if (pid == 0)
        {
            execvp(args[0], args);

            perror("execvp");
            exit(1);
        }

        waitpid(pid, NULL, 0);
    }

    return 0;
}
