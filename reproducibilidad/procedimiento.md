# Procedimiento de reproduccion y verificacion

## Lo que puede reproducirse con esta copia

La red de ejemplo, la lectura del codigo benigno M-001, el metodo de control de integridad y la metodologia experimental. **No** se incluyen imagenes de disco, contenido exacto del corpus sintetico, un servidor HTTP turnkey ni los PCAP originales. Por tanto, no debe prometerse reproducibilidad end-to-end automatizada a partir de este ZIP.

## Secuencia recomendada

1. Preparar un host KVM/libvirt de laboratorio y comprobar que no tenga datos productivos.
2. Crear una red interna segun `arquitectura/red/steallab-net.example.xml` (ajustando IPs/reservas a cada host) y verificar que no aparece `<forward>`; no anadir NAT o bridge fisico.
3. Definir dos VMs Linux con **una sola interfaz** en esa red, IPs previstas `10.10.10.20` (analisis) y `10.10.10.30` (servicio), servicio HTTP benigno interno en el puerto 8080. La VM Windows no es requisito y no fue implementada en la investigacion.
4. Crear snapshots base de las dos VMs; registrar los identificadores reales.
5. Preparar **solo** archivos ficticios `DEMO`/`NO REAL`; para M-001 deben usarse los cuatro nombres explicitos definidos en el script y el directorio `/opt/steallab/m001/datos_demo`.
6. Inspeccionar codigo, contenido ficticio, listener HTTP y conexiones previstas antes de lanzar pruebas. Registrar precondiciones y hashes.
7. Ejecutar solo la simulacion permitida M-001 cuando el ambiente cumpla las precondiciones; recoger stdout, JSON, logs y PCAP filtrado y comprobar que solo aparece trafico previsto.
8. Para M-002 a M-005, consultar resultados historicos resumidos: **los scripts de ejecucion completos no estan adjuntos** y las pruebas no deben darse por reproducidas a partir de este procedimiento conceptual.
9. Registrar excepciones, metadatos anonimizados y nuevos hashes; no sustituir evidencias historicas ni afirmar identidad de nuevas ejecuciones.

## Comprobar el repositorio ORIGINAL del autor

Si se dispone de los 171 ficheros originales y del manifiesto autentico, ejecutar el verificador de solo lectura:

```bash
python3 herramientas/verificar_evidencias_locales.py \
  --root /ruta/TFM_StealLab \
  --manifest /ruta/TFM_StealLab/05_resultados/cierre_20260808/MANIFEST_SHA256_04_EVIDENCIAS.txt
```

Este comando **no funcionara sobre este borrador publico** porque deliberadamente no contiene las 171 evidencias. La verificacion hecha sobre el original por el autor arrojo 171/171 correctos el 16 de octubre de 2026.
