#include <stdbool.h>
#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - function that checks if singly list is a pal
 * @head: first node
 *
 * Return: 1 if true else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next;
	bool is_palindrome = true;

	if (head == NULL)
	{
		return (1);
	}
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (prev != NULL && is_palindrome)
	{
		is_palindrome = (prev->n == slow->n);
		prev = prev->next;
		slow = slow->next;
	}
	slow = *head;
	prev = NULL;

	while (slow != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	return (is_palindrome);
}
