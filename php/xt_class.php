<?php
//基本
class SimpleClass
{
    // property declaration
    public $var = 'a default value';

    // method declaration
    public function displayVar() {
        echo $this->var;
    }
}
$a=new SimPleClass();
$a->displayVar();

echo SimpleClass::class;
?>

