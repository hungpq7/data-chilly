SELECT categorical_col, AGG_FUNC(numerical_col)
FROM my_table
GROUP BY categorical_col