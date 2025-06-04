# 🔐 Encriptación con Algoritmos Clásicos

Este proyecto es una aplicación web educativa construida con **Python (Flask)** que permite cifrar y descifrar mensajes usando algoritmos clásicos de criptografía como:

- Cifrado **César**
- Cifrado **Vigenère**
- Cifrado **Playfair**
- Descifrado automático de Vigenère usando el **método de Kasiski**

## 🎯 Objetivo

El propósito de esta aplicación es facilitar la comprensión y visualización de cómo funcionan estos algoritmos criptográficos tradicionales. Además de permitir cifrar/descifrar mensajes, también ofrece detalles intermedios como los pasos de cifrado y claves deducidas en el caso del análisis Kasiski.

---

## ⚙️ Tecnologías utilizadas

- **Python 3**
- **Flask** (framework web)
- **HTML5/CSS3/JS**
- **Jinja2** (motor de plantillas)

---

## 🚀 Funcionalidades principales

### 🔸 Cifrado César
- Cifrado y descifrado con desplazamiento numérico personalizado.
- Visualización paso a paso del cifrado.

### 🔸 Cifrado Vigenère
- Cifrado y descifrado con clave alfabética.
- Mensajes solo alfabéticos.

### 🔸 Cifrado Playfair
- Cifrado y descifrado con clave alfabética.
- Manejo automático de letras repetidas y pares incompletos.

### 🔸 Método de Kasiski
- Análisis automático para deducir la posible longitud de clave.
- Estimación de la clave y descifrado automático del texto cifrado con Vigenère.
- Muestra de repeticiones encontradas y frecuencias asociadas.

---

## 🧪 Ejecución del proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/NiltonRamosE/algoritmos_encriptacion.git
   cd algoritmos_encriptacion
