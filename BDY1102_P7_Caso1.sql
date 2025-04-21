DROP VIEW vw_clientes;
CREATE VIEW vw_clientes AS
SELECT
    to_char(c.numrun, 'fm99g999g999')
    || '-'
    || c.dvrun          AS "RUN CLIENTE",
    c.pnombre
    || ' '
    || c.snombre
    || ' '
    || c.appaterno
    || ' '
    || c.apmaterno      AS "NOMBRE CLIENTE",
    po.nombre_prof_ofic AS "PROFESION U OFICIO",
    tc.nombre_tipo_contrato,
    to_char(
        max(pc.monto_total_ahorrado),
        'FML99G999G999'
    )                   AS "MONTO TOTAL AHORRADO",
    CASE
        WHEN MAX(pc.monto_total_ahorrado) BETWEEN 100000 AND 1000000   THEN
            'BRONCE'
        WHEN MAX(pc.monto_total_ahorrado) BETWEEN 1000001 AND 4000000  THEN
            'PLATA'
        WHEN MAX(pc.monto_total_ahorrado) BETWEEN 4000001 AND 8000000  THEN
            'SILVER'
        WHEN MAX(pc.monto_total_ahorrado) BETWEEN 8000001 AND 15000000 THEN
            'GOLD'
        WHEN MAX(pc.monto_total_ahorrado) > 15000000                   THEN
            'PLATINUM'
    END                 AS "CATEGORIA CLIENTE"
FROM
         cliente c
    INNER JOIN profesion_oficio           po ON po.cod_prof_ofic = c.cod_prof_ofic
    INNER JOIN tipo_contrato              tc ON c.cod_tipo_contrato = tc.cod_tipo_contrato
    INNER JOIN producto_inversion_cliente pc ON c.nro_cliente = pc.nro_cliente
GROUP BY
    c.numrun,
    c.dvrun,
    c.pnombre,
    c.snombre,
    c.appaterno,
    c.apmaterno,
    po.nombre_prof_ofic,
    tc.nombre_tipo_contrato
ORDER BY
    c.appaterno,
    MAX(pc.monto_total_ahorrado);

COMMIT;

ROLLBACK;