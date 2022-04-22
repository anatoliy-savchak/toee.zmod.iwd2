create or alter function dbo.splitted_idx(@value nvarchar(max), @separator nvarchar(1), @index int) returns nvarchar(max)
as 
begin
	declare @result nvarchar(max);
	select top 1 @result = value from (
		select ordinal = row_number() over (order by (select null)), value
		from string_split(@value, @separator)
		order by 1 offset @index rows fetch next 1 row only
	)z;
	return @result;
end
go
