<?php
    $test = shell_exec("python3 scrape.py");
    echo json_encode($test);
    // $test itself is a json String you even dont need encode/decode
?>
