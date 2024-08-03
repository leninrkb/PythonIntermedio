import numpy as np
import pyaudio
import scipy.signal as signal

# Parámetros del ecualizador
RATE = 44100  # Frecuencia de muestreo
CHUNK = 1024  # Tamaño del buffer de audio
LOW_CUTOFF = 300.0  # Frecuencia de corte para el filtro pasa bajos
HIGH_CUTOFF = 3000.0  # Frecuencia de corte para el filtro pasa altos
ORDER = 5  # Orden del filtro

def design_filter(cutoff, filter_type='low'):
    nyquist = 0.5 * RATE
    normal_cutoff = cutoff / nyquist
    b, a = signal.butter(ORDER, normal_cutoff, btype=filter_type, analog=False)
    return b, a

def apply_filter(data, b, a):
    return signal.lfilter(b, a, data)

# Diseño de los filtros
b_low, a_low = design_filter(LOW_CUTOFF, 'low')
b_high, a_high = design_filter(HIGH_CUTOFF, 'high')

# Inicializar PyAudio
p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    # Convertir el flujo de bytes a numpy array
    audio_data = np.frombuffer(in_data, dtype=np.float32)

    # Aplicar filtros
    low_filtered = apply_filter(audio_data, b_low, a_low)
    high_filtered = apply_filter(audio_data, b_high, a_high)

    # Mezclar las señales filtradas (por ejemplo, sumándolas)
    output_data = low_filtered + high_filtered

    # Convertir de nuevo a flujo de bytes
    out_data = output_data.astype(np.float32).tobytes()
    return (out_data, pyaudio.paContinue)

# Abrir el flujo de audio
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

print("Ecualizador en tiempo real iniciado. Presiona Ctrl+C para detener.")

# Iniciar el flujo
stream.start_stream()

try:
    while stream.is_active():
        pass
except KeyboardInterrupt:
    print("Deteniendo el ecualizador en tiempo real.")

# Detener y cerrar el flujo
stream.stop_stream()
stream.close()
p.terminate()
