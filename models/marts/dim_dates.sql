select distinct
    cast(timestamp::date as date) as date,
    extract(day from timestamp) as day,
    extract(week from timestamp) as week,
    extract(month from timestamp) as month,
    extract(year from timestamp) as year
from {{ ref('stg_telegram_messages') }}
