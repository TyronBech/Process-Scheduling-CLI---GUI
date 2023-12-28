class Process(object):
    def __init__(self, p_id, at, bt, pr=0):
        self.p_id = p_id
        self.at = at
        self.bt = self.temp_bt = bt
        self.pr = pr
        self.ct = 0
        self.tt = 0
        self.wt = 0
    def TTWT(self, ct):
        self.ct = ct
        self.tt = self.ct - self.at
        self.wt = self.tt - self.bt
class cli_input(object):
    def __init__(self, is_priority = False):
        arrival_t = list(map(int, filter(str.isdigit, input("Enter arrival time: ").split())))
        burst_t = list(map(int, filter(str.isdigit, input("Enter burst time: ").split())))
        if len(arrival_t) == len(burst_t):
            if is_priority:
                priority = list(map(int, filter(str.isdigit, input("Enter priority: ").split())))
                if len(arrival_t) == len(priority):
                    self.raw_input = [Process(p_id=p_id + 1, at=at, bt=bt, pr=pr) for p_id, (at, bt, pr)
                                    in enumerate(zip(arrival_t, burst_t, priority))]
                else:
                    print("Error: Number of arrival times did not match to number of priority")
            else:
                self.raw_input = [Process(p_id=p_id + 1, at=at, bt=bt) for p_id, (at, bt)
                                in enumerate(zip(arrival_t, burst_t))]
        else:
            print("Error: Number of arrival times did not match to number of burst times")

