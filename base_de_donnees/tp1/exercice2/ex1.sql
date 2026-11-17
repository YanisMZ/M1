CREATE OR REPLACE FUNCTION fact_iter(n INTEGER)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE
    resultat NUMERIC := 1;
    i INTEGER;
BEGIN
    IF n < 0 THEN
        RAISE EXCEPTION 'n doit être positif ou nul';
    END IF;

    FOR i IN 1..n LOOP
        resultat := resultat * i;
    END LOOP;

    RETURN resultat;
END;
$$;



CREATE OR REPLACE FUNCTION fact_rec(n INTEGER)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    IF n < 0 THEN
        RAISE EXCEPTION 'n doit être positif ou nul';
    ELSIF n = 0 OR n = 1 THEN
        RETURN 1;
    ELSE
        RETURN n * fact_rec(n - 1);
    END IF;
END;
$$;
