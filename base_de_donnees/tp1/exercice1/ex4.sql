DO $$
DECLARE
    n INTEGER := 17;
    m INTEGER := 5;
    r INTEGER;
BEGIN
    IF m = 0 THEN
        RAISE NOTICE 'Erreur : division par zéro impossible.';
    ELSE
        r := n;

        WHILE r >= m LOOP
            r := r - m;
        END LOOP;

        RAISE NOTICE 'Le reste est : %', r;
    END IF;
END $$;