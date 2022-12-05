#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function that checks if singly list is a pal
 * @head: first node
 *
 * Return: 1 if true else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head;
	int *numbers, i = 0, j;

	if (*head == NULL)
		return (1);

	numbers = malloc(1024 * sizeof(int));
	if (numbers == NULL)
		return (0);

	while (node != NULL)
	{
		numbers[i] = node->n;
		node = node->next;
		i++;
	}

	for (j = 0; j < i / 2; j++)
		if (numbers[j] != numbers[i - j -1])
		{
			free(numbers);
			return (0);
		}

	free(numbers);
	return (1);
}
