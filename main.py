from process import Processes


def Solution(initP: list):
    # p1 = Processes('PA')
    # p2 = Processes('PB')
    readyQ1, readyQ2, readyQ3, allProcesses = init(initP)
    t = 0
    timeSequence = {}
    while len(readyQ1) + len(readyQ2) + len(readyQ3) > 0:
        if len(readyQ1) > 0:
            p = readyQ1[0]
            t += p.execute()
            timeSequence[t] = p.pid
            if p.get_burset() == 0:
                # terminate
                readyQ1.pop()
                continue
            else:
                # rejoin
                readyQ1.pop()
                readyQ1.append(p)
                continue
        elif len(readyQ2) > 0:
            p = readyQ2[0]
            t += p.execute()
            timeSequence[t] = p.pid
            if p.check_if_generate_new_process():
                newProcess = Processes('PB')
                readyQ3.append(newProcess)
                p.signaled()
                allProcesses.append(newProcess)
            if p.get_burset() == 0:
                # terminate
                readyQ2.pop(0)
                continue
            else:
                # rejoin
                readyQ2.pop(0)
                readyQ2.append(p)
                continue
        elif len(readyQ3) > 0:
            p = readyQ3[0]
            t += p.execute()
            timeSequence[t] = p.pid
            if p.check_if_generate_new_process():
                p.signaled()
                newProcess = Processes('PC')
                allProcesses.append(newProcess)
                readyQ1.append(newProcess)
            if p.get_burset() == 0:
                # terminate
                readyQ3.pop(0)
                continue
            else:
                # rejoin
                readyQ3.pop(0)
                readyQ3.append(p)
                continue

    print("The Number of Signals received by each Process is as follows:")
    for p in allProcesses:
        print('p' + str(p.get_pid()) + ':' + str(p.get_signalCount()))
    print("The Gantt Chart is as follows:")
    printGanttChart(timeSequence)


def init(processes: list):
    # to store the processes which priority = 1
    readyQ1 = []
    # to store the processes which priority = 2
    readyQ2 = []
    # to store the processes which priority = 3
    readyQ3 = []
    allProcess = []

    for i in processes:
        p = Processes(i)
        allProcess.append(p)
        if i == 'PA':
            readyQ2.append(p)
        elif i == 'PB':
            readyQ3.append(p)
        elif i == 'PC':
            readyQ1.append(p)

    return readyQ1, readyQ2, readyQ3, allProcess


def printGanttChart(timeSequence: dict):
    line = ""
    content = '|'
    timeline = '0'
    for i in timeSequence:
        content += '\tp' + str(timeSequence[i]) + '\t|'
        timeline += '\t\t' + str(i)
    for _ in range(len(timeline)):
        line += "--"
    print(line)
    print(content)
    print(line)
    print(timeline)


if __name__ == '__main__':
    # please input the initial data as following
    # in order, for example p1 running program PA
    processes = ['PA', 'PB']
    Solution(processes)
