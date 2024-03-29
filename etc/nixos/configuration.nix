# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:

{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
    ];

  # Use the systemd-boot EFI boot loader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true; #setback to true

  # networking.hostName = "nixos"; # Define your hostname.
  # networking.wireless.enable = true;  # Enables wireless support via wpa_supplicant.
  nixpkgs.config.allowUnfree = true;
  services.xserver.videoDrivers = [ "nvidia" ];
  # Set your time zone.
  time.timeZone = "America/Chicago";

  # The global useDHCP flag is deprecated, therefore explicitly set to false here.
  # Per-interface useDHCP will be mandatory in the future, so this generated config
  # replicates the default behaviour.
  networking.useDHCP = false;
  networking.interfaces.enp2s0.useDHCP = true;

  # Configure network proxy if necessary
  # networking.proxy.default = "http://user:password@proxy:port/";
  # networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

  # Select internationalisation properties.
   i18n.defaultLocale = "en_US.UTF-8";
   console = {
     font = "Lat2-Terminus16";
     keyMap = "us";
   };

  # Enable the X11 windowing system.
  services.xserver.enable = true;
  services.xserver.displayManager.startx.enable = true;

  # Enable the GNOME Desktop Environment.
  #services.xserver.displayManager.gdm.enable = false;
  services.xserver.displayManager.lightdm.enable = false;
  #services.xserver.desktopManager.gnome.enable = false;
  services.xserver.windowManager.herbstluftwm.enable = true;

#environment.variables = {
#    XDG_CONFIG_HOME = "~/.config";
#  };
#  services.xserver.windowManager.herbstluftwm.configFile = /home/bob/.config/herbstluftwm/autostart;
  

  # Configure keymap in X11
  services.xserver.layout = "us";
  # services.xserver.xkbOptions = "eurosign:e";

  # Enable CUPS to print documents.
  # services.printing.enable = true;

  # Enable sound.
  sound.enable = true;
  hardware.pulseaudio.enable = true;

  # Enable touchpad support (enabled default in most desktopManager).
  # services.xserver.libinput.enable = true;

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.bob = {
    isNormalUser = true;
    extraGroups = [ "wheel" "audio" ]; # Enable ‘sudo’ for the user.
  };

  # List packages installed in system profile. To search, run:
  # $ nix search wget
  environment.systemPackages = with pkgs; [
    # Do not forget to add an editor to edit configuration.nix! The Nano editor is also installed by default.
    amfora #gemini client written in go
    alacritty
    appimage-run
    bat
    dracula-theme
    element-web
    firefox
    fish
    gcc # to use rust this is needed
    git
    ghc
    hicolor-icon-theme #used for protonvpn-gui
    htop
    jump
    koreader #ebook reader
    killall #used specifically for polybar launch.shi
    lagrange #gui gemini browser
    lxappearance
    vlc
    #ncspot # Seems to be buggy and stop playing music all the time moving to spotifyd and spotify-tui to see if that is better. Issue seemed to be with protonvpn using protonvpn dns leak proof feature. Turned that off now better.
    neovim
    nnn #cli file manager
    nyxt
    obs-studio
    pcmanfm 
    picom
    polybar
    polybarFull
    protonvpn-cli
    protonvpn-gui
    wget
    rofi
    sxiv #image viewer
    tango-icon-theme #pcmanfm icons show up a blank place holders without this.
    unzip
    rustup
    slock
    spaceFM
    spotifyd
    spotify-tui
    vim
    vscode
    xautolock #is being started in ~/.xinitrc
    xdo
    xdotool
    xidlehook
    xorg.xkill
  ];

  security.wrappers.slock.source = "${pkgs.slock.out}/bin/slock";  #Allows regular user to run slock without disabling OOM killer see https://github.com/NixOS/nixpkgs/issues/9656#issuecomment-137719381 and https://github.com/NixOS/nixpkgs/issues/9656#issuecomment-362873714
  nixpkgs.config.joypixels.acceptLicense = true;
  fonts.fonts = with pkgs; [
    hack-font
    joypixels #get nice emoji font for polybar
    font-awesome_4
    siji
    tamsyn
  ];

  security.sudo.wheelNeedsPassword = false;

  # Some programs need SUID wrappers, can be configured further or are
  # started in user sessions.
  # programs.mtr.enable = true;
  # programs.gnupg.agent = {
  #   enable = true;
  #   enableSSHSupport = true;
  # };

  # List services that you want to enable:
  services.spotifyd.enable = true;
  # Enable the OpenSSH daemon.
  # services.openssh.enable = true;

  # Open ports in the firewall.
  # networking.firewall.allowedTCPPorts = [ ... ];
  # networking.firewall.allowedUDPPorts = [ ... ];
  # Or disable the firewall altogether.
  # networking.firewall.enable = false;

  # This value determines the NixOS release from which the default
  # settings for stateful data, like file locations and database versions
  # on your system were taken. It‘s perfectly fine and recommended to leave
  # this value at the release version of the first install of this system.
  # Before changing this value read the documentation for this option
  # (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
  system.stateVersion = "21.05"; # Did you read the comment?

}

