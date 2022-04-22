;with s as (
select  FileName = substring(t.FilePath, 76, 100)
, Setting = json_value(t.Content, '$.ItemType')
from iwd2.itm t
)
select Setting, count(*), max(Filename)
from s
group by Setting
order by 1 asc
