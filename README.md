### Useful Stuff I always forget by the time I need it.

#### Using virtualenv for python

1. Install virtualenv ```easy_install virtualenv``` if you do not have it yet (as long as you want to test this locally. Otherwise, go to step 4)
2. Create a new virtualenv inside the downloaded folder with ```virtualenv venv```, open it with ```. venv/bin/activate```
3. Install flask with ```pip install flask```
4. Start the testserver with ```python sprinkler.py```
5. Go to 127.0.0.1:5000


#### Creating Screencasts & .gifs


1. Video aufnehmen (Quicktime.app / Screenflow.app)
2. Für beste Ergebnisse Video aus .avi oder .mov abspeichern
3. ???
4. PROFIT

Liegt das Video vor, kann man es mithilfe von `ffmpeg` zu einem .gif konvertieren. Da der Output für gewöhnlich recht groß ausfällt, kann man das .gif noch mittels `gifsicle` komprimieren.

	$ ffmpeg -i video.avi -s 800x600 -pix_fmt rgb24 -r 10 -f gif output.gif
	$ gifsicle --optimize=3 --delay=10 -i < output.gif > output.gif

Für mehr Qualität, erstmal alle einzel-gifs generieren lassen und dann mit `gifsicle` zu einem output.gif zusammenfügen.
	
	$ ffmpeg -i video.avi -t 10 out%02d.gif
	$ gifsicle --delay=10 --loop *.gif > output.gif
	
Alternativ, die Variante mit convert. Hierfür benötigt man `imageMagick`.
	
	$ ffmpeg -i video.avi -vf scale=320:-1 -r 10 ffout%03d.png
	$ convert -delay 5 -loop 0 frames/ffout*.png output.gif
	
Wenn du immernoch nicht zufrieden bist, versuch das. Wir wandeln somit das Video erst in .png files um, die wir später wieder mit `convert` in ein .gif umwandeln. Smooth!

	$ mkdir gif
	$ ffmpeg -i YOUR_MOVIE.mpg -an -r 10 -y -s 640x480 gif/capture%03d.png
	$ cd gif
	$ for file in *png; do echo converting $file ...; convert $file `basename $file .png`.gif; done
	$ convert -delay 10 cap*gif -loop 0 anim.gif
	$ convert -layers Optimize anim.gif anim_optimized.gif

