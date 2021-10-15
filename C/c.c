#include <unistd.h>

void    ft_putnbr(int number)
{
    if (number > 9)
        ft_putnbr(number / 10);
    write(1, &"0123456789"[number % 10], 1);
}

int     main()
{
    int i;
    int flag;

    i = 1;
    while (i <= 100)
    {
        flag = 0;
        if (number % 3 == 0)
        {
            write(1, "fizz", 4);
            flag++;
        }
        if (number % 5 == 0)
        {
            write(1, "buzz", 4);
            flag++;
        }
        if (flag)
            ft_putnbr(i);
        i++;
    }
}