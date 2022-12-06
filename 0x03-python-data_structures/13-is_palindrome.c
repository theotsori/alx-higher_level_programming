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
	if (*head == NULL)
		return (1);

	listint_t *current = *head;
	int length = 0;

	while (current != NULL)
	{
		length++;
		current = current->next;
	}

	current = *head;

	for (int i = 0; i < length / 2; i++)
	{
		if (current->n != current->next->n)
		return (1);

		current = current->next;
	}

	return (0);
}
