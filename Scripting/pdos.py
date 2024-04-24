import numpy as np
import matplotlib.pyplot as plt

class PDOSPlotter:
    def __init__(self):
        pass

    def load_data(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        data_start_index = None
        for i, line in enumerate(lines):
            if line.startswith("#"):
                data_start_index = i + 1
                break

        if data_start_index is None:
            raise ValueError("Invalid file format. Data not found after header.")

        data = np.loadtxt(file_path, skiprows=data_start_index)

        return data[:, 0], data[:, 1:]

    def get_aopdos(self, files, fermi_energy):
        aopdos_data = {}
        for name, (color, file_path) in files.items():
            energy, pdos = self.load_data(file_path)
            shifted_energy = energy - fermi_energy
            aopdos_data[name] = {"Energy": shifted_energy, "PDOS": pdos, "Color": color}
        return aopdos_data

    def plot_aopdos(self, aopdos_data, xlim=None, ylim=None):
        for name, data in aopdos_data.items():
            energy = data["Energy"]
            pdos = data["PDOS"]  # Get PDOS data
            color = data["Color"]
    
            # Check if PDOS data has only one column
            if pdos.shape[1] == 1:
                plt.fill_between(energy, np.ravel(pdos), color=color, alpha=0.5, label=name)
            else:
                # If PDOS data has two columns, assume it contains pdosup and pdosdw
                pdosup = pdos[:, 0]
                pdosdw = -1 * pdos[:, 1]
                plt.fill_between(energy, pdosup, color=color, alpha=0.5, label=f"{name}")
                plt.fill_between(energy, pdosdw, color=color, alpha=0.5)
    
        plt.ylabel("PDOS (a.u.)", fontweight="bold")
        plt.xlabel("E - E$_f$ (eV)", fontweight="bold")
        plt.axvline(x=0, color='gray', linestyle='--')
        plt.legend()
    
        if xlim is not None:
            plt.xlim(xlim)
        if ylim is not None:
            plt.ylim(ylim)
    
        plt.show()
# How to use
# make sure the aopdos.sh has be run to get the atomic orbitals PDOS, the files should be written like 
# (Atoms)_(orbitals).dat

#plotter = PDOSPlotter()
#files = {
#        "Br_s": ("blue", "../work/Pol_PDOS_Pure/(Br)_(s).dat"),
#        "Br_p": ("green", "../work/Pol_PDOS_Pure/(Br)_(p).dat"),
#        "Cs_s": ("orange", "../work/Pol_PDOS_Pure/(Cs)_(s).dat"),
#        "Cs_p": ("red", "../work/Pol_PDOS_Pure/(Cs)_(p).dat"),
#        "Cs_d": ("magenta", "../work/Pol_PDOS_Pure/(Cs)_(d).dat"),
#        "Pb_s": ("purple", "../work/Pol_PDOS_Pure/(Pb)_(s).dat"),
#        "Pb_p": ("brown", "../work/Pol_PDOS_Pure/(Pb)_(p).dat"),
#        "Pb_d": ("black", "../work/Pol_PDOS_Pure/(Pb)_(d).dat")
#    }

#fermi_energy = 3.5926

#aopdos_data = plotter.get_aopdos(files, fermi_energy)
#plotter.plot_aopdos(aopdos_data, xlim=(-5, 5), ylim=(-80, 80))