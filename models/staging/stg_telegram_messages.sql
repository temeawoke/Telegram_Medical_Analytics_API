with source as (
   select *
     from raw.telegram_messages
),cleaned as (
   select message_id,
          lower(trim(channel_name)) as channel_name,
          timestamp,
          text,
          media_type,
          length(text) as message_length,
          media_type is not null as has_media
     from source
)
select *
  from cleaned