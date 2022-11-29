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
	listint_t *new_node, *tmp = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	new_node->next = tmp->next;
	tmp->next = new_node;
	return (new_node);
}
