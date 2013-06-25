<html>
<head>
<title>Airbnb assistant</title>
</head>
<body>
<?php
//the example of searching data with the sequence based on the field name
//search.php
$dbhandle=mysql_connect("localhost","istavrak","password");//database connection
$selected=mysql_select_db("airbnb_alerts",$dbhandle);
				
$order = "select image_uri,room_price,status,room_URI from entries order by status DESC;";
//order to search data
//declare in the order variable
				
$result = mysql_query($order);
?>
<table>
  <tr>
<?php
$num=mysql_numrows($result);
echo("<td align='center'>$num Airbnb rooms</td>");
?>	

  </tr>
  <tr>
    <td>
      <table border="0">
      <tr>
	<td>Image</td>	        
        <td>Price (Euro)</td>
        <td>Status</td>
        <td>Airbnb link</td>
      </tr>
<?php				
while($data = mysql_fetch_row($result)){
  echo("<tr><td><img src='$data[0]'/></td><td style='text-align:center;font-size:1.1em'>$data[1]</td><td>$data[2]</td><td><a href='$data[3]'>$data[3]</a></td></tr>");
}

//close the connection
mysql_close($dbhandle);
?>
    </table>
  </td>
</tr>
</table>
</body>
</html>
