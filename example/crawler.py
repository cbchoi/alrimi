from evsim.system_simulator import SystemSimulator
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *

from config import *
import example1

class Crawler(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)

        # Open CSV
        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("PROCESS", 3)

        self.insert_input_port("report")

    def ext_trans(self,port, msg):
        if port == "report":
            self._cur_state = "PROCESS"
            

    def output(self):
        if self._cur_state == "PROCESS":
            # if homework exist
            example1.main()
            print("!!!")
            
        return None

    def int_trans(self):
        if self._cur_state == "PROCESS":
            self._cur_state = "PROCESS"