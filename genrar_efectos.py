import os
import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine, WhiteNoise

# Crear carpeta si no existe
os.makedirs("uploads", exist_ok=True)

# Lista de efectos simulados
efectos = [
    ("impacto_metalico", 1.3, Sine(800)),
    ("transicion_digital", 2.1, Sine(1200)),
    ("error_sistema", 0.9, Sine(440)),
    ("click_madera", 0.7, Sine(600)),
    ("ambiente_bosque", 8.0, WhiteNoise()),
    ("suspenso_tension", 4.5, Sine(100).to_audio_segment(duration=1000).fade_in(300).fade_out(500)),
    ("caida_vidrio", 3.2, WhiteNoise()),
    ("campana_suave", 2.3, Sine(1000).to_audio_segment(duration=1000).fade_out(500)),
    ("interferencia_radio", 6.4, WhiteNoise()),
    ("risa_diabolica", 5.5, Sine(400).to_audio_segment(duration=300).fade_in(100).fade_out(300))
]

for nombre, duracion, generador in efectos:
    if isinstance(generador, (Sine, WhiteNoise)):
        audio = generador.to_audio_segment(duration=int(duracion * 1000))
    else:
        audio = generador

    # Normalizamos y exportamos
    audio = audio.set_channels(1).set_frame_rate(44100).set_sample_width(2)
    ruta = f"uploads/{nombre}.mp3"
    audio.export(ruta, format="mp3")
    print(f"✅ Generado: {ruta} ({duracion}s)")

print("\n🎧 Todos los efectos fueron generados en la carpeta 'uploads/'.")
