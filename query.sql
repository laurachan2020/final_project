select g.name as ticket, g.HighestHourlyPrice, s.ts as Datetime from
(select name, max(high) as HighestHourlyPrice from stock group by name) g, stock s
where g.name=s.name and g.HighestHourlyPrice=s.high