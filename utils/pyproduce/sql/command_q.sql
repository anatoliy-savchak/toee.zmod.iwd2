;with s as (
	select t.FileName, body.func_name, targs.def_arg_line
		, tvalue.src
		, srct = iif(tvalue.src like '"%', 'str', iif(try_cast(tvalue.src as int) is not null, 'int', 'name'))
		, tvalue.value
	from iwd2.scripts t
	cross apply openjson(t.Content) 
	with (
		func_name nvarchar(64),
		kind nvarchar(16),
		args nvarchar(max) as json
	) as body
	cross apply openjson(body.args) 
	with (
		def_arg_line nvarchar(max) '$.def.arg_line',
		[values] nvarchar(max) as json
	) as targs
	cross apply openjson(targs.[values]) 
	with (
		src nvarchar(max),
		value nvarchar(max)
	) as tvalue
)
select * from s
--select distinct s.src from s
where s.FileName in ('Subrace')
	--and s.def_arg_line = 'I:Race*Race'