import scipy.constants as sc


# bohr radius
a0 = sc.physical_constants["Bohr radius"][0]  # m
# speed of light
c = sc.c  # m/s
# Planck's constant
h = sc.Planck  # J s
# reduced Planck's constant
hbar = sc.hbar  # J s
E_h = sc.physical_constants["Hartree energy"][0]  # J
E_ry = sc.physical_constants["Rydberg constant times hc in J"][0]  # J


Ry2v = a0 * E_ry / hbar
H2v = a0 * E_h / hbar

if __name__ == "__main__":
    v_Ry = int(input("velocity in Ry: ")) / 10000
    print(f"{v_Ry * Ry2v * sc.pico / sc.angstrom:.3f}")
