#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Stack:
    """An implementation of a Stack"""
    
    def __init__(self):
        self._element=[]

    
    def isEmpty(self):
        """
        Return True if the stack is empty, False otherwise
        """
        return self._element==[]
    
    def push(self, element):
        """
        Push an element into the stack
        return the stack
        """
        self._element.append(element)
        return self
    
    def pop(self):
        """
        pop an element from the stack
        return the poped element
        """
        pop_element=self._element[-1]
        self._element=self._element[:-1]
        return pop_element

    def summit(self):
        """
        red the top element of the stack without removing it.
        return the top element.
        """

        return self._element[-1]

    def size(self):
        """
        read the size of the stack
        return the size as an integer.
        """
        return len(self._element)
        
    def show(self):
        return tuple(self._element)