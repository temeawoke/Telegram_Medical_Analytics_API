-- tests/no_future_messages.sql
select *
  from
   {
      {
         ref('fct_messages')
      }
   }
 where timestamp > now()