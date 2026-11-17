CREATE OR REPLACE FUNCTION fFactR(n INTEGER)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    IF n < 0 THEN
        RAISE EXCEPTION 'n doit être positif ou nul';
    ELSIF n = 0 OR n = 1 THEN
        RETURN 1;
    ELSE
        RETURN n * fFactR(n - 1);
    END IF;
END;
$$;



CREATE OR REPLACE PROCEDURE pFact(n INTEGER)
LANGUAGE plpgsql
AS $$
DECLARE
    resultat NUMERIC;
BEGIN
    resultat := fFactR(n);

    RAISE NOTICE 'La factorielle de % est %', n, resultat;
END;
$$;



DO $$
DECLARE
    n INTEGER := 5;
BEGIN
    CALL pFact(n);
END;
$$;