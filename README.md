# StealLab

**StealLab** es un laboratorio academico de ciberseguridad para el estudio *defensivo* y reproducible de comportamientos representativos de infostealers mediante **simulaciones benignas**, red controlada y evidencias verificables.

- **Modalidad:** Trabajo Fin de Master, investigacion aplicada / estudio de caso.
- **Autor:** Julio Cesar Rodriguez Infante.
- **Universidad:** Universidad Europea.
**Estado:** proyecto historico cerrado en agosto de 2026; esta publicacion presenta una seleccion tecnica derivada de la evidencia original. No es un detector de malware listo para produccion.

## Memoria entregada

- [PDF oficial del TFM](docs/TFM_StealLab.pdf) — **incorporar exclusivamente** la copia identica de `TFM/TFM_FINAL/TFM_StealLab_IngenieroDeSistemas_JCRI2026.pdf` antes del primer commit.
- Presentacion de defensa: **pendiente** de incorporar la version azul definitiva en PDF; no publicar borradores ni el guion oral.

> Los PDF **no estan incluidos** en este borrador tecnico ZIP; deben copiarse desde el directorio local de publicacion previamente verificado.

## Alcance comprobado

- KVM/libvirt, `StealLab-Net`, segmento `10.10.10.0/24`, bridge `virbr-steal`; configuracion de red sin elemento `<forward>`.
- `VM-LINUX-ANALYSIS` (`10.10.10.20`), `VM-SERVICES-SIM` (`10.10.10.30:8080`).
- `VM-WIN-LAB` fue **reserva de diseno**, no una VM Windows implementada ni evaluada.
- Cinco casos M-001...M-005 cerrados en la investigacion y siete controles PV-01...PV-07 documentados.
- Inventario original de **171 evidencias**, cuyo cotejo SHA-256 frente al manifiesto dio **171/171 OK** en la verificacion local aportada por el autor (16-10-2026). Los 171 ficheros de evidencia **no** forman parte de esta copia publica; sus hashes no deben confundirse con los de artefactos saneados.

## Estructura

- [`arquitectura/`](arquitectura/arquitectura.md): plano tecnico, limites y red ejemplo.
- [`laboratorio/`](laboratorio/README.md): codigo benigno M-001 y requisitos de ejecucion.
- [`experimentos/`](experimentos/README.md): casos M-001 a M-005 y resultados observados.
- [`validacion/`](validacion/matriz_pv_ev.md): siete PV y su alcance.
- [`seguridad/`](seguridad/guia_securizacion.md): controles de contencion y comprobaciones.
- [`reproducibilidad/`](reproducibilidad/procedimiento.md): como reconstruir y verificar sin afirmar repeticion empirica no documentada.
- [`herramientas/`](herramientas/verificar_evidencias_locales.py): lector de manifiestos para el repositorio original (solo lectura).

## Aportacion y limitaciones

La contribucion principal es la **metodologia de observacion, contencion y trazabilidad** aplicada a un corpus sintetico. Las conclusiones **no** validan deteccion de infostealers reales, EDR/SIEM, evasion, malware operativo, C2, exfiltracion real ni una garantia universal de aislamiento.

## Seguridad y licencia

Sin muestras de malware, secretos, discos de VM o material ofensivo. No ejecutar el laboratorio conectado a redes ajenas. Consultar [guia de securizacion](seguridad/guia_securizacion.md) y [alcance etico](seguridad/modelo_amenazas_y_etica.md).

**Licencia:** aun no seleccionada. La ausencia de licencia no implica permiso general de reutilizacion; definirla deliberadamente antes de promocionar la reutilizacion del codigo.

**Publicacion:** antes de cambiar el repositorio a publico, completar la revision manual de PDF, metadatos, capturas y contenido staged y comprobar el estado real de GitHub.
