#include <stdio.h>

// int main(void)
// {
//     int n = 50;
//     int *p = &n;
//     printf("&p\n", p); 
// }

int main(void)
{
    char *s = "EMMA";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
}