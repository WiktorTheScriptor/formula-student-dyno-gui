import matplotlib
matplotlib.use("Agg")  # Disable Tk backend

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class TorquePlotter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None
        self.time = None
        self.torque = None

    def load_data(self):
        self.data = pd.read_csv(self.filepath)
        self.time = self.data["time"].values
        self.torque = self.data["torque"].values

    def _finalize_plot(self, filename):
        plt.xlabel("Time")
        plt.ylabel("Torque")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

    def display_linear(self, filename="plot.png"):
        plt.figure()
        plt.title("Linear Plot (Point-to-Point)")
        plt.plot(self.time, self.torque, marker='o', linestyle='-')
        self._finalize_plot(filename)

    def display_step(self, filename="plot.png"):
        plt.figure()
        plt.title("Step Plot")
        plt.step(self.time, self.torque, where="mid")
        self._finalize_plot(filename)

    def display_equation(self, degree=5, filename="plot.png"):
        coeffs = np.polyfit(self.time, self.torque, degree)
        poly = np.poly1d(coeffs)

        smooth_time = np.linspace(min(self.time), max(self.time), 500)
        smooth_torque = poly(smooth_time)

        plt.figure()
        plt.title("Equation Fit Plot")
        plt.plot(self.time, self.torque, 'o', label="Data")
        plt.plot(smooth_time, smooth_torque, label=f"Poly Fit (deg {degree})")
        plt.legend()
        self._finalize_plot(filename)

if __name__ == "__main__":
    plotter = TorquePlotter("data.csv")
    plotter.load_data()

    plotter.display_linear("linear.png")
    plotter.display_step("step.png")
    plotter.display_equation(5, "equation.png")
