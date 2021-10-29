#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[4] = {"EMMA", "RODRIGO", "BRAIN", "DAVID"};

    for (int i = 0; i < 4; i++)
    {
        //파이썬, 자바에서는 가능하지만 로우레벨인 c에서는 안됨
        //if (names[i] == "EMMA")
        if (strcmp(names[i], "EMMA")==0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;

}