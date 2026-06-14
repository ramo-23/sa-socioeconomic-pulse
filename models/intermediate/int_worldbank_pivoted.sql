select
    country_name,
    report_year,
    max(case when indicator = 'unemployment_rate' then indicator_value end) as unemployment_rate,
    max(case when indicator = 'gdp_usd' then indicator_value end) as gdp_usd,
    max(case when indicator = 'inflation_rate' then indicator_value end) as inflation_rate
from {{ ref('stg_worldbank') }}
group by 1, 2