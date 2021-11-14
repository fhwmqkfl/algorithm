#include <stdio.h>

// 하드코딩ver
bool search(node *tree)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (50 < tree->number)
    {
        return search(tree->left);
    }
    else if (50 > tree->number)
    {
        return search(tree->right);
    }
    else if (50 == tree->number)
    {
        return true;
    }
    
}