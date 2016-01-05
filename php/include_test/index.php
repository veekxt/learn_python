<?php
namespace my;
include 'bein1.php';
include 'bein2.php';
use h\i\j as myj;
echo 'I Am Index',"\n";
echo $a,"\n";
echo \h\i\j\add2(6,7),"  //this is 6+7","\n";
function var_dump($a){
echo '\var_dump has be killed';
}
echo myj\add2(8,1);
?>
