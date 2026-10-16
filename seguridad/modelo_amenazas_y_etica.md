# Alcance etico y amenazas contempladas

StealLab es una investigacion aplicada de **simulacion benigna**, no una herramienta ofensiva ni un entorno de produccion. Quedan fuera de alcance: malware real, muestras ejecutables peligrosas, credenciales reales, datos personales, C2, persistencia, evasion y exfiltracion real.

El diseno reduce riesgos por separacion de funciones, red interna controlada, snapshots, datos sinteticos, capturas filtradas e integridad SHA-256. La contencion se observa **dentro del caso y momento evaluados**. No cubre escape del hipervisor, adversarios activos ni configuraciones de terceros.

## Amenazas y mitigaciones razonadas

| Riesgo | Mitigacion documentada/propuesta | Estado |
|---|---|---|
| Conectividad externa accidental | Red libvirt sin `forward`, cliente sin ruta por defecto en M-005 | Comprobado en caso historico M-005; revalidar cada entorno |
| Confusion entre datos DEMO y datos autenticos | Corpus sintético y restricciones eticas | Documentado; el script M-001 **no impone** automaticamente las marcas DEMO |
| Perdida de estado | Snapshots qcow2 | Existencia documentada; restauracion universal no demostrada |
| Perdida de trazabilidad | Identificadores PV/EV, manifiesto y SHA-256 | 171/171 comprobados localmente por el autor (octubre de 2026) |
| Exposicion del receptor HTTP | Limitar escucha a IP interna, revisar firewall | Recomendacion para despliegues nuevos; bind exacto historico no verificado |
| Filtracion de datos al publicar | Lista positiva de archivos y revision de metadatos | Pendiente para PDF y futuras evidencias graficas/PCAP |
