# Display Animated GIFs on 32x32 RGB LED Matrix with Raspberry Pi

This README describes the process of using a **Raspberry Pi** microcontroller along with my `displayGIF.py` script to display an **animated gif** on a **32x32 RGB LED Matrix**.

For example, I used my matrix to display a spooky ghost gif for Halloween. 🎃

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

| [32x32 RGB LED Matrix Panel](https://www.adafruit.com/products/2026) | Raspberry Pi[^rpi] | [Adafruit RGB Matrix HAT + RTC for Raspberry Pi - Mini Kit](https://www.adafruit.com/product/2345) |
| :---: | :---: | :---: |
| <a href="https://www.adafruit.com/products/2026"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2026-05.jpg"></a> | <a href="https://www.adafruit.com/product/3055"><img height="150" src="https://cdn-shop.adafruit.com/970x728/3055-08.jpg"></a> | <a href="https://www.adafruit.com/product/2345"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2345-08.jpg"></a> |
| Displays graphics on a grid of 1024 dazzling RGB LEDs! | The brains of the operation.  Raspberry Pi Model Zero/A+/B+/Pi 2/3/ or Pi 4 are all compatible. | Plugs into your Raspberry Pi and allows you to control the RBG LED Matrix panel. (Soldering required!) |


[^rpi]:
    Originally I used a [Raspberry Pi Model B+](https://www.adafruit.com/products/1914) (and Raspbian OS) for this project back in 2016. In 2022, I revisited the project using a [Raspberry Pi 3 - Model B](https://www.adafruit.com/product/3055) (and Raspberry Pi OS). 

| [MicroSD Memory Card](https://www.adafruit.com/products/2692) | (Optional) [Mini USB WiFi Module](https://www.adafruit.com/product/2810)[^wifi]| [5V 4A power supply](https://www.adafruit.com/product/1466) |
| :---: | :---: | :---: |
| <a href="https://www.adafruit.com/products/2692"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2692-01.jpg"></a>| <a href="https://www.adafruit.com/product/2810"><img height="150" src="https://cdn-shop.adafruit.com/970x728/2810-10.jpg"></a> | <a href="https://www.adafruit.com/product/1466"><img height="150" src="https://cdn-shop.adafruit.com/970x728/1466-02.jpg"></a> | <a href="https://www.adafruit.com/products/368"><img height="150" src="https://cdn-shop.adafruit.com/970x728/368-03.jpg"></a> |
| Storage for Raspberry Pi OS and your projects. | Connects your Raspberry Pi to the internet via wifi. | Powers the RGB LED Matrix. |
  
[^wifi]:
    If you are using a Raspberry Pi that includes built-in wifi (ex: Raspberry Pi 3), you do need to purchase a wifi module. Alternatively, you can use an Ethernet cable for a wired network connection. Originally, I used the [Miniature WiFi (802.11b/g/n) Module](https://www.adafruit.com/product/814) but this product is now discontinued. The product linked in the table is a recommended alternative. 

| [USB MicroSD Card Reader/Writer](https://www.adafruit.com/product/939) | [USB A to Micro-B cable](https://www.adafruit.com/product/592)[^usb] | USB keyboard, HDMI display & cable | Soldering Supplies |
| :---: | :---: | :---: | :---: |
| <a href="https://www.adafruit.com/product/939"><img height="150" src="https://cdn-shop.adafruit.com/970x728/939-06.jpg"></a> | <a href="https://www.adafruit.com/product/592"><img height="150" src="https://cdn-shop.adafruit.com/970x728/592-01.jpg"></a> | ![](https://staging-assets.raspberrypi.com/static/hero__container-bg-89d1baabda817d708f2a5fb82ece2c6c.svg)| <a href="https://learn.adafruit.com/adafruit-guide-excellent-soldering"><img height="150" src="https://cdn-learn.adafruit.com/guides/cropped_images/000/000/102/medium640/Solder_Badge.png"></a> |
| Required for installing Rasberry Pi OS. | Powers the Raspberry Pi using your regular computer’s USB port or a USB wall charger. | You’ll need these items to interface with your Raspberry Pi the first time you log in. Later, you can set up SSH to access your Raspberry Pi remotely. | Soldering iron, solder, and wire cutters are required to assemble the [Adafruit RGB Matrix HAT](https://www.adafruit.com/product/2345). |

[^usb]:
    Alternatively, you can use a [USB C to Micro B Cable](https://www.adafruit.com/product/3878), depending on your preference / available USB ports.

---

## SOFTWARE

| [Raspberry PI OS](https://www.raspberrypi.com/software/) | [Aseprite](https://www.aseprite.org/) | [Nano](https://www.nano-editor.org/) |
| :---: | :---: | :---: |
| <a href="https://www.raspberrypi.com/software/"><img height="150" src="https://upload.wikimedia.org/wikipedia/commons/d/d1/Raspberry_Pi_OS_Logo.png"></a> | <a href="https://www.aseprite.org"><img height="150" src="https://www.aseprite.org/assets/images/header-logo.png"></a> | <a href="https://www.nano-editor.org/"><img height="150" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Gnu-nano.svg/1200px-Gnu-nano.svg.png"></a> |
| The official OS for Raspberry Pi microcontrollers. | Animated sprite editor & pixel art tool. (Or some other program for creating 32x32 animated gif.) | Command line text editor that comes pre-installed on Raspberry Pi OS. (Or some other code editor, such as [Sublime Text](https://www.sublimetext.com/) or [VS Code](https://code.visualstudio.com/).) |

---

## INSTRUCTIONS

### Step 1: Prepare your Raspberry Pi

<ol>
  <li>
    Install <a href="https://www.raspberrypi.com/software/">Raspberry Pi OS</a>.
		<ol>
			<li>Insert your <a href="https://www.adafruit.com/products/2692">MicroSD Memory Card</a> into your <a href="https://www.adafruit.com/product/939">USB MicroSD Card Reader/Writer</a> and attach it to your regular computer.</li>
			<li>Recommended: Use the official <a href="https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager">Raspberry Pi Imager</a> to install Raspberry Pi OS Lite.</li>
		</ol>
    <a href="https://www.raspberrypi.com/software/">
			<img src="https://assets.raspberrypi.com/static/md-bfd602be71b2c1099b91877aed3b41f0.png" height="250">
		</a>
  </li>
	<li>
    Connect accessories and power up.
		<ol>
			<li>Insert the prepared MicroSD card into your Raspberry Pi.</li>
			<li>Connect <strong>your keyboard</strong> and <strong>HDMI display</strong> to your Raspberry Pi.</li>
			<li>If needed, attach your <a href="https://www.adafruit.com/product/2810">Mini USB WiFi Module</a>. Or, if you're using a wired connection, attach your ethernet cable.</li>
			<li>Apply power using your <a href="https://www.adafruit.com/product/592">USB A to Micro-B cable</a> and a USB power source.</li>
		</ol>
  </li>
	<li>
    Log in to your Raspberry Pi.
		<p>The default credentials are <strong>pi</strong> (user name) and <strong>raspberry</strong> (password).</p>
	</li>
	<li><a href="https://www.raspberrypi.com/documentation/computers/configuration.html#wireless-networking-command-line">Connect your Raspberry Pi to Wifi.</a>
		<p>(Ignore this step if you're using a wired network connection.)</p>
		<p>The crucial steps are summarized below. Please reference the <a href="https://www.raspberrypi.com/documentation/computers/configuration.html#wireless-networking-command-line">documentation</a> for more details and troubleshooting.</p>
		<ol>
			<li>Configure the <strong>wireless country</strong> in the <strong>Localization</strong> options using the <code>raspi-config</code> command line tool.</li>
			<li>Edit the <code>wpa-supplicant.conf</code> file to include your wireless network ID and password.</li>
			<li>Reconfigure the interface with <code>wpa_cli -i wlan0 reconfigure</code>.</li>
		</ol>
  </li>
  <li>
    (Optional) <a href="https://www.raspberrypi.org/documentation/remote-access/ssh/">Set Up SSH for Remote Connection</a>.
		<p>With an SSH connection, you can log in to your Raspberry Pi remotely (from your regular computer). You’ll no longer need the HDMI display and USB keyboard to access your Raspberry Pi.</p>
		<p>The crucial steps are summarized below. Please reference the <a href="https://www.raspberrypi.org/documentation/remote-access/ssh/">documentation</a> for more details and troubleshooting.</p>
		<p>On your Raspberry Pi:</p>
		<ol>
			<li>Enable SSH using the <code>raspi-config</code> command line tool.</li>
			<li>Run the <code>hostname -I</code> command and note your Raspberry Pi's IP address.</li>
		</ol>
		<p>On your regular computer:</p>
		<ol>
			<li><a href="https://www.raspberrypi.com/documentation/computers/remote-access.html#secure-shell-from-linux-or-mac-os">Connect to your Raspberry Pi via SSH</a> using the command <code>ssh pi@&lt;IP&gt;</code> in the terminal.</li>
			<p>Replace <code>&lt;IP&gt;</code> with your Raspberry Pi's IP address.</p>
		</ol>
		
  </li>
  <li>
    (Optional) Set Up Remote Code Editing with your preferred code editor, for example <a href="https://github.com/poemusica/rpi-matrix-gif/blob/master/UsingRsub.md">Sublime Text</a>.
		<p>Alternatively, you can ignore this step and use <a href="https://www.nano-editor.org/">Nano</a> to write and edit code via the command line.</p>
  </li>
</ol>   

**Tip**: You can gracefully power off your Raspberry Pi via the command line with the command `sudo shutdown -h now`.

### Step 2: Assemble the HAT

Follow Adafruit's amazing [Assembly](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly) instructions describing how to solder the (included) components of the [Adafruit RGB Matrix HAT](https://www.adafruit.com/product/2345):
* 2x20 pin socket header
* 2 pin terminal block
* 2x8 pin IDC header

You'll need **soldering supplies** (soldering iron, solder, wire cutters) for this step. If you’re new to soldering, see also Adafruit’s [Guide to Excellent Soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering).

Don’t be intimidated! This project was my first time soldering. I was able to do it and you can do it too.
  
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

### Step 3: Activate the Matrix!

Follow Adafruit’s [Driving Matrices](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices) instructions.

The first five steps explain how to connect the HAT to the Rasberry Pi and Matrix using the included cables and wires:
* The 2x20 pin socket header on the HAT attaches to the GPIO header on the Raspberry Pi.
* The red and black cables supply power from the HAT to the Matrix. The end with a 4-pin MOLEX connector attaches to the Matrix. The other end attaches to the terminal block on the HAT.
* The 2x8 ribbon cable provides the data connection between Matrix and the HAT.
* The [5V 4A power supply](https://www.adafruit.com/product/1466) (sold separately) connects to the HAT and supplies power to the Matrix (via the red and black cables).

The last step describes how to download and install a version of the [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library[^lib] by [Henner Zeller](https://github.com/hzeller) ([GNU General Public License Version 2.0](http://www.gnu.org/licenses/gpl-2.0.txt)):

The `curl` command downloads the installer script [`rgb-matrix.sh`](https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/blob/main/rgb-matrix.sh) and the `bash` command runs it.
```bash
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh >rgb-matrix.sh
sudo bash rgb-matrix.sh
```

After the installation is complete, [try out the demos](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices#testing-the-examples-2982010-30) included in the library to test that the Matrix is working.


[^lib]:
    An earlier (2016) version of this project used Adafruit's now [deprecated fork](https://github.com/adafruit/rpi-rgb-led-matrix) of the [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library.

### Step 4: Display the GIF

You're finally ready to display an animated gif on your Matrix.

The gif must be 32x32 pixels. If you'd like to make your own pixel art gif, I recommend using [Aseprite](https://www.aseprite.org/).

1. Assuming your animated gif is on your regular computer, you can use the `scp` command to copy it onto your Raspberry Pi.
  
	Run this command on your regular computer
	
	`
	scp <source> pi@<pi_ip>:<destination>
	`
	
	replacing the following parts as described:
	- `<source>` is the path to the file you want to copy
	- `<pi_ip>` is your Raspberry Pi’s IP address
	- `<destination>` the path to this project directory on your Raspberry Pi

2. On your Raspberry Pi, download my Python `displayGIF.py` script and a sample gif with the `curl` command:
  
	```bash
	curl https://raw.githubusercontent.com/poemusica/rpi-matrix-gif/master/displayGIF.py >displayGIF.py
	curl https://raw.githubusercontent.com/poemusica/rpi-matrix-gif/master/myGIF.gif >myGIF.gif
	```    

3. [FIXME 😭] On your Raspberry Pi, run the Python script:
	
	`python displayGIF.py`
	
	By default, the script displays the included sample gif ![Ghost](https://github.com/poemusica/rpi-matrix-gif/blob/master/myGIF.gif) created by [@jettisonjoe](https://github.com/jettisonjoe).

	To display your own gif, replace `myGIF` in the code with the name of your gif.

**Tip**: If you want to stop the script, use the `Ctrl`+`c` key combination.
    

### (Optional) Step 5: Run on boot

If you want the `displayGIF.py` script to run automatically whenever you start up the Raspberry Pi,
follow [these instructions](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)
to edit the `rc.local` file on your Raspberry Pi.
