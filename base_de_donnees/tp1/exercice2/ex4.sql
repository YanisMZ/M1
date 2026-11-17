CREATE OR REPLACE FUNCTION calcul(n INTEGER, m INTEGER)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN POWER(2, n) + POWER(m, 2);
END;
$$;


--- SELECT calcul(3, 4); ---


/*
DO $$
BEGIN
    RAISE NOTICE 'Résultat : %', calcul(2, 3);
END;
$$;
*/

