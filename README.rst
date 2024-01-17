Template for the Read the Docs tutorial
=======================================

def calculate_electronegativity(element):
    pauling_scale = {
        'H': 2.20, 'He': None, 'Li': 0.98, 'Be': 1.57, 'B': 2.04, 'C': 2.55, 'N': 3.04,
        'O': 3.44, 'F': 3.98, 'Ne': None, 'Na': 0.93, 'Mg': 1.31, 'Al': 1.61, 'Si': 1.90,
        'P': 2.19, 'S': 2.58, 'Cl': 3.16, 'Ar': None, 'K': 0.82, 'Ca': 1.00, 'Sc': 1.36,
        'Ti': 1.54, 'V': 1.63, 'Cr': 1.66, 'Mn': 1.55, 'Fe': 1.83, 'Ni': 1.91, 'Co': 1.88,
        'Cu': 1.90, 'Zn': 1.65, 'Ga': 1.81, 'Ge': 2.01, 'As': 2.18, 'Se': 2.55, 'Br': 2.96,
        'Kr': None, 'Rb': 0.82, 'Sr': 0.95, 'Y': 1.22, 'Zr': 1.33, 'Nb': 1.60, 'Mo': 2.16,
        'Tc': 1.90, 'Ru': 2.20, 'Rh': 2.28, 'Pd': 2.20, 'Ag': 1.93, 'Cd': 1.69, 'In': 1.78,
        'Sn': 1.96, 'Sb': 2.05, 'I': 2.66, 'Te': 2.10, 'Xe': None, 'Cs': 0.79, 'Ba': 0.89,
        'La': 1.10, 'Ce': 1.12, 'Pr': 1.13, 'Nd': 1.14, 'Pm': 1.13, 'Sm': 1.17, 'Eu': 1.20,
        'Gd': 1.20, 'Tb': 1.10, 'Dy': 1.22, 'Ho': 1.23, 'Er': 1.24, 'Tm': 1.25, 'Yb': 1.10,
        'Lu': 1.27, 'Hf': 1.30, 'Ta': 1.50, 'W': 2.36, 'Re': 1.90, 'Os': 2.20, 'Ir': 2.20,
        'Pt': 2.28, 'Au': 2.54, 'Hg': 2.00, 'Tl': 1.62, 'Pb': 2.33, 'Bi': 2.02, 'Th': 1.30,
        'Pa': 1.50, 'U': 1.38, 'Np': 1.36, 'Pu': 1.28, 'Am': 1.30, 'Cm': 1.30, 'Bk': 1.30,
        'Cf': 1.30, 'Es': 1.30, 'Fm': 1.30, 'Md': 1.30, 'No': 1.30, 'Lr': 1.30, 'Rf': None,
        'Db': None, 'Sg': None, 'Bh': None, 'Hs': None, 'Mt': None, 'Ds': None, 'Rg': None,
        'Cn': None, 'Nh': None, 'Fl': None, 'Mc': None, 'Lv': None, 'Ts': None, 'Og': None
    }

    return pauling_scale.get(element, None)

# Calculate the electronegativity of SnO2
electronegativity_Sn = calculate_electronegativity('Sn')
electronegativity_O = calculate_electronegativity('O')

if electronegativity_Sn is not None and electronegativity_O is not None:
    electronegativity_SnO2 = (electronegativity_Sn + 2 * electronegativity_O) / 3
    print(f"Electronegativity of SnO2: {electronegativity_SnO2}")
else:
    print("Unable to calculate electronegativity for SnO2 due to missing data.")
