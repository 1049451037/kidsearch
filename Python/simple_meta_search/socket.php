<?php
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    $con=socket_connect($socket,'127.0.0.1',9999);
    if(!$con){socket_close($socket);exit;}
    $words=$_GET["search"];
    socket_write($socket,$words);
    $hear=socket_read($socket,1024000);
    echo $hear;
    socket_shutdown($socket);
    socket_close($socket);
?>
