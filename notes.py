# -*- coding: UTF-8 -*-

notes = {
    "gpg": """
    gpg --edit-key amy.bowen@gmail.com

    --> expire
    --> set new expiration date
    --> save

    gpg --send-keys 65955E609B076014

    gpg --armor --export 65955E609B076014
    replace on github
    """,
    "android": """
        # mount
        jmtpfs /media/android

        # dismount
        fusermount -u /media/android/

    """,
    "apache": """
        # Serve a simple json file

    after having pasted dict into index.html:

        with open('index.html', 'r') as f:
            data = f.read()

        with open('/tmp/index.html', 'a') as f:
            f.write(json.dumps(eval(data)))
    """,
    "gandi": """

    http://doc.livedns.gandi.net/#managing-zones

    curl -H "X-Api-Key: $GANDI_V5_API_KEY" https://dns.beta.gandi.net/api/v5/zones

    curl -H "X-Api-Key: $GANDI_V5_API_KEY" https://dns.beta.gandi.net/api/v5/zones/dc6d57de-b610-4f61-97b4-9e6d4eac8060/records

    """,
    "readline": """

Moving

Ctrl-a      Move to the start of the current line.
Ctrl-e      Move to the end of the line.
Ctrl-f      Move forward a character.
Ctrl-b      Move back a character.
Alt-f       Move forward to the end of the next word. Words are alphanumeric.
Alt-b       Move back to the start of the current or previous word. Words are alphanumeric.
Ctrl-l      Clear the screen.

History

Ctrl-p      Fetch the previous command from the history list.
Ctrl-n      Fetch the next command from the history list.
Alt-<       Move to the first line in the history.
Alt->       Move to the last line in the history.
Ctrl-r      Search backward through history.
Ctrl-s      Search forward through history.
Alt-p       Search backward through history for a given string.
Alt-n       Search forward through history for a given string.
Ctrl-Alt-y  Insert the first argument to the previous command. With an argument n, insert the nth word from the previous command.
Alt-.
Alt-_       Insert the last argument to the previous command. With an argument n, insert the nth word from the previous command.

Changing Text

Ctrl-d      Delete the character under the cursor.
Delete      Delete the character before the cursor.
Ctrl-v
Ctrl-q      Add the next character you type verbatim.
Ctrl-t      Transpose characters.
Alt-t       Transpose words.
Alt-u       Uppercase the current word.
Alt-l       Lowercase the current word.
Alt-c       Capitalize the current word.

Killing and Yanking (Cutting and Pasting)

Ctrl-k          Kill (cut) forwards to the end of the line.
Ctrl-u
Ctrl-x Delete   Kill (cut) backwards to the start of the line.
Alt-d           Kill (cut) forwards to the end of the current word.
Alt-Delete
Ctrl-w          Kill (cut) backwards to the start of the current word.
Alt-\           Delete whitespace around the cursor.
Ctrl-y          Yank (paste) the top of the kill ring.
Alt-y           Rotate the kill ring, and yank (paste) the new top. Only works after a yank.

Completing

Tab         Autocomplete.
Alt-?       List possible completions.
Alt-*       Insert possible completions.

Macros

Ctrl-x (        Begin saving the characters typed as a macro.
Ctrl-x )        Stop saving the characters typed as a macro.
Ctrl-x e        Execute the most recent macro.

Miscellaneous

Ctrl-x Ctrl-r       Read in the contents of the inputrc file.
Ctrl-g              Abort current editing command
Ctrl-_
Ctrl-x Ctrl-u       Incremental undo, separately remembered for each line.
Alt-r               Undo all changes made to this line. This is like executing the undo command enough times to return the line to its initial state.
Alt-Space
Ctrl-@              Set the mark (save this location).
Ctrl-x Ctrl-x       Set the mark and jump to the previous mark.
Ctrl-]              Search forwards for a single character in the current line and jump to that location.
Ctrl-Alt-]          Search backwards for a single character in the current line and jump to that location.
Alt-#               Comment the current line and start a new one.
Ctrl-e              Enter Emacs editing mode
Ctrl-Alt-j          Enter Vi editing mode
    """,
    "network": """
        $  ip ro ls
        default via 192.168.1.1 dev wlan0  proto static  metric 1024
                     ^^^^^^^^^^ is the router


    # to share ethernet connection

    ## on machine with the connection:
        sudo ip link set eth0 up
        ip a  # to see if you have an IP address
        sudo ip addr add 192.168.3.2/24 dev eth0
        ping 192.168.3.1
        sudo iptables -t nat -I POSTROUTING -s 192.168.3.1 -j MASQUERADE
        sudo iptables -nxvL
        sudo iptables -I FORWARD -s 192.168.3.1 -j ACCEPT
        sudo iptables -I FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

    ## on the other machine
        ip route add default via 192.168.3.2
        ip link set <interface> up
        ip addr add 192.168.3.1/24 dev <interface>

    and update /etc/resolv.conf

    or, someday: launch a dhcp server on home device automatically


    """,
    "trash": """
        ~/.local/share/Trash
    """,
    "gmail": """
    before:YYYY/MM/DD
    after:YYYY/MM/DD
    """,
    "i3": {
        "screenshots": """
        François-Xavier Bourlet (bombela@gmail.com)
        bindsym Shift+Print exec exec mate-screenshot -a
        bindsym Ctrl+Shift+Print exec exec mate-screenshot -w
    """,
        "navigation": """
    ### close floating window
      mod+shift+q

    ### reload i3 config
      mod+shift+r

    ### fullscreen current pane
      mod+f

    ### send something to another desktop
      mod+shift+desktop

    ### send desktop to another monitor

      mod + x

    ### resize

      mod + x to enter resize mode
      then:
      h/j/k/l
      then:
      escape/enter to exit resize mode

    ### shift focus to another pane
      mod + arrows

    ### modify layout

      mod+w = tabbed
      mod+s = stacked
      mod+e = tiled

    ### close current pane
      mod+shift+q
      """,
    },
    "jq": """
        Retrieve only keys in a dict
         cat ~/.convox/auth  | jq 'to_entries[] | .key'
    """,
    "ruby": """
        # rename a hash key
        hash[:new_key] = hash.delete :old_key

        # multiline comments (=begin and =end must be at the beginning of the line)

        =begin
        commented
        code
        =end
    """,
    "bluetooth": """
    # bluetooth

    ## connect to a device

        $ bluetoothctl

            [bluetooth] connect 84:17:66:CB:37:47 # Moto stream
            [bluetooth] connect 90:03:B7:AE:7B:5E # Parrot Zik V1.10

        ... should produce:
            Attempting to connect to 84:17:66:CB:37:47
            [CHG] Device 84:17:66:CB:37:47 Connected: yes
            Connection successful
    then:
        $ pavucontrol
        # change output device ^

    ## bluetooth status

    $ /etc/init.d/bluetooth status

    ## load module if needed

        $ pactl load-module module-bluetooth-discover
        19

  * **hciconfig**: configure bluetooth devices

  # zik: 90:03:B7:AE:7B:5E
  # hci0: 7C:7A:91:04:B7:39

    $ sudo bluetooth-wizard  # setup
    $ hcitool dev                                       # list devices
    $ sudo bluez-simple-agent hci0 7C:7A:91:04:B7:39    # create device?
    $ sudo bluez-test-device trusted 7C:7A:91:04:B7:39 yes
    $ sudo hciconfig hci0 reset                         # reset the adapter

    ## See also
        rfcomm, btmon, hciconfig,
        /etc/bluetooth/, /proc/acpi/ibm/bluetooth, /etc/init.d/bluetooth,
        hciconfig, hcitool, hcidump, hciattach
        """,
    "accents": """
            `set` = show all envvars and functions

            $ setxkbmap -option "compose:ralt" us
            $ é ô
            $ # Jérôme ♥ Amy

        # to view current compose key:
        grep "compose:" /usr/share/X11/xkb/rules/base.lst


        see also: 'halp keyboard'

        """,
    "input": """
        # debug input events

        sudo libinput-debug-events

    """,
    "boot": """
     To change default timeout for OS choice when booting: edit /etc/default/grub

     Then run `sudo update-grub` to apply the changes.
    """,
    "startup": """
    see "boot"
    """,
    "bootloader": """
    when PC can't boot to linux after updating BIOS

    make a linux boot disk
    boot into installer
    rescue mode

    find device/partition corresponding to linux install, e.g. /dev/nvme0asfflkd
    reinstall grub boot loader on that device


    (if it ends with p-something it's a partition, otherwise it's a new disk)

    sda = whole device
    sda1 - partitions

    """,
    "trackpad": """
        # palm detection stuff
          $ syndaemon  --> NO! actually just use mate-control-center -> mouse

        # view touchpad Parameter settings:
          $ synclient

        # get list of input devices:
          $ xinput --list

        # Get id of a specific device:
          $ xinput --list --id-only "SynPS/2 Synaptics TouchPad"

        # enable/disable an input device (e.g. trackpad)

          xinput enable 11
          xinput disable 11
          xinput --list-props <id>  # view config
          xinput --set-prop 10 262 1.5  # 1.0 = faster, 2.0 = slower (razer mouse)

        # display information about input devices:
          $ cat /proc/bus/input/devices | grep -i touchpad -B2 -A9

        # touchpad stuff

          $ synclient RightButtonAreaLeft=0
          $ synclient RightButtonAreaTop=0

        ## fucking touchpad scrolling bullshit
               Property: "Synaptics Off"

               Option "LockedDrags" "boolean"
                      If off, a tap-and-drag gesture ends when you release the finger.  If on, the gesture is
                      active until you tap a second  time,  or  until  LockedDragTimeout  expires.  Property:
                      "Synaptics Locked Drags"

               Option "LockedDragTimeout" "integer"
                      This  parameter  specifies how long it takes (in milliseconds) for the LockedDrags mode
                      to be automatically turned off after the finger is released from  the  touchpad.  Prop‐
                      erty: "Synaptics Locked Drags Timeout"

            omg found it:
            CoastingSpeed           = 10
            synclient CoastingFriction=1000

        old values:
        ○ synclient -l | grep -i coa
            CornerCoasting          = 0
            CoastingSpeed           = 20
            CoastingFriction        = 50

        Tip: To help find the best values for palm detection, you can use evtest to see the width and Z values reported during touchpad use.


    """,
    "images": """
        image viewer:
        $ feh -ZF
         image editor:
        $ digikam
    """,
    "keyboard": """
        ### layouts (including accents)
        mate-keyboard-properties  (in mate-control-center package)
        -> US international (dead keys)

        # see which key codes correspond to physical keys:
        sudo evtest

        ### map

        $ xmodmap -pm
            xmodmap:  up to 4 keys per modifier, (keycodes in parentheses):

            shift       Shift_L (0x32),  Shift_R (0x3e)
            lock        Caps_Lock (0x42)
            control     Control_L (0x25),  Control_R (0x69)
            mod1        Alt_L (0x40),  Alt_R (0x6c),  Meta_L (0xcd)
            mod2        Num_Lock (0x4d)
            mod3
            mod4        Super_L (0x85), Super_R (0x86), Super_L (0xce), Hyper_L (0xcf)
            mod5        ISO_Level3_Shift (0x5c),  Mode_switch (0xcb)

        XF86AudioLowerVolume

        keycode 67 (keysym 0xffbe, F1),

        ### swap alt/option and command keys

            $ echo 1 | sudo tee /sys/module/hid_apple/parameters/swap_opt_cmd
        ### see also

            $ xkbset -q
    """,
    "sudo": """
        preserve environment:
            sudo -E
        path: see /etc/sudoers / secure_path
    """,
    "usb": """
        ## USB devices

        ### mount a USB drive

            $ sudo fdisk -l
            $ sudo mount -t vfat /dev/sdb1 /media/external
            $ sudo mount -t ntfs <device> <desired mountpoint>
            $ sudo umount /media/external

            # note: if it says device is busy:
            $ lsof <mountpoint>
            # or:
            $ fuser -mauv <mountpoint>

            $ dmesg
            [161795.666308]  sdb: unknown partition table
            root@patamushka:/mnt# mount /dev/sdb thing/


    """,
    "battery": """
        ## View power usage
            # sudo powertop
        ... then go to the last tab and change everything to "good"
        ## view battery status

            $ acpi

    """,
    "wifi": """
        Note: wifi networks are stored in /etc/NetworkManager/system-connections

        ## getting the f online

            $ nm-applet
            $ nmcli -p con    # connection list
            $ nmcli -p nm   #

            $ sudo nmcli -p con up uuid 52b9229e-4e3e-44c1-b1f8-ebe412d2d8bd

        I think you can also "up" an interface using its nickname (in my case, I add all wireless networks using "w-$NETWORKNAME")
        (cf my addwifi script)

  413  nmcli
  414  dmesg
  415  wi scan
  416  iw
  417  iw info
  418  iw list
  419  iw list | less
  420  iw scan
  421  iw dev wlan0 scan
  422  nmcli
  423  nmcli r
  424  ifconfig
  425  ifconfig wlan0
  426  ip set dev wlan0 up
  427  ip link dev wlan0 set up
  428  ip link set dev wlan0 up
  429  ifconfig
  430  dmesg
  431  iw dev wlan0 scan
  432  iw dev wlan0 scan | grep SSID
  433  dmesg
  434  nmcli c up Tree
  435  ls /etc/NetworkManager/system-connections/
  436  cd /etc/NetworkManager/
  437  cat Tr
  438  cd system-connections/
  439  cat Tree
  440  cat Tree\ 1
  441  diff Tree Tree\ 1
  442  diff Tree Tree\ 1
  443  diff -Nu Tree Tree\ 1
  444  diff -Nu Tree Tree\ 2
  445  diff -Nu Tree\ 1 Tree\ 2
  446  nmcli c up Tree
  447  nmcli c up Tree\ 1
  448  nmcli c up Tree\ 2
  449  cat Tree
  450  ifconfig wlan0
  451  nmtui
  452  nmcli
  453  nmcli d
  454  ps faux | grep netw
  455  /etc/init.d/network-manager start
  456  nmcli d
  457  ps fauxwww | grep -i network
  458  ps fauxwww | grep -i network | grep -v chrom
  459  ps fauxwww | grep -i network | grep -v chrom
  460  kill 2442
  461  ps fauxwww | grep -i network | grep -v chrom
  462  ps fauxwww | grep -i network | grep -v chrom
  463  nmcli d
  464  /etc/init.d/network-manager start
  465  nmcli d
  466  dmesg

    Next time wifi interface mysteriously gone, try restarting network-manager, i.e.
    $ /etc/init.d/network-manager restart

# slow network?

    Next time internet is mysteriously slow at a hotel, try:
    - ping the default gateway (`ip route`)

$ ip route | grep default
default via 172.20.0.1 dev wlan0 proto static metric 600 

    if the responses are all < 1ms, then the traffic's not really going there.
    check docker networks with `docker network ls` and locate the one starting with the same octets:
    docker network ls -q | xargs docker network inspect | less

And `docker network rm <name>`

Then ping the default gateway again, this output is more normal:

64 bytes from 172.20.0.1: icmp_seq=105 ttl=64 time=1.08 ms
64 bytes from 172.20.0.1: icmp_seq=106 ttl=64 time=1.03 ms
64 bytes from 172.20.0.1: icmp_seq=107 ttl=64 time=2.45 ms
64 bytes from 172.20.0.1: icmp_seq=108 ttl=64 time=0.861 ms
64 bytes from 172.20.0.1: icmp_seq=109 ttl=64 time=1.25 ms

    if you have a stable ping from there then changing the BSSID won't help

    - setting the BSSID manually via nmtui.

    signal strength is negative, so bigger numbers are worse
    filter by first digit of frequency (2 vs 5)
    display the fastest 2 per frequency band

    Run: addwifi.sh scan

    Then set the BSSID manually by editing the connection via nmtui
    ====

# Can't retrieve default nameservers in a captive portal situation:
    random valid server IP: 193.19.211.1

    how to retrieve valid nameservers:
    "maybe running a dhcp client manually i.e. dhclient"

    Run:
    sudo dhclient wlan0
    less /etc/resolvconf/run/resolv.conf
    """,
    "docker": """
        # Copy some directory from a container
        docker run --rm myrepo/private-gems tar -C /gems -cf- . | tar -C /tmp/gems -xf-

        sudo systemctl start docker
        docker-check-config.sh
        docker info
        systemctl show docker


        "ERROR: for bot oci runtime error: no such file or directory"
        --> In a workdir that doesn't exist because it was overwritten by a volume

        Start in verbose mode:
            # stop docker first
            sudo systemctl stop docker

            sudo /usr/bin/dockerd --debug

        View docker logs via systemd:
            sudo journalctl -fu docker.service
    """,
    "markdown": """
        # Collapsible section
        <details>
          <summary>Click to expand</summary>
          whatever
        </details>
    """,
    "games": """
        gnome-mahjongg
    """,
    "system": """

    System info

        uname -a

    start a service at boot:
          $ sudo systemctl enable docker
    or
          $ sudo chkconfig docker on
          $ sudo chkconfig --list

    Edit cron tasks
        $ crontab -e
    """,
    "defaults": """
    Default programs

        xdg-settings
            xdg-settings set default-web-browser google-chrome.desktop
        sudo update-alternatives –config editor
        www-browser
        x-www-browser
        gnome-www-browser
        gnome-open <url>   # uses YET ANOTHER default browser

        ## ~/.config/mimeapps.list

        contained the following lines:
            [Default Applications]
            x-scheme-handler/http=userapp-Firefox-BW8QLY.desktop
        renaming mimeapps.list to mimeapps.list- solved the problem \o/


    Validate desktop file
        desktop-file-validate /usr/share/applications/google-chrome.desktop
    /usr/share/applications/google-chrome.desktop: error: file contains group "NewWindow Shortcut Group", but groups extending the format should start with "X-"
/usr/share/applications/google-chrome.desktop: error: file contains group "NewIncognito Shortcut Group", but groups extending the format should start with "X-"


    Mime / file types handling

        xdg-mime default xpdf.desktop application/pdf

    More:
        http://unix.stackexchange.com/questions/36380/how-to-properly-and-easy-configure-xdg-open-without-any-enviroment


    """,
    "google-fi": """"
    # Manually switch networks
        try maybe switching networks again but with a code. The code that you can dial is *#*#34866#*#*
        After you it's switched, let me know if you get any connection to data.
        AJ Bowen6:55 PM
        it say: switching to MCC/MNC: 310260

        34866 = t-mobile network id
        http://nicholasarmstrong.com/2015/08/network-handover-google-fi/
    """,
    "displays": """
        ## Displays
        ### send desktop to another monitor

          mod + x

        xbacklight -dec 10

        xbacklight -inc 10

        # see also: http://askubuntu.com/questions/149054/how-to-change-lcd-brightness-from-command-line-or-via-script

        # locking the screen

        Need a screenlocker, e.g. xtrlock (bare bones), or i3lock, or buttslock (see Jess's dockerfiles)

        buttslock: in a container; watches for dbus signals, when computer is about to go to sleep it will initiate screenlocking

        # get dimensions
            xdpyinfo | grep dimensions:

        # use JP's laptop as a monitor over ethernet:
            ifconfig -a | grep -i eth  # to get the interface (usually eth0 or eth3)
            ssh <jp_ip_addr>
            tmux    # so that if the session is interrupted it can be restored
            ifconfig <interface> 10.10.10.11/24  # from my machine (and ping .10 from here)
            ifconfig <interface> 10.10.10.10/24  # from jp machine, as root: once done, run `ping 10.10.10.11` from this machine
        then change the display environment variable:
            export DISPLAY="10.10.10.10:1"
    """,
    "timezone": """
        # timezone / date

        To update timezone:
          $ sudo dpkg-reconfigure tzdata

        Stored in:
          /etc/timezone
          ~/.exports

        see also: zdump (timezone dumper), tzconfig (deprecated)
    """,
    "files": """
        # browse files

        nautilus
        vifm

    """,
    "windows": """
        ## Window manipulation and stuff

        See:

        - xdotool
        - wmctrl
        - xwininfo
        - xdpyinfo
    """,
    "power": """
        # putting computer to sleep

         echo mem | sudo tee /sys/power/state
    """,
    "hardware": """
        ## display a bunch of info about CPU, USB, networks etc
            $ sudo lshw

        ## display info on CPU architecture

            $ lscpu

        ### list all PCI devices

            $ lspci

    """,
    "vim": """
        ## vim

        25%  -> move to the 25% point of the file

        zt/zz/zb
        redraw with cursor at top/middle/bottom of page

"Rewrap document to tw:
gw
:set tw=80

"Max out the height of the current split
ctrl + w _

"Max out the width of the current split
ctrl + w |

"Normalize all split sizes, which is very handy when resizing terminal
ctrl + w =

"Swap top/bottom or left/right split
Ctrl+W R

"Break out current window into a new tabview
Ctrl+W T

"Close every window in the current tabview but the current one
Ctrl+W o

Autocompletion:

imap <Tab> <C-P>

    """,
    "session": """
    There are:
    - session managers
    - window managers (i3)
    - desktop managers (or display manager, he's not sure which the right wording) (gdm, xdm)
    - desktop environments, e.g. Gnome
    - display server, e.g. xorg
    - [display] protocol: X11

    # Display manager
        A display manager is the first thing tha shows up on screen and will manage
        the login screen. from there, you put your credentials, possibly select a
        session. then hands off to the session manager.

    # Desktop environment

        Gnome is a desktop environment, it's a whole set of many things

    # Session manager

        A session manager can be gnome, or none at all. The session manager starts the window manager, among other things.

        Session manager can keep track of opened apps, and restart them on login.

        By default it doesn't do anything. It's an optional compontent that sits
        between window manager and the display manager.

        Starting applications via the session manager could look like this:
            #!/bin/sh
            i3 &
            firefox &
            some-other-app &
            wait

    # Window manager

        The window manager will be the first process that belongs to you and that's
        connected to the display. It's responsible for managing the windows. Applications
        will put windows on the display. The window manager will tell how big
        those will be, how big, will decorate with title bars and buttons and borders.
        It also might do things like start status bar.

    # Notes

        User can start apps from either the window manager or the session manager.
        If it's xsession (session mgr), ...?

        there's another way to start a graphical session. login text mode (Ctrl+Alt+F1),
        startx. that starts the X server and immediately starts your session.
        that's for computers without a graphical mode on login. can run startx. starts
        xsession after starting up display.  in that case you don't have a display manager.

    """,
    "backup": """
    borg info /media/external/backup/patamushka::patamushka-2019-01-17\ 14:04:29.168226
    """,
    "bash": """
        # send stdout and stderr to /dev/null
        &>/dev/null

        # debug bash
        ## set -v

        This will echo a line before it is executed.

        ## set -x

        The set -x will output the line after the shell script interpolates the variables and expressions in that line.

        As part of this, you can also create an environment variable called PS4 which will be the prompt printed each time your shell scripts outputs the line being executed. Most people set it to something like PS="\$LINENO: " which will print out the line number for the line being executed.

        Once you're finished, you can turn off debugging by setting set +xv.

    # expansion? don't know what this is called

      !$       Run the last word of the previous command (same as Alt + .)
      !*       Run the previous command except for the last word
      !foo     Run the most recent command that starts with 'foo' (e.g. !ls)

    Moving the cursor:
      Ctrl + a   Go to the beginning of the line (Home)
      Ctrl + e   Go to the End of the line (End)
      Ctrl + p   Previous command (Up arrow)
      Ctrl + n   Next command (Down arrow)
       Alt + b   Back (left) one word
       Alt + f   Forward (right) one word
      Ctrl + f   Forward one character
      Ctrl + b   Backward one character
      Ctrl + xx  Toggle between the start of line and current cursor position


      Alt + t   Swap current word with previous
     Ctrl + t   Swap the last two characters before the cursor (typo).
     Esc  + t   Swap the last two words before the cursor.

    Set Vi Mode in bash:
    $ set -o vi

    Set Emacs Mode in bash:
    $ set -o emacs

    Show current settings:
    $ set -o

    Show current keybindings:
    $ bind -P
    """,
    "aws": """
        ## Mounting aws s3 bucket with sshfs

        echo "$AWS_S3_BUCKET:$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" > ~/.secrets/amazon-s3-passwd
        sudo mkdir /mnt/$AWS_S3_BUCKET
        sudo chown aj:aj blog.soulshake.net/
        s3fs $AWS_S3_BUCKET /mnt/$AWS_S3_BUCKET -o passwd_file=~/.secrets/amazon-s3-passwd
    """,
    "regex": """
    Swap keys/values (containing _) in a yaml file in vim:
        :%s/^\ \ \ \ \(\a\+\): \([A-Za-z_]\+\)/\ \ \ \ \2: \1/
    ^ spaces don't need to be escaped actually

    e.g.:
        MIDNAME: name_middle
        PREFIX: name_prefix
        GENSUFFIX: name_suffix
    becomes:
        name_middle: MIDNAME
        name_prefix: PREFIX
        name_suffix: GENSUFFIX

    """,
    "ethernet": """
        # transfer via ethernet

        ip addr add 10.10.10.10/24 dev eth0
        # eth0 = the name of the interface to which you want to add the address
    """,
    "iptables": """
    # watch iptables counters in real time:
        watch --interval 0 'iptables -nvL'
    """,
    "git": """
        Create new local branch that tracks an upstream branch:
          $ git checkout remote-branch-name  # creates new local branch
          $ git pull origin remote-branch-name

        If checkout doesn't work: delete & reclone repo, or maybe `git fetch` will work

        To see commits that haven't been pushed yet:
          $ git push --dry-run  # then compare commit hashes to git log

        To move commits to another branch:
          $ git branch -f <branch with the misplaced commit> <commit hash of the last wanted commit>

        To discard changes to a specific file:
          $ git checkout README.md
    """,
    "sound": """
        ## adjust volume

            $ pavucontrol / pulseaudio
            $ /usr/bin/pulseaudio
            $ amixer
            $ alsamixer     # gui
            # pavumeter     # gui showing current realtime audio output levels
    """,
    "terminal": """

    Can I specify what characters set the double-click selection boundary in GNOME Terminal?
    http://askubuntu.com/questions/8413/can-i-specify-what-characters-set-the-double-click-selection-boundary-in-gnome-t
    https://bugs.launchpad.net/ubuntu/+source/gnome-terminal/+bug/1401207/comments/8


    $ dconf write /org/gnome/terminal/legacy/profiles:/:65c99ed6-29e0-4c99-9231-91943285e95c/word-char-exceptions '@ms "-,.;/?%&#_=+@~·:"'

    $ dconf list /org/gnome/terminal/legacy/profiles:/:65c99ed6-29e0-4c99-9231-91943285e95c/background-color




    """,
    "travis": """
    # debug job (get job id from build log on web interface)
    curl -s -X POST   -H "Content-Type: application/json"   -H "Accept: application/json"   -H "Travis-API-Version: 3"   -H "Authorization: token $TRAVIS_STAGING_ORG_API_TOKEN"   https://api-staging.travis-ci.org/job/${id}/debug

    """,
    "vpn": """
    you could fire up an EC2 instance and SSH to it enabling socks forwarding
    en gros:
    ssh -D 1111 ubuntu@remote-ec2-instance
    ensuite dans ton navigateur tu lui dit de se connecter via un proxy socks sur localhost:1111
    """,
    "printing": """
    http://localhost:631/printers/

    In Chrome, go to manage printers
    Click printers
    Click unlock
    Add printer
    """,
    "webserver": """
    Run a local webserver serving the current directory:

    $ python3 -m http.server
        """,
    "etc": """

        ## apple stuff

            $ cd /sys/module/hid_apple/parameters

        # Preserving permissions and structure with rsync

        Recursively copy from a remote system to local system preserving permissions and structure:

            $ rsync -a -v -e ssh server:/source/ /dest/

        Where:
        -a  archive mode; includes recursion
        -v  increase verbosity
        -e  specify the remote shell to use

# etc

 grep . *


## FACKING python packaging
everything you want to expose to the user goes in __init__.py
truc = ceci
chouette = bidoule

[    1.207232] Intel(R) Wireless WiFi driver for Linux, in-tree:
[    1.207234] Copyright(c) 2003- 2014 Intel Corporation
[    1.208036] iwlwifi 0000:03:00.0: irq 60 for MSI/MSI-X
[    1.218200] pstore: Registered efi as persistent store backend
[    1.220286] input: PC Speaker as /devices/platform/pcspkr/input/input7
[    1.221704] ACPI: Battery Slot [BAT1] (battery present)
[    1.223048] iwlwifi 0000:03:00.0: firmware: failed to load iwlwifi-7265-9.ucode (-2)
[    1.223095] iwlwifi 0000:03:00.0: Direct firmware load failed with error -2
[    1.223097] iwlwifi 0000:03:00.0: Falling back to user helper

# "THIS IS the trick i did ... this is the module that was outputting the messages ("fireware failed to load") and this is the wireless card that "

# kill the damn thing

win+d, xkill, click unresponsive window

dnsmasq -

is your shell clean? -> one of the login shells is producing output

bash_profile is for interactive shells; it can echo whatever you want
bashrc should not display stuff

""",
}

"""

adding more swap:

   26  docker logs 1ad
   27  docker inspect 1ad
   28  docker inspect 1ad | less
   29  free -m
   30  dd if=/dev/zero of=/swap bs=1024K count=1024
   31  mkswap /swap
   32  swapon /swap
   33  free -m
   34  docker start 1ad

starting service at startup:

chkconfig

have command:
add 'alias have="_have"' to /etc/bash_completion.d/ocamlfind
"""

"""
google sheets tricks

=ImportJSON("https://api.github.com/repos/convox/rack/contributors?per_page=100", "/login", "noHeaders")
"""
