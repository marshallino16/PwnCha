<?php
session_start();
?>
<html>
<head>
<title>SignUp</title>
<link rel="stylesheet" type="text/css" href="style.css" />
<script type="text/javascript" src="js/jquery-1.6.min.js"></script>
<script type="text/javascript" src="js/captcha.js"></script>

</head>
    <body>
	<div class="status">
	<?php
    if(isset($_POST['captcha'])){
		if(($_POST['captcha']!="") || ($_SESSION['captcha_id'])!=""){
    if($_POST['captcha']==$_SESSION['captcha_id']) {
		 	echo '<font color="green"><b>Successful!........</b></font>';

		} else if($_POST['captcha']!=""){

			echo '<font color="red"><b>Not Matching, Try Again...</b></font>';
		}
	 }
 }
  ?>
	</div>
	<?php
		// Include the random string file for captcha
		require 'includes/rand.php';
		$randomObj = new RandomGen();
		$str = $randomObj->createRandom();

		// Set the session contents
		$_SESSION['captcha_id'] = $str;
	?>

	<form  name="signup" id="signupform" method="post">


		<table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin-bottom:13px;">
		<tr>
    			<td><div id="captchaimage"><a href="" id="refreshimg"  title="Another image"><img src="captcha/image.php?<?php echo time(); ?>" alt="Captcha image" width="132" height="46" align="left" /></a></div><p class="signUpText">[Click on image to refresh]</p></td>
    			<td></td>
  		</tr>
		</table>

		<p class="signUpText">Enter the above: <input type="text" maxlength="6" name="captcha" id="captcha" autocomplete=off  /></p><div class="status"></div>
		<p class="signUpText" style='padding-left:120px;' >
			<input class="submit" type="submit" value="Submit"><span align=center valign=top style="font-size: 10px;color: #dadada;" id="dumdiv">
</span>
</div>

		</p>
	</form>

        <br><br><br>

</body>
</html>
