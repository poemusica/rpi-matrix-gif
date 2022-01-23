# Animated GIFs on Adafruit RGB LED Matrix with Raspberry Pi

This tutorial explains how to display an animated gif on an Adafruit RGB LED Matrix panel using a Raspberry Pi microcontroller. 

I used my matrix to display a spooky ghost gif for Halloween. :jack_o_lantern:

---
<a href="https://twitter.com/heatheramahan/status/789191493088980992"><img align="left" height="150" src="https://i.giphy.com/media/rZL5cIy8irYM2JCL75/giphy-downsized-large.gif"></a>

<p>
<a href="https://twitter.com/heatheramahan"><img src="https://pbs.twimg.com/profile_images/840044211680366593/p1P6s56l_400x400.jpg" height="48" width="48"></a>
<a href="https://twitter.com/heatheramahan">@heatheramahan</a> via Twitter
<a href="https://twitter.com/heatheramahan/status/789191493088980992">October 20, 2016</a>
</p>

<p>
Happy Halloween! 👻 Spooky little collab by <a href="https://twitter.com/jettisonjoe">@jettisonjoe</a> (pixel art) & <a href="https://twitter.com/heatheramahan">me</a> (pi hacking).
</p>

<p>
<a href="https://twitter.com/adafruit">@adafruit</a>
<a href="https://twitter.com/hashtag/RaspberryPi">#RaspberryPi</a>
</p>

---

## HARDWARE

