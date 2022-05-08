--create schema iwd2 authorization dbo;
create table iwd2.scripts(
	IID int not null identity(1, 1) constraint pk_scripts primary key clustered,
	FilePath nvarchar(255) null,
	FileName nvarchar(54) null,
	Content nvarchar(max) null
);
