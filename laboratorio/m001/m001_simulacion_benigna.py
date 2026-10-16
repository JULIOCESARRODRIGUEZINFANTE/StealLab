#!/usr/bin/env python3
"""
M-001 simulacion benigna defensiva para StealLab.

Este script NO es malware.
No roba credenciales.
No lee datos reales del sistema.
No accede a navegadores reales.
No accede a wallets reales.
No usa persistencia.
No usa evasion.
No usa C2.
No usa Internet.

Solo procesa ficheros sinteticos DEMO ubicados en:
  /opt/steallab/m001/datos_demo

Y genera resultados locales en:
  /opt/steallab/m001/salida
  /opt/steallab/m001/logs

Tambien realiza una peticion HTTP interna controlada a:
  http://10.10.10.30:8080/
"""

from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import socket
import urllib.request
import sys

BASE = Path("/opt/steallab/m001")
DATOS = BASE / "datos_demo"
SALIDA = BASE / "salida"
LOGS = BASE / "logs"

HTTP_INTERNO = "http://10.10.10.30:8080/"

ARCHIVOS_PERMITIDOS = [
    "credencial_demo.txt",
    "navegador_demo.txt",
    "wallet_demo.txt",
    "sistema_demo.txt",
]

def ahora_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloque in iter(lambda: f.read(8192), b""):
            h.update(bloque)
    return h.hexdigest()

def leer_demo(path: Path) -> dict:
    contenido = path.read_text(encoding="utf-8", errors="replace")
    lineas = contenido.splitlines()
    return {
        "archivo": path.name,
        "bytes": path.stat().st_size,
        "lineas": len(lineas),
        "sha256": sha256_file(path),
        "contiene_demo": "DEMO" in contenido,
        "contiene_no_real": "NO REAL" in contenido,
        "primeras_lineas": lineas[:3],
    }

def peticion_http_interna() -> dict:
    resultado = {
        "url": HTTP_INTERNO,
        "ok": False,
        "status": None,
        "bytes": 0,
        "sha256_respuesta": None,
        "error": None,
    }

    try:
        req = urllib.request.Request(
            HTTP_INTERNO,
            headers={
                "User-Agent": "StealLab-M001-Benign-Simulation/1.0",
                "X-StealLab-Case": "M-001",
                "X-StealLab-Type": "benign-defensive-simulation",
            },
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = resp.read()
            resultado["ok"] = True
            resultado["status"] = getattr(resp, "status", None)
            resultado["bytes"] = len(data)
            resultado["sha256_respuesta"] = hashlib.sha256(data).hexdigest()
    except Exception as exc:
        resultado["error"] = repr(exc)

    return resultado

def main() -> int:
    SALIDA.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)

    log_path = LOGS / "EV-M001-002_ejecucion_preparacion.log"
    resumen_path = SALIDA / "EV-M001-002_resumen_preparacion.json"
    manifiesto_path = SALIDA / "EV-M001-002_manifiesto_archivos.json"
    restricciones_path = SALIDA / "EV-M001-002_restricciones_seguridad.txt"

    inicio = ahora_iso()

    with log_path.open("w", encoding="utf-8") as log:
        log.write("# EV-M001-002 - Log de preparacion de artefacto benigno M-001\n\n")
        log.write(f"inicio_utc={inicio}\n")
        log.write(f"hostname={socket.gethostname()}\n")
        log.write(f"base={BASE}\n")
        log.write(f"datos={DATOS}\n")
        log.write("modo=simulacion_benigna_defensiva\n")
        log.write("restriccion=no_malware_no_c2_no_internet_no_datos_reales\n\n")

        registros = []
        for nombre in ARCHIVOS_PERMITIDOS:
            path = DATOS / nombre
            if not path.exists():
                log.write(f"ERROR faltante={path}\n")
                return 2
            info = leer_demo(path)
            registros.append(info)
            log.write(f"procesado={path} sha256={info['sha256']} bytes={info['bytes']}\n")

        http = peticion_http_interna()
        log.write(f"http_interno_ok={http['ok']} status={http['status']} bytes={http['bytes']} error={http['error']}\n")

    resumen = {
        "id_evidencia": "EV-M001-002",
        "id_muestra": "M-001",
        "tipo": "simulacion_benigna_defensiva",
        "inicio_utc": inicio,
        "fin_utc": ahora_iso(),
        "hostname": socket.gethostname(),
        "datos_origen": str(DATOS),
        "archivos_procesados": registros,
        "http_interno": http,
        "restricciones": [
            "No malware real",
            "No robo de credenciales reales",
            "No lectura de navegadores reales",
            "No lectura de wallets reales",
            "No tokens reales",
            "No C2 real",
            "No Internet",
            "No persistencia",
            "No evasion",
            "Solo datos sinteticos DEMO",
        ],
    }

    resumen_path.write_text(json.dumps(resumen, indent=2, ensure_ascii=False), encoding="utf-8")

    manifiesto = {
        "generado_utc": ahora_iso(),
        "artefactos": [],
    }

    for path in [log_path, resumen_path]:
        manifiesto["artefactos"].append({
            "ruta": str(path),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        })

    restricciones_path.write_text(
        "\n".join([
            "EV-M001-002 - Restricciones de seguridad",
            "",
            "Este artefacto es benigno y defensivo.",
            "No implementa robo de informacion.",
            "No accede a credenciales reales.",
            "No accede a navegadores reales.",
            "No accede a wallets reales.",
            "No usa persistencia.",
            "No usa evasion.",
            "No usa C2.",
            "No usa Internet.",
            "Solo procesa ficheros sinteticos DEMO en /opt/steallab/m001/datos_demo.",
            "La unica comunicacion de red permitida es HTTP interno hacia 10.10.10.30:8080.",
            "",
        ]),
        encoding="utf-8",
    )

    manifiesto["artefactos"].append({
        "ruta": str(restricciones_path),
        "bytes": restricciones_path.stat().st_size,
        "sha256": sha256_file(restricciones_path),
    })

    manifiesto_path.write_text(json.dumps(manifiesto, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps({
        "ok": True,
        "id_evidencia": "EV-M001-002",
        "resumen": str(resumen_path),
        "manifiesto": str(manifiesto_path),
        "log": str(log_path),
        "restricciones": str(restricciones_path),
    }, indent=2, ensure_ascii=False))

    return 0

if __name__ == "__main__":
    sys.exit(main())
