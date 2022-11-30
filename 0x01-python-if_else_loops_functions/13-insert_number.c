#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into
 * a sorted singly linked list
 * @head: first node of the linked list
 * @number: int to be inserted
 *
 * Return: address of new node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = NULL;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}
	if (new_node->n < current->next->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL && current->next->n < new_node->n)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
