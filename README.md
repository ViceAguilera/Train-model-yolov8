# Entrenamiento de modelos YOLOv8

Script simplificado para entrenar un modelo de detección de objetos con YOLOv8 (Ultralytics); la configuración incluida define una única clase, `license_plate` (patente vehicular).

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv8-00FFFF?style=flat)
![Estado](https://img.shields.io/badge/estado-terminado-blue?style=flat)
![Licencia](https://img.shields.io/badge/licencia-MIT-blue?style=flat)
![Último commit](https://img.shields.io/github/last-commit/ViceAguilera/Train-model-yolov8?style=flat)

<!-- Demo: agrega una captura o GIF en docs/demo.gif y descomenta la línea siguiente -->
<!-- <p align="center"><img src="docs/demo.gif" alt="Resultados del entrenamiento YOLOv8" width="800"></p> -->

## Tabla de contenidos

- [Descripción](#descripción)
- [Estado del proyecto](#estado-del-proyecto)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)
- [Autor](#autor)

## Descripción

Repositorio de apoyo para entrenar un detector YOLOv8 a partir de un dataset propio en formato YOLO. Parte del modelo preentrenado `yolov8n.pt` e incluye la plantilla de configuración del dataset. Es un código base breve, pensado para reutilizar en distintos experimentos de detección.

## Estado del proyecto

**Terminado.** Código base breve que no recibe mantenimiento activo.

## Características

- Entrenamiento con `yolov8n.pt`: 150 épocas, imagen de 640 px y batch de 16.
- Configuración del dataset en `config.yaml` (clase `license_plate`).
- Estructura de carpetas `train`, `val` y `test` lista para recibir imágenes y etiquetas.

## Tecnologías

- Python 3.11
- [Ultralytics](https://ultralytics.com/) (YOLOv8)
- PyTorch (se sugiere la versión con CUDA 11.8)

## Requisitos

- Python 3.11
- GPU NVIDIA con CUDA recomendada
- Dataset etiquetado en formato YOLO (se recomienda [Roboflow](https://roboflow.com/))

## Instalación

```bash
git clone https://github.com/ViceAguilera/Train-model-yolov8.git
cd Train-model-yolov8
python -m venv venv
source venv/bin/activate        # En Windows: .\venv\Scripts\activate
pip install ultralytics

# PyTorch con CUDA 11.8
pip uninstall -y torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Configuración

1. Completa el `path` de la primera línea de `config.yaml` con la ruta de la carpeta del proyecto.
2. Guarda en `train`, `val` y `test` una carpeta `images` con las imágenes y una carpeta `labels` con los archivos `.txt` de coordenadas de los objetos.
3. Revisa que `val` en `config.yaml` apunte a la carpeta deseada (actualmente apunta a `train/images`).

## Uso

```bash
python train.py
```

Equivalente por CLI (los parámetros se pueden ajustar):

```bash
yolo task=detect mode=train epochs=150 data=config.yaml model=yolov8n.pt imgsz=640 batch=16
```

## Estructura del proyecto

```
train.py        # Script de entrenamiento
config.yaml     # Configuración del dataset y clases
yolov8n.pt      # Pesos preentrenados base
train/ val/ test/   # Carpetas para imágenes y etiquetas (vacías en el repositorio)
```

## Licencia

Distribuido bajo la licencia MIT. Ver [LICENSE](LICENSE).

## Autor

**Vicente Aguilera Arias** — [Portafolio](https://portfolio.iamsirius.cl) · [GitHub](https://github.com/ViceAguilera) · [LinkedIn](https://www.linkedin.com/in/vicenteaguilera/)
