TQ = 4


class Processes:
    PROCESS_COUNT = 0

    def __init__(self, program):
        Processes.PROCESS_COUNT += 1
        self.pid = Processes.PROCESS_COUNT
        self.program = program
        self.signalCount = 0
        if program == 'PA':
            self.burst = 10
            self.priority = 2
            self.tick = 0
        elif program == 'PB':
            self.burst = 7
            self.priority = 3
            self.tick = 0
        else:
            self.burst = 5
            self.priority = 1

    def execute(self):
        if self.program == 'PC':
            if self.burst < TQ:
                execute_time = self.burst
                self.burst = 0
                return execute_time
            else:
                self.burst -= TQ
                execute_time = TQ
                return execute_time
        else:
            if self.burst < TQ:
                execute_time = self.burst
                self.tick += execute_time
                self.burst = 0
                return execute_time
            else:
                self.burst -= TQ
                execute_time = TQ
                self.tick += execute_time
                return execute_time

    def check_if_generate_new_process(self):
        if self.tick >= 3:
            self.tick -= 3
            return True
        else:
            return False

    def get_burset(self):
        return self.burst

    def get_pid(self):
        return self.pid

    def get_signalCount(self):
        return self.signalCount

    def signaled(self):
        self.signalCount += 1
