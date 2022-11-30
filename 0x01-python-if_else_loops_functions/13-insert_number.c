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
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	listint_t *current;

	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;

		while (current->next != NULL && current->next->n < new_node->n)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
	new_node->n = number;
	new_node->next = NULL;

	return (new_node);
}
