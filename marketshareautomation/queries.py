exist_query = """

    select MAX(DATE_KEY)
    from WM_BENELUX_SANDBOX.WOUT_K.MARKET_SHARE_WM_BENELUX


        

"""

get_data = """

with streaming as (


    select      


                date_trunc('week', fas.date_key)    as week_key


            ,   country_code                        as country_code


            ,   sum(stream_count)                   as stream_count


    from fact_audio_streaming as fas


    where           true=true


                and fas.country_code = 'NL'
                or  fas.country_code = 'BE'
                and fas.customer_key = 1
                and fas.DATE_KEY > 'DATE_REPLACE'
    group by 1,2
),
market_shares as (
                select 
                            fms.date_key                                                                                                                    as date_key
                        ,   date_trunc('week', fms.date_key)                                                                                                as week_key
                        ,   fms.country_code                                                                                                                as country_code
                        ,   case when sum(fms.units) = 0 then avg(fms.market_share)         else sum( fms.market_share * fms.units) / sum(fms.units)    end as wa_market_share
                        -- ,   sum(fms.units)                                                                                                                  as market_share_streams
                        -- ,   case when sum(fms.units) = 0 then 'other'                       else 'weighted'                                             end as type_market_share

                from fact_market_share      as fms
                where           true=true
                        and     fms.country_code IN ('NL', 'BE')
                        and     fms.customer_key = 1
                        and     fms.date_key > 'DATE_REPLACE'
                group by 1,2,3
                order by fms.date_key desc, fms.country_code
)
select      ms.*
    ,   s.stream_count
from market_shares  as ms
left join streaming      as s on ms.week_key = s.week_key and ms.country_code = s.country_code
order by ms.country_code, ms.week_key desc;


"""