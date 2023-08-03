<?php
    include('inc/core.php');

    if($_GET['id'] != null) {
        $id = $_GET['id'];
        $fp = fopen('data.txt', 'r');
        $lines = array();
        if($id != null) {
            while (($ln = fgets($fp)) !== false) {
                $ex = explode('|',trim($ln));
                $i = $ex[1];
                if($i == $id) {
                    $ln[0] = 'R';
                }
                $lines[] = trim($ln);
            }
            fclose($fp);  
            file_put_contents('data.txt',implode("\n",$lines));
        }
    }
    home();
?>
