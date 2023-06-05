#include "lists.h"

/**
 * check_cycle - detects for cycles in linked lists
 * @list: pointer to head node in list
 *
 * Return: 0 if no cycle, 1 otherwise
 * Please note other resource files that work this this file can be found...
 * ... in the resources folder
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = NULL;
	listint_t *slow = NULL;

	if (list == NULL)
		return 0;

	slow = list;
	fast = list->next;

	while (fast != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next;
		if (fast != NULL)
			fast = fast->next;
	}

	return (0);
}
