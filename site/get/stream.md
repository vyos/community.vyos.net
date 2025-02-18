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

  # VyOS Stream

  </div>

  </div>
  </section>

  <section class='content-section'>
    <div class='content-div'>
      <div class='image-signatures'>

  VyOS Stream serves as a technology preview and a quality gate for the upcoming LTS release.
  New images are releases roughly every quarter.

  Features can only be removed from VyOS Stream through a deprecation procedure,
  and we promise to only make forward-compatible changes to the configuration syntax
  and API, so that users, integrators, and developers of external tools
  can prepare their environments and projects for the future LTS release
  and help us identify and fix issues.


  ## Verifying image signatures

  We use [minisign](https://jedisct1.github.io/minisign/) for release signing. To learn about its advantages
  over GPG, read [signify: Securing OpenBSD From Us To You](https://www.openbsd.org/papers/bsdcan-signify.html).

  One obvious advantage is that you don't need to import the key anywhere, you can pass it as a command line argument.
  Once you download an image and its `.minisig` file, you can verify its integrity with this command:

  ```
  minisign -Vm <ISO file> -P RWTR1ty93Oyontk6caB9WqmiQC4fgeyd/ejgRxCRGd2MQej7nqebHneP
  ```

  </div>

  <div class='available-builds' id='available-builds'>

  ## Releases

  <h3 id="1.5-2025-Q1">VyOS Stream 1.5-2025-Q1</h3>

  * Image: [vyos-1.5-stream-2025-Q1-generic-amd64.iso](https://community-downloads.vyos.dev/stream/1.5-stream-2025-Q1/vyos-1.5-stream-2025-Q1-generic-amd64.iso) ([sig](https://community-downloads.vyos.dev/stream/1.5-stream-2025-Q1/vyos-1.5-stream-2025-Q1-generic-amd64.iso.minisig))
  * Source code tarball: [circinus-1.5-stream-2025-Q1.tar.gz](https://community-downloads.vyos.dev/stream/1.5-stream-2025-Q1/circinus-1.5-stream-2025-Q1.tar.gz) ([sig](https://community-downloads.vyos.dev/stream/1.5-stream-2025-Q1/circinus-1.5-stream-2025-Q1.tar.gz.minisig))

  </div>

  </section>

</div>
