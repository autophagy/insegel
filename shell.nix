{ stdenv ? import <nixpkgs> {} }:

let

  inherit (stdenv) pkgs mkShell;
  inherit (stdenv.lib) flatten;

in

mkShell rec {
  name = "venv";
  buildInputs =
    with pkgs; [
      sass
      nodejs
      nodePackages.grunt-cli
      python3
      python3Packages.pip
      python3Packages.virtualenv
    ];

  shellHook = ''
    virtualenv .venv
    source ./.venv/bin/activate
    unset PYTHONPATH
    pip install -r requirements.txt
    npm install
  '';
}
