# Casos experimentales cerrados

| Caso | Procedimiento y observable | Resultado historico | Limite principal |
|---|---|---|---|
| **M-001** | Simulacion benigna con cuatro archivos DEMO, logs/JSON, peticion HTTP local y PCAP | PASS en evidencia original | No malware, credenciales o navegador reales |
| **M-002** | Reconocimiento de cuatro artefactos sinteticos y un archivo de control, directorio autorizado | PASS: 5/5 artefactos DEMO | No lectura fuera del corpus |
| **M-003** | Empaquetado local TAR.GZIP de cinco archivos sinteticos | PASS: 587 bytes, 5 miembros | No hubo transferencia ni exfiltracion |
| **M-004** | Comunicacion HTTP interna y observacion PCAP | PASS: HTTP 200, 398 bytes, 11 paquetes | No documentado PID runtime del servidor |
| **M-005** | Contraste positivo HTTP interno y destino TEST-NET negativo | PASS: interno 200/398 bytes/10 paquetes; externo HTTP 000/0 bytes/0 paquetes | Un unico destino, no aislamiento universal |

**M-005:** `EV-M005-005` registro `FAIL` por una variable de decision no inicializada. `EV-M005-006` documento la correccion **sin repetir el experimento**, y `EV-M005-010` cerro el caso en PASS. La incidencia se conserva por transparencia.

Se describen resultados apoyados por los informes del paquete privado, no se proporcionan scripts originales independientes de M-002 a M-005 porque **no figuran en los 46 archivos suministrados**. Cada caso requiere un protocolo de preparacion y datos DEMO compatibles antes de intentar replicacion independiente.

**Fuentes:** `EV-M002-003`, `EV-M003-003`, `EV-M004-008`, `EV-M005-010`, `05_resultados/cierre_20260808/{05,06,08,09}*`.
