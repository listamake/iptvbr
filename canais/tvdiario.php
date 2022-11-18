<?php
$videoid="x7txn7q";//a static dailymotion video id
$path_log_link='logs/';
$path_download_file='https://github.com/Emanueldelima/iptvmakebr/tree/main/canais/';
$link="";
$page=file_get_contents('http://www.dailymotion.com/embed/video/'.$videoid);
$link = substr($page, strlen('mp4","url":"')+strripos($page, 'mp4","url":"'));  // beginning of link
$link = substr($link, 0, strpos($link, '"}'));  // end of link
$link = str_replace("\\", '', $link);   // delete backslashes\
$path = $path_download_file.$videoid.".m3u";

if ((!file_exists($path)) && (!empty($link))){
  file_put_contents($path_log_link.$videoid.'.txt', $link); // save link in log
  $cmd='wget -bqc '.$link.' -O "'.$path_download_file.$videoid.'.m3u"';
  exec($cmd,$o,$r);
}
?>
