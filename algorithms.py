class FCFS(object):
    def __init__(self, _processes):
        self.processes = _processes
        self.computation(self.processes)
    def computation(self, processes):
        time_sum = sum(process.bt for process in processes)
        j = 0
        queue = list()
        time = 0
        while time < time_sum:
            while j < len(processes) and time >= processes[j].at:
                queue.append(processes[j])
                j += 1
            if len(queue) > 0:
                processing = queue[0].bt
                while processing > 0:
                    processing -= 1
                    time += 1
                queue[0].TTWT(time)
                queue.pop(0)
            else:
                time += 1
                time_sum += 1
class SJF(object):
    def __init__(self, _processes):
        self.processes = _processes
        self.computation(self.processes)
    def computation(self, processes):
        time_sum = sum(process.bt for process in processes)
        j = 0
        queue = list()
        time = 0
        while time < time_sum:
            while j < len(processes) and time >= processes[j].at:
                queue.append(processes[j])
                j += 1
            if len(queue) > 0:
                queue.sort(key= lambda x: (x.bt, x.at, x.p_id))
                processing = queue[0].bt
                while processing > 0:
                    processing -= 1
                    time += 1
                queue[0].TTWT(time)
                queue.pop(0)
            else:
                time += 1
                time_sum += 1
class NPP(object):
    def __init__(self, _processes):
        self.processes = _processes
        self.computation(self.processes)
    def computation(self, processes):
        time_sum = sum(process.bt for process in processes)
        j = 0
        queue = list()
        time = 0
        while time < time_sum:
            while j < len(processes) and time >= processes[j].at:
                queue.append(processes[j])
                j += 1
            if len(queue) > 0:
                queue.sort(key= lambda x: (x.pr, x.at, x.p_id))
                processing = queue[0].bt
                while processing > 0:
                    processing -= 1
                    time += 1
                queue[0].TTWT(time)
                queue.pop(0)
            else:
                time += 1
                time_sum += 1
class SRTF(object):
    def __init__(self, _processes):
        self.processes = _processes
        self.computation(self.processes)
    def computation(self, processes):
        time_sum = sum(process.bt for process in processes)
        j = 0
        queue = list()
        time = 0
        while time < time_sum:
            while j < len(processes) and time == processes[j].at:
                queue.append(processes[j])
                j += 1
            if len(queue) > 0:
                queue.sort(key= lambda x: (x.temp_bt, x.at, x.p_id))
                queue[0].temp_bt -= 1
                time += 1
                if queue[0].temp_bt == 0:
                    queue[0].TTWT(time)
                    queue.pop(0)
            else:
                time += 1
                time_sum += 1
class PP(object):
    def __init__(self, _processes):
        self.processes = _processes
        self.computation(self.processes)
    def computation(self, processes):
        time_sum = sum(process.bt for process in processes)
        j = 0
        queue = list()
        time = 0
        while time < time_sum:
            while j < len(processes) and time == processes[j].at:
                queue.append(processes[j])
                j += 1
            if len(queue) > 0:
                queue.sort(key= lambda x: (x.pr, x.at, x.p_id))
                queue[0].temp_bt -= 1
                time += 1
                if queue[0].temp_bt == 0:
                    queue[0].TTWT(time)
                    queue.pop(0)
            else:
                time += 1
                time_sum += 1
class RR(object):
    def __init__(self, _processes, quantum):
        self.processes = _processes
        self.computation(self.processes, quantum)
    def computation(self, processes, quantum):
        time_sum = sum(process.bt for process in processes)
        j = 0
        queue = list()
        time = 0
        start = 0
        while time < time_sum:
            while j < len(processes) and time == processes[j].at:
                queue.append(processes[j])
                j += 1
            if len(queue) > 0:
                if start >= quantum:
                    queue.append(queue[0])
                    queue.pop(0)
                    start = 0
                start += 1
                time += 1
                queue[0].temp_bt -= 1
                if queue[0].temp_bt == 0:
                    queue[0].TTWT(time)
                    queue.pop(0)
                    start = 0
            else:
                time += 1
                time_sum += 1