# Codigo benigno del laboratorio

## M-001

`m001/m001_simulacion_benigna.py` es una **copia byte a byte** del archivo Python suministrado en el paquete de auditoria. SHA-256 original del script:

```
1bf46fb637153eb7f620eaf959fe72ab4a74dfdd8ca2d16bb89744ffded59452
```

No es un stealer ni analiza credenciales, navegadores o wallets reales. Lee **solo** los nombres de archivo admitidos en `/opt/steallab/m001/datos_demo`: `credencial_demo.txt`, `navegador_demo.txt`, `wallet_demo.txt` y `sistema_demo.txt`. Produce manifiestos, hashes y logs en `/opt/steallab/m001/`; realiza una peticion GET al receptor interno `http://10.10.10.30:8080/`.

**Limite de seguridad importante:** el programa **registra**, pero no fuerza como precondicion, la presencia de las marcas `DEMO` y `NO REAL`. Nunca colocar contenidos autenticos bajo esos nombres. Es obligatoria una preparacion manual de datos ficticios antes de ejecutarlo. Su salida contiene el hostname de la VM y no debe publicarse en bruto sin revision.

**No incluido en esta copia:** el dataset exacto utilizado en el experimento, el servicio HTTP server, discos qcow2, cloud-init, snapshots y otros ficheros de las 171 evidencias. Por tanto, este ZIP no constituye un entorno end-to-end automaticamente ejecutable ni reproduce los hashes historicos al generar nuevas entradas.

Los scripts historicos de resumen de VMs se excluyeron de la publicacion por rutas locales obsoletas y divulgacion de metadatos del host. El programa de verificacion de evidencias es solo de lectura.
