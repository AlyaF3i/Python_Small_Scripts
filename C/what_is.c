int ft_chartype(char c)
{
    if (c >= '0' && c <= '9')
        return (0);
    else if (c >= 'A' && c <= 'Z')
        return (1);
    else if (c >= 'a' && c <= 'z')
        return (2);
    else
        return (3);
}

char    *ft_strcapitalize(char *str)
{
    int i;
    int curr_char_type;
    int prev_char_type;

    prev_char_type = ft_chartype(str[0]);
    curr_char_type = 0;
    i = 0;
    if (prev_char_type == 2)
        str[0] -= 32;
    while (str[++i])
    {
        curr_char_type = ft_chartype(str[i]);
        if (curr_char_type == 2 && prev_char_type == 3)
            str[i] -= 32;
        else if(curr_char_type == 1 && prev_char_type != 3)
            str[i] += 32;
        prev_char_type = curr_char_type
    }
    return (str);
}