#include <stdbool.h>
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
	{
		return (1);
	}

	listint_t **stack = malloc(sizeof(listint_t *));
	int top = 0;

	listint_t *current = *head;

	while (current != NULL)
	{
		stack[top] = current;
		top++;
		current = current->next;
	}

	current = *head;
	top--;
	while (current != NULL)
	{
		if (current->n != stack[top]->n)
		{
			free(stack);
			return (0);
		}
		current = current->next;
		top--;
	}

	free(stack);
	return (1);
}
