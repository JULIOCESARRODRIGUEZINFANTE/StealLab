# Matriz PV/EV consolidada para lectura publica

Esta matriz se deriva de `05_resultados/tablas_fuente/matriz_pv_ev.tsv` (cierre Linux) y de informes M-002 a M-005. **No copiar** la version historica `05_resultados/matriz_pv_ev.md`, que todavia contiene estados `Pendiente` y referencias Sysmon/Procmon no desplegadas.

| PV | Criterio documentado | Estado reportado en fuente de cierre | Limite |
|---|---|---|---|
| PV-01 | Red libvirt aislada y conectividad interna | Completada | No garantiza aislamiento universal |
| PV-02 | Existencia de snapshots base de VMs Linux | Completada | No equivale a ensayos exhaustivos de restauracion |
| PV-03 | Captura de baseline Linux/procesos y puertos | Completada (Linux) | No Sysmon/Procmon Windows |
| PV-04 | Captura PCAP HTTP interno | Completada | Observacion de flujo filtrado |
| PV-05 | Repositorio, hashes, matriz e inventario | Completada (Linux) | Evidencias originales bajo custodia local |
| PV-06 | Informe tecnico M-001 | Completada | Caso M-001 benigno |
| PV-07 | LLM supervisado con revision humana | Completada | LLM no es evidencia tecnica independiente |

**Nota:** El recuento de 171/171 hashes correctos corresponde a una verificacion que el autor ejecuto contra su repositorio original el 16-10-2026. No se acompanan aqui los 171 artefactos; los hashes historicos dejan de ser validos para cualquier copia redactada/saneada.
