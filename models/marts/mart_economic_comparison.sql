select
    *,
    avg(gdp_usd) over (
        partition by country_name 
        order by report_year 
        rows between 4 preceding and current row
    ) as gdp_5yr_moving_avg
from {{ ref('int_worldbank_pivoted') }}