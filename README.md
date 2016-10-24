# Animated GIFs on Adafruit RGB LED Matrix with Raspberry Pi

This tutorial explains how to display an animated gif on an Adafruit RGB LED Matrix panel using a Raspberry Pi microcontroller. 

I used my matrix to display a spooky ghost gif for Halloween. :jack_o_lantern:

The video in the following tweet shows the final result:
<blockquote class="twitter-video" data-lang="en"><p lang="en" dir="ltr">Happy Halloween! 👻 Spooky little collab by <a href="https://twitter.com/jettisonjoe">@jettisonjoe</a> (pixel art) &amp; me (pi hacking).<a href="https://twitter.com/adafruit">@adafruit</a> <a href="https://twitter.com/hashtag/RaspberryPi?src=hash">#RaspberryPi</a> <a href="https://t.co/tVHUMfZBu1">pic.twitter.com/tVHUMfZBu1</a></p>&mdash; Heather Alexis (@heatheramahan) <a href="https://twitter.com/heatheramahan/status/789191493088980992">October 20, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Have fun and feel free to post questions/suggestions.

## HARDWARE

### Matrix
* 32x32 RGB LED Matrix Panel - 5mm Pitch  $44.95

  https://www.adafruit.com/products/2026

### Microcontroller
* Raspberry Pi Model B+ 512MB RAM $29.95
  
  https://www.adafruit.com/products/1914
  
  (This is the one I used, but models A+, B+, Pi 2 and Pi 3 are all fine for this project.)

* Adafruit RGB Matrix HAT + RTC for Raspberry Pi - Mini Kit $24.95
  
  https://www.adafruit.com/product/2345 

* 8GB Class 10 SD/MicroSD Memory Card - SD Adapter Included $9.95
  
  https://www.adafruit.com/products/2692
  
  (Storage for your Raspberry Pi OS and your projects)

* Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more $11.95
  
  https://www.adafruit.com/products/814
  
  (Not needed for Raspberry Pi 3, which has wifi built in.
  Alternatively, you can use an Ethernet cable for a wired network connection.)

### Power
* 5V 4A (4000mA) switching power supply - UL Listed $14.95
  
  https://www.adafruit.com/product/1466 
  
  (Powers the RGB Matrix HAT)

* Female DC Power adapter - 2.1mm jack to screw terminal block $2.00
  
  https://www.adafruit.com/products/368
  
  (Connects the HAT to the power supply.)

### Tools
* USB SD card reader
* Soldering iron and solder
* Wire cutters

### Other
* Micro USB cable
  
  (Powers the Raspberry Pi using your regular computer’s USB port or a USB wall charger.)
  
* USB mouse and keyboard 
* HDMI display and cable

  (You’ll need these last two items to interface with your Raspberry Pi the first time you log in. Later, you can set up SSH to access your Raspberry Pi remotely.)

## SOFTWARE
* Aesprite: animated sprite editor & pixel art tool $14.99

  https://www.aseprite.org/
  
  (Or some other program for creating 32x32 animated gif.)

* Nano, a simple command line editor

  (Comes pre-installed on Raspbian OS)
  
  http://www.tutorialspoint.com/articles/how-to-use-nano-text-editor
  
  (Or some other code editor, such as Sublime Text.)

## INSTRUCTIONS

1. **Prepare your Raspberry Pi**


  1. Follow Adafruit’s instructions for getting Raspbian OS running on your Raspberry Pi.
  
    https://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi
    

  2. Connect your Raspberry Pi to the Internet.
    
    https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/overview 
    
    
  3. Set Up SSH for Remote Connection. (Optional)
  
    With an SSH connection, you can log in to your Raspberry Pi remotely (from your regular computer). You’ll no longer need the HDMI monitor and USB mouse/keyboard connected to your Raspberry Pi.
  
    https://www.raspberrypi.org/documentation/remote-access/ssh/
    

  4. Set Up Remote Code Editing with Sublime Text. (Optional)
  		
	https://github.com/poemusica/rpi-matrix-gif/blob/master/UsingRsub.md
	
	Alternatively, you can ignore this step altogether and just use Nano to write and edit code. Nano is a simple command line text editor that comes preinstalled on Raspbian OS.
    
    http://www.tutorialspoint.com/articles/how-to-use-nano-text-editor
    

2. **Assemble the HAT**

  Don’t be intimidated! This project was my first time soldering. I was able to do it, and you can do it too. :smile:
  
  ![Me soldering](https://pbs.twimg.com/media/Ctz9ssYUkAAT1fu.jpg:thumb)
  ![Me soldering] (https://pbs.twimg.com/media/Ctz9t4qUIAAE99Y.jpg:thumb)
  
  <blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Solder? I hardly know her! <a href="https://twitter.com/hashtag/myfirst?src=hash">#myfirst</a> <a href="https://twitter.com/hashtag/soldering?src=hash">#soldering</a> <a href="https://twitter.com/hashtag/RaspberryPi?src=hash">#RaspberryPi</a>  <a href="https://twitter.com/adafruit">@adafruit</a> <a href="https://t.co/SXCtChieCN">pic.twitter.com/SXCtChieCN</a></p>&mdash; Heather Alexis (@heatheramahan) <a href="https://twitter.com/heatheramahan/status/782779412462743552">October 3, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

  Adafruit has a great tutorial about how to solder the components of the RGB Matrix HAT:
  
  https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly

  If you’re new to soldering, see also Adafruit’s Guide to Excellent Soldering:
  
  https://learn.adafruit.com/adafruit-guide-excellent-soldering
  

3. **Activate the Matrix**
  
  Follow Adafruit’s instructions for connecting the hardware, installing PIL (Python Image Library), and downloading/running their demo code.
  
  https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices
  
  When you have the Adafruit demos working, you’re ready to start creating designs of your own!


4. **Display Pixel Art Animations**


  1. Make a 32x32 pixel art animation using Aesprite (or some other software) and export it as a .gif.
  
    https://www.aseprite.org/

    You’ll probably want to do this step on your regular computer.
    

  2. Copy your animated gif onto your Raspberry Pi.
  
    On your regular computer, open a new terminal and type:
	
    `scp <source> pi@<pi_ip>:<destination>`

    where `<source>` is the path to the file you want to copy, `<pi_ip>` is your Raspberry Pi’s IP address, and `<destination>` the path to this project directory on your Raspberry Pi.
    

  3. Run the displayGIF script to display your animation.
     
     On the Raspberry Pi or in your SSH terminal, type:

    `python displayGIF.py`
  
    By default, the script displays the included sample gif created by @jettisonjoe. (Thanks Joe!) ![Ghost] (https://github.com/poemusica/rpi-matrix-gif/blob/master/myGIF.gif)
  
    To display your own gif, simply replace `myGIF` in the code with the name of your gif.

    Use `Ctrl-C` in the command line to stop the script.
    

5. **Run on boot (Optional)**

  If you want the displayGIF script to run automatically whenever you start up the Raspberry Pi, follow these instructions to edit the `rc.local` file on your Raspberry Pi:
  
  https://www.raspberrypi.org/documentation/linux/usage/rc-local.md
