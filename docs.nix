let
  pkgs = import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/517850fced3b5de6693d5b49ad14e5a12d968741.tar.gz") {};
  pythonPackages = pkgs.python39Packages;
  inherit (pkgs) stdenv;
in
stdenv.mkDerivation {
  name = "insegel-docs";
  src = ./docs;

  buildInputs = with pkgs; [
    pythonPackages.sphinx
    pythonPackages.insegel
  ];

  buildPhase = ''
    make html
  '';

  installPhase = ''
    mkdir -p $out
    cp -r _build/html/* $out
    echo 'insegel.autophagy.io' > $out/CNAME
    '';
  }
