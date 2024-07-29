<?php
    include('inc/core.php');

    $title = 'Add feed';

    if($_GET['url']) {
        $url = $_GET['url'];
        $fp = fopen('feeds.txt', 'a');
        fwrite($fp, "\n" . $url);
        fclose($fp);  
        home();
    }
?>

<?php include('inc/header.php'); ?>
        <h1>Add feed</h1>
        <form method="GET">
            <input type="text" name="url" placeholder="URL" /><br>
            <?php echo getKeyInput(); ?>
            <input type="submit" value="Add" />
        </form>
<?php include('inc/footer.php'); ?>

