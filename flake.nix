{
  description = "Platform bot development flake";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.default = with pkgs; mkShell {
        shellHook = ''
            export PIP_PREFIX=$(pwd)/_build/pip_packages #Dir where built packages are stored
            export PYTHONPATH="$PIP_PREFIX/${pkgs.python311.sitePackages}:$PYTHONPATH"
            export PATH="$PIP_PREFIX/bin:$PATH"
            unset SOURCE_DATE_EPOCH
        '';

        packages = [
          python311
          nodePackages.pyright
          python311Packages.pip
          python311Packages.black
          python311Packages.isort
          python311Packages.pylint
	      ];
      };
    });
}
