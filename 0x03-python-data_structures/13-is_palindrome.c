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
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;

	listint_t **stack = malloc(sizeof(listint_t *));
	int top = -1;

	while (fast != NULL && fast->next != NULL)
	{
		stack[++top] = slow;

		slow = slow->next;
		fast = fast->next->next;
	}

	while (top >= 0 && slow != NULL)
	{
		if (stack[top]->n != slow->n)
		{
			free(stack);
			return (0);
		}

		top--;
		slow = slow->next;
	}

	free(stack);
	return (1);
}
