DO $$
DECLARE
    num_dept INTEGER := 30;
    nb INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO nb
    FROM emp
    WHERE deptno = num_dept;

    RAISE NOTICE 'Nombre d''employés : %', nb;
END $$;