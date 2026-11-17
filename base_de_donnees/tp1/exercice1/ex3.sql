CREATE TABLE nombre (
    a NUMERIC,
    b NUMERIC
);


DO $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..10 LOOP
        IF i = 1 THEN
            INSERT INTO nombre (a, b)
            VALUES (i, 1);
        ELSE
            INSERT INTO nombre (a, b)
            VALUES (i, 3 * i);
        END IF;
    END LOOP;
END $$;