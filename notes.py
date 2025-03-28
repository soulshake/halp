# -*- coding: UTF-8 -*-

notes = {
    "tcpdump": """
    trace a remoteaddr IP to the origin pod:

apply k8s/hacktheplanet.yml from container.training repo after setting spec.hostNetwork: true and uncommenting privileged
install tcpdump / ngrep
ngrep -tpd any -Wbyline /api/v1/ tcp and not port 41485
make the request
""",
    "kubectl": """

# `top pods` for a specific node

kubectl get pods -A -o wide | grep "${NODE}" | awk '{print $2 " " $1}' | while read pod namespace; do kubectl top pod $pod -n $namespace --no-headers; done | awk '{printf "%-60s %-10s %-10s %-10s\n", $1, $2, $3, $NF}'

# unsafe port-forwarding for compatibility with docker compose

use --address 0.0.0.0 flag to kubectl port-forward, e.g.

```
kubectl --address 0.0.0.0 port-forward service/SERVICE_NAME 8000:8000
```
Then use your machine's internal IP address (cf i3 status bar, 10.0.0.28) as the endpoint.
But anyone connected to the same network (i.e. cafe wifi) will be able to access the DB!
Non-Linux users have some envvar like `${DOCKER_HOST}` that includes this IP.

    """,
    "abc": """
A	Alfa [sic]	ˈalfa	ˈælfa	AL fah
B	Bravo	ˈbravo	ˈbraːˈvo	BRAH voh
C	Charlie	ˈtʃali or ˈʃali	ˈtʃɑːli or ˈʃɑːli	CHAR lee or SHAR lee
D	Delta	ˈdɛlta	ˈdeltɑ	DELL tah
E	Echo	ˈɛko	ˈeko	ECK oh
F	Foxtrot	ˈfɔkstrɔt	ˈfɔkstrɔt	FOKS trot
G	Golf	ˈɡɔlf	ɡʌlf [sic]	golf
H	Hotel	hoˈtɛl	hoːˈtel	ho TELL
I	India	ˈɪndia	ˈindi.ɑ	IN dee ah
J	Juliett [sic]	ˈdʒuliˈɛt	ˈdʒuːli.ˈet	JEW lee ETT
K	Kilo	ˈkilo	ˈkiːlo	KEY loh
L	Lima	ˈlima	ˈliːmɑ	LEE mah
M	Mike	ˈmai̯k	mɑik	mike
N	November	noˈvɛmba	noˈvembə	no VEM ber
O	Oscar	ˈɔska	ˈɔskɑ	OSS cah
P	Papa	paˈpa	pəˈpɑ	pah PAH
Q	Quebec	keˈbɛk	keˈbek	keh BECK
R	Romeo	ˈromio	ˈroːmi.o	ROW me oh
S	Sierra	siˈɛra	siˈerɑ	see AIR rah
T	Tango	ˈtaŋɡo	ˈtænɡo	TANG go
U	Uniform	ˈjunifɔm or ˈunifɔm	ˈjuːnifɔːm or ˈuːnifɔrm [sic]	YOU nee form or OO nee form
V	Victor	ˈvɪkta	ˈviktɑ	VIK tah
W	Whiskey	ˈwɪski	ˈwiski	WISS key
X	Xray, x-ray	ˈɛksrei̯	ˈeksˈrei	ECKS ray
Y	Yankee	ˈjaŋki	ˈjænki	YANG key
Z	Zulu	ˈzulu	ˈzuːluː	ZOO loo

    """,
    "alpha": "See abc",
    "apt": """
    See also:
    - /usr/share/keyrings/
    - /etc/apt/trusted.gpg.d/

$ sudo apt install zbarcam-gtk
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 libzbargtk0 : Depends: libzbar0 (= 0.23.90-1) but 0.23.92-7 is to be installed
N: Ignoring file 'debian-bookworm.list.off' in directory '/etc/apt/sources.list.d/' as it has an invalid filename extension
E: Unable to correct problems, you have held broken packages.


apt-cache show zbar-tools
apt-cache show zbar-tools | grep ^Vers
sudo apt install zbar-tools=0.23.90-1
sudo apt install zbar-tools=0.22-1
apt-cache show libzbar0 | grep ^Vers
sudo apt install libzbar0=0.23.90-1
sudo apt install zbar-tools


    """,
    "audio": """

    # helped when speakers/mic not working/detected:
    pulseaudio --kill
    pulseaudio --check

back in the old days, you'd need to start your programs, telling them which sound card to use
like I did with mplayer
mplayer -ao alsa = use the first alsa device
(or rather, the default alsa device, which may not be the first)
mplayer -ao alsa:device=hw=0 → use the first alsa device
aplay -l → list output alsa devices
so back in the days we'd have some alsa.conf somewhere where we'd say "use that particular soundcard"
(actually, back in the days, I only ever had one single sound card so that never was an issue for me, but whatevs)
now we have pulseaudio, pipewire, etc
apps send sound to pulseaudio, and pulseaudio can then route the sound to various outputs
and we can change that routing "live", with pavucontrol and other tools
and pulseaudio tries to remember what's the output that you were using last time, but it's notoriously bad at that, so then scheisse passiert

I suggest that you write a little script that would leverage pacmd list or pactl list or something like that, to show:
- which output device (PA calls them "sinks") is currently the default one
- which output streams (PA calls them "sources" iirc) are currently playing, and on which sink
And with a nice sub thing that would annotate BUILT IN ANALOG STEREO with "[INTERNAL SPEAKERS]" or whatever, so that it reminds you which is which
so then you can just run pawtf.sh and it would show you what's what, in a way that you can immediately understand


sound breakage reasons:
- make sure built-in analog stereo is selected as fallback in pavucontrol (green checkmark)
    """,
    "filewatches": """

    for foo in /proc/\*/fd/*; do readlink -f $foo; done | grep '^/proc/.*inotify' |cut -d/ -f3 |xargs -I '{}' -- ps --no-headers -o '%p %U %a' -p '{}' |uniq -c |sort -n

    """,
    "gpg": """
    gpg --edit-key amy.bowen@gmail.com

    --> expire
    --> set new expiration date
    --> save

    (To renew the subkey, do the same thing, but run 'key 37E069FC2CAD485E' to activate the subkey.)

    gpg --send-keys 65955E609B076014
    (Keyservers are defined in ~/.gnupg/gpg.conf)

    replace on github:
    gpg --armor --export 65955E609B076014 | pbcopy
    https://github.com/settings/keys (must delete the old one first)
    """,
    "android": """
        # mount
        jmtpfs /media/android

        # dismount
        fusermount -u /media/android/

        if it looks like this:

        d?????????? ? ?    ?       ?            ? /media/external/

        ...then change USB mode in phone settings from "Use USB for..." from "no data transfer" to "File transfer"

    rsync

    """,
    "autostart": """
    # List enabled services

    systemctl list-unit-files
    systemctl --user list-unit-files

    # Systemd unit files

    They are stored in /etc/systemd/system/
    and also at ~/.config/systemd/user/

    # Automatically starting things at boot
    After install e.g. package prometheus-node-exporter:
    systemctl enable --now prometheus-node-exporter

    # Run commands at boot

    /etc/rc.local

    # Make i3 start things

    -> See the end of ~/.i3/config
    """,
    "units": """
    see `autostart`
    """,
    "storage": """
    see `disk`
    """,
    "apache": """
        # Serve a simple json file

    after having pasted dict into index.html:

        with open('index.html', 'r') as f:
            data = f.read()

        with open('/tmp/index.html', 'a') as f:
            f.write(json.dumps(eval(data)))
    """,
    "chrome": """
    So, if you see your Chrome acting super slow (1 second delays between every redraw), this will help:

    pkill -f chrome.*type=gpu-process


    https://twitter.com/kolyshkin/status/1339406072860143618
    """,
    "cron": """

    Edit cron tasks
        $ crontab -e
    List cron tasks
        $ crontab -l
    Back up cron tasks
        $ crontab -l > ~/dotfiles/cron/crontab
    'install' cron tasks from file
        $ crontab ~/dotfiles/cron/crontab
    """,
    "gandi": """

    http://doc.livedns.gandi.net/#managing-zones

    curl -H "X-Api-Key: $GANDI_V5_API_KEY" https://dns.beta.gandi.net/api/v5/zones

    curl -H "X-Api-Key: $GANDI_V5_API_KEY" https://dns.beta.gandi.net/api/v5/zones/dc6d57de-b610-4f61-97b4-9e6d4eac8060/records

    """,
    "readline": """

Print all things

bind -p

Config file: ~/.inputrc

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

    # analyze network traffic loads/speeds
    nnload

    # see also
    - ip addr
    - ethtool - query or control network driver and hardware settings
    - sudo lshw -class network  # list (network) hardware
    - nmcli device show enp0s31f6  # show network device details, also which nameservers are used
    """,
    "trash": """
        ~/.local/share/Trash
    """,
    "gmail": """
    before:YYYY/MM/DD
    after:YYYY/MM/DD
    """,
    "screenshots": """
        # see 'i3'
        # and ~/.i3/config
    """,
    "i3": {
        "screenshots": """
        François-Xavier Bourlet (bombela@gmail.com)
        bindsym Shift+Print exec exec mate-screenshot -a
        bindsym Ctrl+Shift+Print exec exec mate-screenshot -w
    """,
        "etc": """
        # make one window fill all 3 screens:
        i3-msg "fullscreen global"
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
    "sort": """
    # sort by node  ( -b  = ignore leading whitespace)
    kubectl get pods -A -o wide | sort -b -k 8
    """,
    "env": """
    Export environment variables from another process:

    while IFS= read -d '' -r -u 2 assignment; do
      export "$assignment"
    done 2< "/proc/2/environ"

    The -d '' option with read sets the null character as the delimiter, and the -u 2 option is used to specify file descriptor 2 for reading from the file.
    """,
    "json": """
    see `jq`
    """,
    "jq": """
        Retrieve only keys in a dict
         cat ~/.convox/auth  | jq 'to_entries[] | .key'

        Split json into key-value pairs:
        $ task='{"target": "google.com", "duration": "30"}'
        $ echo "$task" | jq -r 'to_entries[] | "\(.key)=\"\(.value)\""'
        target="google.com"
        duration="30"
    """,
    "tunnel": """
    - create a new dummy interface
      assign 169.254.169.254 address to that interface: ip address add 169... dev <name of interface>
      bring up the link: ip link set <name of interface> up
      bind socat to that interface to forward the connections
      fire up ssh tunnel
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



    # to connect to motostream
$ bluetoothctl
Agent registered
[CHG] Controller F8:59:71:A4:AF:C3 Pairable: yes
[Moto Stream]# devices
Device 84:17:66:CB:53:F8 Moto Stream
Device 20:74:CF:4A:40:18 Aeropex by AfterShokz
[Moto Stream]# disconnect
20:74:CF:4A:40:18  84:17:66:CB:53:F8

# jp has a script for this
$ ssh jp@hex.local
jp@hex.local's password:
Last login: Tue Apr  6 23:48:29 2021 from 10.0.0.13
Agent pid 1991768
[jp@hex ~]$ cat bin/aeropex
#!/bin/sh
# Connect to my Bluetooth headset.
# If the connection fails, force-reload the bluetooth driver and try again.

if ! bluetoothctl connect 20:74:CF:4A:40:18; then
  sudo rmmod btusb
  sudo rmmod btintel
  sudo modprobe btusb
  sleep 5
  bluetoothctl connect 20:74:CF:4A:40:18
fi

        """,
    "accents": """
            `set` = show all envvars and functions

            $ setxkbmap -option "compose:ralt" us
            $ é ô
            $ # Jérôme ♥ Amy

        # to view current compose key:
        grep "compose:" /usr/share/X11/xkb/rules/base.lst


        see also: 'halp keyboard'

        and:
        $ localectl set-x11-keymap us pc104 compose:ralt
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
    "settings": """

        xdg-settings
        gnome-tweaks (in gnome-tweak-tool package)
        mate-settings-daemon

    """,
    "numlock": """
    numlockx
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
    "date": """
    date -d @1267619929  # (might need to remove nanoseconds, i.e. last 3 digits
    """,
    "disk": """
    Check disk usage via ncurses:
        ncdu -x / --exclude /data
        (-x = don't cross filesystem boundaries)

    du -mxs *


    Seen in syslog:
        zagreb smartd[653]: Device: /dev/nvme1, number of Error Log entries increased from 38514 to 38516

    Check with:
        sudo nvme smart-log /dev/nvme1

    your disks both have "available_spare: 100%", which is good (when a block is defective, it gets replaced with a spare)
    "percentage_used" indicates how worn out the disk is.


    # Check disk errors
    $ sudo nvme error-log /dev/nvme
    status_field	: 0x2002(Invalid Field in Command: A reserved coded value or an unsupported value in a defined field)
    trtype		: The transport type is not indicated or the error is not transport related.

    ^ I think we established that this was caused by the prometheus exporter; it queries the NVME disk but does so in a way that confuses the disk and that generates an error
    but that's the equivalent of an HTTP/400 or HTTP/500 error, nothing to worry about re/ the disk itself

    """,
    "images": """
        image viewer:
        $ feh -ZF
         image editor:
        $ digikam
        $ shotwell (less ideal)

        view image metadata:

        exiftool
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

            YOU DON'T NECESSARILY NEED TO SPECIFY -t

            But to check the type, run e.g.:

            mount
            mount | grep sda

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

        # mount read-only:
        sudo mount -o ro /dev/sda1 /media/external

    """,
    "battery": """
        ## View power usage
            # sudo powertop
        ... then go to the last tab and change everything to "good"
        ## view battery status

            $ acpi

    """,
    "xdg": """
    XDG_DATA_HOME: defaults to ~/.local/share
    XDG_CONFIG_HOME: defaults to ~/.config
    XDG_STATE_HOME: defaults to ~/.local/state
    """,
    "autocomplete": """
    See 'completion'
    """,
    "autocompletion": """
    See 'completion'
    """,
    "completion": """
    Completions are in ~/.local/share/bash-completion/completions

    For completion on aliases, create a file in that directory with the following content:

    ```
    . ~/.alias_completion.sh
    ```

    Q. Where should I install my own local completions?

    A. Put them in the completions subdir of $BASH_COMPLETION_USER_DIR (defaults to $XDG_DATA_HOME/bash-completion or ~/.local/share/bash-completion if $XDG_DATA_HOME is not set) to have them loaded automatically on demand when the respective command is being completed. See also the next question's answer for considerations for these files' names, they apply here as well. Alternatively, you can write them directly in ~/.bash_completion which is loaded eagerly by our main script.

    Get default completiosn dir with:
    pkg-config --variable=completionsdir bash-completion

    https://github.com/scop/bash-completion/blob/master/README.md

    """,
    "xml": """
        # Format XML:
        curl -s 'localhost:8000/sitemap.xml' | xmllint --format -
    """,
    "go": """

    #  Override a package in go.mod:

    replace bitbucket.org/quantgene/go-env => ../go-env

    # Past learnings

    When curl works by returning stuff from a given endpoint, but tests only seem to get an empty response... check omitempty on the structs.
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
    $ /etc/init.d/networking restart

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

    # or
    sudo dhclient wlp4s0
    less /run/NetworkManager/resolv.conf

    /etc/resolv.conf

    # this one time, it worked automatically, so i grepped the logs to facilitate future searches. check it:
    $ sudo grep 172.19.248.1 /var/log/syslog
    Mar  8 16:46:42 zagreb NetworkManager[533]: <info>  [1615243602.1569] dhcp4 (wlp4s0): option domain_name_servers  => '172.19.248.1'
    Mar  8 16:46:42 zagreb NetworkManager[533]: <info>  [1615243602.1575] dhcp4 (wlp4s0): option routers              => '172.19.248.1'

  # nameserver populated but doesn't respond to dns lookups

  check that there's no docker route that conflicts:

  $ ip route
  default via 172.18.0.1 dev wlp4s0
  172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown                  <---- bad
  172.18.0.0/16 dev br-7f70a5ed0ea4 proto kernel scope link src 172.18.0.1 linkdown
  172.18.0.0/16 dev wlp4s0 proto kernel scope link src 172.18.139.177
  192.168.49.0/24 dev br-9276563e123e proto kernel scope link src 192.168.49.1 linkdown

  docker network ls
  docker network inspect  #  check for overlapping subnet:
  "Subnet": "172.18.0.0/16"  # <-- conflicts with nameserver 172.18.0.1

  # Can't open nm-applet (unrelated to wifi, but this is where i'll find it)
  Authorization required, but no authorization protocol specified

  xhost si:localuser:root

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

        When error: docker: Error response from daemon: cgroups: cgroup mountpoint does not exist: unknown.
        run:
            sudo mkdir /sys/fs/cgroup/systemd
            sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd

        When error: django.db.utils.OperationalError: could not resize shared memory segment "/PostgreSQL.2071426192" to 8388608 bytes: No space left on device
        in the container, run `df -h` and check the shm size.
        To run with more memory use --shm-size, e.g.: docker run --shm-size=1G

        Detach keys are set in: ~/.docker/config.json
    """,
    "logs": """
    see `halp journalctl`
    """,
    "journalctl": """
  Query the systemd journal.
  - Show all messages from this [b]oot:
    journalctl -b
  - Show all messages from last [b]oot:
    journalctl -b -1
  - Show all messages with priority level 3 (errors) from this [b]oot:
    journalctl -b --priority=3
  - [f]ollow new messages (like `tail -f` for traditional syslog):
    journalctl -f
  - Show all messages by a specific [u]nit:
    journalctl -u unit
  - Filter messages within a time range (either timestamp or placeholders like "yesterday"):
    journalctl --since now|today|yesterday|tomorrow --until YYYY-MM-DD HH:MM:SS
  - Show all messages by a specific process:
    journalctl _PID=pid
  - Show all messages by a specific executable:
    journalctl path/to/executable
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


    Serial numbers:

            $ sudo dmidecode -t system | grep Serial
            $ sudo dmidecode -t baseboard
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
    "encryption": """
        To encrypt:

        echo "PLAINTEXT_STRING" | openssl enc -aes256 -pbkdf2 -base64 -A
        you'll be prompted to provide a decryption password.
        Use -A to avoid newlines.

        To decrypt:

        echo "ENCRYPTED_STRING" | openssl aes-256-cbc -d -pbkdf2 -a
        enter the decryption password to decrypt.
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
    "brightness": """
    See: displays
    """,
    "displays": """
        ** SEE ALSO: monitors **

        # Displays
        ## send desktop to another monitor

          mod + x

        ## brightness

        ### reset screen when washed out

        $ nvidia-settings

        $ echo 50 | sudo tee /sys/class/backlight/nvidia_0/brightness

        xbacklight -dec 10

        xbacklight -inc 10

        # see also: http://askubuntu.com/questions/149054/how-to-change-lcd-brightness-from-command-line-or-via-script

        ## locking the screen

        Need a screenlocker, e.g. xtrlock (bare bones), or i3lock, or buttslock (see Jess's dockerfiles)

        buttslock: in a container; watches for dbus signals, when computer is about to go to sleep it will initiate screenlocking

        ## get dimensions
            xdpyinfo | grep dimensions:

        ## use JP's laptop as a monitor over ethernet:
            ifconfig -a | grep -i eth  # to get the interface (usually eth0 or eth3)
            ssh <jp_ip_addr>
            tmux    # so that if the session is interrupted it can be restored
            ifconfig <interface> 10.10.10.11/24  # from my machine (and ping .10 from here)
            ifconfig <interface> 10.10.10.10/24  # from jp machine, as root: once done, run `ping 10.10.10.11` from this machine
        then change the display environment variable:
            export DISPLAY="10.10.10.10:1"

        ## See also
        nvidia-settings
        xrandr
        xrandr --fb 3840x2160  # force reconfigures the screen to the specified size.

        # set framebuffer, i.e. when undesired scanning/panning. (Insert into screenlayout generated by arandr)
        xrandr --fb $((1080 + 3840 + 1080))x2160

        # To autoload monitor configuration at boot/replug
        autorandr --save U2414H-P51S --force  # where names correspond to monitors, according to JP suggestion
        autorandr -c, --change  # Automatically load the first detected profile

        ## might need to run:
        autorandr --default


        Btw, for Dell monitors, the model number  corresponds to the diagonal in inches & the year
        "U2414H" = 24 inches, came out in 2014, H is for full HD
        Q = Quad, ~4K


        When borked after sleep, run:
        ~/metamode.sh

    """,
    "grep": """
        highlight search results without removing non-matching lines:
        grep -E "^|text" --color='always' file
    """,
    "time": """
    sudo systemctl status systemd-timesyncd

    timedatectl

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
    "ipython": """
    when history gets weird:

    cd ~/.ipython/profile_default
    sqlite3 history.sqlite
    SELECT * from history limit 30;

    Delete rows as needed.

    """,
    "windows": """
        ## Window manipulation and stuff

        See:

        - xdotool
        - wmctrl
        - xwininfo
        - xdpyinfo
    """,
    "pdf": """
    # edit pdfs

    xournalpp

    # pdfseparate

    This command would extract pages 1 - 5 of input.pdf into files named output-page1.pdf, output-page2.pdf, ...

    pdfseparate -f 1 -l 5 input.pdf output-page%d.pdf

    # pdfunite
    If you want to recombine them into page ranges, for example pages 1-3 in one document and pages 4-5 in another, you can use the companion program, pdfunite, as follows:

    pdfunite output-page1.pdf output-page2.pdf output-page3.pdf final-pages1-3.pdf
    pdfunite output-page4.pdf output-page5.pdf final-pages4-5.pdf

    """,
    "psql": """
    # Auto vertical output
    \\x auto

    # Disable pager
    \\pset pager off

    # Show timing info
    \\timing

    # Make it give only bare output:

    psql -t -A -c 'your command'

    # Use certificate auth
    k get secrets eks-prd-ca -o json | jq -r '.data["ca.crt"]' | bd > /tmp/prd-ca.crt
    k get secrets eks-prd-replication -o json | jq -r '.data["tls.key"]' | bd > /tmp/prd-tls.key
    k get secrets eks-prd-replication -o json | jq -r '.data["tls.crt"]' | bd > /tmp/prd-tls.crt
    chmod 600 /tmp/prd-tls.key
    PGSSLMODE=verify-ca PGHOST=$PGHOST_RW PGUSER=streaming_replica PGDATABASE=postgres psql "sslrootcert=/tmp/prd-ca.crt sslkey=/tmp/prd-tls.key sslcert=/tmp/prd-tls.crt dbname=postgres"  -w -X
    """,
    "power": """
        # putting computer to sleep

         echo mem | sudo tee /sys/power/state

        # see also

        powerkit
        config is in .config/powerkit/powerkit.conf

        Note: homeboy switched to xidlehook
    """,
    "curl": """
    Get http status code only:

    curl -s -o /dev/null -w "%{http_code}" http://169.254.169.254/latest/meta-data/spot/instance-action

    """,
    "k9s": """
    get info, including log location:
        k9s info

    k9s config files:
        ~/.config/k9s/
    cluster config files:
        ~/.local/share/k9s/clusters/es/es/config.yaml
    """,
    "spot": """
    check for spot instance interruptions:

    while true; do code=$(curl -s -o /dev/null -w "%{http_code}"  http://169.254.169.254/latest/meta-data/spot/instance-action); if [ $code = "404" ]; then echo "all good"; else echo "code is $code"; curl http://169.254.169.254/latest/meta-data/spot/instance-action; fi; sleep 5; done
    """,
    "helm": """
    list charts in a repo:

    $ helm repo add cnpg https://cloudnative-pg.io/charts/
    $ helm search repo cnpg -l

    search for a keyword:
    $ helm search repo nginx
    """,
    "hardware": """
        ## display a bunch of info about CPU, USB, networks etc
            $ sudo lshw

        ## display info on CPU architecture

            $ lscpu

        ### list all PCI devices

            $ lspci

        ### other helpful things
        sensors (in lm-sensors package)

        cpupower -c 0-7 frequency-info -fm

    """,
    "make": """
        # Touchy variables, an experimental hack.
        # This rule rebuilds dependent targets if any "touchy" variables have changed.
        # Some notes on this rather complex syntax:
        #   &        = this is a "grouped target" rather than a single target.
        #   $(@F)    = ENVVAR
        #   ${$(@F)} = $ENVVAR
        # Step-by-step explanation of how each variable in $(TOUCHY_VARIABLE_NAMES) is processed by this rule:
        # 1. if $ENVVAR is unset or empty, delete /tmp/.make-targets/ENVVAR.
        # 2. If /tmp/.make-targets/ENVVAR doesn't exist, write the value of $ENVVAR.
        # 3. if $ENVVAR is different from the contents of /tmp/.make-targets/ENVVAR, update it.
        # The end result is that the files in /tmp/.make-targets will be written only when
        # the corresponding envvars change, provoking files depending on $(TOUCHY_VARIABLES)
        # to be rebuilt. For example: changing AWS_IAM_USER => rebuild the AWS config.
        $(TOUCHY_VARIABLES) & : track $(MAKE_TARGETS)
            @if [[ -z "${$(@F)}" ]]; then
                rm -f $@
            elif [[ ! -f "/tmp/.make-targets/$(@F)" ]]; then
                echo ${$(@F)} > $@
            elif [[ `cat $@` != "${$(@F)}" ]]; then
                echo -e "${red} $(@F) must be set to ${$(@F)} ${reset} in $@"
                echo ${$(@F)} > $@
            fi

        # Turn ENV1 ENV2 into /tmp/.make-targets/ENV1, /tmp/.make-targets/ENV2
        # (cf. make's "static pattern" syntax)
        $(TOUCHY_VARIABLE_NAMES) & : % : /tmp/.make-targets/% | $(SUBDIRS)


        Insert a tab character in vim:
        <CTRL-V><Tab> in "insert mode"
    """,
    "qr": """
    zbarcam
    """,
    "vim": """
        ## vim
        Find whole word under cursor: * or #
        Find partial word under cursor: g* or g#
        Case-sensitive find whole word under cursor: same as above, then press /, up arrow, Enter
        Case-sensitive lowercase search: append \C to search term

        Reverse line order of visual selection
        '<,'>!tac

        Copy visual selection to clipboard
        :set mouse=a
        "+y

        Join lines without adding a space: gJ

        Surround word with {}: ysiw}  (`ysiq{` to inclue a space)

        expand all folds: zR

        :noautocmd w  -> disable autoformat on save (see .vimrc)
        or:
            BLACK=no vim whatever.py  # (see .vimrc)

        25%  -> move to the 25% point of the file

        zt/zz/zb
        redraw with cursor at top/middle/bottom of page


        ### Spellcheck
        :set spell
        zg -> add word to spellfile
        zw -> mark as bad word
        ]s, [s -> jump to next/previous misspelled word

        # copy to system clipboard
        "+y
        "+p  <-- paste

        # delete surrounding thing
        ds" # delete surrounding quotes

        % -> jump to matching bracket
        } -> jump to next paragraph

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

Commenting (nerdcommenter plugin):

    \ c<space> = comment lines
    \ cu = uncomment lines
    \ ci = toggle comments on selected lines

    See https://github.com/preservim/nerdcommenter for more

Disable highlighting and plugins (e.g. for very large files):
    vim -u NONE filename

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

    insync

    """,
    "k8s": """
    # copy secret to other namespace
    kubectl get secret regcred -n prd -oyaml | grep -v '^\s*namespace:\s' | kubectl apply -n meilisearch -f -

    # copy secret to other cluster
    kubectl get secret -n db prd-replication -oyaml | sed 's/name: prd-replication/name: eks-prd-replication/g' |  yq e 'del(.metadata.ownerReferences)' - | kubectl --kubeconfig $NEW_KUBECONFIG apply -n db -f -

    Also remember the `kubectl neat` plugin!

    # show pods without resource requests
    kubectl get pods -A -o json | jq -r '.items[] | select(.spec.containers[].resources.requests.memory|not) | [.metadata.namespace, .metadata.name, .metadata.ownerReferences[0].kind, .metadata.ownerReferences[0].name] | @tsv' | column
    """,
    "mouse": """
    to see which mouse buttons correspond to which codes:

    xev -event button | grep button

    # Lenovo Legion Y740 autogenerates KeyRelease events everytime a character key is pressed on RHEL 7.8
    xinput list

    Under "Virtual core keyboard" (NOT Virtual core pointer):
    ↳ Lenovo Lenovo Y Gaming Precision Mouse Consumer Control	id=10	[slave  keyboard (3)]
    ↳ Lenovo Lenovo Y Gaming Precision Mouse  	id=19	[slave  keyboard (3)]  <-- this one

    xinput disable 19

    or copy/paste (or add to ~/.xinitrc to disable it on startup):

    xinput list | grep 'Virtual core keyboard' -A99 | grep 'Lenovo Lenovo Y Gaming Precision Mouse' | grep -v 'Consumer Control' | awk -F= '{ print $2 }' | awk -F' ' '{ print $1 }' | xargs -I{} xinput --disable {}

    """,
    "mypy": """
    reveal_type(var)
    """,
    "minikube": """
    # install
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube

    # in ~/.docker/config.json
    "stackOrchestrator": "kubernetes",

    eval $(minikube docker-env)
    """,
    "bash": """
        # send all output from the rest of this file to FILE.WAT
        exec >FILE.WAT
        exec >>FILE.WAT  # append
        exec 2>FILE.WAT  # send just stderr?
        # (can be run in a subshell)

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

    Moving the cursor (readline):
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


    # string up to colon
    echo "${s%%:*}"
    after =
    value=${str#*=}

    # signals / exit / status code reference
    Remember: higher than 128 means the process was killed by a signal

    kill -l
    Add 128 to the signal number to get the exit status code


    SHOW DIALOG BOXES FROM SHELL SCRIPTS -> whiptail - display dialog boxes from shell scripts
    (used by haos-vm.sh)
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
        Checkout a single file from stash
        git checkout stash@{0} -- FILENAME

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

        To edit a commit message on a closed PR:

            @kolia:

            here's what I [@kolia] did:
            git fetch origin 9bffa0422db545c3052515324f9a18796ec621dc  (the tip of the offending PR branch)
            git checkout -b ks/import_lots  create a branch with the same name as the original PR branch, pointing to the same commit id 9bffa04 ...
            git rebase -i HEAD~4 and go through the steps to amend the offending commit message
            git push --force origin ks/import_lots  which results in https://github.com/beacon-biosignals/OndaEDF.jl/compare/ks/import_lots, which indeed no longer has the offending client name

            however after all this, the old offending and now closed PR still shows the old commit message, and I can't re-open the PR
            imma try this https://gist.github.com/robertpainsi/2c42c15f1ce6dab03a0675348edd4e2c
            :phew: PR re-opened
            and rebased branch force-pushed
            scrubbing complete :tada:

            open github PRs reflect whatever the PR branch points to, and update after force-pushing but
            :til: closed PRs are immutable, they will not update after updating the PR branch
            :til: you cannot re-open a close PR if the PR branch no longer points to the commit id it pointed to when it was closed
            :til: you can fix that by git push --force <commit-id-at-PR-close-time>:<branch-name>
            :til: git rebase -i  is useful

    """,
    "notifications": """
    dunst: ~/.config/dunst/dunstrc
    more dunst: see "Notifications" section in ~/.i3/config

    bindsym Ctrl+shift+$mod+space exec dunstctl close
    bindsym Ctrl+grave exec dunstctl history-pop
    bindsym Ctrl+alt+space exec dunstctl close-all

    can reload i3 if something's amiss

    dunstctl [close|history-pop]

    # workaround to reload dunst (discards current notifications):
    killall dunst;notify-send foo
    """,
    "sound": """
        ## adjust volume

            $ pavucontrol / pulseaudio
            $ /usr/bin/pulseaudio
            $ amixer
            $ alsamixer     # gui
            # pavumeter     # gui showing current realtime audio output levels
    """,
    "textexpansion": """
    texpander, espanso, autokey
    """,
    "terminal": """

    Can I specify what characters set the double-click selection boundary in GNOME Terminal?
    http://askubuntu.com/questions/8413/can-i-specify-what-characters-set-the-double-click-selection-boundary-in-gnome-t
    https://bugs.launchpad.net/ubuntu/+source/gnome-terminal/+bug/1401207/comments/8


    $ dconf write /org/gnome/terminal/legacy/profiles:/:65c99ed6-29e0-4c99-9231-91943285e95c/word-char-exceptions '@ms "-,.;/?%&#_=+@~·:"'

    $ dconf list /org/gnome/terminal/legacy/profiles:/:65c99ed6-29e0-4c99-9231-91943285e95c/background-color


    Strip ANSI color codes from text:
    cat plan-output.txt  | sed 's/^[[^m]*m//g'


    """,
    "spelling": """
    git spell check personal dictionary location: ~/.git-spell-check
    """,
    "travis": """
    # debug job (get job id from build log on web interface)
    curl -s -X POST   -H "Content-Type: application/json"   -H "Accept: application/json"   -H "Travis-API-Version: 3"   -H "Authorization: token $TRAVIS_STAGING_ORG_API_TOKEN"   https://api-staging.travis-ci.org/job/${id}/debug

    """,
    "markdown": """
    reText (pip-installed)
    """,
    "monitors": """
    ** SEE ALSO: displays **

# cf. xrandr output
# 3 arbitrary monitor name
# 4 horizontal resolution in pixels
# 5 horizontal size in mm
# 6 vertical res in pixels
# 7 vertical size in mm
# 8 horizontal offset in pixels
# 9 vertical "
# 10 which output is this superseding
# 1    2            3      4    5   6    7   8    9  10
xrandr --setmonitor DP-5-M 2160/529x2160/529+1920+0 DP-5
xrandr --setmonitor DP-5-L 840/205x2160/529+1080+0 none
xrandr --setmonitor DP-5-R 840/205x2160/529+4080+0 none

# to unsplit, will have to run this for each monitor

xrandr --delmonitor DP-5-{L,M,R}

# my total h res in pixels = 8760 (all 3 screens) (3840 monitor)
# to get pixels, see randr output:
# DP-5 connected primary 3840x2160+1080+0 (normal left inverted right x axis y axis) 941mm x 529mm
# 470

# split big honking monitor left!
# xrandr --setmonitor DP-5-L 1920/470x2160/529+1080+0 DP-5  # <-- DP-5 is the one we're replacing

# split big honking monitor right!
# xrandr --setmonitor DP-5-R 1920/470x2160/529+3000+0 none   # <-- put none here, because we're not replacing anything

# xrandr --listmonitors

# to restore layout
autorandr -c

    """,
    "kernel": """
    need to install linux-headers at the same time, else nvidia driver might be unhappy
    using nvidia driver closed-source
    dkms compiles

    display doesn't work after upgrading kernel:

less /var/log/Xorg.0.log
dpkg -l *nividia*
dpkg -l *nv*
lsmod | grep nv
lsmod | grep nouv
modprobe nouveau
sudo modprobe nouveau
startx
sudo rmmod nouveau
sudo vim /etc/X11/xorg.conf.d/90-monitor.conf
cd /etc/X11/xorg.conf.d/
ls
sudo mv 90-monitor.conf  90-monitor.conf.disabled
X
less /var/log/Xorg.0.log
dpkg -S nouveau
ls -l
apt search fbterm
apt-cache search fbterm
sudo apt install fbterm
cat /etc/resolv.conf
nmtui
sudo apt install fbterm
fbterm -s 40
fbterm -s 60
cd
X
cd /var/log/
ls -ltr
date
ps faux | grep X
ls gdm3/
sudo ls gdm3



    $ dkms status
    nvidia-current, 470.129.06, 5.17.0-1-amd64, x86_64: installed
    v4l2loopback, 0.12.5, 5.10.0-7-amd64, x86_64: installed
    v4l2loopback, 0.12.5, 5.10.0-8-amd64, x86_64: installed
    v4l2loopback, 0.12.5, 5.17.0-1-amd64, x86_64: installed

    dpkg-reconfigure nvidia-driver or something

    sudo apt-get update
    sudo apt-get install linux-image-amd64 linux-headers-amd64
    """,
    "ssh": """
    Get public key for use with OpenSSH (i.e. adding to https://bitbucket.org/account/settings/ssh-keys/ ):
        ssh-keygen -y -f ~/.ssh/privatekey.pem

    Get public key in ----BEGIN PUBLIC KEY---- format
        openssl rsa -in ~/.ssh/privatekey.pem -pubout -out ~/.ssh/pubkey.pub
    """,
    "ssl": """
        openssl s_client -connect statamic.quantgene.dev:443
    """,
    "ec2": """
    instance types: https://github.com/wrble/public/blob/main/aws-instance-types.md
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

    Note: this requires gnome-control-center. If clicking 'unlock' doesn't seem to do anything, check syslog, and try running 'sudo gnome-control-center' instead.
    """,
    "fonts": """
    xfontsel
    """,
    "webcam": """
        guvcview

        guvcview --device=/dev/video1

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
    "yubikey": """
packages:
yubikey-personalization
yubikey-manager
yubioath-desktop -- required to use CCID interface


# view enabled modes
ykman mode
# enable CCID mode
ykman mode OTP+FIDO+CCID

(remove and re-insert yubikey)
sudo yubioath-desktop

Up to jessie, to use the card as a non-root users, you need to add a line to /etc/udev/rules.d/99-yubikeys.rules to the tell udev either
https://wiki.debian.org/Smartcards/YubiKey4


ykman oath add -t LABEL SECRET
# -t = require touch

ykman oath code
""",
    "sleep": """
sleep 3; xdg-screensaver activate


see also: power
""",
    "yq": """
    yq eval 'explode(.)' .circleci/config.yml
    yq eval 'explode(.)' bitbucket-pipelines.yml

    # check path to a key
    cat /tmp/values.yaml | yq e -o=json | gron | grep annotations | sort
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
