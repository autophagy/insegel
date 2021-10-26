{ pkgs ? import <nixpkgs> {}
, pythonPackages ? pkgs.python3Packages
}:
let
  gitignoreSrc = pkgs.fetchFromGitHub {
    owner = "hercules-ci";
    repo = "gitignore.nix";
    rev = "5b9e0ff9d3b551234b4f3eb3983744fa354b17f1";
    sha256 = "sha256:01l4phiqgw9xgaxr6jr456qmww6kzghqrnbc7aiiww3h6db5vw53";
  };
  inherit (import gitignoreSrc { inherit (pkgs) lib; }) gitignoreSource;
in
pythonPackages.buildPythonPackage rec {
  pname = "insegel";
  version = "1.3.1";
  src = gitignoreSource ./.;
  doCheck = false;
  pythonImportsCheck = [ "insegel" ];
}
