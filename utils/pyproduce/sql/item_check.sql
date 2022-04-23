
;with s  as (
select  FileName = replace(substring(t.FilePath, 77, 100), '.json', '')
, Name = json_value(t.Content, '$.IdentifiedName.Text')
, Price = cast(json_value(t.Content, '$.Price') as int)
, Description = isnull(json_value(t.Content, '$.IdentifiedDescription.Text'), json_value(t.Content, '$.UnidentifiedDescription.Text'))
, TwoH = json_value(t.Content, '$.Flags.TwoHanded')
, ItemType = json_value(t.Content, '$.ItemType')
from iwd2.itm t
) 
select *
from s
where ItemType = 'Axes' --and FileName = '00LEAT01.json'
	and Name = 'Battleaxe'
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
where Item = '00HAMT01'

;with s as (
select  CreFileName = substring(t.FilePath, 81, 100)
, SlotCode, ItemTypeEval, ItemFileName
from iwd2.cre t
cross apply openjson(t.Content, '$.Items') 
with (
	SlotCode nvarchar(max) '$.SlotCode',
	ItemTypeEval nvarchar(max) '$.ItemTypeEval',
	ItemFileName nvarchar(max) '$.Item.Filename'
) as j
)
select SlotCode, ItemTypeEval, [count] = count(*), CreFileName = min(CreFileName), ItemFileName = min(ItemFileName) from s 
where ItemTypeEval is not null
group by SlotCode, ItemTypeEval order by 1
--where SlotCode = '00LEAT01'