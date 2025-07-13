select distinct
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
   channel_name
  from
   {
      {
         ref('stg_telegram_messages')
      }
   }