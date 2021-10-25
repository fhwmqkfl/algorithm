#include <cs50.h>
#include <stdio.h>

//argv[0]는 커멘드라인의 첫번째 명령어 입력됨 
int main(int argc, string argv[])
{
    if (argc !=2)
    {
        printf("missing command-line argument\n");
        return 1;
    }
    print("hello, %s\n", argv[1]);
    return 0;
}