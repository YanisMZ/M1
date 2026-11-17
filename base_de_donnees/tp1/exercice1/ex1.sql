DO $$
DECLARE
    a NUMERIC := 10;
    b NUMERIC := 20;
    maxi NUMERIC;
BEGIN
    IF a > b THEN
        maxi := a;
    ELSE
        maxi := b;
    END IF;

    RAISE NOTICE 'Le maximum est : %', maxi;
END $$;