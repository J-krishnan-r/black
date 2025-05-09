import numpy as np
import matplotlib.pyplot as plt

# Constants (in SI units)
h = 6.62607015e-34  # Planck's constant (J·s)
c = 2.99792458e8    # Speed of light (m/s)
k = 1.380649e-23    # Boltzmann constant (J/K)

# Planck's Law: Spectral radiance as a function of wavelength and temperature
def plancks_law(wavelength, temperature):
    """
    Calculate spectral radiance of a black body at given temperature.
    
    Parameters:
        wavelength (float or np.array): Wavelength in meters.
        temperature (float): Temperature in Kelvin.
    
    Returns:
        Spectral radiance in W·sr⁻¹·m⁻³.
    """
    exponent = (h * c) / (wavelength * k * temperature)
    return (2.0 * h * c**2) / (wavelength**5 * (np.exp(exponent) - 1.0))

# Wavelength range: 100 nm to 3000 nm (converted to meters)
wavelengths = np.linspace(100e-9, 3000e-9, 500)

# Temperature in Kelvin
temperature = 5800  # Approximate surface temperature of the Sun

# Calculate spectral radiance
radiance = plancks_law(wavelengths, temperature)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(wavelengths * 1e9, radiance, label=f"T = {temperature} K", color='orange')
plt.title("Black Body Radiation Spectrum")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral Radiance (W·sr⁻¹·m⁻³)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
