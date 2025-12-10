-- DO
-- $$
-- DECLARE
--     rows_deleted INTEGER;
-- BEGIN
--     WITH Duplicates AS (
--         SELECT
--             ctid,
--             user_id,
--             event_time,
--             LAG(user_id, 1) OVER (
--                 PARTITION BY user_id, event_time 
--                 ORDER BY ctid
--             ) AS previous_user_id
--         FROM
--             customers
--     )
--     DELETE FROM customers
--     WHERE ctid IN (
--         SELECT d.ctid
--         FROM Duplicates d
--         WHERE d.user_id = d.previous_user_id
--     );
--     GET DIAGNOSTICS rows_deleted = ROW_COUNT;
--     RAISE NOTICE 'Nombre de doublons supprimés de la table customers : %', rows_deleted;
-- END
-- $$;

DO $$
DECLARE
    initial_count INTEGER;
    final_count INTEGER;
    rows_deleted_actual INTEGER; -- Utilisation de la variable pour stocker le ROW_COUNT du DELETE
BEGIN
    -- 1. Compte initial (pour information)
    SELECT COUNT(*) INTO initial_count FROM customers;
    RAISE NOTICE 'Initial row count: %', initial_count;

    -- 2. Suppression des doublons et identification
    WITH Duplicates_to_Delete AS (
        SELECT
            ctid -- Nous sélectionnons le ctid des lignes à supprimer
        FROM (
            SELECT
                ctid,
                event_time,
                -- Calcule l'horodatage de l'événement précédent dans la même partition
                LAG(event_time) OVER (
                    PARTITION BY event_type, product_id, user_id, price, user_session
                    ORDER BY event_time
                ) AS previous_time
            FROM customers
        ) AS sub
        -- Critère de doublon temporel : la ligne précédente existe ET l'écart est <= 1 seconde
        WHERE previous_time IS NOT NULL
          AND event_time - previous_time <= INTERVAL '1 second'
    )
    -- DELETE directement sur le ctid des lignes identifiées
    DELETE FROM customers c
    USING Duplicates_to_Delete d
    WHERE c.ctid = d.ctid;

    -- Capture le nombre de lignes réellement supprimées
    GET DIAGNOSTICS rows_deleted_actual = ROW_COUNT;
    RAISE NOTICE 'Removed % duplicate rows', rows_deleted_actual;

    -- 3. Compte final (pour information)
    SELECT COUNT(*) INTO final_count FROM customers;
    RAISE NOTICE 'Final row count: %', final_count;
    RAISE NOTICE 'Duplicate removal completed successfully!';
    
END $$;