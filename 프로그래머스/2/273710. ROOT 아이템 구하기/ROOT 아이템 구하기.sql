SELECT I.ITEM_ID, I.ITEM_NAME
FROM ITEM_INFO I, ITEM_TREE T
WHERE I.ITEM_ID = T.ITEM_ID
    AND PARENT_ITEM_ID IS NULL
ORDER BY ITEM_ID