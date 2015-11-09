<?php

$arr=['xt','bob','kevin','michel'];
$s='';
foreach ($arr as $my_var)
{
    $s=' '.$my_var.$s;
}
echo "$s";
