# Using rsub with Raspberry Pi

If you’re used to writing code on your regular computer using Sublime Text, you might want to set up rsub/rmate. Then you can open files located your Raspberry Pi using Sublime Text on your regular computer. 

1. On your regular computer:
  1. Install the rsub plugin for Sublime Text.
     
     https://packagecontrol.io/packages/rsub
  
  2. Modify your `~/.ssh/config` file to include the following lines:

    ```
    Host <pi_ip>
    RemoteForward 52698 127.0.0.1:52698
    ```

    where `<pi_ip>` is your Raspberry Pi’s IP address.


2. On your Raspberry Pi:

  1. Download rmate
  
    `curl https://raw.githubusercontent.com/aurora/rmate/master/rmate > rmate`

  2. Move it to `/usr/local/bin` and make it executable:

    `sudo mv rmate /usr/local/bin`

    `sudo chmod +x /usr/local/bin/rmate`

  3. Make a symlink so that you can invoke Sublime Text from the command line:

    `ln -s /usr/local/bin/rmate.sh  /usr/local/bin/subl`

Now you can use the command `subl <file>` to open your Raspberry Pi files via SSH using Sublime Text.
