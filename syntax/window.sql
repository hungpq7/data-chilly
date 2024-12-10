SELECT *
    , WINDOW_FUNCTION() OVER (
        PARTITION BY grouping_columns
        ORDER BY ordering_columns
        ROWS BETWEEN ... PRECEDING AND ... FOLLOWING
    )
FROM my_table