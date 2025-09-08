import requests
import time
import json
from pathlib import Path
import statistics

class BackendBenchmark:
    def __init__(self):
        self.js_url = "http://localhost:3000"
        self.python_url = "http://localhost:8000"
        self.results = {
            "js": [],
            "python": []
        }

    def test_backend(self, name: str, base_url: str, file_path: Path, iterations: int = 3):
        """Prueba un backend específico varias veces para obtener un promedio"""
        print(f"\nProbando backend {name}...")
        iteration_results = []

        for i in range(iterations):
            print(f"Iteración {i + 1}/{iterations}")
            
            try:
                # Medir tiempo de subida y procesamiento
                start_time = time.time()
                
                # Subir archivo
                with open(file_path, 'rb') as f:
                    files = {'file': (file_path.name, f, 'text/csv')}
                    response = requests.post(f"{base_url}/upload", files=files)
                    if response.status_code != 200:
                        raise Exception(f"Error en upload: {response.text}")
                
                upload_time = time.time() - start_time

                # Obtener y procesar datos
                process_start = time.time()
                response = requests.get(f"{base_url}/historical")
                if response.status_code != 200:
                    raise Exception(f"Error obteniendo datos históricos: {response.text}")
                
                data = response.json()
                process_time = time.time() - process_start
                total_time = time.time() - start_time

                # Calcular tamaño de respuesta
                response_size = len(response.content) / 1024  # KB

                result = {
                    "upload_time": upload_time,
                    "process_time": process_time,
                    "total_time": total_time,
                    "response_size_kb": response_size,
                    "records_processed": len(data.get('data', [])) if isinstance(data, dict) else 0
                }
                
                iteration_results.append(result)
                print(f"  Tiempo total: {total_time:.2f}s")
                print(f"  Tamaño de respuesta: {response_size:.2f}KB")

            except Exception as e:
                print(f"Error en iteración {i + 1}: {str(e)}")
                continue

        if iteration_results:
            # Calcular promedios
            avg_result = {
                "backend": name,
                "avg_upload_time": statistics.mean(r["upload_time"] for r in iteration_results),
                "avg_process_time": statistics.mean(r["process_time"] for r in iteration_results),
                "avg_total_time": statistics.mean(r["total_time"] for r in iteration_results),
                "avg_response_size": statistics.mean(r["response_size_kb"] for r in iteration_results),
                "records_processed": iteration_results[0]["records_processed"],
                "iterations": len(iteration_results)
            }
            self.results[name].append(avg_result)
            return avg_result
        return None

    def run_benchmark(self, test_file: Path):
        """Ejecuta el benchmark completo para ambos backends"""
        print(f"Iniciando benchmark usando archivo: {test_file}")
        print(f"Tamaño del archivo: {test_file.stat().st_size / 1024:.2f}KB")
        
        # Probar cada backend
        js_result = self.test_backend("js", self.js_url, test_file)
        python_result = self.test_backend("python", self.python_url, test_file)

        # Generar reporte comparativo
        if js_result and python_result:
            print("\n=== Reporte Comparativo ===")
            print(f"{'Métrica':<20} {'JavaScript':<15} {'Python':<15} {'Diferencia %':<15}")
            print("-" * 65)
            
            metrics = [
                ("Tiempo de subida", "avg_upload_time", "s"),
                ("Tiempo proceso", "avg_process_time", "s"),
                ("Tiempo total", "avg_total_time", "s"),
                ("Tamaño respuesta", "avg_response_size", "KB")
            ]
            
            for name, key, unit in metrics:
                js_value = js_result[key]
                py_value = python_result[key]
                diff_percent = ((py_value - js_value) / js_value) * 100
                print(f"{name:<20} {js_value:,.2f}{unit:<10} {py_value:,.2f}{unit:<10} {diff_percent:>+.1f}%")

            # Guardar resultados detallados
            with open('benchmark_results.json', 'w') as f:
                json.dump({
                    "test_file": str(test_file),
                    "file_size_kb": test_file.stat().st_size / 1024,
                    "results": {
                        "javascript": js_result,
                        "python": python_result
                    }
                }, f, indent=2)
            print("\nResultados detallados guardados en benchmark_results.json")

if __name__ == "__main__":
    print("=== Benchmark de Backends CSV ===")
    print("Asegúrate de que ambos servidores estén corriendo:")
    print("- JavaScript: http://localhost:3000")
    print("- Python: http://localhost:8000")
    
    # Usar el archivo test_data.csv existente
    test_file = Path("test_data.csv")
    if not test_file.exists():
        print("Error: No se encontró el archivo test_data.csv")
    else:
        benchmark = BackendBenchmark()
        benchmark.run_benchmark(test_file)
