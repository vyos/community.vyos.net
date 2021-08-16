# VyOS nightly builds

VyOS nightly builds are automatically produced from the `current` branch and the development branch for the LTS release,
at least once a day.
They include all the latest code from maintainers and community contributors.

Nightly builds are not hand-tested before upload. A basic set of automated
[smoke tests](https://github.com/vyos/vyos-1x/tree/current/smoketest/scripts/cli) is executed
for each build ensuring that basic functionality is working. In addition we load arbitrary
[configurations](https://github.com/vyos/vyos-1x/tree/current/smoketest/configs) to ensure
there are no errors during config migration and system bootup.

## Available builds
