# Guia de securizacion de StealLab

## 1. Preparacion previa

Usar un host y VMs dedicados al laboratorio, datos inventados y discos sin informacion personal. **No** conectar muestras de malware ni ejecutar experimentos en equipos corporativos. Mantener actualizados host, libvirt y utilidades. Guardar una copia offline de los artefactos originales de evidencia.

## 2. Red aislada

La red de ejemplo no incluye elemento `<forward>`. La red historica poseia interfaz `virbr-steal`, host `10.10.10.1` y el segmento `10.10.10.0/24`. La VM cliente era `10.10.10.20`; el servidor benigno `10.10.10.30`. Al desplegar, **verificar** que cada VM tiene solo la interfaz prevista y que no dispone de ruta por defecto o interfaz NAT adicional.

Comandos de **inspeccion** sin mutaciones:

```bash
virsh -c qemu:///system net-info StealLab-Net
virsh -c qemu:///system net-dumpxml StealLab-Net
virsh -c qemu:///system domiflist VM-LINUX-ANALYSIS
virsh -c qemu:///system domiflist VM-SERVICES-SIM
```

Desde el cliente, inspeccionar rutas y realizar una prueba **solo contra destino documental**; no ejecutar controles hacia servicios reales:

```bash
ip route
ip route get 192.0.2.1
```

La ausencia de una ruta hacia ese destino no prueba por si sola aislamiento global. Complementar con revisiones de firewall, interfaces, conectividad y trazas.

## 3. Receptor interno HTTP

Restringir al puerto y direccion internos necesarios. En una arquitectura de VMs separadas, `127.0.0.1` no permite a otra VM acceder al receptor; preferir un bind especifico a `10.10.10.30` si el servidor lo soporta. Revisar su escucha **dentro del guest del servidor**:

```bash
ss -ltn
```

No se ha verificado a partir de este ZIP el bind historico exacto. Registrar esa comprobacion como evidencia nueva, separada de las realizadas para el TFM entregado.

## 4. Aislamiento operativo

Aplicar principio de minimo privilegio, no reutilizar contrasenas y evitar que `cloud-init`/`user-data` contengan secretos en un repositorio. Tomar snapshot previo, usar exclusivamente archivos marcados DEMO/NO REAL, fijar criterios de aceptacion y no publicar logs con nombre de host, usuario o rutas locales sin sanear.

## 5. Captura, integridad y custodia

Filtrar las capturas de red al trafico autorizado, registrar contexto y limites, calcular SHA-256 y preservar los originales inmutables. Cualquier evidencia saneada tiene **hash distinto** y debe declararse derivada, nunca original.

## 6. Difusion publica

No publicar qcow2, ISO seed, historicos de contrasenas, archivos cloud-init, logs extensos, directorios de backup ni PCAP sin revisar. Inspeccionar manualmente el PDF oficial y la presentacion definitiva (incluyendo metadatos e imagenes) antes de subirlos. Verificar `git diff --cached` y secretos del staging antes de `git push`.

Este documento es una **guia de controles razonados** basada en el caso; no es una certificacion de hardening universal.
