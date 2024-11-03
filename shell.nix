{ pkgs ? import <nixpkgs> {}
}:
pkgs.mkShell {               # mkShell is a helper function
  name="dev-environment";    # that requires a name
  buildInputs = [            # and a list of packages
    pkgs.python3
    pkgs.python3Packages.virtualenv
    pkgs.python312Packages.google-generativeai
  ];
  shellHook = ''             # bash to run when you enter the shell
    echo "Start developing..."
  '';
}
