DECLARE @p int = 20

WHILE @p >= 1

BEGIN PRINT REPLICATE('* ',@p)
SET @p = @p-1
END;
