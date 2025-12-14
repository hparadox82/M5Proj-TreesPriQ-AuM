import heapq
from operator import is_
class TriageSys:
    #pri-q based triage system, prioritizes severity (higher = more severe). ties broken by FIFO order.

    _arrival_counter = 0

    def __init__(self):
        self._queue=[]

    @classmethod
    def _next_arrival_order(cls):

        #gets next arrival seq number

        cls._arrival_counter+=1
        return cls._arrival_counter

    def is_empty(self):
        #checks if triage queue is empty, returns true if empty
        return len(self._queue)==0

    def size(self):
        #no. of patients in queue
        return len(self._queue)

    def clear(self):
        #removes patients from queue
        self._queue=[]

    def add_patient(self, name, severity):
        #adds patient + severity code, checks for invalid severity code input

        if not name:
            raise ValueError("Patient name must be filled in.")
        if not isinstance(severity, int) or not (1<=severity<=5):
            raise ValueError("Severity code must be an integer between 1 and 5.")

        #get arrival order
        arrival_order=self._next_arrival_order()

        #prioritizing higher severity utilizing "negative" severity, if severities are equal then compares arrival order.
        entry = (-severity, arrival_order, name)
        heapq.heappush(self._queue, entry)

    def peek_next(self):
        #returns name/severity without removing, none if empty
        if self.is_empty():
            return None
        neg_severity, _, name = self._queue[0]
        return (name, -neg_severity)

    def process_next(self):
        #rem+ret name/severity of highest pri patient, none if empty.
        if self.is_empty():
            return None
        neg_severity, _, name=heapq.heappop(self._queue)
        return(name, -neg_severity)




