;with s as (
select  FileName = substring(t.FilePath, 81, 100)
, feat = feats.value
from iwd2.cre t
cross apply openjson(t.Content, '$.Feats') as feats
)
select *
from s
where feat = 'wild shape shambler'