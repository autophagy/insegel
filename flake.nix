{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    utils = {
      url = "github:numtide/flake-utils";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python3Packages;
      in
      {

        packages.insegel = pythonPackages.buildPythonPackage rec {
          pname = "insegel";
          version = "1.3.1";
          src = ./.;
          doCheck = false;
          pythonImportsCheck = [ "insegel" ];
        };

        packages.docs = pkgs.stdenv.mkDerivation {
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
          '';
        };

        packages.default = self.packages.${system}.insegel;

      }

    );
}
