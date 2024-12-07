SELECT lt.columns, rt.columns
FROM left_table AS lt
JOIN right_table AS rt
    ON lt.id_col = rt.id_col