# Sistema de Triaje y Dispensación Farmacéutica - Centro de Salud Paiján

Proyecto de Evaluación Parcial — **Lenguajes de Programación (UPN)**  
**Estudiante:** Joseph Thomas Cumpa Silva (`N00556388`)  
**Docente:** Ing. Edgard Vílchez Valdez  

## Descripción
Aplicación de consola en Python 3.10+ que modela el flujo de triaje preventivo (peso, talla, IMC, temperatura) y dispensación básica de medicamentos en el **Centro de Salud Paiján**, aplicando programación imperativa, orientada a objetos y funcional, además de la protección de datos personales conforme a la **Ley N.° 29733**.

## Estructura del Proyecto
- `src/excepciones/`: Excepciones personalizadas (`DniInvalidoError`, `DatoClinicoInvalidoError`).
- `src/modelo/`: Clases del dominio (`Persona`, `Paciente`, `PersonalSalud`, `CentroSalud`, `FichaAtencion`, `ItemMedicamento`).
- `src/servicio/`: `GestorCentroSalud` (Patrón Singleton + `filter`, `map`, `reduce` y función pura `calcular_imc`).
- `src/main.py`: Punto de entrada con menú interactivo en consola y manejo de excepciones.
- `docs/`: Diagrama de clases UML (`diagrama-clases.puml` y `diagrama-clases.png`).
- `evidencias/`: Capturas de ejecución y pruebas con fecha y hora.

## Ejecución
```bash
python src/main.py