Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Idea:
用2个pointers，slow和fast
fast travels 2 times speed as slow
They all set off to go to next item in the linked list
If: there is no cycle: they will never meet again
Else: they will always meet if a cycle exist. Like mixting time of Markov chain random walks.