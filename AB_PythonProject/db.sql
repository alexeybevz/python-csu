CREATE TABLE whse (
	id int IDENTITY(1,1) NOT NULL,
	good_name nvarchar(100) NOT NULL,
	qty decimal(18,8) NOT NULL,
	manufacter nvarchar(100) NOT NULL,
	price decimal(18,2) NOT NULL,
	size decimal(18,2) NOT NULL,
	PRIMARY KEY(id),
);
GO

CREATE NONCLUSTERED INDEX IX_whse_name ON whse (good_name ASC);
GO