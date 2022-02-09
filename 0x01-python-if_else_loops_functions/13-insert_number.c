#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head
 * @number: nbr to be inserted
 * Return: listint_t*
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *present, *new, *previous = NULL;

	if (head == NULL)
		return (NULL);
	present = *head;
	while (present != NULL)
	{
		if (present->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			if (present != NULL)
				previous->next = new;
			new->next = present;
			if (present == *head)
				*head = new;
			new->n = number;
			return (new);
		}
		previous = present;
		present = present->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
		*head = new;
	else
		previous->next = new;
	new->next = NULL;
	new->n = number;
	return (new);
}
