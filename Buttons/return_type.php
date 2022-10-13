class QRimage {  
  
  
    //----------------------------------------------------------------------  
    public static function png($frame, $filename = false, $pixelPerPoint = 4, $outerFrame = 4,$save = TRUE, $print = false)   
    {  
        $image = self::image($frame, $pixelPerPoint, $outerFrame, "png", 85, $filename, $save, $print);  
    }  
  
    //----------------------------------------------------------------------  
    public static function jpg($frame, $filename = false, $pixelPerPoint = 8, $outerFrame = 4, $q = 85,$save = TRUE, $print = false)   
    {  
        $image = self::image($frame, $pixelPerPoint, $outerFrame, "jpeg", $q, $filename, $save, $print);  
    }  
  
    //----------------------------------------------------------------------  
    private static function image($frame, $pixelPerPoint = 4, $outerFrame = 4, $format = "png", $quality = 85, $filename = FALSE, $save = TRUE, $print = false)   
    {  
        $imgH = count($frame);  
        $imgW = strlen($frame[0]);  
  
        $col[0] = new \ImagickPixel("white");  
        $col[1] = new \ImagickPixel("black");  
  
        $image = new \Imagick();  
        $image->newImage($imgW, $imgH, $col[0]);  
  
        $image->setCompressionQuality($quality);  
        $image->setImageFormat($format);   
  
        $draw = new \ImagickDraw();  
        $draw->setFillColor($col[1]);  
  
        for($y=0; $y<$imgH; $y++) {  
            for($x=0; $x<$imgW; $x++) {  
                if ($frame[$y][$x] == '1') {  
                    $draw->point($x,$y);   
                }  
            }  
        }  
  
        $image->drawImage($draw);  
        $image->borderImage($col[0],$outerFrame,$outerFrame);  
        $image->scaleImage( ($imgW + 2*$outerFrame) * $pixelPerPoint, 0 );  
  
        if($save){  
            if($filename === false){  
                throw new Exception("QR Code filename can't be empty");  
            }  
            $image->writeImages($filename, true);   
        }  
  
        if($print){  
                Header("Content-type: image/" . $format);  
                echo $image;  
        }  
    }      
}
