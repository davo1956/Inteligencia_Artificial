import numpy as np


class priorityQueue(object):

    """clase para dar la cola de prioridad"""

    def _init_(self,f=lambda x: 1):
        self.queue = []
        self.f = f

    def _str_(self):
        return ' '.join([str(q) for q in self.queue])
    
    def isEmpty(self):
        return self.queue == []

    def push(self, element):
        self.queue.append(element)

    def pop(self):

        #encuentra el elemento de max costo
        min_element = np.argmin([element.f for element in self.queue])

        #guarda el elem max
        item = self.queue[min_element]

        #lo borra de la cola
        del self.queue[min_element]

        return item


