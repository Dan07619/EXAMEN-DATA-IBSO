-- SQL Queries 
DATABASE1

SELECT
    DOC.DNUM AS "# de ticket",
    DOC.DFECHA AS "Fecha",
    DOC.DCANT AS "Monto sin IVA",
    (DOC.DCANT + DOC.DIVA) AS "Monto con IVA",
    DOC.DPAR1 AS "Vendedor",
    CLI.CLINOM AS "Cliente",
    AUX.ICOD AS "Productos comprados (SKU)",
    INV.IDESCR AS "Descripción",
    AUX.AIPZAS AS "Cantidad (unidades)",
    AUX.AIALMACEN AS "Almacén que vendió",
    INV.ILISTA3 AS "Precio de lista",
    INV.IFAM3 AS "Talla",
    INV.IFAM4 AS "Color",
    INV.IFAM5 AS "Temporada"
FROM
    DOCUMENTOS DOC
    JOIN CLIENTES CLI ON DOC.CLICOD = CLI.CLICOD
    JOIN AUXILIAR_INVENTARIOS AUX ON DOC.DNUM = AUX.FMOV
    JOIN INVENTARIOS INV ON AUX.ICOD = INV.ICOD
WHERE
    DOC.DESCXC = 1 -- Ventas
ORDER BY
    DOC.DNUM;
