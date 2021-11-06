#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char *i =  get_string("i : ");
    char *j = get_string("j : ");

    printf("%p\n", i);
    printf("%p\n", j);

    if (*i==*j)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
