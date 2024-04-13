SELECT u.username
FROM users u
JOIN (
    SELECT to_user_id
    FROM messages
    GROUP BY to_user_id
    ORDER BY COUNT(*) DESC, to_user_id ASC
    LIMIT 1
) m ON u.id = m.to_user_id;
