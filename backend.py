from gui import RemoteGUI

# TODO: change print error messages for entry getters so they display a gui warning


class Backend():
    def __init__(self, GUI: RemoteGUI):
        self.gui = GUI
        self.gui.setStopButtonFunction(self.emergencyStop)
        self.gui.setSendButtonFunction(self.sendTorque)
        self.gui.setStepUpButtonFunction(self.stepUp)
        self.gui.setStepDownButtonFunction(self.stepDown)

        self.gui.setTorqueEntry(0.0)
        self.gui.setTargetTorque(0.0)
        self.gui.setActualTorque(0.0)   # might also have to sent an initial 0 trq command

    def getInputTorque(self):
        text = self.gui.getTorqueEntry()
        try:
            return float(text)
        except ValueError:
            raise ValueError("non-value torque input")     # make also show warning on gui display

    def getStepValue(self):
        text = self.gui.getStepEntry()
        try:
            return float(text)
        except ValueError:
            raise ValueError("non-value step input")     # make also show warning on gui display

    def sendTorque(self, torque=None):
        try:
            if (torque is None):
                torque = self.getInputTorque()
        except ValueError:
            print("command not sent")      # replace this with either another error message on gui, or combine with other
        else:
            print(torque)                      # TODO: make this send to car using scripts
            self.gui.setTargetTorque(torque)  # shouldnt update if there are errors

    def emergencyStop(self):
        self.sendTorque(0.0)     # needs to make sure it actually sends?
        self.gui.setTorqueEntry(0.0)
        print("emergency stop signal")        # TODO: implement actual emergency stop signal

    def stepUp(self):
        try:
            increment = self.getStepValue()
            current = self.getInputTorque()
        except ValueError:
            print("torque not changed")     # also change this to act with deeper step->float error
        else:
            self.gui.setTorqueEntry(current + increment)

    def stepDown(self):  # minimum torque is 0
        try:
            decrement = self.getStepValue()
            current = self.getInputTorque()
        except ValueError:
            print("torque not changed")   # change this like with stepUp
        else:
            if (current - decrement < 0):
                self.gui.setTorqueEntry(0.0)
            else:
                self.gui.setTorqueEntry(current - decrement)
