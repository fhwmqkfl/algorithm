#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("input : ");
    printf("output: ");
    //첫번째
    for (int i =0, n = strlen(s); i < n ; i++)

    //두번째 for (int i =0; s[i] != '\0' ; i++);
    {
        printf("%c",s[i]);
    }
    printf("\n");
}