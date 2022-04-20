--create schema iwd2 authorization dbo;
create table iwd2.cre(
	IID int not null identity(1, 1) constraint pk_cre primary key clustered,
	FilePath nvarchar(255) null,
	Content nvarchar(max) null
);
