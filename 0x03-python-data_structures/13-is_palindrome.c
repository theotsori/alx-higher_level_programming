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
	if (!head || !*head || !(*head)->next)
		return (1);

	listint_t *slow = *head, *fast = *head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *last = slow, *prev = NULL;

	while (last)
	{
		listint_t *next = last->next;

		last->next = prev;
		prev = last;
		last = next;
	}

	listint_t *first = *head;

	while (prev)
	{
		if (prev->n != first->n)
			return (0);

		prev = prev->next;
		first = first->next;
	}

	return (1);
}
