TQ = 4
class Processes:

    def __init__(self, pid, program, arriveTime):
        self.pid = pid
        self.program = program
        if program == 'PA':
            self.burst = 10
            self.priority = 2
        elif program == 'PB':
            self.burst = 7
            self.priority = 3
        else:
            self.burst = 5
            self.priority = 1
        self.arriveTime = arriveTime

    def execute(self):
        self.burst -= TQ

    def get_burset(self):
        return self.burst