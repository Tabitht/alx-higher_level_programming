#include "lists.h"
/**
 * check_cycle - to check if a linked list has cycle or not
 * @list: list to check
 * Return: return 1 if true and 0 if false
 */
int check_cycle(listint_t *list){
	listint_t *holder;
	if (list == NULL){
		return (0);
	}
	holder = list;
	while (holder != list){
		holder = holder->next;
	}
	if (holder->next == list){
		return (1);
	}
	return (0);
}
