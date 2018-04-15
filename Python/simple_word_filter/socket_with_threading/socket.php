<?php
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
    $con=socket_connect($socket,'127.0.0.1',9999);
    if(!$con){socket_close($socket);exit;}
    $words="北京你是谁";
    socket_write($socket,$words);
    $hear=socket_read($socket,1024);
    echo $hear;
    socket_shutdown($socket);
    socket_close($socket);
?>