### Matrix
* [32x32 RGB LED Matrix Panel - 5mm Pitch](https://www.adafruit.com/products/2026)

  <a href="https://www.adafruit.com/products/2026"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2026-05.jpg"></a>
  
  Displays your animated gif / graphics on a grid of 1024 RGB LEDs!
  

### Microcontroller
* [Raspberry Pi Model B+ 512MB RAM](https://www.adafruit.com/products/1914)
  
  <a href="https://www.adafruit.com/products/1914"><img height="150" src="https://cdn-shop.adafruit.com/970x728/1914-01.jpg"></a>

  The brains of the operation. I used Model B+, but models A+, Pi 2 and Pi 3 are also fine for this project.

* [Adafruit RGB Matrix HAT + RTC for Raspberry Pi - Mini Kit](https://www.adafruit.com/product/2345)
  
  <a href="https://www.adafruit.com/product/2345"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2345-08.jpg"></a>

  Plugs into your Raspberry Pi and allows you to control the RBG LED Matrix panel. 
  
* [8GB Class 10 SD/MicroSD Memory Card - SD Adapter Included](https://www.adafruit.com/products/2692)

  <a href="https://www.adafruit.com/products/2692"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2692-01.jpg"></a>
  
  Storage for your Raspberry Pi OS and your projects.

* ~~<s> (Optional) [Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi and more](https://www.adafruit.com/product/814) </s>~~
  
  This product is now discontinued. See the item below for alternatives.
  
* (Optional) [Mini USB WiFi Module - RTL8188eu - 802.11b/g/n](https://www.adafruit.com/product/2810)
  
  <a href="https://www.adafruit.com/product/2810"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2810-10.jpg"></a>
  
  Connects your Raspberry Pi to the internet via wifi.
  * If you are using a Raspberry Pi that includes built-in wifi (ex: Raspberry Pi 3), you do need to purchase a wifi module.
  * Alternatively, you can use an Ethernet cable for a wired network connection. 


### Power
* [5V 4A (4000mA) switching power supply - UL Listed](https://www.adafruit.com/product/1466)
  
  <a href="https://www.adafruit.com/product/1466"><img height="150" src="https://cdn-shop.adafruit.com/970x728/1466-02.jpg"></a>
  
  Powers the RGB Matrix HAT.

* [Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/products/368)
  
  <a href="https://www.adafruit.com/products/368"><img height="150" src="https://cdn-shop.adafruit.com/970x728/368-03.jpg"></a>

  Connects the HAT to the power supply.

### Tools
* USB SD card reader
* Soldering iron and solder
* Wire cutters

### Other
* Micro USB cable
  
  Powers the Raspberry Pi using your regular computer’s USB port or a USB wall charger.

* USB mouse and keyboard 
* HDMI display and cable


You’ll need these last two items to interface with your Raspberry Pi the first time you log in. Later, you can set up SSH to access your Raspberry Pi remotely.

---

## SOFTWARE
* [Aesprite](https://www.aseprite.org/)
  
  Animated sprite editor & pixel art tool. (Or some other program for creating 32x32 animated gif.)

* Nano
  
  A simple command line editor that omes pre-installed on Raspberry Pi OS. (Or some other code editor, such as VS Code.)

---

## INSTRUCTIONS

### Prepare your Raspberry Pi

<ol>
  <li>
    Follow Adafruit’s instructions for getting Raspberry Pi OS running on your Raspberry Pi.
    I used the <a href="https://www.raspberrypi.com/software/">Raspberry Pi Imager</a> to install Raspberry Pi OS on a microSD card. 
    Insert the prepared microSD card into the Raspberry Pi and boot it up!
  </li>
  <li>
		<a href="https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/overview">Connect your Raspberry Pi to the Internet.</a>
  </li>
	<li>
		(Optional) <a href="https://www.raspberrypi.org/documentation/remote-access/ssh/">Set Up SSH for Remote Connection</a>.
		With an SSH connection, you can log in to your Raspberry Pi remotely (from your regular computer). You’ll no longer need the HDMI monitor and USB mouse/keyboard connected to your Raspberry Pi.
	</li>
	<li>
		(Optional) Set Up Remote Code Editing with your preferred code editor, for example <a href="https://github.com/poemusica/rpi-matrix-gif/blob/master/UsingRsub.md">Sublime Text</a>.
		Alternatively, you can ignore this step altogether and just use Nano to write and edit code. Nano is a simple command line text editor that comes preinstalled on Raspberry Pi OS.
  </li>
</ol>    

### Assemble the HAT

Follow Adafruit's [great tutorial](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly)
on how to solder the components of the RGB Matrix HAT.

Don’t be intimidated! This project was my first time soldering. I was able to do it, and you can do it too.

If you’re new to soldering, see also Adafruit’s [Guide to Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering).
  
 ---
<a href="https://twitter.com/heatheramahan/status/782779412462743552"><img align="left" height="150" src="https://pbs.twimg.com/media/Ctz9ssYUkAAT1fu.jpg"></a>

<p>
<a href="https://twitter.com/heatheramahan"><img src="https://pbs.twimg.com/profile_images/840044211680366593/p1P6s56l_400x400.jpg" height="48" width="48"></a>
<a href="https://twitter.com/heatheramahan">@heatheramahan</a> via Twitter
<a href="https://twitter.com/heatheramahan/status/782779412462743552">October 3, 2016</a>
</p>

<p>
Solder? I hardly know her!
<a href="https://twitter.com/hashtag/myfirst">#myfirst</a>
<a href="https://twitter.com/hashtag/soldering">#soldering</a>
</p>
<p>
<a href="https://twitter.com/adafruit">@adafruit</a>
<a href="https://twitter.com/hashtag/RaspberryPi">#RaspberryPi</a>
</p>

---

### Activate the Matrix

Follow Adafruit’s [instructions](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices)
for connecting the hardware, installing PIL (Python Image Library), and downloading/running their demo code.
    
When you have the Adafruit demos working, you’re ready to start creating designs of your own!

## Display Pixel Art Animations


  1. Make a 32x32 pixel art animation using [Aesprite](https://www.aseprite.org/) (or some other software) and export it as a .gif.
    You’ll probably want to do this step on your regular computer.
    

  2. Copy your animated gif onto your Raspberry Pi.
     On your regular computer, open a new terminal and type:
    `scp <source> pi@<pi_ip>:<destination>`
    where `<source>` is the path to the file you want to copy, `<pi_ip>` is your Raspberry Pi’s IP address, and `<destination>` the path to this project directory on your Raspberry Pi.
    

  3. Run the displayGIF script to display your animation.
     On the Raspberry Pi or in your SSH terminal, type:
    `python displayGIF.py`
    By default, the script displays the included sample gif created by [@jettisonjoe](https://twitter.com/jettisonjoe). (Thanks Joe!) ![Ghost](https://github.com/poemusica/rpi-matrix-gif/blob/master/myGIF.gif)
    To display your own gif, simply replace `myGIF` in the code with the name of your gif.
    Use `Ctrl-C` in the command line to stop the script.
    

### (Optional) Run on boot

If you want the `displayGIF.py` script to run automatically whenever you start up the Raspberry Pi,
follow [these instructions](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)
to edit the `rc.local` file on your Raspberry Pi.
