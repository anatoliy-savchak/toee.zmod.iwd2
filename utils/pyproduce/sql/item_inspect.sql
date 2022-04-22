
select  FileName = substring(t.FilePath, 77, 100)
, Name = json_value(t.Content, '$.IdentifiedName.Text')
, Price = cast(json_value(t.Content, '$.Price') as int)
, Description = isnull(json_value(t.Content, '$.IdentifiedDescription.Text'), json_value(t.Content, '$.UnidentifiedDescription.Text'))
, TwoH = json_value(t.Content, '$.Flags.TwoHanded')
from iwd2.itm t
where json_value(t.Content, '$.ItemType') = 'Daggers'
order by 3 asc