#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to the first node of the list
 * @number: integer to be inserted into the list
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number){
	listint_t *current, *position, *new_node;
	new_node = malloc(sizeof(listint_t));
	if(!new_node){
		return (NULL);
	}
	new_node->n = number;
	current = *head;
	if (*head == NULL || current->n >= new_node->n){
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current != NULL && new_node->n > current->n){
		position = current;
		current = current->next;
	}
	position->next = new_node;
	new_node->next = current;
	return (new_node);

}
