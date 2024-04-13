SELECT COUNT(*) AS "No. of Public Schools" , "city" FROM "schools" WHERE "type" = 'Public School'
    GROUP BY "city"
        ORDER BY "No. of Public Schools" DESC, "city" ASC
            LIMIT 10;
