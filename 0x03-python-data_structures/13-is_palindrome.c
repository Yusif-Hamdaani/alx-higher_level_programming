#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct ListNode {
    int val;
    struct ListNode* next;
} ListNode;

/* Function to check if a singly linked list is a palindrome */
int is_palindrome(ListNode** head) {
    /* Initialize two pointers to the head of the list */
    ListNode* slow_ptr = *head;
    ListNode* fast_ptr = *head;

    /* Find the middle of the list using a slow and a fast pointer */
    while (fast_ptr != NULL && fast_ptr->next != NULL) {
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }

    /* Reverse the second half of the list */
    ListNode* prev_ptr = NULL;
    ListNode* curr_ptr = slow_ptr;
    while (curr_ptr != NULL) {
        ListNode* next_ptr = curr_ptr->next;
        curr_ptr->next = prev_ptr;
        prev_ptr = curr_ptr;
        curr_ptr = next_ptr;
    }

    /* Compare the first and second halves of the list */
    ListNode* left_ptr = *head;
    ListNode* right_ptr = prev_ptr;
    while (right_ptr != NULL) {
        if (left_ptr->val != right_ptr->val) {
            return 0;  // not a palindrome
        }
        left_ptr = left_ptr->next;
        right_ptr = right_ptr->next;
    }

    return 1;  // palindrome
}

/* Test the function */
int main() {
    /* Create a singly linked list */
    ListNode* node1 = malloc(sizeof(ListNode));
    ListNode* node2 = malloc(sizeof(ListNode));
    ListNode* node3 = malloc(sizeof(ListNode));
    ListNode* node4 = malloc(sizeof(ListNode));
    ListNode* node5 = malloc(sizeof(ListNode));
    node1->val = 1;
    node1->next = node2;
    node2->val = 2;
    node2->next = node3;
    node3->val = 3;
    node3->next = node4;
    node4->val = 2;
    node4->next = node5;
    node5->val = 1;
    node5->next = NULL;

    /* Check if the list is a palindrome */
    int result = is_palindrome(&node1);
    printf("%d\n", result);  // output: 1 (true)

    /* Free the memory used by the list */
    free(node1);
    free(node2);
    free(node3);
    free(node4);
    free(node5);

    return 0;
}
