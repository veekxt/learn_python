<?php
$myarr = array('foo'=>'bar','bar'=>'foo');
$myarr2 = ['foo'=>'bar2','bar'=>'foo2','2'=>'1','last'];
var_dump($myarr2);

var_dump($myarr2[3]);

$array = array(
    "foo" => "bar",
    42    => 24,
    "multi" => array(
         "dimensional" => array(
             "array" => "foo"
         )
    )
);
var_dump($array["multi"]["dimensional"]["array"]);
