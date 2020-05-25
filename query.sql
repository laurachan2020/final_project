select g.name as ticket, g.HighestHourlyPrice, s.ts as Datetime, SUBSTRING(s.ts, 12, 2) AS hour from
(select name, max(high) as HighestHourlyPrice from "stock-db"."18" group by name) g, "stock-db"."18" s
where g.name=s.name and g.HighestHourlyPrice=s.high