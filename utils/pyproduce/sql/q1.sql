;with s as (
select  FileName = substring(t.FilePath, 81, 100)
, Setting = json_value(t.Content, '$.StrengthBonus')
from iwd2.cre t
)
select Setting, count(*), max(Filename)
from s
group by Setting
order by 2 desc