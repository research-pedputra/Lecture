import numpy as np
import matplotlib.pyplot as plt

class BandStructure:
    def __init__(self):
        self.data = None
        self.fermi_energy = None
        self.k = None
        self.bands = None
        self.high_symmetry_points = None
        self.fig, self.ax = None, None

    def get_bandstructure(self, data, fermi_energy, kpoints):
        self.data = data
        self.fermi_energy = fermi_energy
        self.k = np.unique(data[:, 0])
        self.bands = np.reshape(data[:, 1], (-1, len(self.k)))
        self.high_symmetry_points = kpoints

    def plot_band_structure(self):
        if self.data is None:
            raise ValueError("Band structure data has not been loaded.")
        self.fig, self.ax = plt.subplots(1, 1, figsize=(4,6))
        for i, band in enumerate(self.bands):
            self.ax.plot(self.k, band - self.fermi_energy, linewidth=1, alpha=0.5, color='r')
        self.ax.set_xlim(min(self.k), max(self.k))
        self.ax.set_ylim(-5, 5)
        
        if self.high_symmetry_points is not None:
            x_coords = [x_coord for _, x_coord in self.high_symmetry_points]
            x_labels = [symmetry_point for symmetry_point, _ in self.high_symmetry_points]
            self.ax.set_xticks(x_coords)
            self.ax.set_xticklabels(x_labels)

            for _, x_coordinate in self.high_symmetry_points:
                self.ax.axvline(x=x_coordinate, color='k', linestyle='-', linewidth=1)
        self.ax.set_ylabel("E-E$_f$ (eV)", fontweight='bold')

    def plot_band_number(self, band_number, overlay=True):
        if band_number < 1 or band_number > len(self.bands):
            raise ValueError("Invalid band number.")
        
        if overlay:
            if self.fig is None or self.ax is None:
                self.plot_band_structure()  # Plot the band structure if not plotted already
            self.ax.plot(self.k, self.bands[band_number - 1] - self.fermi_energy, linewidth=1, color='b')
        else:
            fig, ax = plt.subplots(1, 1, figsize=(4,6))
            for i, band in enumerate(self.bands):
                ax.plot(self.k, band - self.fermi_energy, linewidth=1, alpha=0.5, color='r')
            ax.plot(self.k, self.bands[band_number - 1] - self.fermi_energy, linewidth=1, color='b')
            ax.set_xlim(min(self.k), max(self.k))
            ax.set_ylim(-5, 5)
            
            if self.high_symmetry_points is not None:
                x_coords = [x_coord for _, x_coord in self.high_symmetry_points]
                x_labels = [symmetry_point for symmetry_point, _ in self.high_symmetry_points]
                ax.set_xticks(x_coords)
                ax.set_xticklabels(x_labels)
                for _, x_coordinate in self.high_symmetry_points:
                    ax.axvline(x=x_coordinate, color='k', linestyle='-', linewidth=1)
            ax.set_ylabel("E-E$_f$ (eV)", fontweight='bold')
            ax.set_title(f"Band {band_number}")
            plt.show()
    
    def get_band_data_point(self, band_number):
        if band_number < 1 or band_number > len(self.bands):
            raise ValueError("Invalid band number.")
        
        return self.k, self.bands[band_number - 1] - self.fermi_energy
