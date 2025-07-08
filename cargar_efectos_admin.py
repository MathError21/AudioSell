import os
from pydub import AudioSegment
from main import db, Usuario, Efecto, app

# Asegúrate de estar en el contexto de Flask
with app.app_context():
    admin = Usuario.query.filter_by(email="admin@audio.com").first()
    if not admin:
        print("❌ Admin no encontrado en la base de datos.")
        exit()

    carpeta = "uploads"
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".mp3")]

    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)

        if Efecto.query.filter_by(filename=archivo).first():
            print(f"⚠️ Ya existe: {archivo}")
            continue

        audio = AudioSegment.from_file(ruta)
        duracion = round(len(audio) / 1000, 2)  # en segundos
        precio = round(1 + (duracion / 10) * 4, 2)  # entre $1 y $5 aprox

        efecto = Efecto(
            filename=archivo,
            duracion=duracion,
            usuario_id=admin.id,
            estado_venta="aprobado",
            precio=precio
        )
        db.session.add(efecto)
        print(f"✅ Registrado: {archivo} ({duracion}s, ${precio})")

    db.session.commit()
    print("\n🎉 Todos los efectos fueron registrados en la base de datos.")
