/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asalmarz <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/07/14 03:27:38 by asalmarz          #+#    #+#             */
/*   Updated: 2021/07/14 04:12:51 by asalmarz         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		ft_check(char c, char *charset)
{
	int i;

	i = -1;
	while (charset[++i] != '\0')
		if (charset[i] == c)
			return (1);
	return (0);
}

int		ft_strnbr(char *str, char *charset)
{
	int n;
	int i;

	n = 0;
	i = 0;
	while (str[i])
	{
		while (str[i] && ft_check(str[i], charset) == 1)
			i++;
		if (str[i] && ft_check(str[i], charset) == 0)
			n++;
		while (str[i] && ft_check(str[i], charset) == 0)
			i++;
	}
	return (n);
}

char	**ft_split(char *str, char *charset)
{
	char	**strs;
	int		strcnt;
	int		i;
	int		j;

	strcnt = ft_strnbr(str, charset);
	if (!(strs = (char **)malloc((strcnt + 1) * sizeof(char *))))
		return (0);
	i = 0;
	while (i < strcnt)
	{
		while (*str && ft_check(*str, charset) == 1)
			str++;
		j = 0;
		while (str[j] && ft_check(str[j], charset) == 0)
			j++;
		if (!(strs[i] == (char *)malloc(j + 1)))
			return (0);
		j = 0;
		while (*str && ft_check(*str, charset) == 0)
			strs[i][j++] = *str++;
		strs[i++][j] = 0;
	}
	strs[i] = 0;
	return (strs);
}
