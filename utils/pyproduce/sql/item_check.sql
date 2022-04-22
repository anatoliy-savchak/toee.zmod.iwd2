
;with s  as (
select  FileName = substring(t.FilePath, 77, 100)
, Name = json_value(t.Content, '$.IdentifiedName.Text')
, Price = cast(json_value(t.Content, '$.Price') as int)
, Description = isnull(json_value(t.Content, '$.IdentifiedDescription.Text'), json_value(t.Content, '$.UnidentifiedDescription.Text'))
, TwoH = json_value(t.Content, '$.Flags.TwoHanded')
, ItemType = json_value(t.Content, '$.ItemType')
from iwd2.itm t
) 
select *
from s
where ItemType = 'LeatherArmor' --and FileName = '00LEAT01.json'
order by 3 asc

;with s as (
select  FileName = substring(t.FilePath, 81, 100)
, Item
from iwd2.cre t
cross apply openjson(t.Content, '$.Items') 
with (
	Item nvarchar(max) '$.Item.Filename'
) as j
)
select * from s
where Item = '00LEAT01'