import tkinter as tk
import tkinter.messagebox
from class_module import gui_input, Process
import algorithms as al
class gui_object(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x500")
        self.window.title("Process Scheduling")
        self.window.resizable(False, False)
        main_frame = tk.Frame(self.window, bg="#C499F3")
        main_frame.pack(expand=True, fill=tk.BOTH)
        title = tk.Label(main_frame, text="Process\nScheduling", font=("Helvetica", 20, "bold"), fg="#33186B", bg="#C499F3")
        title.pack(pady=10)
        choices = tk.Label(main_frame, text="Choose an algorithm", font=("Helvetica", 10, "bold"), fg="#33186B", bg="#C499F3")
        choices.pack(pady=10)
        self.fcfs_b = tk.Button(main_frame, text="FCFS", width=10, height=1, command=lambda: self.process_window(algo_title="fcfs"))
        self.fcfs_b.pack(padx=10, pady=7)
        self.sjf_b = tk.Button(main_frame, text="SJF", width=10, height=1, command=lambda: self.process_window(algo_title="sjf"))
        self.sjf_b.pack(padx=10, pady=7)
        self.npp_b = tk.Button(main_frame, text="NPP", width=10, height=1, command=lambda: self.process_window(algo_title="npp", algo=1))
        self.npp_b.pack(padx=10, pady=7)
        self.pp_b = tk.Button(main_frame, text="PP", width=10, height=1, command=lambda: self.process_window(algo_title="pp", algo=1))
        self.pp_b.pack(padx=10, pady=7)
        self.srtf_b = tk.Button(main_frame, text="SRTF", width=10, height=1, command=lambda: self.process_window(algo_title="srtf"))
        self.srtf_b.pack(padx=10, pady=7)
        self.rr_b = tk.Button(main_frame, text="RR", width=10, height=1, command=lambda: self.process_window(algo_title="rr", algo=2))
        self.rr_b.pack(padx=10, pady=7)
        self.window.mainloop()
    def process_window(self, algo_title, algo = 0):
        self.disable()
        self.window.iconify()
        main_window = tk.Toplevel(self.window)
        main_window.geometry("900x700")
        main_window.title("Process Scheduling")
        main_window.resizable(False, False)
        main_frame = tk.Frame(main_window, bg="#C499F3")
        main_frame.pack(expand=True, fill=tk.BOTH)
        Arrival_t = gui_input(main_frame, "Enter Arrival Time")
        Burst_t = gui_input(main_frame, "Enter Burst Time")
        if algo == 1:
            Priority_t = gui_input(main_frame, "Enter Priority Time")
            self.submit_b = tk.Button(main_frame, text="Submit", width=10, height=1,
                                  command=lambda: self.algo(_algorithm=algo_title, frame=main_frame, Arrival=Arrival_t, Burst=Burst_t, Priority=Priority_t, is_pr=True))
            self.submit_b.pack(pady=10)
        elif algo == 2:
            Quantum_t = gui_input(main_frame, "Enter Quantum Time")
            self.submit_b = tk.Button(main_frame, text="Submit", width=10, height=1,
                                  command=lambda: self.algo(_algorithm=algo_title, frame=main_frame, Arrival=Arrival_t, Burst=Burst_t, quantum=Quantum_t))
            self.submit_b.pack(pady=10)
        else:
            self.submit_b = tk.Button(main_frame, text="Submit", width=10, height=1,
                                  command=lambda: self.algo(_algorithm=algo_title, frame=main_frame, Arrival=Arrival_t, Burst=Burst_t))
            self.submit_b.pack(pady=10)
        self.exit_b = tk.Button(main_frame, text="Exit", width=10, height=1, command=lambda: self.exit(main_window))
        self.exit_b.pack(pady=10)

    def algo(self, _algorithm, frame, Arrival, Burst, Priority = None, quantum = None, is_pr = False):
        try:
            processes = []
            arrival_values = None
            burst_values = None
            priority_values = None
            if is_pr:
                arrival_values = list(map(int, Arrival.get_text().split())) 
                burst_values = list(map(int, Burst.get_text().split()))
                priority_values = list(map(int, Priority.get_text().split()))
            else:
                arrival_values = list(map(int, Arrival.get_text().split())) 
                burst_values = list(map(int, Burst.get_text().split()))

            if any(val < 0 for val in arrival_values):
                raise ValueError("Negative numbers are not allowed.")
            
            if len(arrival_values) == len(burst_values):
                if is_pr:
                    if len(arrival_values) == len(priority_values):
                        processes = [Process(p_id=p_id + 1, at=at, bt=bt, pr=pr) for p_id, (at, bt, pr) in enumerate(zip(arrival_values, burst_values, priority_values))]
                    else:
                        raise ValueError("No. of arrival didn't match to no. of priorities")
                else:
                    processes = [Process(p_id=p_id + 1, at=at, bt=bt) for p_id, (at, bt) in enumerate(zip(arrival_values, burst_values))]
                self.submit_b.config(state=tk.DISABLED)
                result = None
                if _algorithm == "fcfs":
                    result = al.FCFS(processes)
                elif _algorithm == "sjf":
                    result = al.SJF(processes)
                elif _algorithm == "npp":
                    result = al.NPP(processes)
                elif _algorithm == "pp":
                    result = al.PP(processes)
                elif _algorithm == "srtf":
                    result = al.SRTF(processes)
                elif _algorithm == "rr":
                    q = list(map(int, quantum.get_text().split()))
                    if len(q) > 1:
                        raise ValueError("Multiple quantum are not allowed.")
                    if q[0] <= 0:
                        raise ValueError("Negative numbers are not allowed.")
                    result = al.RR(processes, quantum=q[0])
                self.Display_table(window=frame, processes=result.processes, pr_flag=is_pr)
            else:
                raise ValueError("No. of arrival didn't match to no. of burst")
        except ValueError as e:
            tkinter.messagebox.showerror("Error", str(e))

    def exit(self, new_window):
        new_window.destroy()
        self.fcfs_b.config(state=tk.NORMAL)
        self.sjf_b.config(state=tk.NORMAL)
        self.npp_b.config(state=tk.NORMAL)
        self.pp_b.config(state=tk.NORMAL)
        self.srtf_b.config(state=tk.NORMAL)
        self.rr_b.config(state=tk.NORMAL)
        self.window.deiconify()

    def Display_table(self, window, processes, pr_flag):
        frame = tk.Frame(window, bg="#C499F3")
        if pr_flag:
            header_labels = ["Process ID", "Arrival Time", "Burst Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"]
            for col, header in enumerate(header_labels):
                Data_label = tk.Label(frame, text=header, font=("Arial", 10, "bold"),
                                    height=1, width=15, fg='white', anchor='center', justify='center', bg="#31304D", relief='solid', border=1)
                Data_label.grid(row=0, column=col, sticky="nsew")

            for row, process in enumerate(processes):
                for col, attr in enumerate(["p_id", "at", "bt", "pr", "ct", "tt", "wt"]):
                    Data_label = tk.Label(frame, text=getattr(process, attr), font=("Arial", 10),
                                        height=1, width=15, bg="#F0ECE5", anchor='center', justify='center', relief='solid', border=1)
                    Data_label.grid(row=row + 1, column=col, sticky="nsew")
        else:
            header_labels = ["Process ID", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"]
            for col, header in enumerate(header_labels):
                Data_label = tk.Label(frame, text=header, font=("Arial", 10, "bold"),
                                    height=1, width=15, fg='white', anchor='center', justify='center', bg="#31304D", relief='solid', border=1)
                Data_label.grid(row=0, column=col, sticky="nsew")

            for row, process in enumerate(processes):
                for col, attr in enumerate(["p_id", "at", "bt", "ct", "tt", "wt"]):
                    Data_label = tk.Label(frame, text=getattr(process, attr), font=("Arial", 10),
                                        height=1, width=15, bg="#F0ECE5", anchor='center', justify='center', relief='solid', border=1)
                    Data_label.grid(row=row + 1, column=col, sticky="nsew")
        frame.pack()
        self.clear_button = tk.Button(frame, text="clear", height=1, width=10, command=lambda: self.clear(frame))
        self.clear_button.grid(row=len(processes) + 2, column=0, columnspan=len(header_labels), pady=5)
        window.update()
    def clear(self, frame):
        frame.destroy()
        self.submit_b.config(state=tk.NORMAL)
        self.clear_button.destroy()
    def disable(self):
        self.fcfs_b.config(state=tk.DISABLED)
        self.sjf_b.config(state=tk.DISABLED)
        self.npp_b.config(state=tk.DISABLED)
        self.pp_b.config(state=tk.DISABLED)
        self.srtf_b.config(state=tk.DISABLED)
        self.rr_b.config(state=tk.DISABLED)
