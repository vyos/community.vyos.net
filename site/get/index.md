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

Or you can build an LTS image from source.

## Legacy LTS releases

We also provide images of legacy LTS releases as a courtesy. Currently available images are:

### 1.2.9-S1 [#](#1.2.9-S1)

* [1.2.9-S1 generic ISO image](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-amd64.iso) (signatures: [GPG](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-amd64.iso.asc), [Minisign](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-amd64.iso.minisig))
* [1.2.9-S1 Qcow2 image for KVM](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-10G-qemu.qcow2) (signatures: [GPG](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-10G-qemu.qcow2.asc), [Minisign](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-10G-qemu.qcow2.minisig))
* [1.2.9-S1 OVA for VMware (with cloud-init)](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-cloud-init-vmware.ova) (signatures: [GPG](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-cloud-init-vmware.ova.asc), [Minisign](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-cloud-init-vmware.ova.minisig)).
* [1.2.9-S1 OVA for VMware (simple)](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-simple-vmware.ova) (signatures: [GPG](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-simple-vmware.ova.asc), [Minisign](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-simple-vmware.ova.minisig))
* [1.2.9-S1 for Microsoft Hyper-V](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-hyperv-amd64.vhdx) (signatures: [GPG](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-hyperv-amd64.vhdx.asc), [Minisign](https://legacy-lts-images.vyos.io/1.2.9-S1/vyos-1.2.9-S1-hyperv-amd64.vhdx.minisig))
