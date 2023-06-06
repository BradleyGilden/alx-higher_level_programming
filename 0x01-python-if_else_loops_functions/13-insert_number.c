#include "lists.h"

/**
 * add_node_beg - adds node at the beginning
 * @head: head node of the list
 * @new: newly created node
 * Return: pointer to head node
 */
listint_t *add_node_beg(listint_t **head, listint_t *new)
{
    new->next = *head;
    *head = new;
    return (*head);
}

/**
 * insert_node - inserts node in sorted linked list
 * @head: head node of the list
 * @number: node data
 * Return: pointer to newly created node
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *ptr = *head;
    listint_t *new, *temp;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;
    if (head == NULL || *head == NULL)
        *head = new;

    while (ptr->next != NULL)
    {   if (ptr->next->next == NULL && new->n > ptr->next->n)
        {
            ptr->next->next = new;
            break;
        }

        if (new->n <= ptr->n && ptr->next == (*head)->next)
        {
            *head = add_node_beg(head, new);
            break;
        }
        if (new->n >= ptr->n && new->n <= ptr->next->n)
        {
            temp = ptr->next;
            ptr->next = new;
            new->next = temp;
            break;
        }
        ptr = ptr->next;
    }

    return (new);
}
