# Punto de entrada: Menú en consola (Tema 1), Polimorfismo (Tema 2) y try/except/finally (Tema 4)
import os
import sys

# Asegura que Python encuentre los paquetes dentro de src/ sin importar desde dónde se ejecute
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from excepciones.errores_clinicos import DniInvalidoError, DatoClinicoInvalidoError
from modelo.paciente import Paciente
from modelo.ficha_atencion import FichaAtencion
from servicio.gestor_centro_salud import GestorCentroSalud


def mostrar_menu() -> None:
    print("\n========================================================")
    print("  SISTEMA DE TRIAJE Y FARMACIA - CENTRO DE SALUD PAIJÁN ")
    print("========================================================")
    print("1. Registrar nuevo paciente")
    print("2. Registrar ficha de triaje y dispensación")
    print("3. Listar personas registradas (Polimorfismo)")
    print("4. Reporte anonimizado de atenciones (map + Ley 29733)")
    print("5. Filtrar pacientes con fiebre >= 38.0 °C (filter)")
    print("6. Total de medicamentos dispensados (reduce)")
    print("0. Salir")


def main() -> None:
    gestor = GestorCentroSalud()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                dni = input("DNI (8 dígitos): ")
                nombre = input("Nombre completo ficticio: ")
                historia = input("N.° Historia Clínica (ej. HC-1003): ")
                alergias = input("Alergias (Enter si no tiene): ")
                paciente = Paciente(dni, nombre, historia, alergias)
                gestor.registrar_paciente(paciente)
                print(f"[OK] Paciente registrado con DNI protegido: {paciente.get_dni_enmascarado()}")

            elif opcion == "2":
                codigo = input("Código de ficha (ej. FA-003): ")
                historia = input("N.° Historia del paciente (ej. HC-1001): ")
                paciente = gestor.buscar_paciente_por_historia(historia)
                responsable = gestor.centro.get_personal()[0]

                ficha = FichaAtencion(codigo, paciente, responsable)
                peso = float(input("Peso (kg): "))
                talla = float(input("Talla (m, ej. 1.65): "))
                temp_txt = input("Temperatura °C (Enter para 36.5 °C por defecto): ").strip()

                if temp_txt == "":
                    ficha.registrar_triaje(peso, talla)  # Llamada con 2 argumentos
                else:
                    ficha.registrar_triaje(peso, talla, float(temp_txt))  # Llamada con 3 argumentos

                while True:
                    med = input("Nombre de medicamento (o 'fin' para terminar): ").strip()
                    if med.lower() == "fin":
                        break
                    cant = int(input(f"Cantidad de '{med}': "))
                    ficha.agregar_medicamento(med, cant)

                gestor.registrar_ficha(ficha)
                print(f"[OK] Ficha {ficha.get_codigo()} guardada correctamente.")

            elif opcion == "3":
                print("\n--- LISTADO POLIMÓRFICO DE PERSONAS ---")
                personas = gestor.centro.get_personal() + gestor.get_pacientes()
                for p in personas:
                    print(f"- {p.get_nombre_completo()} | DNI: {p.get_dni_enmascarado()} -> {p.obtener_rol()}")

            elif opcion == "4":
                print("\n--- REPORTE ANONIMIZADO DE ATENCIONES (map) ---")
                for linea in gestor.generar_reporte_anonimizado():
                    print(linea)

            elif opcion == "5":
                print("\n--- PACIENTES CON FIEBRE >= 38.0 °C (filter) ---")
                con_fiebre = gestor.filtrar_fichas_con_fiebre()
                if not con_fiebre:
                    print("No hay pacientes con fiebre registrados.")
                for f in con_fiebre:
                    p = f.get_paciente()
                    print(f"- [{f.get_codigo()}] {p.get_nombre_completo()} ({p.get_dni_enmascarado()}) -> {f.get_temperatura_c()} °C")

            elif opcion == "6":
                total = gestor.contar_total_medicamentos()
                print(f"\n[REDUCE] Total de unidades de medicamentos dispensadas: {total}")

            elif opcion == "0":
                print("Cerrando sistema del Centro de Salud Paiján...")
                break
            else:
                print("[AVISO] Opción no válida. Intente nuevamente.")

        except (DniInvalidoError, DatoClinicoInvalidoError) as e:
            print(f"[ERROR DE VALIDACIÓN] {e}")
        except ValueError:
            print("[ERROR DE FORMATO] Ingrese un número válido en peso, talla, temperatura o cantidad.")
        finally:
            print("--- Operación finalizada ---")


if __name__ == "__main__":
    main()