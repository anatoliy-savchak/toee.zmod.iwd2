truncate table iwd2.scripts;
go

insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\actionlistempty.json', 'actionlistempty', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\actionlistempty.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\actionoverride.json', 'actionoverride', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\actionoverride.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\activate.json', 'activate', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\activate.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\addexperiencepartycr.json', 'addexperiencepartycr', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\addexperiencepartycr.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\addfeat.json', 'addfeat', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\addfeat.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\addjournalentry.json', 'addjournalentry', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\addjournalentry.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\addxpvar.json', 'addxpvar', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\addxpvar.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\alignment.json', 'alignment', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\alignment.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\allegiance.json', 'allegiance', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\allegiance.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\allowarearesting.json', 'allowarearesting', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\allowarearesting.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\anypconmap.json', 'anypconmap', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\anypconmap.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\anypcseesenemy.json', 'anypcseesenemy', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\anypcseesenemy.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\applyspell.json', 'applyspell', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\applyspell.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\arearestdisabled.json', 'arearestdisabled', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\arearestdisabled.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\attack.json', 'attack', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\attack.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\attackedby.json', 'attackedby', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\attackedby.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\attackoneround.json', 'attackoneround', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\attackoneround.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\attackreevaluate.json', 'attackreevaluate', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\attackreevaluate.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\backstab.json', 'backstab', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\backstab.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\bitglobal.json', 'bitglobal', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\bitglobal.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changeaiscript.json', 'changeaiscript', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changeaiscript.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changecurrentscript.json', 'changecurrentscript', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changecurrentscript.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changeenemyally.json', 'changeenemyally', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changeenemyally.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changespecifics.json', 'changespecifics', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changespecifics.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changestat.json', 'changestat', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\changestat.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\chargecount.json', 'chargecount', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\chargecount.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkareadifflevel.json', 'checkareadifflevel', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkareadifflevel.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkdoorflags.json', 'checkdoorflags', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkdoorflags.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkskillgt.json', 'checkskillgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkskillgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkskilllt.json', 'checkskilllt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkskilllt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkspellstate.json', 'checkspellstate', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkspellstate.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkstat.json', 'checkstat', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkstat.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkstatgt.json', 'checkstatgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkstatgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkstatlt.json', 'checkstatlt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\checkstatlt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\chunkcreature.json', 'chunkcreature', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\chunkcreature.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\class.json', 'class', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\class.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\classex.json', 'classex', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\classex.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\clearactions.json', 'clearactions', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\clearactions.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\clearallactions.json', 'clearallactions', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\clearallactions.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\clearpartyeffects.json', 'clearpartyeffects', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\clearpartyeffects.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\clearspriteeffects.json', 'clearspriteeffects', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\clearspriteeffects.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\closedoor.json', 'closedoor', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\closedoor.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\createcreature.json', 'createcreature', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\createcreature.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\createitem.json', 'createitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\createitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\creaturehidden.json', 'creaturehidden', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\creaturehidden.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\currentareais.json', 'currentareais', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\currentareais.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\daynight.json', 'daynight', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\daynight.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\deactivate.json', 'deactivate', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\deactivate.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dead.json', 'dead', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dead.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\debug.json', 'debug', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\debug.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\destroyitem.json', 'destroyitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\destroyitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\destroyself.json', 'destroyself', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\destroyself.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dialoginterrupt.json', 'dialoginterrupt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dialoginterrupt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dialogue.json', 'dialogue', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dialogue.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\died.json', 'died', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\died.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\difficulty.json', 'difficulty', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\difficulty.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\displaymessage.json', 'displaymessage', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\displaymessage.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\displaystring.json', 'displaystring', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\displaystring.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dropinventory.json', 'dropinventory', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dropinventory.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dropinventoryex.json', 'dropinventoryex', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dropinventoryex.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dropitem.json', 'dropitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\dropitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\eighthnearest.json', 'eighthnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\eighthnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\eigthnearestenemyof.json', 'eigthnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\eigthnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\endcutscenemode.json', 'endcutscenemode', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\endcutscenemode.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\endgame.json', 'endgame', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\endgame.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\enemy.json', 'enemy', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\enemy.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\entirepartyonmap.json', 'entirepartyonmap', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\entirepartyonmap.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\equipitem.json', 'equipitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\equipitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\equipmostdamagingmelee.json', 'equipmostdamagingmelee', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\equipmostdamagingmelee.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\equipranged.json', 'equipranged', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\equipranged.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\equipweapon.json', 'equipweapon', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\equipweapon.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\escapearea.json', 'escapearea', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\escapearea.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\escapeareadestroy.json', 'escapeareadestroy', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\escapeareadestroy.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\exists.json', 'exists', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\exists.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\explore.json', 'explore', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\explore.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\face.json', 'face', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\face.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\faceobject.json', 'faceobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\faceobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\facesavedlocation.json', 'facesavedlocation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\facesavedlocation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fadefromcolor.json', 'fadefromcolor', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fadefromcolor.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fadetocolor.json', 'fadetocolor', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fadetocolor.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\farthest.json', 'farthest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\farthest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\farthestenemyof.json', 'farthestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\farthestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fifthnearest.json', 'fifthnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fifthnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fifthnearestenemyof.json', 'fifthnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fifthnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\floatmessage.json', 'floatmessage', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\floatmessage.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\forcehide.json', 'forcehide', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\forcehide.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\forcemarkedspell.json', 'forcemarkedspell', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\forcemarkedspell.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\forcespell.json', 'forcespell', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\forcespell.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\forcespellpoint.json', 'forcespellpoint', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\forcespellpoint.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fourthnearest.json', 'fourthnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fourthnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fourthnearestenemyof.json', 'fourthnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\fourthnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\gender.json', 'gender', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\gender.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\general.json', 'general', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\general.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\giveitem.json', 'giveitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\giveitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\giveitemcreate.json', 'giveitemcreate', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\giveitemcreate.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\global.json', 'global', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\global.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\globalgt.json', 'globalgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\globalgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\globallt.json', 'globallt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\globallt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\globaltimerexpired.json', 'globaltimerexpired', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\globaltimerexpired.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\globaltimernotexpired.json', 'globaltimernotexpired', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\globaltimernotexpired.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hasitem.json', 'hasitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hasitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hasiteminslot.json', 'hasiteminslot', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hasiteminslot.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\havespell.json', 'havespell', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\havespell.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\heard.json', 'heard', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\heard.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\help.json', 'help', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\help.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hide.json', 'hide', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hide.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hidecreature.json', 'hidecreature', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hidecreature.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hitby.json', 'hitby', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hitby.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hp.json', 'hp', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hp.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hpgt.json', 'hpgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hpgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hplost.json', 'hplost', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hplost.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hplostgt.json', 'hplostgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hplostgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hplt.json', 'hplt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hplt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hppercent.json', 'hppercent', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hppercent.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hppercentgt.json', 'hppercentgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hppercentgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hppercentlt.json', 'hppercentlt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\hppercentlt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\incrementchapter.json', 'incrementchapter', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\incrementchapter.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\incrementglobal.json', 'incrementglobal', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\incrementglobal.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\incrementinternal.json', 'incrementinternal', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\incrementinternal.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\incutscenemode.json', 'incutscenemode', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\incutscenemode.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\inparty.json', 'inparty', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\inparty.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\internal.json', 'internal', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\internal.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\internalgt.json', 'internalgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\internalgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isactive.json', 'isactive', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isactive.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isanimationid.json', 'isanimationid', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isanimationid.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\iscreatureareaflag.json', 'iscreatureareaflag', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\iscreatureareaflag.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\iscreaturehiddeninshadows.json', 'iscreaturehiddeninshadows', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\iscreaturehiddeninshadows.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isextendednight.json', 'isextendednight', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isextendednight.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isfacingsavedrotation.json', 'isfacingsavedrotation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isfacingsavedrotation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isheartoffurymodeon.json', 'isheartoffurymodeon', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isheartoffurymodeon.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\ismarkedspell.json', 'ismarkedspell', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\ismarkedspell.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\ispathcriticalobject.json', 'ispathcriticalobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\ispathcriticalobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isplayernumber.json', 'isplayernumber', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isplayernumber.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isrotation.json', 'isrotation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isrotation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isscriptname.json', 'isscriptname', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isscriptname.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isspelltargetvalid.json', 'isspelltargetvalid', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isspelltargetvalid.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isteambiton.json', 'isteambiton', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isteambiton.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isweaponranged.json', 'isweaponranged', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\isweaponranged.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\itemisidentified.json', 'itemisidentified', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\itemisidentified.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\jumptoobject.json', 'jumptoobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\jumptoobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\jumptopoint.json', 'jumptopoint', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\jumptopoint.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\jumptosavedlocation.json', 'jumptosavedlocation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\jumptosavedlocation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\kill.json', 'kill', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\kill.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\kit.json', 'kit', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\kit.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lastattackerof.json', 'lastattackerof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lastattackerof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lastheardby.json', 'lastheardby', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lastheardby.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lastseenby.json', 'lastseenby', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lastseenby.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lasttalkedtoby.json', 'lasttalkedtoby', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lasttalkedtoby.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lasttargetedby.json', 'lasttargetedby', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lasttargetedby.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\level.json', 'level', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\level.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\levelgt.json', 'levelgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\levelgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\levelinclass.json', 'levelinclass', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\levelinclass.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\levelinclassgt.json', 'levelinclassgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\levelinclassgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lock.json', 'lock', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\lock.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\los.json', 'los', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\los.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\makeunselectable.json', 'makeunselectable', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\makeunselectable.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\markobject.json', 'markobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\markobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\markspellandobject.json', 'markspellandobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\markspellandobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\moraleset.json', 'moraleset', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\moraleset.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\mostdamagedof.json', 'mostdamagedof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\mostdamagedof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\movetoobject.json', 'movetoobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\movetoobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\movetoobjectfollow.json', 'movetoobjectfollow', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\movetoobjectfollow.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\movetoobjectuntilsee.json', 'movetoobjectuntilsee', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\movetoobjectuntilsee.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\movetopoint.json', 'movetopoint', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\movetopoint.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\moveviewobject.json', 'moveviewobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\moveviewobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\moveviewpoint.json', 'moveviewpoint', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\moveviewpoint.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\multiplayersync.json', 'multiplayersync', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\multiplayersync.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearest.json', 'nearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearestenemyof.json', 'nearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearestenemysummoned.json', 'nearestenemysummoned', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearestenemysummoned.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearestpc.json', 'nearestpc', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearestpc.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearlocation.json', 'nearlocation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearlocation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearsavedlocation.json', 'nearsavedlocation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\nearsavedlocation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\ninthnearest.json', 'ninthnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\ninthnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\ninthnearestenemyof.json', 'ninthnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\ninthnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\noaction.json', 'noaction', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\noaction.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numinparty.json', 'numinparty', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numinparty.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numinpartygt.json', 'numinpartygt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numinpartygt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numinpartylt.json', 'numinpartylt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numinpartylt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numitemspartygt.json', 'numitemspartygt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numitemspartygt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numtimestalkedto.json', 'numtimestalkedto', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numtimestalkedto.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numtimestalkedtogt.json', 'numtimestalkedtogt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numtimestalkedtogt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numtimestalkedtolt.json', 'numtimestalkedtolt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\numtimestalkedtolt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\oncreation.json', 'oncreation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\oncreation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\opendoor.json', 'opendoor', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\opendoor.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\openstate.json', 'openstate', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\openstate.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\outofammo.json', 'outofammo', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\outofammo.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\panic.json', 'panic', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\panic.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\partygoldgt.json', 'partygoldgt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\partygoldgt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\partygoldlt.json', 'partygoldlt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\partygoldlt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\partyhasitem.json', 'partyhasitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\partyhasitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\picklockfailed.json', 'picklockfailed', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\picklockfailed.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\pickpocketfailed.json', 'pickpocketfailed', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\pickpocketfailed.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\playdead.json', 'playdead', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\playdead.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player1.json', 'player1', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player1.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player2.json', 'player2', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player2.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player3.json', 'player3', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player3.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player4.json', 'player4', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player4.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player5.json', 'player5', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player5.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player6.json', 'player6', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\player6.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\playsequence.json', 'playsequence', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\playsequence.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\playsound.json', 'playsound', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\playsound.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\polymorph.json', 'polymorph', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\polymorph.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\race.json', 'race', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\race.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\randomnum.json', 'randomnum', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\randomnum.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\randomnumlt.json', 'randomnumlt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\randomnumlt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\randomturn.json', 'randomturn', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\randomturn.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\randomwalk.json', 'randomwalk', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\randomwalk.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\range.json', 'range', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\range.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\reallyforcespell.json', 'reallyforcespell', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\reallyforcespell.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\removespell.json', 'removespell', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\removespell.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\resetjoinrequests.json', 'resetjoinrequests', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\resetjoinrequests.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\rest.json', 'rest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\rest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\restparty.json', 'restparty', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\restparty.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\restuntilhealed.json', 'restuntilhealed', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\restuntilhealed.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\returntosavedlocation.json', 'returntosavedlocation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\returntosavedlocation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\runawayfrom.json', 'runawayfrom', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\runawayfrom.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\runawayfromnoleavearea.json', 'runawayfromnoleavearea', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\runawayfromnoleavearea.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\savegame.json', 'savegame', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\savegame.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\screenshake.json', 'screenshake', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\screenshake.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\scripts_index.json', 'scripts_index', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\scripts_index.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\secondnearest.json', 'secondnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\secondnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\secondnearestenemyof.json', 'secondnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\secondnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\see.json', 'see', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\see.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sendtrigger.json', 'sendtrigger', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sendtrigger.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sequence.json', 'sequence', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sequence.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setapparentnamestrref.json', 'setapparentnamestrref', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setapparentnamestrref.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setbestweapon.json', 'setbestweapon', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setbestweapon.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setcreatureareaflag.json', 'setcreatureareaflag', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setcreatureareaflag.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setcriticalpathobject.json', 'setcriticalpathobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setcriticalpathobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setdialog.json', 'setdialog', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setdialog.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setdialoguerange.json', 'setdialoguerange', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setdialoguerange.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setdoorflag.json', 'setdoorflag', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setdoorflag.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setextendednight.json', 'setextendednight', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setextendednight.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobal.json', 'setglobal', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobal.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobalrandom.json', 'setglobalrandom', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobalrandom.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobaltimer.json', 'setglobaltimer', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobaltimer.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobaltimeronce.json', 'setglobaltimeronce', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobaltimeronce.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobaltimerrandom.json', 'setglobaltimerrandom', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setglobaltimerrandom.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sethp.json', 'sethp', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sethp.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sethppercent.json', 'sethppercent', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sethppercent.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setinternal.json', 'setinternal', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setinternal.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setinterrupt.json', 'setinterrupt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setinterrupt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setlastmarkedobject.json', 'setlastmarkedobject', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setlastmarkedobject.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setmusic.json', 'setmusic', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setmusic.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setmytarget.json', 'setmytarget', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setmytarget.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setnumtimestalkedto.json', 'setnumtimestalkedto', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setnumtimestalkedto.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setregularnamestrref.json', 'setregularnamestrref', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setregularnamestrref.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setrestencounterchance.json', 'setrestencounterchance', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setrestencounterchance.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setsavedlocation.json', 'setsavedlocation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setsavedlocation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setsavedlocationpoint.json', 'setsavedlocationpoint', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setsavedlocationpoint.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setspelltarget.json', 'setspelltarget', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setspelltarget.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setstartpos.json', 'setstartpos', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setstartpos.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setteambit.json', 'setteambit', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\setteambit.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\seventhnearest.json', 'seventhnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\seventhnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\seventhnearestenemyof.json', 'seventhnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\seventhnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\shout.json', 'shout', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\shout.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sixthnearest.json', 'sixthnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sixthnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sixthnearestenemyof.json', 'sixthnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\sixthnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\smallwait.json', 'smallwait', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\smallwait.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\specifics.json', 'specifics', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\specifics.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spell.json', 'spell', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spell.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellcasteffect.json', 'spellcasteffect', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellcasteffect.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellhiteffectpoint.json', 'spellhiteffectpoint', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellhiteffectpoint.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellhiteffectsprite.json', 'spellhiteffectsprite', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellhiteffectsprite.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellpoint.json', 'spellpoint', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellpoint.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellwait.json', 'spellwait', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\spellwait.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startcutscene.json', 'startcutscene', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startcutscene.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startcutscenemode.json', 'startcutscenemode', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startcutscenemode.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startmovie.json', 'startmovie', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startmovie.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startrandomtimer.json', 'startrandomtimer', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startrandomtimer.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startstore.json', 'startstore', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\startstore.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\starttimer.json', 'starttimer', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\starttimer.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\statecheck.json', 'statecheck', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\statecheck.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\stopjoinrequests.json', 'stopjoinrequests', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\stopjoinrequests.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\subrace.json', 'subrace', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\subrace.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\takepartygold.json', 'takepartygold', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\takepartygold.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\takepartyitem.json', 'takepartyitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\takepartyitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\takepartyitemall.json', 'takepartyitemall', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\takepartyitemall.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\takepartyitemnum.json', 'takepartyitemnum', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\takepartyitemnum.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\targetunreachable.json', 'targetunreachable', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\targetunreachable.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\tenthnearest.json', 'tenthnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\tenthnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\tenthnearestenemyof.json', 'tenthnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\tenthnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\thirdnearest.json', 'thirdnearest', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\thirdnearest.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\thirdnearestenemyof.json', 'thirdnearestenemyof', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\thirdnearestenemyof.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timegt.json', 'timegt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timegt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timelt.json', 'timelt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timelt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timeofday.json', 'timeofday', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timeofday.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timeractive.json', 'timeractive', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timeractive.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timerexpired.json', 'timerexpired', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\timerexpired.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\totalitemcnt.json', 'totalitemcnt', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\totalitemcnt.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\transferinventory.json', 'transferinventory', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\transferinventory.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\triggeractivation.json', 'triggeractivation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\triggeractivation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\turn.json', 'turn', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\turn.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\undoexplore.json', 'undoexplore', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\undoexplore.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\unlock.json', 'unlock', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\unlock.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\useitem.json', 'useitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\useitem.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\wait.json', 'wait', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\wait.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\waitanimation.json', 'waitanimation', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\waitanimation.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\waitrandom.json', 'waitrandom', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\waitrandom.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\weather.json', 'weather', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\weather.json', single_clob) as Contents;
go
insert into iwd2.scripts(FilePath, FileName, Content) select 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\xequipitem.json', 'xequipitem', BulkColumn from openrowset(bulk 'D:\Dev.Home\GitHub\anatoliy-savchak\toee.zmod.iwd2\resources\iwd2_exp\Scripts\xequipitem.json', single_clob) as Contents;
go