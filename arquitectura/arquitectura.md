# Arquitectura verificada y limites

## Topologia

```text
HOST KVM/libvirt (plano de control y custodia)
  |-- StealLab-Net: virbr-steal, 10.10.10.0/24 (sin forward XML)
       |-- VM-LINUX-ANALYSIS  10.10.10.20  (ejecucion/captura)
       `-- VM-SERVICES-SIM    10.10.10.30  (receptor HTTP benigno :8080)

VM-WIN-LAB: reserva de diseno (10.10.10.10), no implementada.
```

El host posee IP interna `10.10.10.1`. `StealLab-Pool` se utilizo para los discos qcow2, conservados fuera de esta publicacion. Las VMs de Linux estaban apagadas al cierre documentado; la red figuraba activa/persistente/autostart en el cierre de agosto de 2026.

El XML de referencia bajo [`red/steallab-net.example.xml`](red/steallab-net.example.xml) conserva el segmento y ausencia de `forward`, **pero omite los MAC y reservas especificas del host original**. Quien replique debe configurar direcciones estaticas de sus VMs o sus propias reservas coherentes. No es una imagen de la topologia ejecutandose ni un deployment automatico validado.

### Alcance del aislamiento

La ausencia de NAT/forward en la configuracion de libvirt y la ausencia de ruta por defecto desde el cliente durante M-005 apoyan la contencion observada. No prueban ausencia de cualquier canal alternativo ni proteccion ante escape de hipervisor. No utilizar un adaptador adicional NAT/bridge externo y revisar rutas e interfaces en el sistema invitado y en el host.

### Servicio de escucha

Se verifico el acceso a `10.10.10.30:8080`, **no** se incluyo en los 46 archivos evidencia suficiente para certificar el `bind` exacto del proceso en runtime. Para reducir exposicion, configurar el receptor para escuchar en `10.10.10.30` cuando el servicio lo permita, en lugar de `0.0.0.0`. No usar `127.0.0.1` para un receptor que debe ser accesible desde otra VM sin cambiar el diseno.

**Fuentes tecnicas del archivo privado:** `03_laboratorio/steallab-net.xml`; `05_resultados/cierre_20260808/10_estado_final_libvirt.txt`; `EV-M005-010`.
