<?php
class MyDB extends SQLite3
{
    function __construct()
    {
        $this->open('shipDatabase.db');
    }
}

$db = new MyDB();
if(!$db)
{
    echo $db->lastErrorMsg();
}

$results = $db->query('SELECT id FROM coords')->fetchArray();
echo $results['id'];
?>    