#include <stdio.h>
#include <string.h>
#include <cs50.h>

// int main(void)
// {
//     char s[5];
//     printf("s :");
//     scanf("%s", s);
//     printf("s: %s\n", s);
// }

//phonebook
int main(void)
{
    //Open file
    FILE *file = fopen("phonebook.csv", "a");

    //get string from user
    char *name = get_string("name: ");
    char *number = get_string("number: ");

    // print(wirte) strings to file]
    fprintf(file, "%s,%s\n", name, number);

    // close file
    fclose(file);
}
