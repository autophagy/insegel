============
Installation
============

Via PyPI
========

To use the Insegel theme from PyPI, you can install via pip::

  pip install insegel

Or, you can add it to your documentations' pip requirements file.
You can then set Sphinx to use the theme via::

  html_theme = 'insegel'

within your documentations ``conf.py``.


Via Nixpkgs
===========

If you are using Nix to manage your project's dependencies, Insegel is available
in the ``nixpkgs-unstable`` channel as ``python3Packages.insegel``.

It can be used by adding it to your derivation's ``buildInputs``, for
example::

    { pkgs ? import <nixpkgs> {} }:

    let
      inherit (pkgs) stdenv;
    in
    stdenv.mkDerivation {
      name = "myproject";
      src = ./docs;

      buildInputs = with pkgs; [
        python3Packages.sphinx
        python3Packages.insegel
      ];

      buildPhase = ''
        make html
      '';

      installPhase = ''
        mkdir -p $out
        cp -r _build/html/* $out
        '';
    }
