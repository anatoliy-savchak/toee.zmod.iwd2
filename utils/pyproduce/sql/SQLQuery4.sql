begin tran

truncate table iwd2.cre;
go

insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00BUG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00BUG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00CHI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00CHI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00COW.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00COW.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00COWDED.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00COWDED.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00DOG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00DOG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00DOGDED.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00DOGDED.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00GOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00GOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00GOBAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00GOBAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00GOBARE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00GOBARE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00GOBE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00GOBE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00HOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00HOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00HUMDED.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00HUMDED.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00ORCAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00ORCAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00ORCARE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00ORCARE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00OROBLA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00OROBLA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00WELP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\00WELP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10BLACK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10BLACK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10BLANC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10BLANC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10BROGAN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10BROGAN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10CATF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10CATF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10CRANDA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10CRANDA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10DOP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10DOP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10ELDGUL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10ELDGUL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10FIRTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10FIRTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10FIRTHH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10FIRTHH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBARD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBARD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBARW.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBARW.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBSC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBSC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBW.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOBW.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOHAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GOHAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GUTHE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10GUTHE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10HEDRON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10HEDRON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10HINT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10HINT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10JON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10JON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10JORUN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10JORUN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG2E.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG2E.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG3E.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG3E.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEG6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEGE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KEGE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KICKSH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10KICKSH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10MAGDR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10MAGDR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10MALED.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10MALED.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10REIG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10REIG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10RUKWU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10RUKWU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10SAILRD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10SAILRD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10SCREED.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10SCREED.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10SOLDRD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10SOLDRD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10ULEK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\10ULEK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11CAHLHY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11CAHLHY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DEADG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DEADG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DEADS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DEADS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DEAGLE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DEAGLE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DEIRD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DEIRD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DENHAM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DENHAM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DOGL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DOGL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DOGS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11DOGS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11ELYTHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11ELYTHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11GARRAD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11GARRAD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11GHILLE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11GHILLE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11JEMEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11JEMEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11KOLUHM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11KOLUHM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11LOMAN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11LOMAN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11LUMBAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11LUMBAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11MAXIEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11MAXIEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11OSWALD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11OSWALD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11PHAEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11PHAEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11RAGNIB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11RAGNIB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11ULBREC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11ULBREC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11URBEKS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11URBEKS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11VALIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\11VALIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12ANSON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12ANSON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12ARCHER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12ARCHER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12BLACK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12BLACK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12BLANC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12BLANC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12CABALL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12CABALL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12CAULDE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12CAULDE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12DRILL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12DRILL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GABLE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GABLE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GHOTRA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GHOTRA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GOBAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GOBAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GOBE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12GOBE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12HARLES.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12HARLES.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12ILLIGM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12ILLIGM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12ISHER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12ISHER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12KADENC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12KADENC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12KEGMEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12KEGMEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12MENON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12MENON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12MERC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12MERC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12MESS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12MESS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12NILES.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12NILES.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12NOLAN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12NOLAN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12OLAP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12OLAP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12PHAEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12PHAEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12RECRUI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12RECRUI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12SHAWFO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12SHAWFO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12SWIFT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12SWIFT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12SWIFTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12SWIFTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12TABARD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12TABARD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12TARRAN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12TARRAN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12TARSOL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12TARSOL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12TRAINE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12TRAINE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12VGHOTA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12VGHOTA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12WEAPON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12WEAPON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12WOLF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\12WOLF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ARTE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ARTE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20BORARC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20BORARC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20CARCWL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20CARCWL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20DEDVF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20DEDVF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20DEDVM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20DEDVM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20DERETH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20DERETH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20DERHID.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20DERHID.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20EMMA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20EMMA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20GRNSLM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20GRNSLM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20HGHCAT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20HGHCAT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KAITLN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KAITLN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KEG1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KEG1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KEG2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KEG2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KEG3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KEG3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KNTVIR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KNTVIR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KRIS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20KRIS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20MADLEP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20MADLEP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20MALARA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20MALARA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20MALARH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20MALARH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20MALARP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20MALARP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20OCRJEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20OCRJEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20OLVSLM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20OLVSLM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCA3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCA3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCA4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCA4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCACH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCACH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCAV.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCAV.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCAV3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCAV3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCAV4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCAV4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCCHF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCCHF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCFIR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCFIR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCRUN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCRUN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCSHM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCSHM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCSHV.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCSHV.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCW3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCW3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCW4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCW4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCWAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCWAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCWV.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCWV.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCWV3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCWV3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCWV4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20ORCWV4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESF1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESF1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESF2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESF2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESF3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESF3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESM1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESM1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESM2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESM2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESM3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20PESM3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20SABRIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20SABRIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20SLMZMB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20SLMZMB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20SNOLEP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20SNOLEP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20STRLEP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20STRLEP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20VREK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\20VREK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ANIVIL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ANIVIL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21BUGCPT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21BUGCPT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ELFMGE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ELFMGE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21GAERNT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21GAERNT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21HGHSNK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21HGHSNK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21HINT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21HINT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21HRP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21HRP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21OGR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21OGR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ORCACE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ORCACE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ORCCOM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ORCCOM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ORCELT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21ORCELT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21SPDQN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21SPDQN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21SPDSML.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21SPDSML.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21SUPPRT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21SUPPRT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21SUPRT2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21SUPRT2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21VERB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21VERB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21WERBGR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21WERBGR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21WERRAT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21WERRAT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21XUKI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\21XUKI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30BEETQ.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30BEETQ.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DEKGOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DEKGOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DFDND.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DFDND.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DGOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DGOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DGOBE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DGOBE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DHAGOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DHAGOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM5.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM5.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DRUM6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DSKEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DSKEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DTSKEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30DTSKEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ENNELI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ENNELI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30FBEET.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30FBEET.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30FIRTLG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30FIRTLG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30FIRTRL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30FIRTRL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBAES.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBAES.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBARS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBARS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBDED.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBDED.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBES.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBES.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBHO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBHO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBHOE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBHOE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBHOS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBHOS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBKRU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBKRU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBMOK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBMOK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBOGR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBOGR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBOV1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBOV1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBPOH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBPOH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBPON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBPON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBSH1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBSH1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBSOR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBSOR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBVUN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBVUN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWLP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWLP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWR1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWR1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWR2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWR2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWRC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30GOBWRC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30HAGOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30HAGOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30HOBDG2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30HOBDG2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30HOBDGU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30HOBDGU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30HOBGUM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30HOBGUM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ICETRL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ICETRL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ILQUAG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ILQUAG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRCH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRCH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRGA2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRGA2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRGA3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRGA3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRGAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRGAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OGRS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCARS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCARS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCGOT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCGOT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCRU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCRU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCRU2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCRU2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCSH1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCSH1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCSHH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCSHH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCTRU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCTRU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCWA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCWA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCWAE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCWAE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCWAS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCWAS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCWD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30ORCWD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OROBLS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OROBLS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OROCA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OROCA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OROPUS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OROPUS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OROTAS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OROTAS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OTY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30OTY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30SPIWO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30SPIWO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30SPIWOD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30SPIWOD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30SPIWOQ.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30SPIWOQ.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30TEQUAG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30TEQUAG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30TROLL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30TROLL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30WOLWOR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30WOLWOR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30WOLWOS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30WOLWOS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30WWLF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30WWLF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30YQUOGG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\30YQUOGG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BRASTD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BRASTD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BRASTO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BRASTO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BUGB00.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BUGB00.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BUGB01.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BUGB01.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BUGGUT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BUGGUT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BUGJAI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31BUGJAI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GIAVER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GIAVER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBHC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBHC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBHO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBHO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBHOE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBHOE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBOV1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBOV1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBSH1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBSH1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBSH2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBSH2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBSO2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBSO2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBSOR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31GOBSOR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31HOBAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31HOBAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31HOBCH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31HOBCH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31HOBE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31HOBE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31HOBSER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31HOBSER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31OGRCOO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31OGRCOO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCARE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCARE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCHC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCHC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCHSB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCHSB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCHSH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCHSH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCOLD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCOLD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCSH1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCSH1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCSH2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCSH2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCWA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCWA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCWD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCWD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCWD2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31ORCWD2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31OROBRA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31OROBRA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31OROCH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31OROCH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31OROCO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31OROCO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31SHERIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\31SHERIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40BCULTC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40BCULTC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40BDAWN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40BDAWN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40BDCULT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40BDCULT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40BENEST.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40BENEST.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40DOGWLD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40DOGWLD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40DRUIDF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40DRUIDF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40DRUIDM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40DRUIDM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40GBLKA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40GBLKA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40GIAFOM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40GIAFOM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ILIUM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ILIUM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ILUM2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ILUM2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ILUM3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ILUM3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ODEA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ODEA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ODEA2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ODEA2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ODEA3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40ODEA3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40OSWALD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40OSWALD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RANGRC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RANGRC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RANGRF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RANGRF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RANGRM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RANGRM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RIPBRO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RIPBRO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RIPMOM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RIPMOM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RIPPOP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RIPPOP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RIPSIS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40RIPSIS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40SPIFR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40SPIFR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40SPIFRH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40SPIFRH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40SPIPHS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40SPIPHS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40WOLFWI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40WOLFWI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40YETITU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40YETITU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40YURST.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\40YURST.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ABISHW.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ABISHW.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ALTAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ALTAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41AOCHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41AOCHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ASSASS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ASSASS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41BARSHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41BARSHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41BARWAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41BARWAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41BEARPO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41BEARPO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41BISHOP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41BISHOP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CATHI2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CATHI2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CATHI3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CATHI3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CATHIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CATHIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CLERIF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CLERIF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CLERIM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CLERIM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CORNUG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41CORNUG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41DEER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41DEER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41DOOMGD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41DOOMGD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41GLABRE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41GLABRE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41GOLEIC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41GOLEIC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41GOLEMC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41GOLEMC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41HENCHM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41HENCHM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41HENCHX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41HENCHX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41INGRAT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41INGRAT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LEMURE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LEMURE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LUSOLD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LUSOLD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LYSAR2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LYSAR2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LYSAR3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LYSAR3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LYSARA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41LYSARA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41MYSTIC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41MYSTIC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41NATE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41NATE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41NECROM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41NECROM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41NICK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41NICK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ONDABO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ONDABO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ORIA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ORIA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ORIA2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ORIA2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ORIA3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ORIA3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ORIAES.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ORIAES.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PAINT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PAINT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PFIEND.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PFIEND.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRIESF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRIESF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRIESM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRIESM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO5.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO5.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41PRISO6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41RABISH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41RABISH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41RAHM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41RAHM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41REMHZA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41REMHZA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41REMHZQ.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41REMHZQ.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41REMHZZ.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41REMHZZ.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41RENGAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41RENGAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHADOW.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHADOW.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHAMAF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHAMAF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHAMAM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHAMAM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHERI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHERI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHERI2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHERI2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHERI3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41SHERI3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41TEMLEV.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41TEMLEV.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41THAGRO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41THAGRO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41TROICE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41TROICE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41TROSNO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41TROSNO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41VRASSI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41VRASSI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41WABISH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41WABISH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41WARRIO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41WARRIO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41WYVERN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41WYVERN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41XHAAN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41XHAAN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ZACK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\41ZACK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50ABOMIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50ABOMIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50AGOG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50AGOG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50AGOGH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50AGOGH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARLD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARLD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARSH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARSH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARSHH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARSHH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARW2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARW2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARWA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARWA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARWAH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BARWAH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BONES.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50BONES.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CARITA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CARITA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CARYNA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CARYNA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CHILDF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CHILDF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CHILDM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CHILDM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CORPSE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50CORPSE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50DRAWY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50DRAWY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50ETR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50ETR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50GHOAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50GHOAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50GHOBA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50GHOBA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50GHOHU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50GHOHU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50GNTFO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50GNTFO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HADBRU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HADBRU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HANNU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HANNU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HGHOST.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HGHOST.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HNT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HNT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HNT2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HNT2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HNT3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50HNT3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50ISAIR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50ISAIR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50JARI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50JARI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50KURTTU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50KURTTU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50KYOSTI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50KYOSTI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50LEEVI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50LEEVI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50LIMHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50LIMHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50LIMHA2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50LIMHA2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50MADAE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50MADAE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50NWSOLD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50NWSOLD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50NYM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50NYM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50PAIRI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50PAIRI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50RDEAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50RDEAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50RDEBA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50RDEBA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50RDEHU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50RDEHU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SPIFH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SPIFH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SPIFH2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SPIFH2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SPIFR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SPIFR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SPIFR2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SPIFR2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SUOMA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50SUOMA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TAHVO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TAHVO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50THVARA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50THVARA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TREDA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TREDA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TREDE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TREDE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TREDG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TREDG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TROSG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TROSG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TROSH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TROSH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TROSN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TROSN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TROSS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50TROSS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50VENLA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50VENLA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50VIL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50VIL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50VIL2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50VIL2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50VIL3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50VIL3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WFDFH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WFDFH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WFDH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WFDH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WFWGH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WFWGH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WFWH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WFWH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WIL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WIL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WIL2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WIL2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WIL3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WIL3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WILH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WILH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WILX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WILX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WIT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WIT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WITBA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WITBA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WLFDF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WLFDF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WLFDI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WLFDI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WLFWG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WLFWG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WLFWI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WLFWI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WYRWH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WYRWH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WYV.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WYV.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WYVH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\50WYVH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51BARUD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51BARUD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51BEAWA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51BEAWA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51BEEFD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51BEEFD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51BEEFI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51BEEFI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51CATBA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51CATBA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DARGAB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DARGAB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DRAGU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DRAGU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DRAWY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DRAWY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DUEBO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DUEBO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DUECL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DUECL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DUEWA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51DUEWA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HARHOR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HARHOR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HARSHO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HARSHO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHRGH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHRGH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHRGU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHRGU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHRH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHRH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHRMA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HHRMA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HNTMN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HNTMN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HSTMU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51HSTMU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51OCH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51OCH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51OCHH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51OCHH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51ORCSS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51ORCSS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51OTID.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51OTID.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51SHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51SHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51SPE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51SPE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51TROIC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51TROIC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51WYRWH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51WYRWH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51ZAMA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\51ZAMA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52ARUMA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52ARUMA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52BARUD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52BARUD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52BERED.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52BERED.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DARGAB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DARGAB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DOLON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DOLON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUEBO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUEBO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUEBOX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUEBOX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUECL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUECL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUECLX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUECLX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUELE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUELE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUEWA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUEWA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUEWAX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52DUEWAX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52GOLIR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52GOLIR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52HARHOR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52HARHOR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKFL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKFL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKFLX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKFLX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKMH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKMH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKML.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKML.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKMLX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MNKMLX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MOROHE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52MOROHE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52NONIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52NONIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52ORCSS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52ORCSS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52PORTAL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52PORTAL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52PROXI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52PROXI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52SALISA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52SALISA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52SALISX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52SALISX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52SERSA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52SERSA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52SVALTI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52SVALTI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52VEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52VEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52VENH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52VENH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52WYRWH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52WYRWH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52YETGH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52YETGH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52YETTG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52YETTG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52YETTU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52YETTU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52YETUH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52YETUH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52ZAMA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\52ZAMA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53ABDOSH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53ABDOSH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53BEELTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53BEELTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53BLUMYC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53BLUMYC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53CELEDR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53CELEDR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53CRADDR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53CRADDR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DEEPTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DEEPTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DESATH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DESATH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DESPGU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DESPGU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRACAH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRACAH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRFIT2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRFIT2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRFITH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRFITH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIDFI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIDFI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIDPR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIDPR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIDWI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIDWI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIFIH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIFIH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIPRH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIPRH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIWIH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRIWIH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DROAS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DROAS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DROPR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DROPR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DROSS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DROSS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRWITH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DRWITH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DUFITH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53DUFITH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53EAELEM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53EAELEM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53ECKTAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53ECKTAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53ELDERB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53ELDERB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53FGOLEM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53FGOLEM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53FOMOTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53FOMOTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53FORGE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53FORGE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GALOOM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GALOOM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GINAFA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GINAFA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GINAFD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GINAFD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GOBFOD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GOBFOD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GOLIM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GOLIM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GOLIMH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GOLIMH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GOLIMX.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53GOLIMX.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53HARPY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53HARPY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53HEGGR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53HEGGR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53IMPHRA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53IMPHRA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53KADRES.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53KADRES.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53LAB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53LAB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53LIGGEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53LIGGEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MAJRAS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MAJRAS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MALAVO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MALAVO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MARALI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MARALI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MGOLEM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MGOLEM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MINOTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MINOTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MIRABE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MIRABE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MORHIZ.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MORHIZ.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MYCBLH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MYCBLH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MYCREH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MYCREH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MYRVEK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53MYRVEK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53NADAL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53NADAL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53OINCHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53OINCHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53OOLAY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53OOLAY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53OSWALD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53OSWALD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53POD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53POD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53REDMYC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53REDMYC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SORAPP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SORAPP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SORN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SORN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SPIGIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SPIGIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SPISW.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SPISW.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SPISWH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SPISWH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SPITDR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53SPITDR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VALAS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VALAS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VICISC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VICISC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VIDRFI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VIDRFI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VIDRPR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VIDRPR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VIDRWI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VIDRWI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VIIZRA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53VIIZRA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53WODE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53WODE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53ZEPH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\53ZEPH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60ABPRIE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60ABPRIE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60ASHRA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60ASHRA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CCABAL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CCABAL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CEDRA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CEDRA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CHEAP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CHEAP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CONLAH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CONLAH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CONLAN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60CONLAN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60DRAY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60DRAY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60GERBAH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60GERBAH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60GERBAS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60GERBAS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60GUARDI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60GUARDI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HARPY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HARPY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HEART.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HEART.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HEDEAD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HEDEAD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HIEPHE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HIEPHE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HIEPHH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HIEPHH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HISTAC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60HISTAC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60INHATR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60INHATR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60INITIA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60INITIA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60ISELOR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60ISELOR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60JERMSH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60JERMSH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60JERMSY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60JERMSY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60JESZRA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60JESZRA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60KATCHM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60KATCHM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60KHAV.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60KHAV.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60KHAVH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60KHAVH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60MADAE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60MADAE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60MEZWAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60MEZWAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60MOTHER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60MOTHER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NATE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NATE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NATEH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NATEH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60NEOORP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60OJAIHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60OJAIHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60PBFIGT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60PBFIGT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60PBSORC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60PBSORC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60SASHKA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60SASHKA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60SHEEMH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60SHEEMH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60SHEEMI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60SHEEMI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60VIFANG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60VIFANG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WIGARC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WIGARC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WIGHT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WIGHT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WIGHTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WIGHTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WIGHTL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WIGHTL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WRAITH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WRAITH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WRAITN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60WRAITN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTARCH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTARCH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTCOOK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTCOOK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTELIT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTELIT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTHIPR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTHIPR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTPRIE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTPRIE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTSORC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YTSORC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YUANTI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\60YUANTI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61ALCHEM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61ALCHEM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61AMPHIT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61AMPHIT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61ARCHON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61ARCHON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61AWYVER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61AWYVER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61BRIDGE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61BRIDGE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61CITADE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61CITADE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DEFREE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DEFREE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DFIRPE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DFIRPE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DHELHO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DHELHO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DLIZLE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DLIZLE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DLOTHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DLOTHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DMEPLA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DMEPLA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DTROLL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DTROLL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYAARC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYAARC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYAPRI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYAPRI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYASEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYASEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYHPRI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYHPRI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYHSOR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYHSOR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYPBLA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYPBLA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYPFIG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61DYPFIG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61EFREET.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61EFREET.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61EMBASS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61EMBASS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61FIRPEO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61FIRPEO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61GOLIRO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61GOLIRO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61GRISHU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61GRISHU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61HELHOU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61HELHOU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61HISTAC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61HISTAC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61IZBEL2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61IZBEL2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61IZBELA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61IZBELA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61JAGUAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61JAGUAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61JASPER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61JASPER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61LIZLEA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61LIZLEA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61LIZSHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61LIZSHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61LIZWAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61LIZWAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61LOTHAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61LOTHAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61MANDAL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61MANDAL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61MEPLAV.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61MEPLAV.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61MUSJEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61MUSJEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61NHEERO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61NHEERO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PALACE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PALACE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISF1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISF1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISF2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISF2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISF3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISF3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISI1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISI1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISI2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISI2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISI3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISI3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISTR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISTR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISU1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISU1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISU2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISU2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISU3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PRISU3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PYROS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PYROS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PYROSD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61PYROSD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61RAKSHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61RAKSHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61RYHPRI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61RYHPRI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61RYHSOR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61RYHSOR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SALFRO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SALFRO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SKEARM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SKEARM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SLIOLI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SLIOLI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SNAGIA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SNAGIA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SPIGIA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SPIGIA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SPISWD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61SPISWD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61STOSLB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61STOSLB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61THORAS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61THORAS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61THRONE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61THRONE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61TROLL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61TROLL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61VENOMI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61VENOMI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61WEBGEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61WEBGEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61WYVERN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61WYVERN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YAARCH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YAARCH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YAPRIE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YAPRIE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YASENT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YASENT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YASUMM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YASUMM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YHPRIE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YHPRIE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YHSORC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YHSORC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YPBLAD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YPBLAD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YPFIGH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61YPFIGH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61ZILTYO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\61ZILTYO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS5.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62CBNS5.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL5.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL5.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDEL6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR5.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR5.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR7.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR7.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR8.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR8.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR9.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDOR9.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDORE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRDORE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRGARD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62DRGARD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62ELFIG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62ELFIG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62ELFIG2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62ELFIG2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62EORO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62EORO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62FDND.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62FDND.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62FDND2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62FDND2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62FEYR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62FEYR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62GFYR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62GFYR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62GFYR2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62GFYR2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62GORG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62GORG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HADR2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HADR2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HAGOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HAGOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HAGOB1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HAGOB1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HAYUA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HAYUA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HAYUA2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HAYUA2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HORC2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HORC2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HORC4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62HORC4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62ICEZOM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62ICEZOM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62KRATU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62KRATU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62MDARF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62MDARF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62NEOORC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62NEOORC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62NEOORN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62NEOORN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62OROGR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62OROGR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62OROGR2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62OROGR2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62OROGR4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62OROGR4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62PUUK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62PUUK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62REDWI3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62REDWI3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62REDWIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62REDWIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SAABL1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SAABL1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SAABL2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SAABL2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SARALO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SARALO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SKXVM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SKXVM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SPBLD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62SPBLD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62TSOL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62TSOL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62WANMOK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62WANMOK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62WTRFAL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\62WTRFAL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ABASH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ABASH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ABGDEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ABGDEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ABGDN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ABGDN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63BUVAI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63BUVAI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63CEDDED.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63CEDDED.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63CEDRIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63CEDRIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63CHIMH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63CHIMH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63COOK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63COOK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63COOK2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63COOK2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63DMNCON.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63DMNCON.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63DMNGEM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63DMNGEM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63DRACE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63DRACE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63DROTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63DROTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63EELE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63EELE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63EELE2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63EELE2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63EELE3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63EELE3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ERADRU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ERADRU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FOOD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FOOD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FORMIS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FORMIS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FW1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FW1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FW2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FW2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FW3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FW3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FW4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FW4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FYNNE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63FYNNE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GADU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GADU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLABS1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLABS1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLABS2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLABS2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLABSL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLABSL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLABSR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLABSR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLBXP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GLBXP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDCOM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDCOM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDFEA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDFEA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDFN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDFN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDFNA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDFNA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDFP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDFP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW5.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW5.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDLW6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD5.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD5.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMD6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMNA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMNA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63GRDMP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63INSTRC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63INSTRC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63INVSTK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63INVSTK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ISAIR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ISAIR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ISAIR2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ISAIR2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ISARN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ISARN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ISARN2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ISARN2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63JAE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63JAE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63JERRE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63JERRE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63KAV.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63KAV.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63KEG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63KEG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63KNTXVM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63KNTXVM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MADAE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MADAE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MADAE2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MADAE2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MADAN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MADAN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MADAN2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MADAN2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MNKF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MNKF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MNKFH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MNKFH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MNKM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MNKM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MNKMH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MNKMH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MOURN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MOURN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MW1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MW1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MW2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MW2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MW3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MW3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MW4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63MW4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ORRICF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ORRICF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PFIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PFIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PFINH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PFINH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PFINN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PFINN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PHAEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PHAEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PREC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63PREC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63RIKI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63RIKI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ROGA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ROGA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63RUINL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63RUINL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63SERAK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63SERAK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63SLAVES.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63SLAVES.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TASHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TASHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63THAYMF.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63THAYMF.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63THAYMM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63THAYMM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TILZEN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TILZEN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TUTU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TUTU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TUTUH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TUTUH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TUTUN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63TUTUN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63VASHTI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63VASHTI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63VESE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63VESE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63VYLU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63VYLU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63XAVIER.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63XAVIER.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63YSHA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63YSHA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63YXBU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63YXBU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63YXBUH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63YXBUH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63YXBUN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63YXBUN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ZAEM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ZAEM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ZIGMAL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ZIGMAL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ZIGMAM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ZIGMAM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ZILVAR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\63ZILVAR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64GNLAPR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64GNLAPR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64GOBAPR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64GOBAPR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64IGOLEM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64IGOLEM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64ORRICH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64ORRICH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64ORRICK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64ORRICK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64WEENA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\64WEENA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65BHDR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65BHDR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65BRUTAI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65BRUTAI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65COREL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65COREL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65CORN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65CORN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65DRDEL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65DRDEL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65FLRART.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65FLRART.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65GARUK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65GARUK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65GLAB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65GLAB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65GNLLIB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65GNLLIB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65GOBWLP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65GOBWLP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HAORC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HAORC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST7.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65HTMST7.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65ILLMAT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65ILLMAT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65IYTXM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65IYTXM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65IYTXMS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65IYTXMS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65LEMURE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65LEMURE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65NEOORC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65NEOORC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65NEOORE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65NEOORE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65ORRUIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65ORRUIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL6.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL6.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL7.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65RUCOL7.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65SILVA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65SILVA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65SKXVM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65SKXVM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65SKXVM2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65SKXVM2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65SUNE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65SUNE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WELP.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WELP.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WLMR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WLMR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WORSH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WORSH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WORSH2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WORSH2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WORSH3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WORSH3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WORSH4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65WORSH4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65YQUOG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\65YQUOG.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66BISBE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66BISBE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66BUGB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66BUGB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66BUGBC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66BUGBC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66CHIM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66CHIM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66DGAERN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66DGAERN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66DGUTH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66DGUTH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66DHARSH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66DHARSH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66DSHERI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66DSHERI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66ELTOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66ELTOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAGOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAGOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAGOB1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAGOB1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAGOB3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAGOB3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAORC1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAORC1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAORC3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAORC3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAYUA.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAYUA.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAYUA3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66HAYUA3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK1.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK1.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MNK4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MORVYN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66MORVYN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66OROC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66OROC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66OROGR7.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66OROGR7.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66PUDU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66PUDU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66RHDR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66RHDR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66STUB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66STUB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66STUBH.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66STUBH.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66VYXEIN.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\66VYXEIN.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\673NORC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\673NORC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\673RHDR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\673RHDR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\673SKXVM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\673SKXVM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ABGD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ABGD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67BHDR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67BHDR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67BUVAI.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67BUVAI.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67CARL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67CARL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67DEKNT.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67DEKNT.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67EHAGOB.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67EHAGOB.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ENEOO.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ENEOO.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ENEOO2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ENEOO2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ENEOO3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ENEOO3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67GFYR.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67GFYR.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67GRBGD.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67GRBGD.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67HAGOBE.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67HAGOBE.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67HAORC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67HAORC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67HAORC2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67HAORC2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67HARC.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67HARC.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS2.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS2.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS4.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS4.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS5.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67LMRS5.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67NALAK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67NALAK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67OBBAK.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67OBBAK.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ORMIS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ORMIS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ORMISL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67ORMISL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67PUDDY.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67PUDDY.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67PUSJU.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67PUSJU.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67REDWI3.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67REDWI3.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67SKXVM.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67SKXVM.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67SPLMRS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67SPLMRS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67TORAL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67TORAL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67TRMAL.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67TRMAL.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67WLMRS.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\67WLMRS.json', single_clob) as Contents;
go
insert into iwd2.cre(FilePath, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\DYNOKEG.json', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Creatures\DYNOKEG.json', single_clob) as Contents;
go
commit;
