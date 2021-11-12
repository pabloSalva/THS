const rowsDomicilios = DomiciliosDelBack.map((domicilio) => {
  return {
    id: domicilio.id,
    nombre: domicilio.nombre,
    cantidad_personas: domicilio.cantidad_personas,
    antiguedad: domicilio.antiguedad,
    localidad: domicilio.localidad.nombre_localidad,
  };
});
setRows(rowsdomicilios);
