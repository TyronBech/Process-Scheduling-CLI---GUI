import tkinter as tk

class Input_text(object):
    def __init__(self, window, initial_text):
        self.Text_label = tk.Label(window, text=initial_text, font=("Arial", 10), bg="#B6BBC4")
        self.Text_label.pack(padx=20, pady=3)
        self.input_txt = tk.Text(window, height=1, width=40)
        self.input_txt.pack(padx=10, pady=5)
    def get_text(self):
        return self.input_txt.get(1.0, "end-1c")

class Process(object):
    def __init__(self, p_id, at, bt, pr=0):
        self.p_id = p_id
        self.at = at
        self.bt = bt
        self.pr = pr
        self.ct = 0
        self.tt = 0
        self.wt = 0
    def CTTWT(self, com, tt, wt):
        self.com = com
        self.tt = tt
        self.wt = wt

class FCFS(object):
    def __init__(self, _processes):
        self.processes = _processes
        self.processes = sorted(self.processes, key=lambda x: x.at)
        time_sum = sum(process.bt for process in self.processes)
        j = 0
        queue = list()
        self.completion = list()
        time = 0
        while time < time_sum:
            while j < len(self.processes) and time >= self.processes[j].at:
                queue.append(self.processes[j])
                j += 1
            if len(queue) != 0:
                processing = queue[0].bt
                while processing > 0:
                    processing -= 1
                    time += 1
                self.completion.append(time)
                queue.pop(0)
            else:
                time += 1
                time_sum += 1
        self.TTWT()
        self.Display()
    def TTWT(self):
        TT = 0
        for i in range(len(self.processes)):
            TT = self.completion[i] - self.processes[i].at
            self.processes[i].CTTWT(self.completion[i], TT, (TT - self.processes[i].bt))
    def Display(self):
        frame = tk.Frame(window, width=650, height=500)
        header_labels = ["Process ID", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"]
        for col, header in enumerate(header_labels):
            Data_label = tk.Label(frame, text=header, font=("Arial", 10, "bold"),
                                  height=1, width=15, fg='white', anchor='center', justify='center', bg="#31304D", relief='solid', border=1)
            Data_label.grid(row=0, column=col)
        for row, process in enumerate(self.processes):
            for col, attr in enumerate(["p_id", "at", "bt", "com", "tt", "wt"]):
                Data_label = tk.Label(frame, text=getattr(process, attr), font=("Arial", 10),
                                      height=1, width=15, bg="#F0ECE5", anchor='center', justify='center', relief='solid', border=1)
                Data_label.grid(row=row + 1, column=col)
        frame.pack()

def retrieved():
    global processes
    global Arrival
    global Burst
    
    arrival_values = list(map(int, Arrival.get_text().split()))
    burst_values = list(map(int, Burst.get_text().split()))
    
    if len(arrival_values) == len(burst_values):
        processes = FCFS([Process(p_id=p_id + 1, at=at, bt=bt) for p_id, (at, bt) in enumerate(zip(arrival_values, burst_values))])

window = tk.Tk()
window.title("Process Scheduling")
window.geometry("900x700")
window.config(background="#B6BBC4")

Arrival = Input_text(window, "Enter arrival time")
Burst = Input_text(window, "Enter burst time")

submit_button = tk.Button(window, text="submit", height=1, width=10, command=retrieved)
submit_button.pack(padx=10, pady=5)

window.mainloop()
