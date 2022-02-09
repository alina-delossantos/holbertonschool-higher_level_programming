#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head
 * @number: nbr to be inserted
 * Return: adress of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *present_node, *new, *previous = NULL;

	if (head == NULL)
		return (NULL);
	present_node = *head;
	while (present_node != NULL)
	{
		if (present_node->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			if (previous != NULL)
				previous->next = new;
			new->next = present_node;
			if (present_node == *head)
				*head = new;
			new->n = number;
			return (new);
		}
		previous = present_node;
		present_node = present_node->next;
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
