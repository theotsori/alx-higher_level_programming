#include "lists.h"

/**
 * check_cycle - checks if there are loops
 * in a linked list
 * @list: the lnked list
 * Return: always 0
 */
int check_cycle(listint_t *list)
{
	listint_t *firstP = list, *secondP = list;

	while (secondP && firstP && firstP->next)
	{
		secondP = secondP->next;
		firstP = firstP->next->next;
		if (secondP == firstP)
		{
			return (1);
		}
	}
	return (0);
}
