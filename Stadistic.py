class Stadistic:

    def __init__(self, time, typep):
        self.time = time
        self.typep = typep
        self.number = 0

    def calculate_call(self, list_calls):
        for call_in in list_calls:
            if call_in.typep == "Call":
                ##print(call_in.typep)
                self.time = self.time + call_in.duration
                self.number = self.number + 1
        return self

    def calculate_conference(self, list_calls):
        for call_in in list_calls:
            if call_in.typep == "Conference":
                ##rint(call_in.typep)
                self.time = self.time + call_in.duration
                self.number = self.number + 1
        return self
