<?php
class RandomGen {
	function createRandom() {
		$char = strtoupper(substr(str_shuffle('abcdefghjkmnpqrstuvwxyz'), 0, 4));	
		$str = rand(1, 7) . rand(1, 7) . $char;
		return $str;
	}
}

?>
