import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
file_path = "s00.csv"  # Update with your file path
df = pd.read_csv(file_path)

# Extract first 150 points of the clean signal
clean_signal = df['clean'][:1500]  # Ensure 'Clean' is a valid column name

# Add synthetic noise to create a noisy signal
noise = np.random.normal(0, 1, len(clean_signal))  # Gaussian noise with mean 0 and std 0.1
noisy_signal = clean_signal + noise  # Noisy version of EEG

# Create subplots: One for Clean Signal, One for Noisy Signal
fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Plot Clean Signal
axs[0].plot(clean_signal, label="Clean Signal", color='blue', alpha=0.8)
axs[0].legend()
axs[0].set_title("Clean EEG Signal")
axs[0].set_ylabel("Amplitude")
axs[0].grid(True)

# Plot Noisy Signal
axs[1].plot(noisy_signal, label="Noisy Signal", color='red', alpha=0.8)
axs[1].legend()
axs[1].set_title("Noisy EEG Signal")
axs[1].set_xlabel("Sample Index")
axs[1].set_ylabel("Amplitude")
axs[1].grid(True)

# Show the plots
plt.tight_layout()
plt.show()
