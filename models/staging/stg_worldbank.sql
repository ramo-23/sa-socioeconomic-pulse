with source as (
    select * from {{ source('raw_stats_sa', 'raw_worldbank_data') }}
)

select
    cast(country as string) as country_name,
    cast(year as integer) as report_year,
    cast(indicator_name as string) as indicator,
    cast(value as float64) as indicator_value
from source