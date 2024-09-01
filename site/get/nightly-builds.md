<div class='nightly-builds-page'>
  <section class='banner'>
    <div class='containerCustom'>
      <div class='left-shape'>
        <img src='/img/global/shape-left.svg' />
      </div>
      <div class='right-shape'>
        <img src='/img/global/shape-right.svg' />
      </div>

  <div class='banner-div'>

  # VyOS nightly builds

  </div>

  </div>
  </section>

  <section class='content-section'>
    <div class='content-div'>
      <div class='image-signatures'>

  VyOS nightly builds are automatically produced from the `current` branch and the development branch for the LTS release,
  at least once a day.
  They include all the latest code from maintainers and community contributors.

  Nightly builds are not hand-tested before upload. A basic set of automated
  [smoke tests](https://github.com/vyos/vyos-1x/tree/current/smoketest/scripts/cli) is executed
  for each build ensuring that basic functionality is working. In addition we load arbitrary
  [configurations](https://github.com/vyos/vyos-1x/tree/current/smoketest/configs) to ensure
  there are no errors during config migration and system bootup.

  ## Verifying image signatures

  We use [minisign](https://jedisct1.github.io/minisign/) for release signing. To learn about its advantages
  over GPG, read [signify: Securing OpenBSD From Us To You](https://www.openbsd.org/papers/bsdcan-signify.html).

  One obvious advantage is that you don't need to import the key anywhere, you can pass it as a command line argument.
  Once you download an image and its `.minisig` file, you can verify its integrity with this command:

  ```
  minisign -Vm <ISO file> -P RWSIhkR/dkM2DSaBRniv/bbbAf8hmDqdbOEmgXkf1RxRoxzodgKcDyGq
  ```

  If in doubt, you can get the public key from the [nightly builds repository](https://github.com/vyos/vyos-nightly-build/blob/main/minisign.pub).
  If you are _really_ in doubt (i.e., you have a reason to suspect that the repository and/or this website were compromised),
  you should report that to the maintainers.

  Currently, we create nightly builds with GitHub Actions and store them in releases of the [vyos/vyos-nightly-build](https://github.com/vyos/vyos-nightly-build/releases)
  repository. Here is an auto-generated list of available builds.

  </div>

  <div class='available-builds' id='available-builds'>

  ## Available builds

  </div>

  </section>

</div>
