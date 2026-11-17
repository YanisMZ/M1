CREATE OR REPLACE PROCEDURE afficher_n(n INTEGER)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
BEGIN
    IF n < 1 THEN
        RAISE NOTICE 'n doit être supérieur ou égal à 1';
    ELSE
        FOR i IN 1..n LOOP
            RAISE NOTICE '%', i;
        END LOOP;
    END IF;
END;
$$;




-- CALL afficher_n(5); --



/* DO $$
DECLARE
    n INTEGER := 10;
BEGIN
    CALL afficher_n(n);
END;
$$; 
*/
