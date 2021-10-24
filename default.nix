{ pkgs ? import <nixpkgs> {}
, pythonPackages ? pkgs.python3Packages
}:

pythonPackages.buildPythonPackage rec {
  pname = "insegel";
  version = "1.3.1";
  src = ./.;
  doCheck = false;
  pythonImportsCheck = [ "insegel" ];
}
