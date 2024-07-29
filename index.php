<?php
     include('inc/core.php');   
    $title = 'Home';
?>

<?php include('inc/header.php'); ?>
<h1>Feeds</h1>
<p>
    [<a href="add.php?key=<?php echo $key; ?>">Add feed</a>]
</p>
<ol start='0'>
    <?php
        $fp = fopen('data.txt', 'r');
        $lines = array();
        while (($ln = fgets($fp)) !== false) {
            $ex = explode('|',trim($ln));
            if($ex[0] == 'U') {
                echo '<li>[<a href="read.php?key='.$key.'&id='.$ex[1].'">mark read</a>] <a href="articles/' . $ex[1] . '.html">'.$ex[2].'</a></li>';
            }
        }
        fclose($fp);  
    ?>
</ol>
<?php include('inc/footer.php'); ?>
