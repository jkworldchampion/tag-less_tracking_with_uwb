#### This is a 8 methods for tag-less tracking with UWB
#### The methods are: total energy (TE), maximal amplitude (MA), 
# normalized strongest path energy (SPE), SNR, rise time (RT), 
# MED, root- mean-square delay spread (RDS) and kurtosis (KUR)


import numpy as np
from scipy.stats import kurtosis

def calculate_total_energy(data):
    """
    Calculate the total energy of a signal waveform.
    :param data: A list or numpy array containing the discrete samples of the signal.
    :return: Total energy of the signal.
    """
    total_energy = np.sum(np.abs(data)**2)
    return total_energy

def calculate_max_amplitude(data):
    """
    Calculate the maximum amplitude of a signal waveform.
    :param data: A list or numpy array containing the discrete samples of the signal.
    :return: Maximum amplitude of the signal.
    """
    max_amplitude = np.max(np.abs(data))
    return max_amplitude

def calculate_normalized_strongest_path_energy(data):
    """
    Calculate the normalized strongest path energy of a signal waveform.
    :param data: A list or numpy array containing the discrete samples of the signal.
    :return: Normalized strongest path energy.
    """
    total_energy = calculate_total_energy(data)
    max_amplitude = calculate_max_amplitude(data)
    normalized_energy = (max_amplitude ** 2) / total_energy if total_energy != 0 else 0
    return normalized_energy

def calculate_signal_to_noise_ratio(data, noise_variance):
    """
    Calculate the signal-to-noise ratio (SNR) of a signal waveform.
    :param data: A list or numpy array containing the discrete samples of the signal.
    :param noise_variance: The variance of the noise (sigma^2).
    :return: Signal-to-noise ratio in dB.
    """
    max_amplitude = calculate_max_amplitude(data)
    snr = 10 * np.log10((max_amplitude ** 2) / (2 * noise_variance)) if noise_variance != 0 else float('inf')
    return snr

def calculate_rise_time(data, sampling_times):
    """
    Calculate the rise time of a signal waveform.
    :param data: A list or numpy array containing the discrete samples of the signal.
    :param sampling_times: A list or numpy array containing the sampling times corresponding to each sample.
    :return: Rise time of the signal.
    """
    max_amplitude = calculate_max_amplitude(data)
    t_start_indices = np.where(np.abs(data) >= 0.1 * max_amplitude)[0]
    t_stop_indices = np.where(np.abs(data) >= 0.9 * max_amplitude)[0]
    if len(t_start_indices) == 0 or len(t_stop_indices) == 0:
        return None
    t_start = sampling_times[t_start_indices[0]]
    t_stop = sampling_times[t_stop_indices[0]]
    rise_time = t_stop - t_start
    return rise_time

def calculate_kurtosis(data):
    """
    Calculate the kurtosis of a signal waveform.
    :param data: A list or numpy array containing the discrete samples of the signal.
    :return: Kurtosis of the signal.
    """
    return kurtosis(data)

def calculate_mean_excess_delay(data, sampling_times):
    """
    Calculate the mean excess delay of a signal waveform.
    :param data: A list or numpy array containing the discrete samples of the signal.
    :param sampling_times: A list or numpy array containing the sampling times corresponding to each sample.
    :return: Mean excess delay of the signal.
    """
    power = np.abs(data) ** 2
    total_power = np.sum(power)
    if total_power == 0:
        return 0
    mean_excess_delay = np.sum(sampling_times * power) / total_power
    return mean_excess_delay

def calculate_rms_delay_spread(data, sampling_times):
    """
    Calculate the root-mean-square (RMS) delay spread of a signal waveform.
    :param data: A list or numpy array containing the discrete samples of the signal.
    :param sampling_times: A list or numpy array containing the sampling times corresponding to each sample.
    :return: RMS delay spread of the signal.
    """
    power = np.abs(data) ** 2
    total_power = np.sum(power)
    if total_power == 0:
        return 0
    mean_excess_delay = calculate_mean_excess_delay(data, sampling_times)
    mean_square_delay = np.sum((sampling_times ** 2) * power) / total_power
    rms_delay_spread = np.sqrt(mean_square_delay - mean_excess_delay ** 2)
    return rms_delay_spread