with messages as (
   select *
     from
      {
         {
            ref('stg_telegram_messages')
         }
      }
)
select message_id,
       {
          {
             dbt_utils.generate_surrogate_key(
                [
                   'channel_name'
                ]
             )
          }
       }
    as channel_id,
       cast(timestamp as timestamp) as timestamp,
       media_type,
       message_length,
       has_media
  from messages