# Get VyOS

VyOS has three release "channels": nightly builds, monthly snapshots, and LTS releases.

## Nightly builds

Nightly builds are automatically produced at least once a day and include all the latest
code (bug fixes and features) from maintainers and community contributors.

Nightly builds are not hand-tested before upload. A basic set of automated
[smoke tests](https://github.com/vyos/vyos-1x/tree/current/smoketest/scripts/cli) is executed
for each build ensuring that basic functionality is working. In addition we load arbitrary
[configurations](https://github.com/vyos/vyos-1x/tree/current/smoketest/configs) to ensure
there are no errors during config migration and system bootup.

Nightly builds are for you if you...

* want to help us test latest VyOS code
* want to check whether a bug is fixed in the latest code
* made a patch and want to test it before making a pull request

Go to the [nightly builds page](/get/nightly-builds).

## LTS release

Prebuilt LTS release images are available to people and companies who help us move the project
forward.

There are many ways to get access:

* Purchase a [software access subscription](https://vyos.io/subscriptions/software/).
* Get free access with a [support subscription](https://vyos.io/subscriptions/support/).
* Apply for a free subscription as a [contributor](/get/contributor-subscriptions).
* Apply for a free subscription as an
  [educational instutution](https://vyos.io/community/for-educational-institutions/),
  [non-profit](https://vyos.io/community/for-non-commercial-organizations/), or an
  [emergency service](http://vyos.io/community/for-first-responders/).

You can also build an LTS image from the source.

## Legacy LTS releases

As a courtesy, we offer images of legacy LTS releases. To access all available legacy LTS releases, kindly complete the form below. Upon submission, you will receive an email containing links to download the images.

<div id="application-form">

<script charset="utf-8" type="text/javascript" src="//js.hsforms.net/forms/embed/v2.js"></script>
<script>
  hbspt.forms.create({
    region: "na1",
    portalId: "4129050",
    formId: "ebb05a53-23d6-4454-824d-817d0d8b86d4"
  });
</script>

</div>